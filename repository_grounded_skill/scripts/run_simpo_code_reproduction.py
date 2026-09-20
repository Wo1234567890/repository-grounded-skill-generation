from __future__ import annotations

import argparse
import json
import sys

from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv


# ============================================================
# Project root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(PROJECT_ROOT),
    )

load_dotenv(
    PROJECT_ROOT / ".env"
)


# ============================================================
# Project imports
# ============================================================

from src.agents.claude_agent import ClaudeCodingAgent
from src.clients.llm_client import FixedLLMClient
from src.pipeline import run_repository_grounded_pipeline


# ============================================================
# Fixed experiment configuration
# ============================================================

TASK_NAME = "simpo-code-reproduction"

TARGET_MODEL = "claude-haiku-4-5-20251001"
AUX_MODEL = "claude-sonnet-4-6"

EXPECTED_BASE_COMMIT = (
    "86fa6b3e97715093daf7e12cf232612c0aee457e"
)

HOME = Path.home()

SKILL_GENERATION_ROOT = (
    HOME
    / "Desktop"
    / "skill-generation"
)

TASK_DIR = (
    SKILL_GENERATION_ROOT
    / "experiments"
    / "tasks"
    / "skillsbench"
    / TASK_NAME
)

TASK_FILE = (
    TASK_DIR
    / "task.md"
)

TRAJECTORY_SKILL_FILE = (
    SKILL_GENERATION_ROOT
    / "experiments"
    / "trajectory_generated_skills"
    / TASK_NAME
    / "SKILL.md"
)

ANYTHING2SKILL_FILE = (
    SKILL_GENERATION_ROOT
    / "anything2skill"
    / "eval_skills_swe"
    / TASK_NAME
    / "simpo-model-training-launch"
    / "SKILL.md"
)

NO_SKILL_RUN_DIR = (
    SKILL_GENERATION_ROOT
    / "skillsbench"
    / "jobs"
    / "simpo-code-reproduction_skillx_noskill_run2"
)

REPOSITORY_PATH = (
    HOME
    / "Desktop"
    / "repository_grounded_tasks"
    / TASK_NAME
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "outputs"
    / TASK_NAME
    / "run1"
)

EVALUATION_SKILL_DIR = (
    SKILL_GENERATION_ROOT
    / "experiments"
    / "repository_grounded_skills"
    / TASK_NAME
)


# ============================================================
# File helpers
# ============================================================

def read_text(
    path: Path,
) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"Required file does not exist:\n{path}"
        )

    if not path.is_file():
        raise RuntimeError(
            f"Expected a file but found something else:\n{path}"
        )

    return path.read_text(
        encoding="utf-8"
    )


def extract_task_description(
    task_text: str,
) -> str:
    """
    SkillsBench task.md contains YAML front matter.

    The actual agent prompt is the body after the closing '---'.
    This matches the prompt used in the benchmark trajectory.
    """

    stripped = task_text.lstrip()

    if not stripped.startswith("---"):
        return task_text.strip()

    lines = stripped.splitlines()

    closing_index = None

    for index in range(
        1,
        len(lines),
    ):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise RuntimeError(
            "task.md starts with YAML front matter but "
            "the closing '---' delimiter was not found."
        )

    body = "\n".join(
        lines[
            closing_index + 1:
        ]
    ).strip()

    if not body:
        raise RuntimeError(
            "Task description is empty after removing YAML front matter."
        )

    return body


def find_precomputed_trajectory() -> Path:
    """
    Use the fixed experimental rule:

    simpo-code-reproduction -> no-skill run2 (run1 trajectory was empty; earliest technically valid fallback).

    The timestamp / rollout id is discovered automatically so that
    the script does not depend on those generated directory names.
    """

    if not NO_SKILL_RUN_DIR.exists():
        raise FileNotFoundError(
            "No-skill run1 directory does not exist:\n"
            f"{NO_SKILL_RUN_DIR}"
        )

    matches = sorted(
        NO_SKILL_RUN_DIR.glob(
            "*/simpo-code-reproduction__*/trajectory/acp_trajectory.jsonl"
        )
    )

    if len(matches) == 0:
        raise FileNotFoundError(
            "Could not find run1 ACP trajectory under:\n"
            f"{NO_SKILL_RUN_DIR}"
        )

    if len(matches) > 1:
        raise RuntimeError(
            "More than one ACP trajectory was found in run1. "
            "Refusing to select one implicitly.\n\n"
            + "\n".join(
                str(path)
                for path in matches
            )
        )

    return matches[0]


