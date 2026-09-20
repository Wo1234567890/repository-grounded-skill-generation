#!/usr/bin/env python3
"""
V6: Conservative task-aligned verifier generator for SWE-Skills-Bench batch1.

Architecture
------------
LLM: task specification -> structured verifier PLAN only.
Deterministic compiler: PLAN -> pytest verifier.

The LLM never writes verifier code or regexes.

Supported primitives are intentionally narrow:
  FILE_EXISTS
  TS_INTERFACE_FIELDS
  STRING_LITERAL_IN_FILE
  IDENTIFIER_IN_FILE
  UNVERIFIED

Coverage is assigned mechanically:
  FILE_EXISTS          -> FULL
  TS_INTERFACE_FIELDS  -> FULL
  STRING_LITERAL...    -> PARTIAL
  IDENTIFIER...        -> PARTIAL
  UNVERIFIED           -> UNVERIFIED

Every plan argument is mechanically checked against the task specification.
Unsupported or unsound requirements remain UNVERIFIED instead of being tested
with a weak proxy.

This is deliberately conservative. It is intended to produce candidate
task-aligned verifiers that are auditable, not to pretend every requirement
can be automatically verified from task text alone.
"""

from __future__ import annotations

import argparse
import json
import os
import py_compile
import re
import sys
import time
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml", file=sys.stderr)
    raise

try:
    from anthropic import Anthropic
except ImportError:
    print("Missing dependency: anthropic", file=sys.stderr)
    raise


PLAN_SYSTEM = r"""
You extract a conservative, task-aligned verification PLAN from a software
engineering task specification.

The task specification is the ONLY source of requirements.
Repository metadata may only identify the repository root.

Do NOT write Python code.
Do NOT write regexes.
Do NOT invent filenames, commands, type names, field names, thresholds,
architectures, or implementation details.

Break the task into atomic requirements. For each requirement choose exactly
one supported primitive:

1. FILE_EXISTS
   Use ONLY when the task explicitly names an exact file path whose existence
   is required.

   args:
   {"path": "exact/path/from/task"}

2. TS_INTERFACE_FIELDS
   Use ONLY when ALL of the following are explicitly specified by the task:
   - an exact TypeScript file path;
   - an exact interface name;
   - exact field names;
   - exact field types.
   This primitive verifies fields inside that named interface body.

   args:
   {
     "path": "exact/path/from/task",
     "interface_name": "ExactInterfaceName",
     "fields": [
       {"name": "field_name", "type": "ExactTypeFromTask"}
     ]
   }

3. STRING_LITERAL_IN_FILE
   Use only when the task explicitly requires an exact string value/name and
   also explicitly identifies the file where that definition belongs.
   This is only PARTIAL verification because the string could still appear in
   another valid code context.

   args:
   {"path": "exact/path/from/task", "value": "exact_value_from_task"}

4. IDENTIFIER_IN_FILE
   Use only when an exact identifier is explicitly required and the exact file
   is explicitly specified by the task.
   This is only PARTIAL verification.

   args:
   {"path": "exact/path/from/task", "value": "ExactIdentifierFromTask"}

5. UNVERIFIED
   Use for runtime behavior, compilation/build correctness when no explicit
   executable command is supplied, semantic association that cannot be proven
   without guessing implementation structure, quality requirements, or any
   requirement that the supported primitives cannot soundly verify.

IMPORTANT:
- Never turn "use snake_case" into a global prohibition on camelCase.
- Never test hard-coded expected names just to prove those hard-coded names are
  snake_case. If no sound primitive can test the implementation's naming
  structure, mark the naming requirement UNVERIFIED.
- Never assume payload type names if the task does not specify them.
- Never associate fields with an event by scanning the whole file.
- Never add fallback checks.
- Never claim runtime behavior from static string presence.
- If unsure, choose UNVERIFIED.

Return ONLY valid JSON:
{
  "requirements": [
    {
      "id": "R1",
      "requirement": "atomic requirement copied/paraphrased from the task",
      "primitive": "FILE_EXISTS|TS_INTERFACE_FIELDS|STRING_LITERAL_IN_FILE|IDENTIFIER_IN_FILE|UNVERIFIED",
      "args": {},
      "reason": "why this primitive is sound, or why it is unverified"
    }
  ]
}
"""


