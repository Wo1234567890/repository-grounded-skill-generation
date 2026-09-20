#!/usr/bin/env python3
"""
Generate task-aligned deterministic pytest verifiers for SWE-Skills-Bench batch1.

Design goals
------------
1. Ground each verifier only in:
   - the task Markdown specification; and
   - non-solution benchmark metadata (repo URL/name/commit) from benchmark_config.yaml.
2. Never use agent outputs, patches, trajectories, gold solutions, hidden tests, or
   original benchmark verifier code as generation input.
3. Use a second LLM review pass to detect:
   - invented requirements;
   - missing task requirements;
   - over-broad repository scans;
   - weak proxy checks;
   - contradictions with the task.
4. Save the generated verifier, requirement mapping, review record, and summary.
5. Syntax-check every saved Python verifier with py_compile.

Example
-------
python generate_batch1_verifiers.py \
  --tasks-dir ~/Desktop/skill-generation/experiment2/tasks/swe/batch1 \
  --config ~/Desktop/skill-generation/experiment2/config/benchmark_batch1.yaml \
  --output-dir ~/Desktop/skill-generation/experiment2/verifiers/swe/batch1

Smoke test one task first:
python generate_batch1_verifiers.py ... --only analytics-events

Environment
-----------
Uses ANTHROPIC_AUTH_TOKEN or ANTHROPIC_API_KEY.
Model priority:
  --model
  VERIFIER_MODEL
  ANTHROPIC_DEFAULT_SONNET_MODEL
  claude-haiku-4-5-20251001
"""

from __future__ import annotations

import argparse
import ast
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
    print("Missing dependency: pyyaml. Install with: pip install pyyaml", file=sys.stderr)
    raise

try:
    from anthropic import Anthropic
except ImportError:
    print("Missing dependency: anthropic. Install with: pip install anthropic", file=sys.stderr)
    raise


GENERATOR_SYSTEM = r"""
You are constructing a task-aligned deterministic verifier for a software-engineering benchmark.

SOURCE-OF-TRUTH POLICY:
- Derive requirements ONLY from the supplied task specification.
- Repository URL/name/base commit are context for locating the repository only.
- Never use or assume agent output, trajectories, generated patches, gold patches,
  hidden tests, human solutions, or the benchmark's original verifier.
- The verifier must be fixed independently of experimental outcomes.

STRICT REQUIREMENT FIDELITY:
- Do NOT invent requirements that are absent from the task.
- Do NOT strengthen OR weaken an explicit task requirement.
- Preserve exact numeric/count requirements.
- Preserve exact literal types when explicitly specified.
  Example: Record<string, unknown> MUST NOT accept Record<string, any>.
- If the task explicitly requires an interface, do not silently accept a type alias
  unless the task itself permits both.
- Do NOT assume identifier names, type names, helper names, class names, function
  names, or implementation architecture unless the task explicitly specifies them.
- A requirement such as "include TypeScript type definitions for each payload"
  does NOT imply names such as DashboardViewedPayload or QuestionSavedPayload.

FILE SCOPE:
- If the task specifies exact file paths, check those exact paths.
- Do not scan the entire repository for vaguely similar files when an exact path is given.
- Do not allow unrelated pre-existing repository files to satisfy the requested change.

STRUCTURAL CHECKING:
- Structural requirements must be checked within the relevant syntactic scope.
  Example: fields required in AnalyticsEvent must all be verified inside the
  AnalyticsEvent body, not independently somewhere else in the file.
- Object/interface/type field checks MUST be order-independent unless the task
  explicitly requires an order.
- Do not rely on a regex that assumes fields appear in a particular sequence.
- Avoid plain substring checks for structural requirements.
- Comments and unrelated strings should not satisfy structural requirements.
- Prefer small deterministic helpers that extract the relevant balanced-brace
  block and then inspect that block.
- When a sound structural association cannot be established from the available
  source, mark the requirement PARTIAL or UNVERIFIED rather than inventing a proxy.

NAMING REQUIREMENTS:
- Verify the exact names explicitly required by the task.
- Do not prohibit unrelated camelCase or other identifiers unless the task
  explicitly prohibits them.
- For a requirement such as "required payload fields use snake_case", checking
  the specified required fields is preferable to globally banning camelCase.

BEHAVIORAL REQUIREMENTS:
- Runtime behavior must not be claimed FULLY verified by static string matching.
- If deterministic execution can be derived directly from the task and requires
  no invented assumptions, it may be tested.
- Otherwise mark runtime behavior PARTIAL or UNVERIFIED.

BUILD / TYPECHECK:
- Do not invent npm, yarn, pnpm, Maven, Gradle, TypeScript, or other commands
  that are not supplied or established by the provided context.
- Brace balancing is NOT equivalent to compilation.
- If real compilation cannot be soundly performed, mark compilation PARTIAL or
  UNVERIFIED and describe exactly what is checked.

GENERAL QUALITY:
- Checks must be deterministic.
- Every assertion must correspond to a task requirement.
- Every failed assertion should have a useful message.
- The verifier must be pytest-compatible and self-contained.
- Use REPO_DIR from an environment variable with the supplied default repository path.
- If a task requirement cannot be soundly verified, explicitly record it as
  UNVERIFIED instead of creating a weak proxy just to increase coverage.

OUTPUT:
Return ONLY a valid JSON object, no Markdown fences, with exactly:
{
  "verifier_py": "<complete Python pytest file>",
  "requirement_mapping": [
    {
      "requirement": "<task requirement>",
      "test_name": "<pytest test name or UNVERIFIED>",
      "coverage": "FULL|PARTIAL|UNVERIFIED",
      "reason": "<short explanation>"
    }
  ],
  "notes": ["<optional short note>"]
}
"""