def load_jsonl_trajectory(
    path: Path,
) -> List[Dict[str, Any]]:
    trajectory: List[
        Dict[str, Any]
    ] = []

    with path.open(
        "r",
        encoding="utf-8",
    ) as handle:

        for line_number, line in enumerate(
            handle,
            start=1,
        ):
            line = line.strip()

            if not line:
                continue

            try:
                event = json.loads(
                    line
                )
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    "Invalid JSON in trajectory.\n"
                    f"File: {path}\n"
                    f"Line: {line_number}\n"
                    f"Error: {exc}"
                ) from exc

            if not isinstance(
                event,
                dict,
            ):
                raise RuntimeError(
                    "Every trajectory JSONL line must contain "
                    "a JSON object.\n"
                    f"File: {path}\n"
                    f"Line: {line_number}"
                )

            trajectory.append(
                event
            )

    if not trajectory:
        raise RuntimeError(
            f"Trajectory is empty:\n{path}"
        )

    return trajectory


# ============================================================
# Serialization
# ============================================================

def make_serializable(
    value: Any,
) -> Any:

    if is_dataclass(value):
        return {
            key: make_serializable(item)
            for key, item
            in asdict(value).items()
        }

    if isinstance(
        value,
        Path,
    ):
        return str(
            value
        )

    if isinstance(
        value,
        dict,
    ):
        return {
            str(key): make_serializable(item)
            for key, item
            in value.items()
        }

    if isinstance(
        value,
        (list, tuple),
    ):
        return [
            make_serializable(item)
            for item in value
        ]

    if isinstance(
        value,
        (str, int, float, bool),
    ) or value is None:
        return value

    return str(
        value
    )


# ============================================================
# Input validation
# ============================================================

def validate_inputs() -> None:

    required_files = [
        TASK_FILE,
        TRAJECTORY_SKILL_FILE,
        ANYTHING2SKILL_FILE,
    ]

    for path in required_files:
        if not path.exists():
            raise FileNotFoundError(
                f"Required input file is missing:\n{path}"
            )

    if not REPOSITORY_PATH.exists():
        raise FileNotFoundError(
            "Repository snapshot is missing:\n"
            f"{REPOSITORY_PATH}"
        )

    git_dir = (
        REPOSITORY_PATH
        / ".git"
    )

    if not git_dir.exists():
        raise RuntimeError(
            "Repository snapshot does not contain .git:\n"
            f"{REPOSITORY_PATH}"
        )


# ============================================================
# Main experiment
# ============================================================

