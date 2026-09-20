#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from anthropic import Anthropic


PLAN_SYSTEM = r"""
You extract a conservative verification PLAN from a software-engineering task.

The task specification is the ONLY source of evaluation requirements.
Repository metadata may only identify the repository root.

Do NOT write Python code or regexes.
Do NOT invent filenames, commands, type names, field names, thresholds,
architectures, or implementation details.

Choose exactly one primitive for each atomic requirement:

FILE_EXISTS
- Only when the task explicitly names an exact required file path.
- args: {"path": "exact/path/from/task"}

TS_INTERFACE_FIELDS
- Only when the task explicitly gives an exact TypeScript file path,
  an exact interface name, exact field names, and exact field types.
- args:
  {
    "path": "exact/path/from/task",
    "interface_name": "ExactInterfaceName",
    "fields": [{"name": "field", "type": "ExactType"}]
  }

STRING_LITERAL_IN_FILE
- Only when the task explicitly requires an exact string value/name and
  explicitly identifies the file where it belongs.
- This is PARTIAL evidence only.
- args: {"path": "exact/path/from/task", "value": "exact_value"}

IDENTIFIER_IN_FILE
- Only when an exact identifier is explicitly required and an exact file
  is explicitly named by the task.
- This is PARTIAL evidence only.
- args: {"path": "exact/path/from/task", "value": "ExactIdentifier"}

UNVERIFIED
- Use for runtime behavior, compilation when no executable command is supplied,
  semantic association requiring guessed implementation structure, or anything
  that the supported primitives cannot soundly test.
- args: {}

Important:
- Never assume payload type names unless the task states them.
- Never infer event-to-payload association from whole-file search.
- Never turn snake_case into a global camelCase prohibition.
- Never claim runtime behavior from static text.
- If unsure, use UNVERIFIED.

Return ONLY valid JSON:
{
  "requirements": [
    {
      "id": "R1",
      "requirement": "atomic task requirement",
      "primitive": "FILE_EXISTS|TS_INTERFACE_FIELDS|STRING_LITERAL_IN_FILE|IDENTIFIER_IN_FILE|UNVERIFIED",
      "args": {},
      "reason": "why this is sound, or why it is unverified"
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


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--tasks-dir", type=Path, required=True)
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--model", default=None)
    p.add_argument("--only", nargs="*", default=None)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--overwrite", action="store_true")
    return p.parse_args()


def model_name(args):
    return (
        args.model
        or os.getenv("VERIFIER_MODEL")
        or os.getenv("ANTHROPIC_DEFAULT_SONNET_MODEL")
        or "claude-haiku-4-5-20251001"
    )


def client():
    token = os.getenv("ANTHROPIC_AUTH_TOKEN") or os.getenv("ANTHROPIC_API_KEY")
    if not token:
        raise SystemExit("Export ANTHROPIC_AUTH_TOKEN or ANTHROPIC_API_KEY first.")
    kwargs: dict[str, Any] = {"api_key": token}
    if os.getenv("ANTHROPIC_BASE_URL"):
        kwargs["base_url"] = os.environ["ANTHROPIC_BASE_URL"]
    return Anthropic(**kwargs)


def text_of(resp):
    return "\n".join(
        block.text
        for block in getattr(resp, "content", [])
        if getattr(block, "type", None) == "text"
    ).strip()


def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        a, b = text.find("{"), text.rfind("}")
        if a >= 0 and b > a:
            return json.loads(text[a:b+1])
        raise


def call_plan(api, model, payload):
    last = None
    for attempt in range(3):
        try:
            resp = api.messages.create(
                model=model,
                max_tokens=10000,
                system=PLAN_SYSTEM,
                messages=[{
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False, indent=2),
                }],
            )
            return parse_json(text_of(resp))
        except Exception as e:
            last = e
            time.sleep(2 * (attempt + 1))
    raise last


def load_config(path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def repo_metadata(config):
    out = {}
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


def grounded(task_text, value):
    if not value:
        return False
    if value in task_text:
        return True
    return re.sub(r"\s+", "", value) in re.sub(r"\s+", "", task_text)


def sanitize(raw_plan, task_text):
    reqs = raw_plan.get("requirements")
    if not isinstance(reqs, list):
        raise ValueError("Plan has no requirements list")

    cleaned, warnings = [], []

    for i, raw in enumerate(reqs, 1):
        if not isinstance(raw, dict):
            continue

        rid = str(raw.get("id") or f"R{i}")
        requirement = str(raw.get("requirement") or "").strip()
        primitive = str(raw.get("primitive") or "UNVERIFIED").upper()
        args = raw.get("args") if isinstance(raw.get("args"), dict) else {}
        reason = str(raw.get("reason") or "").strip()

        def downgrade(msg):
            nonlocal primitive, args, reason
            warnings.append(f"{rid}: {msg}")
            primitive = "UNVERIFIED"
            args = {}
            reason = (reason + " " + msg).strip()

        if primitive not in SUPPORTED:
            downgrade("unsupported primitive")

        elif primitive == "FILE_EXISTS":
            if not grounded(task_text, str(args.get("path") or "")):
                downgrade("path not grounded in task")

        elif primitive in {"STRING_LITERAL_IN_FILE", "IDENTIFIER_IN_FILE"}:
            path = str(args.get("path") or "")
            value = str(args.get("value") or "")
            if not grounded(task_text, path):
                downgrade("path not grounded in task")
            elif not grounded(task_text, value):
                downgrade("value not grounded in task")

        elif primitive == "TS_INTERFACE_FIELDS":
            path = str(args.get("path") or "")
            name = str(args.get("interface_name") or "")
            fields = args.get("fields")
            if not grounded(task_text, path):
                downgrade("interface path not grounded")
            elif not grounded(task_text, name):
                downgrade("interface name not grounded")
            elif not isinstance(fields, list) or not fields:
                downgrade("interface fields missing")
            else:
                for f in fields:
                    if not isinstance(f, dict):
                        downgrade("invalid interface field")
                        break
                    fn = str(f.get("name") or "")
                    ft = str(f.get("type") or "")
                    if not grounded(task_text, fn) or not grounded(task_text, ft):
                        downgrade("interface field/type not grounded")
                        break

        cleaned.append({
            "id": rid,
            "requirement": requirement,
            "primitive": primitive,
            "args": args,
            "reason": reason,
        })

    return cleaned, warnings


def coverage(primitive):
    if primitive in {"FILE_EXISTS", "TS_INTERFACE_FIELDS"}:
        return "FULL"
    if primitive in {"STRING_LITERAL_IN_FILE", "IDENTIFIER_IN_FILE"}:
        return "PARTIAL"
    return "UNVERIFIED"


HELPERS = r"""
import os
import re
from pathlib import Path
import pytest