REVIEWER_SYSTEM = r"""
You are the independent second-stage reviewer for a task-aligned software benchmark verifier.

The task specification is the ONLY source of evaluation requirements.
Repository metadata may only be used to locate the repository.

Review every task requirement against the proposed verifier.

You MUST reject and fix the verifier if ANY of the following occurs:

1. INVENTED REQUIREMENT
- It tests something the task never required.
- It introduces extra event counts, fields, APIs, filenames, commands, behaviors,
  naming restrictions, or implementation choices.

2. REQUIREMENT STRENGTHENING OR WEAKENING
- Explicit counts or thresholds differ from the task.
- Exact specified types are widened or narrowed.
  Example: task says Record<string, unknown>, verifier accepting `any` is incorrect.
- A required interface is replaced by acceptance of an unrelated construct.

3. INVENTED IDENTIFIER / ARCHITECTURE
- It assumes type names, class names, function names, variable names, or helper
  structure not specified by the task.
- Example: requiring a type named DashboardViewed is invalid if the task merely
  asks for a TypeScript payload definition.

4. WRONG FILE SCOPE
- It scans the whole repository when the task gives exact paths.
- Existing unrelated repository content can satisfy the test.

5. WRONG SYNTACTIC SCOPE
- Fields that must belong to one interface/type/object are searched globally.
- Independent strings anywhere in the file can satisfy one structural requirement.
- Comments or unrelated text can satisfy a structural requirement.

6. ORDER-SENSITIVE STRUCTURAL CHECK
- A regex requires fields to occur in one arbitrary order even though the task
  does not specify ordering.
- Rewrite such checks so field order does not affect PASS/FAIL.

7. WEAK PROXY
- Runtime behavior is claimed FULLY verified using static substring matching.
- Compilation is claimed verified through brace/bracket balancing.
- Keyword counts are used when a direct deterministic structural check is possible.

8. UNSOUND NEGATIVE CHECK
- It globally prohibits camelCase or other constructs when the task only requires
  particular specified names to use snake_case.

9. MISSING REQUIREMENT
- An important explicit task requirement is omitted without being represented as
  PARTIAL or UNVERIFIED in the requirement mapping.

10. NON-DETERMINISM OR INVALID PYTHON
- The verifier is non-deterministic, unsafe, malformed, or not pytest-compatible.

CORRECTION POLICY:
- Fix every detected issue while remaining strictly grounded in the task.
- Prefer exact-path and syntactically scoped checks.
- Use order-independent field-set checks.
- NEVER test a naming rule by applying the naming predicate only to hard-coded
  expected strings inside the verifier. The test must inspect identifiers or
  properties extracted from the submitted repository file.
- NEVER fall back from a failed event/type association to searching the entire
  file. If the association cannot be established soundly, mark that requirement
  PARTIAL or UNVERIFIED.
- A global `field in content` or equivalent substring test is NOT sufficient to
  claim that a field belongs to a particular payload.
- If the task explicitly names a file that must be created or modified, exact
  file existence is directly verifiable and should be tested.
- Reviewer notes and requirement_mapping MUST describe what the FINAL verifier
  actually does, not what an earlier draft did.
- If a requirement cannot be verified soundly from the available information,
  mark it PARTIAL or UNVERIFIED instead of inventing a proxy.

MINIMAL-SOUNDNESS MODE:
- Soundness is more important than coverage.
- If associating a field with a particular event/type requires guessing an
  unspecified type name or implementation structure, DO NOT guess.
  Mark that requirement PARTIAL or UNVERIFIED.
- Do NOT use whole-file substring presence to claim structural association.
- Do NOT use fallback logic that searches the whole file after a scoped search fails.
- Do NOT create tests that simply validate hard-coded expected strings, e.g.
  assert is_snake_case("dashboard_viewed"). Such a test validates the verifier,
  not the submitted implementation.
- Do NOT globally prohibit camelCase unless the task explicitly requires that.
- Exact file existence is directly verifiable when the task gives the path.
- Exact explicitly named interface fields may be checked only inside that
  extracted interface body.
- A requirement_mapping entry marked FULL must be supported by tests that
  directly verify that requirement.
- requirement_mapping may reference ONLY test functions that actually exist
  in verifier_py.

REQUIREMENT-MAPPING CONTRACT:
- `coverage` must be exactly one of FULL, PARTIAL, UNVERIFIED.
- `test_name` must NEVER be the literal value FULL or PARTIAL.
- If coverage is FULL:
  `test_name` must list one or more real pytest test functions that directly verify the requirement.
- If coverage is PARTIAL:
  `test_name` must list one or more real pytest test functions that perform the partial verification.
  The `reason` must clearly state what remains unverified.
- If there is no real executable test for the requirement:
  use `test_name: "UNVERIFIED"` and `coverage: "UNVERIFIED"`.
- Every test function referenced in requirement_mapping must exist in verifier_py.
- Do not claim PARTIAL coverage without an actual executable partial test.
- It is acceptable for a verifier to have UNVERIFIED requirements.
  Soundness is more important than artificial coverage.

Return ONLY valid JSON, no Markdown fences:
{
  "verdict": "PASS|FIXED",
  "issues": ["<issue>"],
  "verifier_py": "<final complete Python pytest file>",
  "requirement_mapping": [
    {
      "requirement": "<task requirement>",
      "test_name": "<pytest test name or UNVERIFIED>",
      "coverage": "FULL|PARTIAL|UNVERIFIED",
      "reason": "<short explanation>"
    }
  ]
}
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--tasks-dir", type=Path, required=True)
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--model", default=None)
    p.add_argument("--only", nargs="*", default=None,
                   help="Task IDs to generate, e.g. --only analytics-events django-patterns")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--no-review", action="store_true",
                   help="Skip the independent second LLM review pass")
    p.add_argument("--sleep", type=float, default=0.5,
                   help="Seconds between API calls")
    return p.parse_args()


def load_config(path: Path) -> dict[str, Any]:
    with path.expanduser().open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def skill_metadata(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in config.get("skills", []):
        tid = item.get("id")
        if not tid:
            continue
        repo = item.get("repo") or {}
        url = repo.get("url", "")
        name = ""
        if url:
            name = url.rstrip("/").split("/")[-1]
            if name.endswith(".git"):
                name = name[:-4]
        out[str(tid)] = {
            "repo_url": url,
            "repo_name": name,
            "commit": repo.get("commit", ""),
        }
    return out


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
            "or ANTHROPIC_API_KEY in this terminal."
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
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


def call_json(
    client: Anthropic,
    model: str,
    system: str,
    user_payload: str,
    max_tokens: int = 12000,
    retries: int = 3,
) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": user_payload}],
            )
            return extract_json(response_text(resp))
        except Exception as e:
            last_error = e
            if attempt == retries:
                break
            time.sleep(2 * attempt)
    assert last_error is not None
    raise last_error


def safe_test_filename(task_id: str) -> str:
    return "test_" + re.sub(r"[^A-Za-z0-9_]+", "_", task_id).strip("_") + ".py"


def default_repo_dir(meta: dict[str, Any]) -> str:
    name = meta.get("repo_name") or ""
    return f"/workspace/{name}" if name else "/workspace"


def generation_payload(task_id: str, task_text: str, meta: dict[str, Any]) -> str:
    return json.dumps(
        {
            "task_id": task_id,
            "repository_context": {
                "repo_url": meta.get("repo_url", ""),
                "repo_name": meta.get("repo_name", ""),
                "base_commit": meta.get("commit", ""),
                "default_repo_dir": default_repo_dir(meta),
            },
            "task_specification": task_text,
        },
        ensure_ascii=False,
        indent=2,
    )


def review_payload(
    task_id: str,
    task_text: str,
    meta: dict[str, Any],
    generated: dict[str, Any],
) -> str:
    return json.dumps(
        {
            "task_id": task_id,
            "repository_context": {
                "repo_url": meta.get("repo_url", ""),
                "repo_name": meta.get("repo_name", ""),
                "base_commit": meta.get("commit", ""),
                "default_repo_dir": default_repo_dir(meta),
            },
            "task_specification": task_text,
            "proposed_verifier_py": generated.get("verifier_py", ""),
            "proposed_requirement_mapping": generated.get("requirement_mapping", []),
        },
        ensure_ascii=False,
        indent=2,
    )



def validate_requirement_mapping(source: str, mapping):
    """
    Mechanical consistency audit:
    every mapped pytest test name must actually exist in verifier_py.
    """
    import ast

    tree = ast.parse(source)

    test_names = {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test_")
    }

    problems = []

    for item in mapping or []:
        coverage = item.get("coverage")
        test_name = str(item.get("test_name", "")).strip()

        if test_name == "UNVERIFIED":
            if coverage != "UNVERIFIED":
                problems.append(
                    f"{item.get('requirement')}: test_name is UNVERIFIED "
                    f"but coverage={coverage}"
                )
            continue

        names = [
            x.strip()
            for x in test_name.split(",")
            if x.strip()
        ]

        missing = [name for name in names if name not in test_names]

        if missing:
            problems.append(
                f"{item.get('requirement')}: mapping references "
                f"missing test(s): {missing}"
            )

    if problems:
        raise ValueError(
            "Requirement-mapping consistency check failed:\n- "
            + "\n- ".join(problems)
        )


def validate_python_source(source: str, target_path: Path) -> None:
    # Fast AST validation before writing.
    ast.parse(source)
    target_path.write_text(source.rstrip() + "\n", encoding="utf-8")
    # Compile the actual saved file too.
    py_compile.compile(str(target_path), doraise=True)


def main() -> None:
    args = parse_args()
    tasks_dir = args.tasks_dir.expanduser().resolve()
    config_path = args.config.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    if not tasks_dir.is_dir():
        raise SystemExit(f"Tasks directory not found: {tasks_dir}")
    if not config_path.is_file():
        raise SystemExit(f"Config file not found: {config_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir = output_dir / "_metadata"
    reviews_dir = output_dir / "_reviews"
    raw_dir = output_dir / "_raw"
    metadata_dir.mkdir(exist_ok=True)
    reviews_dir.mkdir(exist_ok=True)
    raw_dir.mkdir(exist_ok=True)

    config = load_config(config_path)
    metadata = skill_metadata(config)

    task_files = sorted(tasks_dir.glob("*.md"))
    if args.only:
        wanted = set(args.only)
        task_files = [p for p in task_files if p.stem in wanted]
    if args.limit is not None:
        task_files = task_files[: args.limit]

    if not task_files:
        raise SystemExit("No task Markdown files selected.")

    model = resolve_model(args)
    client = make_client()

    print(f"Tasks selected: {len(task_files)}")
    print(f"Model: {model}")
    print(f"Output: {output_dir}")
    print(f"Review pass: {'disabled' if args.no_review else 'enabled'}")
    print()

    summary: list[dict[str, Any]] = []

    for idx, task_path in enumerate(task_files, start=1):
        task_id = task_path.stem
        out_path = output_dir / safe_test_filename(task_id)
        mapping_path = metadata_dir / f"{task_id}.json"
        review_path = reviews_dir / f"{task_id}.json"

        if out_path.exists() and not args.overwrite:
            print(f"[{idx}/{len(task_files)}] SKIP {task_id} (exists)")
            summary.append({
                "task_id": task_id,
                "status": "skipped_existing",
                "verifier": str(out_path),
            })
            continue

        print(f"[{idx}/{len(task_files)}] GENERATE {task_id}")

        task_text = task_path.read_text(encoding="utf-8", errors="replace")
        meta = metadata.get(task_id, {})
        if not meta:
            print(f"  warning: no config metadata found for task {task_id}")

        try:
            generated = call_json(
                client,
                model,
                GENERATOR_SYSTEM,
                generation_payload(task_id, task_text, meta),
            )
            (raw_dir / f"{task_id}.generator.json").write_text(
                json.dumps(generated, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            final = generated
            review_record: dict[str, Any] | None = None

            if not args.no_review:
                current = generated
                review_history = []

                for review_round in range(1, 4):
                    time.sleep(args.sleep)

                    review_record = call_json(
                        client,
                        model,
                        REVIEWER_SYSTEM,
                        review_payload(task_id, task_text, meta, current),
                    )

                    review_history.append({
                        "round": review_round,
                        "verdict": review_record.get("verdict"),
                        "issues": review_record.get("issues", []),
                    })

                    (raw_dir / f"{task_id}.reviewer_round{review_round}.json").write_text(
                        json.dumps(review_record, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )

                    current = {
                        "verifier_py": review_record.get(
                            "verifier_py", current.get("verifier_py", "")
                        ),
                        "requirement_mapping": review_record.get(
                            "requirement_mapping",
                            current.get("requirement_mapping", []),
                        ),
                        "notes": current.get("notes", []),
                    }

                    if review_record.get("verdict") == "PASS":
                        break

                final = current

                if review_record.get("verdict") != "PASS":
                    raise ValueError(
                        "Verifier did not reach reviewer PASS within 3 rounds"
                    )

            source = final.get("verifier_py")
            if not isinstance(source, str) or not source.strip():
                raise ValueError("Model did not return non-empty verifier_py")

            validate_requirement_mapping(
                source,
                final.get("requirement_mapping", []),
            )

            validate_python_source(source, out_path)

            mapping_doc = {
                "task_id": task_id,
                "task_file": str(task_path),
                "repo": meta,
                "model": model,
                "generation_policy": {
                    "task_spec_only": True,
                    "agent_outputs_used": False,
                    "gold_patch_used": False,
                    "original_verifier_used": False,
                    "review_pass": not args.no_review,
                },
                "requirement_mapping": final.get("requirement_mapping", []),
                "notes": final.get("notes", []),
            }
            mapping_path.write_text(
                json.dumps(mapping_doc, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            if review_record is not None:
                review_path.write_text(
                    json.dumps(
                        {
                            "task_id": task_id,
                            "verdict": review_record.get("verdict"),
                            "issues": review_record.get("issues", []),
                        },
                        ensure_ascii=False,
                        indent=2,
                    ),
                    encoding="utf-8",
                )

            summary.append({
                "task_id": task_id,
                "status": "ok",
                "review_verdict": (
                    review_record.get("verdict") if review_record else "NOT_RUN"
                ),
                "verifier": str(out_path),
                "mapping": str(mapping_path),
            })
            print(f"  saved: {out_path.name}")
            print("  syntax: OK")
            if review_record is not None:
                print(f"  review: {review_record.get('verdict', 'UNKNOWN')}")

        except Exception as e:
            print(f"  ERROR: {type(e).__name__}: {e}", file=sys.stderr)
            summary.append({
                "task_id": task_id,
                "status": "error",
                "error": f"{type(e).__name__}: {e}",
            })

        time.sleep(args.sleep)

    summary_path = output_dir / "batch1_verifier_summary.json"
    summary_path.write_text(
        json.dumps(
            {
                "model": model,
                "tasks_selected": len(task_files),
                "results": summary,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    ok = sum(1 for x in summary if x["status"] == "ok")
    skipped = sum(1 for x in summary if x["status"] == "skipped_existing")
    errors = sum(1 for x in summary if x["status"] == "error")

    print()
    print("=" * 72)
    print(f"Done. OK={ok}, skipped={skipped}, errors={errors}")
    print(f"Summary: {summary_path}")
    print("=" * 72)

    if errors:
        sys.exit(2)


if __name__ == "__main__":
    main()