def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Run repository-grounded residual skill generation "
            "for simpo-code-reproduction."
        )
    )

    parser.add_argument(
        "--check-only",
        action="store_true",
        help=(
            "Validate and print all experiment inputs "
            "without making any API calls."
        ),
    )

    args = parser.parse_args()

    print()
    print(
        "=============================================="
    )
    print(
        " Repository-Grounded Skill Experiment"
    )
    print(
        "=============================================="
    )
    print(
        f"Task:         {TASK_NAME}"
    )
    print(
        f"Target model: {TARGET_MODEL}"
    )
    print(
        f"Aux model:    {AUX_MODEL}"
    )
    print()

    # --------------------------------------------------------
    # Validate paths
    # --------------------------------------------------------

    validate_inputs()

    trajectory_path = (
        find_precomputed_trajectory()
    )

    # --------------------------------------------------------
    # Read task
    # --------------------------------------------------------

    raw_task_text = (
        read_text(
            TASK_FILE
        )
    )

    task_description = (
        extract_task_description(
            raw_task_text
        )
    )

    # --------------------------------------------------------
    # Read candidate skills
    # --------------------------------------------------------

    trajectory_skill = (
        read_text(
            TRAJECTORY_SKILL_FILE
        )
    )

    anything2skill = (
        read_text(
            ANYTHING2SKILL_FILE
        )
    )

    candidate_skills = {
        "trajectory_generated": (
            trajectory_skill
        ),
        "anything2skill": (
            anything2skill
        ),
    }

    # --------------------------------------------------------
    # Read existing benchmark trajectory
    # --------------------------------------------------------

    trajectory = (
        load_jsonl_trajectory(
            trajectory_path
        )
    )

    # --------------------------------------------------------
    # Print experiment manifest
    # --------------------------------------------------------

    print(
        "===== INPUT MANIFEST ====="
    )

    print(
        f"Task file:\n  {TASK_FILE}"
    )

    print(
        f"Repository:\n  {REPOSITORY_PATH}"
    )

    print(
        f"Base commit:\n  {EXPECTED_BASE_COMMIT}"
    )

    print(
        f"No-skill trajectory:\n  {trajectory_path}"
    )

    print(
        f"Trajectory events:\n  {len(trajectory)}"
    )

    print(
        f"Trajectory skill:\n  {TRAJECTORY_SKILL_FILE}"
    )

    print(
        f"Anything2Skill:\n  {ANYTHING2SKILL_FILE}"
    )

    print()

    print(
        "===== TASK DESCRIPTION ====="
    )
    print(
        task_description
    )
    print()

    print(
        "===== CANDIDATE SKILLS ====="
    )
    print(
        f"trajectory_generated: {len(trajectory_skill)} characters"
    )
    print(
        f"anything2skill:       {len(anything2skill)} characters"
    )
    print()

    if args.check_only:
        print(
            "CHECK ONLY: all required experiment inputs are available."
        )
        print(
            "No API calls were made."
        )
        return

    # --------------------------------------------------------
    # Create output directory
    # --------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    manifest = {
        "task_name": TASK_NAME,
        "target_model": TARGET_MODEL,
        "aux_model": AUX_MODEL,
        "expected_base_commit": (
            EXPECTED_BASE_COMMIT
        ),
        "repository_path": str(
            REPOSITORY_PATH
        ),
        "task_file": str(
            TASK_FILE
        ),
        "trajectory_path": str(
            trajectory_path
        ),
        "trajectory_event_count": len(
            trajectory
        ),
        "candidate_skill_files": {
            "trajectory_generated": str(
                TRAJECTORY_SKILL_FILE
            ),
            "anything2skill": str(
                ANYTHING2SKILL_FILE
            ),
        },
        "evaluation_skill_dir": str(
            EVALUATION_SKILL_DIR
        ),
    }

    (
        OUTPUT_DIR
        / "manifest.json"
    ).write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    (
        OUTPUT_DIR
        / "task_description.txt"
    ).write_text(
        task_description,
        encoding="utf-8",
    )

    (
        OUTPUT_DIR
        / "input_trajectory.json"
    ).write_text(
        json.dumps(
            trajectory,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Construct target agent
    # --------------------------------------------------------

    print(
        "===== CREATE TARGET AGENT ====="
    )

    agent = ClaudeCodingAgent(
        model=TARGET_MODEL,
        max_turns=50,
        max_tokens_per_turn=4096,
        command_timeout=120,
    )

    print(
        "Target agent ready."
    )

    # --------------------------------------------------------
    # Construct auxiliary LLM
    # --------------------------------------------------------

    print()
    print(
        "===== CREATE AUXILIARY LLM ====="
    )

    aux_llm = FixedLLMClient(
        model=AUX_MODEL,
        max_tokens=4096,
    )

    print(
        "Auxiliary LLM ready."
    )

    # --------------------------------------------------------
    # Run complete method
    # --------------------------------------------------------

    print()
    print(
        "===== START PIPELINE ====="
    )
    print()

    result = (
        run_repository_grounded_pipeline(
            agent=agent,
            repository_path=str(
                REPOSITORY_PATH
            ),
            expected_base_commit=(
                EXPECTED_BASE_COMMIT
            ),
            task_description=(
                task_description
            ),
            candidate_skills=(
                candidate_skills
            ),
            aux_llm=(
                aux_llm
            ),
            verbose=True,
            precomputed_trajectory=(
                trajectory
            ),
            checkpoint_path=(
                str(
                    OUTPUT_DIR
                    / "pipeline_checkpoint.pkl"
                )
            ),
            checkpoint_metadata={
                "task_name": (
                    TASK_NAME
                ),
                "target_model": (
                    TARGET_MODEL
                ),
                "aux_model": (
                    AUX_MODEL
                ),
                "trajectory_path": (
                    str(
                        trajectory_path
                    )
                ),
                "task_file": (
                    str(
                        TASK_FILE
                    )
                ),
                "trajectory_skill_file": (
                    str(
                        TRAJECTORY_SKILL_FILE
                    )
                ),
                "anything2skill_file": (
                    str(
                        ANYTHING2SKILL_FILE
                    )
                ),
            },
            resume_from_checkpoint=True,
        )
    )

    # --------------------------------------------------------
    # Save complete result
    # --------------------------------------------------------

    serializable_result = (
        make_serializable(
            result
        )
    )

    result_file = (
        OUTPUT_DIR
        / "pipeline_result.json"
    )

    result_file.write_text(
        json.dumps(
            serializable_result,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Save final residual skill
    # --------------------------------------------------------

    final_skill = (
        result.final_skill
        if result.final_skill
        else ""
    )

    final_skill_file = (
        OUTPUT_DIR
        / "FINAL_SKILL.md"
    )

    final_skill_file.write_text(
        final_skill,
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Save evaluation-ready residual skill
    #
    # An empty residual skill is a legitimate experimental
    # outcome. In that case we must NOT create a header-only
    # SKILL.md, because that would incorrectly turn the run
    # into a with-skill condition.
    # --------------------------------------------------------

    EVALUATION_SKILL_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    evaluation_skill_file = (
        EVALUATION_SKILL_DIR
        / "SKILL.md"
    )

    residual_skill_status_file = (
        OUTPUT_DIR
        / "residual_skill_status.json"
    )

    if final_skill.strip():

        evaluation_skill_text = (
            "---\n"
            "name: repository-grounded-residual-skill\n"
            "description: Repository-grounded residual knowledge "
            f"for {TASK_NAME}.\n"
            "---\n\n"
            "# Repository-Grounded Residual Skill\n\n"
            f"{final_skill.strip()}\n"
        )

        evaluation_skill_file.write_text(
            evaluation_skill_text,
            encoding="utf-8",
        )

        residual_skill_status = {
            "task": TASK_NAME,
            "status": "HAS_RESIDUAL_SKILL",
            "evaluation_skill_file": (
                str(
                    evaluation_skill_file
                )
            ),
        }

    else:

        # Remove a stale skill left by an older run.
        if evaluation_skill_file.exists():
            evaluation_skill_file.unlink()

        residual_skill_status = {
            "task": TASK_NAME,
            "status": "NO_RESIDUAL_SKILL",
            "evaluation_skill_file": None,
        }

    residual_skill_status_file.write_text(
        json.dumps(
            residual_skill_status,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Save compact target summary
    # --------------------------------------------------------

    target_summary = []

    for record in result.target_records:

        target_summary.append(
            {
                "gap_id": (
                    record.gap_id
                ),
                "target_id": (
                    record.target_id
                ),
                "status": (
                    record.status
                ),
                "baseline_majority_correct": (
                    None
                    if record.baseline_result is None
                    else record.baseline_result.majority_correct
                ),
                "repository_provided": (
                    None
                    if record.repository_redundancy is None
                    else record.repository_redundancy.is_provided
                ),
                "matching_candidate_ids": [
                    match.candidate_id
                    for match
                    in record.candidate_matches
                    if match.is_match
                ],
                "effective_candidate_ids": [
                    intervention.candidate_id
                    for intervention
                    in record.intervention_results
                    if intervention.delta == 1
                ],
                "representative_candidate_id": (
                    None
                    if record.representative is None
                    else record.representative.candidate_id
                ),
                "final_statement": (
                    None
                    if record.final_statement is None
                    else record.final_statement.text
                ),
            }
        )

    (
        OUTPUT_DIR
        / "target_summary.json"
    ).write_text(
        json.dumps(
            target_summary,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Print final summary
    # --------------------------------------------------------

    print()
    print(
        "=============================================="
    )
    print(
        " PIPELINE COMPLETED"
    )
    print(
        "=============================================="
    )

    print(
        f"Candidate units: {len(result.candidates)}"
    )

    print(
        f"Observed gaps:   {len(result.gaps)}"
    )

    print(
        f"Targets:         {len(result.targets)}"
    )

    print(
        f"Final statements:{len(result.final_statements)}"
    )

    print()

    print(
        "===== TARGET OUTCOMES ====="
    )

    for record in result.target_records:
        print(
            f"{record.target_id}: {record.status}"
        )

    print()
    print(
        "===== FINAL RESIDUAL SKILL ====="
    )

    if final_skill:
        print(
            final_skill
        )
    else:
        print(
            "[EMPTY]"
        )

    print()
    print(
        "===== OUTPUT FILES ====="
    )
    print(
        f"Manifest:\n  {OUTPUT_DIR / 'manifest.json'}"
    )
    print(
        f"Full result:\n  {result_file}"
    )
    print(
        f"Target summary:\n  {OUTPUT_DIR / 'target_summary.json'}"
    )
    print(
        f"Raw final skill:\n  {final_skill_file}"
    )
    if final_skill.strip():
        print(
            f"Evaluation SKILL.md:\n  {evaluation_skill_file}"
        )
    else:
        print(
            "Evaluation SKILL.md:\n"
            "  [NOT CREATED: NO_RESIDUAL_SKILL]"
        )

    print(
        "Residual skill status:\n"
        f"  {residual_skill_status_file}"
    )


if __name__ == "__main__":
    main()