REPO_DIR = Path(os.environ.get("REPO_DIR", "__REPO__"))

def _read(rel):
    p = REPO_DIR / rel
    assert p.is_file(), f"Required file does not exist: {p}"
    return p.read_text(encoding="utf-8", errors="replace")

def _strip_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return re.sub(r"//[^\n]*", "", text)

def _interface_body(text, name):
    m = re.search(r"\binterface\s+" + re.escape(name) + r"\b[^{]*\{", text)
    if not m:
        return None
    start = text.find("{", m.start())
    depth = 0
    quote = None
    escaped = False
    i = start
    while i < len(text):
        ch = text[i]
        if quote is not None:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
            i += 1
            continue
        if text.startswith("//", i):
            j = text.find("\n", i + 2)
            i = len(text) if j < 0 else j + 1
            continue
        if text.startswith("/*", i):
            j = text.find("*/", i + 2)
            if j < 0:
                return None
            i = j + 2
            continue
        if ch in {"'", '"', "`"}:
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start+1:i]
        i += 1
    return None

def _field_type(body, field, typ):
    if body is None:
        return False
    body = _strip_comments(body)
    body = re.sub(r"\s+", "", body)
    field = re.escape(re.sub(r"\s+", "", field))
    typ = re.escape(re.sub(r"\s+", "", typ))
    return bool(re.search(r"(^|[;,{])" + field + r"\??:" + typ + r"(?=[;,}]|$)", body))