SUPPORTED = {
    "FILE_EXISTS",
    "TS_INTERFACE_FIELDS",
    "STRING_LITERAL_IN_FILE",
    "IDENTIFIER_IN_FILE",
    "UNVERIFIED",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--tasks-dir", type=Path, required=True)
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--model", default=None)
    p.add_argument("--only", nargs="*", default=None)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--sleep", type=float, default=0.4)
    return p.parse_args()


def resolve_model(args: argparse.Namespace) -> str:
    return (
        args.model
        or os.getenv("VERIFIER_MODEL")
        or os.getenv("ANTHROPIC_DEFAULT_SONNET_MODEL")
        or "claude-haiku-4-5-20251001"
    )


def make_client() -> Anthropic:
    token = os.getenv("ANTHROPIC_AUTH_TOKEN") or os.getenv("ANTHROPIC_API_KEY")
    if not token:
        raise SystemExit(
            "No Anthropic credential found. Export ANTHROPIC_AUTH_TOKEN "
            "or ANTHROPIC_API_KEY."
        )
    kwargs: dict[str, Any] = {"api_key": token}
    base_url = os.getenv("ANTHROPIC_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return Anthropic(**kwargs)


def response_text(resp: Any) -> str:
    parts = []
    for block in getattr(resp, "content", []):
        if getattr(block, "type", None) == "text":
            parts.append(block.text)
    return "\n".join(parts).strip()


def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        a = text.find("{")
        b = text.rfind("}")
        if a >= 0 and b > a:
            return json.loads(text[a:b + 1])
        raise


def call_plan(
    client: Anthropic,
    model: str,
    payload: dict[str, Any],
    retries: int = 3,
) -> dict[str, Any]:
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=10000,
                system=PLAN_SYSTEM,
                messages=[
                    {
                        "role": "user",
                        "content": json.dumps(payload, ensure_ascii=False, indent=2),
                    }
                ],
            )
            return extract_json(response_text(resp))
        except Exception as e:
            last = e
            if attempt < retries:
                time.sleep(attempt * 2)
    assert last is not None
    raise last


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def metadata_by_task(config: dict[str, Any]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for item in config.get("skills", []):
        tid = str(item.get("id", "")).strip()
        if not tid:
            continue
        repo = item.get("repo") or {}
        url = str(repo.get("url", ""))
        name = url.rstrip("/").split("/")[-1] if url else ""
        if name.endswith(".git"):
            name = name[:-4]
        out[tid] = {
            "repo_url": url,
            "repo_name": name,
            "commit": str(repo.get("commit", "")),
        }
    return out


def normalized_ws(s: str) -> str:
    return re.sub(r"\s+", "", s)


def text_contains_grounded(task_text: str, value: str) -> bool:
    if value in task_text:
        return True
    return normalized_ws(value) in normalized_ws(task_text)


def sanitize_plan(
    raw_plan: dict[str, Any],
    task_text: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Mechanically reject unsupported or hallucinated checks.

    Invalid executable checks are downgraded to UNVERIFIED instead of guessed.
    """
    reqs = raw_plan.get("requirements")
    if not isinstance(reqs, list):
        raise ValueError("Plan must contain a requirements list")

    cleaned: list[dict[str, Any]] = []
    warnings: list[str] = []

    for idx, raw in enumerate(reqs, start=1):
        if not isinstance(raw, dict):
            warnings.append(f"R{idx}: non-object requirement downgraded")
            continue

        rid = str(raw.get("id") or f"R{idx}")
        requirement = str(raw.get("requirement") or "").strip()
        primitive = str(raw.get("primitive") or "UNVERIFIED").strip().upper()
        args = raw.get("args") if isinstance(raw.get("args"), dict) else {}
        reason = str(raw.get("reason") or "").strip()

        if primitive not in SUPPORTED:
            warnings.append(f"{rid}: unsupported primitive {primitive}; downgraded")
            primitive = "UNVERIFIED"
            args = {}

        def downgrade(msg: str) -> None:
            nonlocal primitive, args, reason
            warnings.append(f"{rid}: {msg}; downgraded to UNVERIFIED")
            primitive = "UNVERIFIED"
            args = {}
            reason = (reason + " " + msg).strip()

        if primitive == "FILE_EXISTS":
            path = str(args.get("path") or "")
            if not path or path not in task_text:
                downgrade("file path is not explicitly grounded in task text")

        elif primitive in {"STRING_LITERAL_IN_FILE", "IDENTIFIER_IN_FILE"}:
            path = str(args.get("path") or "")
            value = str(args.get("value") or "")
            if not path or path not in task_text:
                downgrade("file path is not explicitly grounded in task text")
            elif not value or not text_contains_grounded(task_text, value):
                downgrade("required value is not explicitly grounded in task text")

        elif primitive == "TS_INTERFACE_FIELDS":
            path = str(args.get("path") or "")
            interface_name = str(args.get("interface_name") or "")
            fields = args.get("fields")

            if not path or path not in task_text:
                downgrade("TypeScript file path is not explicitly grounded")
            elif not interface_name or interface_name not in task_text:
                downgrade("interface name is not explicitly grounded")
            elif not isinstance(fields, list) or not fields:
                downgrade("interface fields are missing")
            else:
                bad = False
                for f in fields:
                    if not isinstance(f, dict):
                        bad = True
                        break
                    name = str(f.get("name") or "")
                    typ = str(f.get("type") or "")
                    if (
                        not name
                        or not typ
                        or not text_contains_grounded(task_text, name)
                        or not text_contains_grounded(task_text, typ)
                    ):
                        bad = True
                        break
                if bad:
                    downgrade("one or more interface fields/types are not task-grounded")

        cleaned.append(
            {
                "id": rid,
                "requirement": requirement,
                "primitive": primitive,
                "args": args,
                "reason": reason,
            }
        )

    return cleaned, warnings


def coverage_for(primitive: str) -> str:
    if primitive in {"FILE_EXISTS", "TS_INTERFACE_FIELDS"}:
        return "FULL"
    if primitive in {"STRING_LITERAL_IN_FILE", "IDENTIFIER_IN_FILE"}:
        return "PARTIAL"
    return "UNVERIFIED"


def test_name_for(req: dict[str, Any], index: int) -> str:
    primitive = req["primitive"]
    if primitive == "UNVERIFIED":
        return "UNVERIFIED"
    rid = re.sub(r"[^A-Za-z0-9_]+", "_", req["id"]).strip("_").lower()
    if not rid:
        rid = f"r{index}"
    return f"test_{rid}_{primitive.lower()}"


def py_repr(obj: Any) -> str:
    return repr(obj)


HELPERS = r