def _string_literal(text, value):
    text = _strip_comments(text)
    return bool(re.search(r"(['\"])" + re.escape(value) + r"\1", text))

def _identifier(text, value):
    text = _strip_comments(text)
    return bool(re.search(r"\b" + re.escape(value) + r"\b", text))
"""


def safe_name(text):
    return re.sub(r"[^A-Za-z0-9_]+", "_", text).strip("_").lower()


def compile_verifier(task_id, reqs, repo_dir):
    lines = [
        '"""Task-aligned conservative verifier for ' + task_id + '."""',
        "",
        HELPERS.replace("__REPO__", repo_dir).strip(),
        "",
    ]
    mapping = []

    for i, req in enumerate(reqs, 1):
        prim = req["primitive"]
        cov = coverage(prim)

        if prim == "UNVERIFIED":
            mapping.append({
                **req,
                "test_name": "UNVERIFIED",
                "coverage": "UNVERIFIED",
            })
            continue

        test_name = f"test_{safe_name(req['id']) or f'r{i}'}_{prim.lower()}"
        args = req["args"]
        lines.append(f"def {test_name}():")
        lines.append(f"    # {req['requirement']}")

        if prim == "FILE_EXISTS":
            path = args["path"]
            lines.append(f"    p = REPO_DIR / {path!r}")
            lines.append(f"    assert p.is_file(), {('Missing required file: ' + path)!r}")

        elif prim == "STRING_LITERAL_IN_FILE":
            path, value = args["path"], args["value"]
            lines.append(f"    text = _read({path!r})")
            lines.append(f"    assert _string_literal(text, {value!r}), {('Missing required string literal: ' + value)!r}")

        elif prim == "IDENTIFIER_IN_FILE":
            path, value = args["path"], args["value"]
            lines.append(f"    text = _read({path!r})")
            lines.append(f"    assert _identifier(text, {value!r}), {('Missing required identifier: ' + value)!r}")

        elif prim == "TS_INTERFACE_FIELDS":
            path = args["path"]
            name = args["interface_name"]
            lines.append(f"    text = _read({path!r})")
            lines.append(f"    body = _interface_body(text, {name!r})")
            lines.append(f"    assert body is not None, {('Missing required interface: ' + name)!r}")
            for f in args["fields"]:
                msg = f"{name} missing exact field/type {f['name']}: {f['type']}"
                lines.append(f"    assert _field_type(body, {f['name']!r}, {f['type']!r}), {msg!r}")

        lines.append("")
        mapping.append({
            **req,
            "test_name": test_name,
            "coverage": cov,
        })

    if not any(x["test_name"] != "UNVERIFIED" for x in mapping):
        lines += [
            "def test_no_sound_automatic_checks_available():",
            "    pytest.skip('No sound executable checks derivable with supported primitives.')",
            "",
        ]

    return "\n".join(lines), mapping


def validate_mapping(source, mapping):
    tests = set(re.findall(r"^def\s+(test_[A-Za-z0-9_]+)\s*\(", source, flags=re.MULTILINE))
    for item in mapping:
        name = item["test_name"]
        if name != "UNVERIFIED" and name not in tests:
            raise ValueError(f"Mapping references missing test: {name}")


def safe_filename(task_id):
    return "test_" + re.sub(r"[^A-Za-z0-9_]+", "_", task_id).strip("_") + ".py"


def main():
    args = parse_args()
    tasks_dir = args.tasks_dir.expanduser().resolve()
    config_path = args.config.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    output_dir.mkdir(parents=True, exist_ok=True)
    plans_dir = output_dir / "_plans_v6"
    meta_dir = output_dir / "_metadata_v6"
    plans_dir.mkdir(exist_ok=True)
    meta_dir.mkdir(exist_ok=True)

    config = load_config(config_path)
    metadata = repo_metadata(config)

    tasks = sorted(tasks_dir.glob("*.md"))
    if args.only:
        wanted = set(args.only)
        tasks = [p for p in tasks if p.stem in wanted]
    if args.limit:
        tasks = tasks[:args.limit]

    if not tasks:
        raise SystemExit("No task files selected")

    api = client()
    model = model_name(args)

    print(f"Tasks selected: {len(tasks)}")
    print(f"Model: {model}")
    print(f"Output: {output_dir}")
    print("Architecture: LLM plan -> deterministic compiler")
    print()

    summary = []

    for n, task_path in enumerate(tasks, 1):
        task_id = task_path.stem
        out = output_dir / safe_filename(task_id)

        if out.exists() and not args.overwrite:
            print(f"[{n}/{len(tasks)}] SKIP {task_id}")
            continue

        print(f"[{n}/{len(tasks)}] PLAN {task_id}")
        task_text = task_path.read_text(encoding="utf-8", errors="replace")
        m = metadata.get(task_id, {})
        repo_name = m.get("repo_name", "")
        repo_dir = f"/workspace/{repo_name}" if repo_name else "/workspace"

        try:
            raw = call_plan(api, model, {
                "task_id": task_id,
                "repository_context": {
                    "repo_url": m.get("repo_url", ""),
                    "repo_name": repo_name,
                    "base_commit": m.get("commit", ""),
                    "default_repo_dir": repo_dir,
                },
                "task_specification": task_text,
            })

            reqs, warnings = sanitize(raw, task_text)
            source, mapping = compile_verifier(task_id, reqs, repo_dir)
            validate_mapping(source, mapping)
            compile(source, str(out), "exec")

            out.write_text(source, encoding="utf-8")

            counts = {
                k: sum(1 for x in mapping if x["coverage"] == k)
                for k in ["FULL", "PARTIAL", "UNVERIFIED"]
            }

            (plans_dir / f"{task_id}.json").write_text(
                json.dumps({
                    "task_id": task_id,
                    "model": model,
                    "raw_plan": raw,
                    "sanitized_requirements": reqs,
                    "warnings": warnings,
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            (meta_dir / f"{task_id}.json").write_text(
                json.dumps({
                    "task_id": task_id,
                    "repo": m,
                    "coverage_counts": counts,
                    "requirements": mapping,
                    "warnings": warnings,
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            print(
                f"  saved: {out.name} | FULL={counts['FULL']} "
                f"PARTIAL={counts['PARTIAL']} UNVERIFIED={counts['UNVERIFIED']}"
            )
            if warnings:
                print(f"  sanitizer warnings: {len(warnings)}")
            print("  syntax: OK")

            summary.append({
                "task_id": task_id,
                "status": "ok",
                "coverage": counts,
                "warnings": len(warnings),
            })

        except Exception as e:
            print(f"  ERROR: {type(e).__name__}: {e}", file=sys.stderr)
            summary.append({
                "task_id": task_id,
                "status": "error",
                "error": f"{type(e).__name__}: {e}",
            })

    summary_path = output_dir / "batch1_v6_summary.json"
    summary_path.write_text(
        json.dumps({"model": model, "results": summary}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    ok = sum(1 for x in summary if x["status"] == "ok")
    err = sum(1 for x in summary if x["status"] == "error")
    print()
    print("=" * 72)
    print(f"Done. OK={ok}, errors={err}")
    print(f"Summary: {summary_path}")
    print("=" * 72)

    if err:
        sys.exit(2)


if __name__ == "__main__":
    main()
