import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from src.clients.llm_client import FixedLLMClient
from src.config import CONFIG, ExperimentConfig
from src.models import (
    KnowledgeTarget,
    ObservedGap,
    RepositoryEvidence,
)
from src.tools.repository_tools import RepositoryTools


# ============================================================
# Shared Constants
# ============================================================

MAX_RETRIEVAL_ACTIONS = 12
MAX_EVIDENCE_CHARS_PER_ITEM = 8000

ALLOWED_EVIDENCE_TYPES = {
    "failing_test",
    "explicit_constraint",
    "source_code",
    "documentation",
}


# ============================================================
# Shared Helpers
# ============================================================

def _normalize_whitespace(
    text: str,
) -> str:
    """
    Normalize whitespace while preserving wording.

    This allows evidence spans containing line breaks to match
    equivalent text returned on one line by the auxiliary LLM.
    """

    return " ".join(
        text.split()
    ).strip()


# ============================================================
# Repository Snapshot Protection
# ============================================================

@dataclass
class RepositorySnapshotInfo:
    """
    Verified repository state used for repository-grounded
    evidence retrieval.
    """

    repository_root: str
    expected_commit: str
    head_commit: str
    clean: bool


def _run_git(
    repository_path: Path,
    args: List[str],
) -> str:
    """
    Execute one Git command without invoking a shell.
    """

    result = subprocess.run(
        [
            "git",
            "-C",
            str(repository_path),
            *args,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Git repository validation failed.\n"
            f"Command: git {' '.join(args)}\n"
            f"Repository: {repository_path}\n"
            f"Error: {result.stderr.strip()}"
        )

    return (
        result.stdout.strip()
    )


def verify_repository_snapshot(
    repository_path: str,
    expected_base_commit: str,
) -> RepositorySnapshotInfo:
    """
    Verify that repository evidence comes from exactly the
    expected base_commit and a clean working tree.

    This prevents accidental evidence leakage from:

    - gold patches;
    - benchmark test patches;
    - no-skill agent modifications;
    - staged changes;
    - unstaged changes;
    - untracked files.
    """

    expected_base_commit = (
        expected_base_commit.strip()
    )

    if not expected_base_commit:
        raise ValueError(
            "expected_base_commit is required."
        )

    repository = Path(
        repository_path
    ).expanduser().resolve()

    if not repository.exists():
        raise RuntimeError(
            f"Repository does not exist: {repository}"
        )

    if not repository.is_dir():
        raise RuntimeError(
            f"Repository path is not a directory: {repository}"
        )

    # --------------------------------------------------------
    # Confirm repository root
    # --------------------------------------------------------

    actual_root_text = _run_git(
        repository,
        [
            "rev-parse",
            "--show-toplevel",
        ],
    )

    actual_root = Path(
        actual_root_text
    ).resolve()

    if actual_root != repository:
        raise RuntimeError(
            "repository_path must point to the Git repository root.\n"
            f"Provided: {repository}\n"
            f"Actual root: {actual_root}"
        )

    # --------------------------------------------------------
    # Resolve expected commit
    # --------------------------------------------------------

    expected_commit = _run_git(
        repository,
        [
            "rev-parse",
            "--verify",
            f"{expected_base_commit}^{{commit}}",
        ],
    )

    # --------------------------------------------------------
    # Check HEAD
    # --------------------------------------------------------

    head_commit = _run_git(
        repository,
        [
            "rev-parse",
            "HEAD",
        ],
    )

    if head_commit != expected_commit:
        raise RuntimeError(
            "Repository is not at the required base_commit.\n"
            f"Expected: {expected_commit}\n"
            f"Current HEAD: {head_commit}"
        )

    # --------------------------------------------------------
    # Check staged / unstaged / untracked files
    # --------------------------------------------------------

    status = _run_git(
        repository,
        [
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        ],
    )

    if status:
        preview = status

        if len(preview) > 4000:
            preview = (
                preview[:4000]
                + "\n...[TRUNCATED]"
            )

        raise RuntimeError(
            "Repository working tree is not clean.\n"
            "Stage 1 repository evidence must come from a pristine "
            "base_commit snapshot.\n\n"
            f"git status:\n{preview}"
        )

    return RepositorySnapshotInfo(
        repository_root=str(
            repository
        ),
        expected_commit=(
            expected_commit
        ),
        head_commit=(
            head_commit
        ),
        clean=True,
    )


# ============================================================
# Stage 1A
# Observed Gap Discovery
# ============================================================

GAP_DISCOVERY_SYSTEM_PROMPT = """
You are the fixed auxiliary LLM used in a research pipeline for
repository-grounded knowledge probing.

Your current task is ONLY to identify observed execution gaps from
a target coding agent's no-skill execution trajectory.

An observed execution gap describes a concrete limitation, mistake,
omission, ineffective action, unsupported assumption, or unresolved
problem visible in the execution trajectory.

IMPORTANT:

An execution gap is NOT automatically a knowledge gap.

You must NOT claim that the agent lacks knowledge merely because
it failed to perform an action.

Every identified gap must be grounded in concrete trajectory
evidence.

Use evidence-bounded wording.

Prefer:

"no inspection is recorded in the supplied trajectory"

rather than:

"the agent never inspected".

Do not use external knowledge.
Do not invent repository facts.
Do not construct knowledge targets yet.
Do not generate diagnostic questions yet.
""".strip()


def _format_trajectory(
    trajectory: List[Dict[str, Any]],
) -> str:
    """
    Give each trajectory event a stable EVENT_ID.
    """

    formatted_events: List[
        str
    ] = []

    for index, event in enumerate(
        trajectory,
        start=1,
    ):
        event_id = (
            f"E{index}"
        )

        event_json = json.dumps(
            event,
            ensure_ascii=False,
            indent=2,
            default=str,
        )

        formatted_events.append(
            f"{event_id}\n{event_json}"
        )

    return "\n\n".join(
        formatted_events
    )


def _build_gap_prompt(
    task_description: str,
    trajectory_text: str,
) -> str:
    """
    Construct Stage 1A gap-discovery prompt.
    """

    return f"""
Identify the concrete observed execution gaps in the no-skill
execution below.

A gap must satisfy ALL of the following:

1. It is visible in the execution trajectory.

2. It describes something that went wrong, remained unresolved,
   was omitted despite being relevant to the attempted solution,
   or caused ineffective / unsupported execution.

3. It is specific enough that later stages could investigate
   repository-grounded knowledge relevant to the gap.

4. It does NOT assume that the cause is missing knowledge.

5. It cites one or more EVENT_ID values containing direct evidence.

6. Describe only what is observable from the supplied trajectory.
   Do not make stronger claims than the trajectory supports.

Do NOT identify a gap merely because a better strategy could be
imagined.

Do NOT use hindsight from a gold solution.

Do NOT use information absent from the task and trajectory.

If there is no concrete observable gap, return an empty gaps list.

Return exactly:

{{
  "gaps": [
    {{
      "description": "concise description of the observed gap",
      "event_ids": ["E2", "E5"]
    }}
  ]
}}

TASK:
----------------
{task_description}
----------------

NO-SKILL EXECUTION TRAJECTORY:
----------------
{trajectory_text}
----------------
""".strip()


def _validate_gap_output(
    parsed: Dict[str, Any],
    trajectory: List[
        Dict[str, Any]
    ],
) -> List[
    Dict[str, Any]
]:
    """
    Stage 1A uses fail-fast validation.

    Invalid event references are structural grounding errors.
    """

    gaps = parsed.get(
        "gaps"
    )

    if not isinstance(
        gaps,
        list,
    ):
        raise RuntimeError(
            "Stage 1A output must contain 'gaps' as a list."
        )

    valid_event_ids = {
        f"E{i}"
        for i in range(
            1,
            len(trajectory) + 1,
        )
    }

    validated: List[
        Dict[str, Any]
    ] = []

    for gap_index, gap in enumerate(
        gaps,
        start=1,
    ):
        if not isinstance(
            gap,
            dict,
        ):
            raise RuntimeError(
                f"Gap {gap_index} must be a JSON object."
            )

        description = gap.get(
            "description"
        )

        event_ids = gap.get(
            "event_ids"
        )

        if (
            not isinstance(
                description,
                str,
            )
            or not description.strip()
        ):
            raise RuntimeError(
                f"Gap {gap_index} has no valid description."
            )

        if (
            not isinstance(
                event_ids,
                list,
            )
            or not event_ids
        ):
            raise RuntimeError(
                f"Gap {gap_index} must cite at least one EVENT_ID."
            )

        clean_event_ids: List[
            str
        ] = []

        for event_id in event_ids:
            if not isinstance(
                event_id,
                str,
            ):
                raise RuntimeError(
                    f"Gap {gap_index} contains an invalid EVENT_ID."
                )

            event_id = (
                event_id.strip()
            )

            if (
                event_id
                not in valid_event_ids
            ):
                raise RuntimeError(
                    f"Gap {gap_index} cited nonexistent "
                    f"trajectory event: {event_id}"
                )

            if (
                event_id
                not in clean_event_ids
            ):
                clean_event_ids.append(
                    event_id
                )

        validated.append(
            {
                "description": (
                    description.strip()
                ),
                "event_ids": (
                    clean_event_ids
                ),
            }
        )

    return validated


def _get_event_by_id(
    trajectory: List[
        Dict[str, Any]
    ],
    event_id: str,
) -> Dict[str, Any]:
    """
    Retrieve E3 -> trajectory[2].
    """

    index = (
        int(
            event_id[1:]
        )
        - 1
    )

    return trajectory[
        index
    ]


def _serialize_evidence_events(
    trajectory: List[
        Dict[str, Any]
    ],
    event_ids: List[str],
) -> str:
    """
    Serialize concrete trajectory evidence for one gap.
    """

    parts: List[
        str
    ] = []

    for event_id in event_ids:
        event = (
            _get_event_by_id(
                trajectory=trajectory,
                event_id=event_id,
            )
        )

        parts.append(
            event_id
            + "\n"
            + json.dumps(
                event,
                ensure_ascii=False,
                indent=2,
                default=str,
            )
        )

    return "\n\n".join(
        parts
    )


def discover_observed_gaps(
    task_description: str,
    trajectory: List[
        Dict[str, Any]
    ],
    llm: Optional[
        FixedLLMClient
    ] = None,
) -> List[
    ObservedGap
]:
    """
    Stage 1A.

    Task + no-skill trajectory -> observed execution gaps.

    This stage does NOT infer missing knowledge.
    """

    task_description = (
        task_description.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if (
        not isinstance(
            trajectory,
            list,
        )
        or not trajectory
    ):
        raise ValueError(
            "trajectory must be a non-empty list."
        )

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    trajectory_text = (
        _format_trajectory(
            trajectory
        )
    )

    parsed = llm.complete_json(
        prompt=_build_gap_prompt(
            task_description=(
                task_description
            ),
            trajectory_text=(
                trajectory_text
            ),
        ),
        system_prompt=(
            GAP_DISCOVERY_SYSTEM_PROMPT
        ),
    )

    validated_gaps = (
        _validate_gap_output(
            parsed=parsed,
            trajectory=trajectory,
        )
    )

    observed_gaps: List[
        ObservedGap
    ] = []

    for index, gap in enumerate(
        validated_gaps,
        start=1,
    ):
        trajectory_evidence = (
            _serialize_evidence_events(
                trajectory=trajectory,
                event_ids=gap[
                    "event_ids"
                ],
            )
        )

        observed_gaps.append(
            ObservedGap(
                gap_id=(
                    f"g_{index}"
                ),
                description=(
                    gap[
                        "description"
                    ]
                ),
                local_trajectory=(
                    trajectory_evidence
                ),
                trajectory_evidence=(
                    trajectory_evidence
                ),
            )
        )

    return observed_gaps


# ============================================================
# Stage 1B
# Execution Signals -> Repository Evidence
# ============================================================

EVIDENCE_RETRIEVAL_SYSTEM_PROMPT = """
You are the fixed auxiliary LLM used in a research pipeline for
repository-grounded knowledge probing.

Your task is to construct a READ-ONLY repository retrieval plan
for one observed execution gap.

The retrieval plan must be grounded in:

1. the observed execution gap;
2. the local execution trajectory;
3. the visible repository structure.

First identify concrete execution signals, such as:

- file paths;
- failing tests;
- error messages;
- symbols or functions;
- modules or packages;
- dependencies;
- configuration files;
- repository instructions;
- commands observed in the trajectory.

Then propose a small set of repository retrieval actions relevant
to understanding the gap.

IMPORTANT:

- Do not solve the task.
- Do not construct knowledge targets yet.
- Do not generate diagnostic questions.
- Do not infer missing knowledge yet.
- Do not use external knowledge.
- Do not request file writes.
- Do not request shell commands.
- Do not retrieve unrelated repository content.
- Every retrieval action must follow from a concrete signal.

If the observed gap involves a potentially missing symbol,
configuration value, dependency declaration, instruction, or other
item whose absence may matter, use a targeted search_text action
when appropriate.

A successful search returning no matches is useful negative
repository evidence and should not be ignored.
""".strip()


@dataclass
class EvidenceRetrievalResult:
    """
    Complete Stage 1B output for one observed gap.
    """

    gap_id: str

    signals: List[
        Dict[str, Any]
    ]

    retrieval_actions: List[
        Dict[str, Any]
    ]

    evidence: List[
        RepositoryEvidence
    ]

    errors: List[str]

    repository_overview: str

    snapshot: (
        RepositorySnapshotInfo
    )


def _build_evidence_retrieval_prompt(
    task_description: str,
    gap: ObservedGap,
    repository_overview: str,
) -> str:
    """
    Ask the auxiliary LLM for bounded read-only retrieval actions.
    """

    return f"""
Construct a repository-evidence retrieval plan for the observed
execution gap below.

First identify concrete signals from the gap and trajectory.

Then produce retrieval actions using ONLY:

- read_file
- search_text

Do NOT use run_command.
Do NOT use write_file.

Evidence types must be one of:

- failing_test
- explicit_constraint
- source_code
- documentation

Definitions:

failing_test:
    Existing visible tests directly related to the failure.

explicit_constraint:
    Configuration, dependency, version, build, schema, or other
    explicit repository constraints.

source_code:
    Source implementation relevant to the observed behavior.

documentation:
    README files, AGENTS.md, CLAUDE.md, repository instructions,
    or other repository documentation.

IMPORTANT NEGATIVE-EVIDENCE RULE:

If a concrete signal suggests that the presence or absence of a
specific symbol, dependency, instruction, configuration entry, or
other textual item may matter, consider a targeted search_text
action.

A no-match search may later support a narrowly scoped textual
absence claim.

For read_file:

{{
  "tool": "read_file",
  "relative_path": "path/to/file",
  "start_line": 1,
  "end_line": 300,
  "evidence_type": "source_code",
  "rationale": "why this retrieval follows from a concrete signal"
}}

For search_text:

{{
  "tool": "search_text",
  "query": "symbol or error text",
  "relative_path": ".",
  "max_results": 50,
  "evidence_type": "source_code",
  "rationale": "why this retrieval follows from a concrete signal"
}}

Return exactly:

{{
  "signals": [
    {{
      "type": "file|error|test|symbol|dependency|config|instruction|command|other",
      "value": "concrete signal",
      "trajectory_basis": "what in the trajectory supports this signal"
    }}
  ],
  "retrieval_actions": [
    {{
      "tool": "read_file",
      "relative_path": "path/to/file",
      "start_line": 1,
      "end_line": 300,
      "evidence_type": "source_code",
      "rationale": "reason"
    }}
  ]
}}

Use no more than {MAX_RETRIEVAL_ACTIONS} retrieval actions.

TASK:
----------------
{task_description}
----------------

OBSERVED GAP:
----------------
ID: {gap.gap_id}

DESCRIPTION:
{gap.description}
----------------

LOCAL TRAJECTORY EVIDENCE:
----------------
{gap.trajectory_evidence}
----------------

VISIBLE REPOSITORY STRUCTURE:
----------------
{repository_overview}
----------------
""".strip()


def _validate_relative_path(
    relative_path: str,
) -> str:
    """
    Prevent repository path escape.
    """

    relative_path = (
        relative_path.strip()
        if relative_path
        else "."
    )

    path = Path(
        relative_path
    )

    if path.is_absolute():
        raise RuntimeError(
            f"Absolute repository path is not allowed: "
            f"{relative_path}"
        )

    if ".." in path.parts:
        raise RuntimeError(
            f"Repository path escape is not allowed: "
            f"{relative_path}"
        )

    return relative_path


def _validate_retrieval_plan(
    parsed: Dict[str, Any],
) -> Tuple[
    List[Dict[str, Any]],
    List[Dict[str, Any]],
]:
    """
    Validate signals and read-only retrieval actions.
    """

    signals = parsed.get(
        "signals"
    )

    actions = parsed.get(
        "retrieval_actions"
    )

    if not isinstance(
        signals,
        list,
    ):
        raise RuntimeError(
            "Stage 1B 'signals' must be a list."
        )

    if not isinstance(
        actions,
        list,
    ):
        raise RuntimeError(
            "Stage 1B 'retrieval_actions' must be a list."
        )

    if (
        len(actions)
        > MAX_RETRIEVAL_ACTIONS
    ):
        raise RuntimeError(
            "Stage 1B produced too many retrieval actions: "
            f"{len(actions)} > {MAX_RETRIEVAL_ACTIONS}"
        )

    # --------------------------------------------------------
    # Validate signals
    # --------------------------------------------------------

    clean_signals: List[
        Dict[str, Any]
    ] = []

    for index, signal in enumerate(
        signals,
        start=1,
    ):
        if not isinstance(
            signal,
            dict,
        ):
            raise RuntimeError(
                f"Signal {index} must be a JSON object."
            )

        signal_type = str(
            signal.get(
                "type",
                ""
            )
        ).strip()

        value = str(
            signal.get(
                "value",
                ""
            )
        ).strip()

        trajectory_basis = str(
            signal.get(
                "trajectory_basis",
                ""
            )
        ).strip()

        if not signal_type:
            raise RuntimeError(
                f"Signal {index} has no type."
            )

        if not value:
            raise RuntimeError(
                f"Signal {index} has no value."
            )

        clean_signals.append(
            {
                "type": (
                    signal_type
                ),
                "value": (
                    value
                ),
                "trajectory_basis": (
                    trajectory_basis
                ),
            }
        )

    # --------------------------------------------------------
    # Validate actions
    # --------------------------------------------------------

    clean_actions: List[
        Dict[str, Any]
    ] = []

    seen_actions = set()

    for index, action in enumerate(
        actions,
        start=1,
    ):
        if not isinstance(
            action,
            dict,
        ):
            raise RuntimeError(
                f"Retrieval action {index} must be a JSON object."
            )

        tool = str(
            action.get(
                "tool",
                ""
            )
        ).strip()

        if tool not in {
            "read_file",
            "search_text",
        }:
            raise RuntimeError(
                f"Stage 1B attempted disallowed tool: {tool}"
            )

        evidence_type = str(
            action.get(
                "evidence_type",
                ""
            )
        ).strip()

        if (
            evidence_type
            not in ALLOWED_EVIDENCE_TYPES
        ):
            raise RuntimeError(
                f"Invalid evidence type: {evidence_type}"
            )

        rationale = str(
            action.get(
                "rationale",
                ""
            )
        ).strip()

        if not rationale:
            raise RuntimeError(
                f"Retrieval action {index} has no rationale."
            )

        # ----------------------------------------------------
        # read_file
        # ----------------------------------------------------

        if tool == "read_file":
            relative_path = (
                _validate_relative_path(
                    str(
                        action.get(
                            "relative_path",
                            ""
                        )
                    )
                )
            )

            if relative_path == ".":
                raise RuntimeError(
                    "read_file requires a file path."
                )

            start_line = int(
                action.get(
                    "start_line",
                    1,
                )
            )

            end_line = int(
                action.get(
                    "end_line",
                    300,
                )
            )

            if start_line < 1:
                start_line = 1

            if end_line < start_line:
                end_line = (
                    start_line + 299
                )

            if (
                end_line
                - start_line
                > 499
            ):
                end_line = (
                    start_line + 499
                )

            clean_action = {
                "tool": (
                    tool
                ),
                "relative_path": (
                    relative_path
                ),
                "start_line": (
                    start_line
                ),
                "end_line": (
                    end_line
                ),
                "evidence_type": (
                    evidence_type
                ),
                "rationale": (
                    rationale
                ),
            }

            signature = (
                tool,
                relative_path,
                start_line,
                end_line,
            )

        # ----------------------------------------------------
        # search_text
        # ----------------------------------------------------

        else:
            query = str(
                action.get(
                    "query",
                    ""
                )
            ).strip()

            if not query:
                raise RuntimeError(
                    "search_text requires a query."
                )

            relative_path = (
                _validate_relative_path(
                    str(
                        action.get(
                            "relative_path",
                            "."
                        )
                    )
                )
            )

            max_results = int(
                action.get(
                    "max_results",
                    50,
                )
            )

            max_results = max(
                1,
                min(
                    max_results,
                    100,
                ),
            )

            clean_action = {
                "tool": (
                    tool
                ),
                "query": (
                    query
                ),
                "relative_path": (
                    relative_path
                ),
                "max_results": (
                    max_results
                ),
                "evidence_type": (
                    evidence_type
                ),
                "rationale": (
                    rationale
                ),
            }

            signature = (
                tool,
                query,
                relative_path,
            )

        if signature in seen_actions:
            continue

        seen_actions.add(
            signature
        )

        clean_actions.append(
            clean_action
        )

    return (
        clean_signals,
        clean_actions,
    )


# ============================================================
# Positive / Negative Search Evidence Handling
# ============================================================

def _is_negative_search_result(
    content: str,
) -> bool:
    """
    Determine whether a SUCCESSFUL search_text call produced no
    matches.

    Empty stdout from a successful search_text call is also
    treated as NO_MATCHES.

    This function should therefore only be used when the retrieval
    action itself is search_text.
    """

    stripped = (
        content.strip().lower()
    )

    if not stripped:
        return True

    negative_markers = {
        "no matches found",
        "no matches found.",
        "no results",
        "no results.",
        "(no matches)",
    }

    return (
        stripped
        in negative_markers
    )


def _retrieval_is_empty(
    content: str,
) -> bool:
    """
    Detect genuinely empty non-search retrieval output.

    Negative search handling occurs before this check.
    """

    return not bool(
        content.strip()
    )


def _build_negative_search_evidence(
    action: Dict[str, Any],
) -> str:
    """
    Convert a successful no-match search into explicit,
    machine-readable negative repository evidence.
    """

    return (
        "NEGATIVE_SEARCH_EVIDENCE\n"
        f"QUERY: {action['query']}\n"
        f"SCOPE: {action['relative_path']}\n"
        "RESULT: NO_MATCHES"
    )


def _execute_retrieval_action(
    repository_tools: RepositoryTools,
    action: Dict[str, Any],
) -> str:
    """
    Execute one validated READ-ONLY repository retrieval action.
    """

    if (
        action[
            "tool"
        ]
        == "read_file"
    ):
        return str(
            repository_tools.read_file(
                relative_path=(
                    action[
                        "relative_path"
                    ]
                ),
                start_line=(
                    action[
                        "start_line"
                    ]
                ),
                end_line=(
                    action[
                        "end_line"
                    ]
                ),
            )
        )

    if (
        action[
            "tool"
        ]
        == "search_text"
    ):
        return str(
            repository_tools.search_text(
                query=(
                    action[
                        "query"
                    ]
                ),
                relative_path=(
                    action[
                        "relative_path"
                    ]
                ),
                max_results=(
                    action[
                        "max_results"
                    ]
                ),
            )
        )

    raise RuntimeError(
        f"Unsupported retrieval tool: "
        f"{action['tool']}"
    )


def retrieve_repository_evidence(
    repository_path: str,
    task_description: str,
    gap: ObservedGap,
    expected_base_commit: str,
    llm: Optional[
        FixedLLMClient
    ] = None,
) -> EvidenceRetrievalResult:
    """
    Stage 1B.

    Repository evidence retrieval requires expected_base_commit.

    Repository integrity is verified BEFORE any repository
    contents are exposed to the auxiliary LLM.
    """

    task_description = (
        task_description.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    # --------------------------------------------------------
    # Leakage guard
    # --------------------------------------------------------

    snapshot = (
        verify_repository_snapshot(
            repository_path=(
                repository_path
            ),
            expected_base_commit=(
                expected_base_commit
            ),
        )
    )

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    repository_tools = (
        RepositoryTools(
            repository_root=(
                snapshot.repository_root
            )
        )
    )

    # --------------------------------------------------------
    # Repository structural overview
    # --------------------------------------------------------

    repository_overview = str(
        repository_tools.list_files(
            relative_path=".",
            max_depth=4,
        )
    )

    # --------------------------------------------------------
    # Retrieval planning
    # --------------------------------------------------------

    parsed = llm.complete_json(
        prompt=_build_evidence_retrieval_prompt(
            task_description=(
                task_description
            ),
            gap=(
                gap
            ),
            repository_overview=(
                repository_overview
            ),
        ),
        system_prompt=(
            EVIDENCE_RETRIEVAL_SYSTEM_PROMPT
        ),
    )

    signals, actions = (
        _validate_retrieval_plan(
            parsed
        )
    )

    # --------------------------------------------------------
    # Execute retrieval
    # --------------------------------------------------------

    evidence_items: List[
        RepositoryEvidence
    ] = []

    errors: List[
        str
    ] = []

    for action_index, action in enumerate(
        actions,
        start=1,
    ):
        try:
            raw_content = (
                _execute_retrieval_action(
                    repository_tools=(
                        repository_tools
                    ),
                    action=(
                        action
                    ),
                )
            )

        except Exception as exc:
            errors.append(
                f"Action {action_index} failed: "
                f"{type(exc).__name__}: {exc}"
            )
            continue

        # ----------------------------------------------------
        # Explicit negative search evidence
        # ----------------------------------------------------

        if (
            action[
                "tool"
            ]
            == "search_text"
            and _is_negative_search_result(
                raw_content
            )
        ):
            content = (
                _build_negative_search_evidence(
                    action
                )
            )

            evidence_path = (
                f"{action['relative_path']} "
                f"[negative search: "
                f"{action['query']}]"
            )

        # ----------------------------------------------------
        # Empty non-search result
        # ----------------------------------------------------

        elif _retrieval_is_empty(
            raw_content
        ):
            continue

        # ----------------------------------------------------
        # read_file evidence
        # ----------------------------------------------------

        elif (
            action[
                "tool"
            ]
            == "read_file"
        ):
            content = (
                raw_content
            )

            evidence_path = (
                action[
                    "relative_path"
                ]
            )

        # ----------------------------------------------------
        # Positive search evidence
        # ----------------------------------------------------

        else:
            content = (
                raw_content
            )

            evidence_path = (
                f"{action['relative_path']} "
                f"[search: "
                f"{action['query']}]"
            )

        evidence_id = (
            f"{gap.gap_id}_R"
            f"{len(evidence_items) + 1}"
        )

        evidence_items.append(
            RepositoryEvidence(
                evidence_id=(
                    evidence_id
                ),
                gap_id=(
                    gap.gap_id
                ),
                evidence_type=(
                    action[
                        "evidence_type"
                    ]
                ),
                path=(
                    evidence_path
                ),
                content=(
                    content
                ),
                rationale=(
                    action[
                        "rationale"
                    ]
                ),

                # Stage 3 decides RepositoryProvides(KT_k).
                explicit_guidance=False,
            )
        )

    return EvidenceRetrievalResult(
        gap_id=(
            gap.gap_id
        ),
        signals=(
            signals
        ),
        retrieval_actions=(
            actions
        ),
        evidence=(
            evidence_items
        ),
        errors=(
            errors
        ),
        repository_overview=(
            repository_overview
        ),
        snapshot=(
            snapshot
        ),
    )


# ============================================================
# Stage 1C
# Repository-Grounded Knowledge Target Construction
# ============================================================

TARGET_CONSTRUCTION_SYSTEM_PROMPT = """
You are the fixed auxiliary LLM used for repository-grounded
knowledge target construction.

Identify distinct pieces of CODEBASE-SPECIFIC knowledge REQUIRED
to correctly handle one observed execution gap.

A repository fact is NOT a valid target merely because it is nearby,
related to the same file, symbol, dependency, component, or broad topic.

The target must represent knowledge that could materially affect how the
observed gap is diagnosed, handled, or resolved.

A knowledge target is NOT:

- a generic software-engineering recommendation;
- a description of the agent's mistake;
- a proposed patch;
- a sequence of actions;
- a claim that the agent lacks knowledge;
- an inferred solution.

A valid knowledge target must be grounded in BOTH:

1. trajectory evidence showing why the knowledge is relevant;

2. repository evidence showing the actual codebase-specific facts.

Every repository fact used by a target must be accompanied by
EXACT source spans copied from the supplied repository evidence.

Do not infer causality merely from correlation.

For example:

Evidence:
- a test imports foo;
- source defines bar.

You may state those observed facts.

You may NOT automatically conclude:

- bar should be renamed foo;
- bar should be exported as foo;
- the missing export is definitely the root cause;
- matching behavior proves bar is intended to be foo.

NEGATIVE / ABSENCE CLAIM RULE:

A negative textual claim such as:

- "foo does not occur in this file";
- "the file contains no textual occurrence of foo";
- "no matching declaration of X was found in this scope";

must NOT be inferred merely because positive evidence does not
show the item.

A negative textual claim is allowed only when repository support
contains explicit evidence of the form:

NEGATIVE_SEARCH_EVIDENCE
QUERY: ...
SCOPE: ...
RESULT: NO_MATCHES

The query and scope must directly support the claimed textual
absence.

Negative search evidence establishes only the absence of a textual
match for QUERY within SCOPE.

It does NOT automatically establish stronger semantic claims such
as:

- the program cannot expose the symbol dynamically;
- the symbol does not exist under any possible mechanism;
- the behavior cannot exist at runtime;
- the missing text is definitely the root cause.

EXCLUSIVITY CLAIM RULE:

Do not use exclusivity claims such as:

- "only X is defined";
- "X is the only implementation";
- "there are no other functions";
- "the file contains only X";
- "the repository provides only X";

unless the supplied evidence explicitly establishes the complete
relevant scope.

Seeing an exact positive span defining X does NOT prove that X is
the only definition or item.

For example:

An exact span:

def bar():

supports:

"bar is defined"

but does NOT by itself support:

"bar is the only function defined".

Prefer direct factual statements over stronger exclusivity claims.

Absence of positive evidence is not evidence of absence.

Do not use external knowledge.
Do not use gold patches.
Do not use benchmark test patches.
Do not use hidden tests.
Do not invent repository facts.
""".strip()


TARGET_SUPPORT_SYSTEM_PROMPT = """
You are the strict evidence-support verifier in a
repository-grounded knowledge probing pipeline.

For each proposed knowledge target, determine whether EVERY
substantive claim in its description is directly supported by
the supplied exact trajectory and repository evidence spans.

Mark UNSUPPORTED if the description:

- adds an unstated causal claim;
- claims a root cause not directly established by evidence;
- infers developer intent;
- proposes or implies a patch;
- claims two symbols are equivalent without explicit evidence;
- turns correlation into causation;
- contains generic advice rather than codebase-specific knowledge;
- contains any substantive fact absent from the supplied spans.

NEGATIVE / ABSENCE CLAIM RULE:

For any negative textual claim, such as:

- "foo does not occur in file X";
- "no declaration of X was found in scope Y";

mark the target UNSUPPORTED unless repository support contains
explicit:

NEGATIVE_SEARCH_EVIDENCE
QUERY: ...
SCOPE: ...
RESULT: NO_MATCHES

and the query and scope directly establish the narrowly stated
textual absence.

Seeing another symbol in a file is NOT sufficient evidence that
the claimed symbol is absent.

A negative textual search does NOT automatically support stronger
runtime or semantic claims such as:

- "the package cannot expose foo";
- "foo does not exist under any mechanism";
- "this proves the root cause".

EXCLUSIVITY CLAIM RULE:

Mark a target UNSUPPORTED if it makes an exclusivity claim such as:

- "only X is defined";
- "X is the only implementation";
- "there are no other functions";
- "the file contains only X";
- "the repository provides only X";

unless the supplied evidence explicitly establishes the complete
relevant scope needed for that claim.

An exact positive span showing:

def bar():

supports:

"bar is defined"

but does NOT by itself support:

"bar is the only function defined".

Prefer directly supported factual claims over stronger exclusivity
claims.

This is a conservative verification step.

Do not repair or rewrite an unsupported target.
""".strip()


DUPLICATE_TARGET_SYSTEM_PROMPT = """
You are the same fixed auxiliary LLM used for repository-grounded
knowledge target construction.

Your task is only to identify duplicate knowledge targets.

Two targets are duplicates ONLY when answering either target
requires the same underlying repository-grounded knowledge.

Targets are NOT duplicates merely because:

- their wording is similar;
- they concern the same file;
- they concern the same error;
- they belong to the same broad topic.

Do not rewrite targets.
Do not create new knowledge.
Only identify duplicate groups.
""".strip()


# ============================================================
# Stage 1C Audit Structures
# ============================================================

@dataclass
class RejectedTarget:
    """
    One LLM-proposed target rejected during Stage 1C.
    """

    proposal_id: str
    description: str
    rejection_stage: str
    reason: str

    details: Dict[
        str,
        Any
    ] = field(
        default_factory=dict
    )


@dataclass
class TargetSupportRecord:
    """
    Exact evidence supporting one validated target.
    """

    target_id: str
    proposal_id: str

    trajectory_spans: List[
        str
    ]

    repository_support: List[
        Dict[str, Any]
    ]


@dataclass
class _GroundedTargetProposal:
    """
    Internal representation after deterministic evidence grounding
    but before semantic support verification.
    """

    proposal_id: str
    description: str

    trajectory_spans: List[
        str
    ]

    repository_support: List[
        Dict[str, Any]
    ]

    repository_evidence_ids: List[
        str
    ]


@dataclass
class TargetConstructionResult:
    """
    Complete Stage 1C result including process metrics.
    """

    gap_id: str

    proposed_target_count: int

    grounding_valid_count: int

    generated_targets: List[
        KnowledgeTarget
    ]

    rejected_targets: List[
        RejectedTarget
    ]

    support_records: List[
        TargetSupportRecord
    ]

    merged_targets: List[
        KnowledgeTarget
    ]

    selected_targets: List[
        KnowledgeTarget
    ]

    duplicate_groups: List[
        List[str]
    ]

    @property
    def validated_target_count(
        self,
    ) -> int:
        """
        Number passing both deterministic grounding and semantic support.
        """

        return len(
            self.generated_targets
        )

    @property
    def grounding_pass_rate(
        self,
    ) -> float:
        """
        Deterministic evidence-grounding pass rate.
        """

        if (
            self.proposed_target_count
            == 0
        ):
            return 0.0

        return (
            self.grounding_valid_count
            / self.proposed_target_count
        )

    @property
    def overall_validation_pass_rate(
        self,
    ) -> float:
        """
        Final Stage 1C validation pass rate.
        """

        if (
            self.proposed_target_count
            == 0
        ):
            return 0.0

        return (
            self.validated_target_count
            / self.proposed_target_count
        )


# ============================================================
# Repository Evidence Formatting
# ============================================================

def _format_repository_evidence_for_targets(
    evidence_items: List[
        RepositoryEvidence
    ],
) -> str:
    """
    Format repository evidence while preserving evidence IDs.
    """

    parts: List[
        str
    ] = []

    for evidence in evidence_items:
        content = (
            evidence.content
        )

        if (
            len(content)
            > MAX_EVIDENCE_CHARS_PER_ITEM
        ):
            content = (
                content[
                    :MAX_EVIDENCE_CHARS_PER_ITEM
                ]
                + "\n...[TRUNCATED]"
            )

        parts.append(
            "\n".join(
                [
                    (
                        f"EVIDENCE_ID: "
                        f"{evidence.evidence_id}"
                    ),
                    (
                        f"TYPE: "
                        f"{evidence.evidence_type}"
                    ),
                    (
                        f"PATH: "
                        f"{evidence.path}"
                    ),
                    (
                        f"RATIONALE: "
                        f"{evidence.rationale}"
                    ),
                    "CONTENT:",
                    content,
                ]
            )
        )

    return "\n\n".join(
        parts
    )


# ============================================================
# Target Proposal Generation
# ============================================================

def _build_target_construction_prompt(
    task_description: str,
    gap: ObservedGap,
    evidence_items: List[
        RepositoryEvidence
    ],
) -> str:
    """
    Ask for repository-grounded target proposals using stable
    trajectory EVENT_IDs and repository EVIDENCE_IDs.

    The auxiliary LLM does not copy evidence text. It only points
    to evidence that already exists in the pipeline.
    """

    evidence_text = (
        _format_repository_evidence_for_targets(
            evidence_items
        )
    )

    return f"""
Identify distinct repository-grounded knowledge targets REQUIRED
to correctly handle the observed execution gap.

GAP-REQUIREDNESS RULE:

A target is valid only when the repository-grounded knowledge it
represents could materially affect the diagnosis, execution decision,
expected behavior, or next action needed to handle THIS observed gap.

Do NOT create a target merely because a repository fact:

- appears in the same file;
- concerns the same class or module;
- is discovered during repository retrieval;
- is generally useful;
- is technically interesting;
- is related only by broad topic.

Ask:

"If the agent did not have this knowledge, could that reasonably prevent
it from correctly handling the observed gap?"

If the answer is no, do not create the target.

For EACH target:

1. State ONE distinct piece of codebase-specific knowledge.

2. Cite one or more trajectory EVENT_IDs exactly as shown in the
   supplied TRAJECTORY EVIDENCE.

   Examples:

   E12
   E28

   Do NOT copy or paraphrase the trajectory text into this field.
   Return only existing EVENT_ID values.

3. Cite one or more repository EVIDENCE_IDs exactly as shown in
   the supplied REPOSITORY EVIDENCE.

   Example:

   g_1_R1

   Do NOT copy repository source text into this field.
   Return only existing EVIDENCE_ID values.

4. State only facts directly supported by the cited trajectory
   events and repository evidence.

TEMPORAL-STATE GROUNDING RULE:

Repository evidence is retrieved from the clean BASE-COMMIT
repository snapshot.

Therefore, repository evidence may establish the repository state
at the base commit, but it does NOT by itself establish the
repository state after the agent's execution.

Do NOT infer from base-commit repository evidence that:

- an agent edit persisted;
- an agent edit failed to persist;
- a patch was successfully or unsuccessfully applied;
- the final post-execution file still contains some content;
- the repository returned to its original state.

Any claim about repository state AFTER an edit must be directly
supported by a later trajectory observation that occurs after the
relevant edit, such as a file read, search result, command output,
or diff inspection.

If no such later trajectory observation exists, describe the
base-commit repository fact and the observed agent action
separately. Do not infer the post-execution state.

TARGET-DESCRIPTION SEPARATION RULE:

The target description must state ONLY the repository-grounded
knowledge that should later be probed.

The description must NOT narrate or evaluate the agent's execution.

Do NOT mention:

- the agent or the agent's actions;
- trajectory event IDs such as E12 or E64;
- edits performed by the agent;
- whether an edit persisted or failed to persist;
- whether a patch was successfully applied;
- whether the final post-execution repository changed.

Trajectory evidence is used only to identify and motivate the
knowledge target. It is stored separately as provenance.

For example:

GOOD:
"In the base-commit version of agentops/event.py, ErrorEvent does
not inherit from Event."

BAD:
"After the agent's edit E64, ErrorEvent still does not inherit
from Event."

BAD:
"The agent's edit failed to persist."

5. Do not claim a root cause unless the supplied evidence
   explicitly establishes it.

6. Do not infer that one symbol should replace, rename, alias,
   or correspond to another merely because their behavior appears
   similar.

7. Do not propose a patch or solution.

8. Do not state generic advice such as:

   "inspect dependencies"

   or

   "run the tests".

9. Do not claim that the target agent lacks this knowledge.

10. Do not create multiple targets requiring the same underlying
    repository-grounded knowledge.

11. Any negative textual claim that something is absent, missing,
    undefined, or not present in a specific scope must cite
    repository evidence containing:

    NEGATIVE_SEARCH_EVIDENCE
    QUERY: ...
    SCOPE: ...
    RESULT: NO_MATCHES

12. Do not infer absence merely because another positive source
    does not show an item.

13. Negative search evidence only supports textual absence within
    the searched scope. Do not convert it into stronger semantic
    or runtime claims.

14. Do not use exclusivity wording such as:

    - "only X is defined";
    - "X is the only implementation";
    - "there are no other functions";
    - "the file contains only X";

    unless the supplied evidence explicitly establishes the
    complete relevant scope.

Return exactly:

{{
  "targets": [
    {{
      "description": "one factual repository-grounded knowledge target",
      "trajectory_event_ids": [
        "E12"
      ],
      "repository_evidence_ids": [
        "g_1_R1"
      ]
    }}
  ]
}}

TASK:
----------------
{task_description}
----------------

OBSERVED GAP:
----------------
{gap.description}
----------------

TRAJECTORY EVIDENCE:
----------------
{gap.trajectory_evidence}
----------------

REPOSITORY EVIDENCE:
----------------
{evidence_text}
----------------
""".strip()


# ============================================================
# Deterministic ID Grounding
# ============================================================

def _extract_trajectory_event_blocks(
    trajectory_evidence: str,
) -> Dict[
    str,
    str,
]:
    """
    Convert serialized trajectory evidence such as:

        E12
        {...}

        E28
        {...}

    into:

        {
            "E12": "E12\\n{...}",
            "E28": "E28\\n{...}",
        }

    The returned text comes from the pipeline's stored trajectory,
    not from the auxiliary LLM.
    """

    if not isinstance(
        trajectory_evidence,
        str,
    ):
        return {}

    matches = list(
        re.finditer(
            r"(?m)^(E\d+)\s*$",
            trajectory_evidence,
        )
    )

    blocks: Dict[
        str,
        str,
    ] = {}

    for index, match in enumerate(
        matches
    ):

        event_id = (
            match.group(1)
        )

        start = (
            match.start()
        )

        if (
            index + 1
            < len(matches)
        ):
            end = (
                matches[
                    index + 1
                ].start()
            )
        else:
            end = len(
                trajectory_evidence
            )

        block = (
            trajectory_evidence[
                start:end
            ]
            .strip()
        )

        if block:
            blocks[
                event_id
            ] = block

    return blocks


# ============================================================
# Deterministic Evidence Validation
# ============================================================

def _validate_target_proposals(
    parsed: Dict[str, Any],
    gap: ObservedGap,
    evidence_items: List[
        RepositoryEvidence
    ],
) -> Tuple[
    int,
    List[
        _GroundedTargetProposal
    ],
    List[
        RejectedTarget
    ],
]:
    """
    Deterministically validate trajectory EVENT_IDs and repository
    EVIDENCE_IDs, then recover trusted evidence text.

    Invalid proposed targets are recorded rather than silently
    discarded.
    """

    raw_targets = parsed.get(
        "targets"
    )

    if not isinstance(
        raw_targets,
        list,
    ):
        raise RuntimeError(
            "Stage 1C output must contain 'targets' as a list."
        )

    proposed_count = (
        len(
            raw_targets
        )
    )

    normalized_trajectory = (
        _normalize_whitespace(
            gap.trajectory_evidence
        )
    )

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    trajectory_event_blocks = (
        _extract_trajectory_event_blocks(
            gap.trajectory_evidence
        )
    )

    if not trajectory_event_blocks:
        raise RuntimeError(
            "Could not recover trajectory EVENT_IDs "
            "from gap.trajectory_evidence."
        )

    grounded: List[
        _GroundedTargetProposal
    ] = []

    rejected: List[
        RejectedTarget
    ] = []

    for index, raw_target in enumerate(
        raw_targets,
        start=1,
    ):
        proposal_id = (
            f"P{index}"
        )

        # ----------------------------------------------------
        # Structure validation
        # ----------------------------------------------------

        if not isinstance(
            raw_target,
            dict,
        ):
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal_id
                    ),
                    description="",
                    rejection_stage=(
                        "structure"
                    ),
                    reason=(
                        "proposal_not_json_object"
                    ),
                )
            )

            continue

        description = str(
            raw_target.get(
                "description",
                ""
            )
        ).strip()

        if not description:
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal_id
                    ),
                    description="",
                    rejection_stage=(
                        "structure"
                    ),
                    reason=(
                        "missing_description"
                    ),
                )
            )

            continue

        # ----------------------------------------------------
        # Resolve stable evidence IDs
        #
        # The LLM selects IDs only. The actual evidence text is
        # reconstructed here from trusted pipeline data.
        # ----------------------------------------------------

        raw_target = dict(
            raw_target
        )

        trajectory_event_ids = (
            raw_target.get(
                "trajectory_event_ids"
            )
        )

        if trajectory_event_ids is not None:

            if (
                not isinstance(
                    trajectory_event_ids,
                    list,
                )
                or not trajectory_event_ids
                or not all(
                    isinstance(
                        event_id,
                        str,
                    )
                    and event_id.strip()
                    for event_id
                    in trajectory_event_ids
                )
            ):
                rejected.append(
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "trajectory_grounding"
                        ),
                        reason=(
                            "invalid_trajectory_event_ids"
                        ),
                    )
                )

                continue

            clean_event_ids: List[
                str
            ] = []

            unknown_event_id: Optional[
                str
            ] = None

            for event_id in (
                trajectory_event_ids
            ):

                event_id = (
                    event_id.strip()
                )

                if (
                    event_id
                    not in trajectory_event_blocks
                ):
                    unknown_event_id = (
                        event_id
                    )
                    break

                if (
                    event_id
                    not in clean_event_ids
                ):
                    clean_event_ids.append(
                        event_id
                    )

            if (
                unknown_event_id
                is not None
            ):
                rejected.append(
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "trajectory_grounding"
                        ),
                        reason=(
                            "unknown_trajectory_event_id"
                        ),
                        details={
                            "event_id": (
                                unknown_event_id
                            ),
                            "allowed_event_ids": (
                                sorted(
                                    trajectory_event_blocks.keys()
                                )
                            ),
                        },
                    )
                )

                continue

            raw_target[
                "trajectory_spans"
            ] = [
                trajectory_event_blocks[
                    event_id
                ]
                for event_id
                in clean_event_ids
            ]

        repository_evidence_ids = (
            raw_target.get(
                "repository_evidence_ids"
            )
        )

        if (
            repository_evidence_ids
            is not None
        ):

            if (
                not isinstance(
                    repository_evidence_ids,
                    list,
                )
                or not repository_evidence_ids
                or not all(
                    isinstance(
                        evidence_id,
                        str,
                    )
                    and evidence_id.strip()
                    for evidence_id
                    in repository_evidence_ids
                )
            ):
                rejected.append(
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "invalid_repository_evidence_ids"
                        ),
                    )
                )

                continue

            clean_evidence_ids: List[
                str
            ] = []

            unknown_evidence_id: Optional[
                str
            ] = None

            for evidence_id in (
                repository_evidence_ids
            ):

                evidence_id = (
                    evidence_id.strip()
                )

                if (
                    evidence_id
                    not in evidence_by_id
                ):
                    unknown_evidence_id = (
                        evidence_id
                    )
                    break

                if (
                    evidence_id
                    not in clean_evidence_ids
                ):
                    clean_evidence_ids.append(
                        evidence_id
                    )

            if (
                unknown_evidence_id
                is not None
            ):
                rejected.append(
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "unknown_repository_evidence_id"
                        ),
                        details={
                            "evidence_id": (
                                unknown_evidence_id
                            ),
                            "allowed_evidence_ids": (
                                sorted(
                                    evidence_by_id.keys()
                                )
                            ),
                        },
                    )
                )

                continue

            raw_target[
                "repository_support"
            ] = [
                {
                    "evidence_id": (
                        evidence_id
                    ),
                    "path": (
                        evidence_by_id[
                            evidence_id
                        ].path
                    ),
                    "evidence_type": (
                        evidence_by_id[
                            evidence_id
                        ].evidence_type
                    ),
                    "source_spans": [
                        evidence_by_id[
                            evidence_id
                        ].content
                    ],
                }
                for evidence_id
                in clean_evidence_ids
            ]

        # ----------------------------------------------------
        # Trajectory grounding
        # ----------------------------------------------------

        trajectory_spans = (
            raw_target.get(
                "trajectory_spans"
            )
        )

        if (
            not isinstance(
                trajectory_spans,
                list,
            )
            or not trajectory_spans
        ):
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal_id
                    ),
                    description=(
                        description
                    ),
                    rejection_stage=(
                        "trajectory_grounding"
                    ),
                    reason=(
                        "missing_trajectory_spans"
                    ),
                )
            )

            continue

        clean_trajectory_spans: List[
            str
        ] = []

        invalid_trajectory_span: Optional[
            str
        ] = None

        for span in trajectory_spans:
            if not isinstance(
                span,
                str,
            ):
                invalid_trajectory_span = (
                    repr(
                        span
                    )
                )

                break

            normalized_span = (
                _normalize_whitespace(
                    span
                )
            )

            if (
                not normalized_span
                or normalized_span
                not in normalized_trajectory
            ):
                invalid_trajectory_span = (
                    normalized_span
                )

                break

            clean_trajectory_spans.append(
                normalized_span
            )

        if (
            invalid_trajectory_span
            is not None
        ):
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal_id
                    ),
                    description=(
                        description
                    ),
                    rejection_stage=(
                        "trajectory_grounding"
                    ),
                    reason=(
                        "trajectory_span_not_found"
                    ),
                    details={
                        "invalid_span": (
                            invalid_trajectory_span
                        )
                    },
                )
            )

            continue

        # ----------------------------------------------------
        # Repository grounding
        # ----------------------------------------------------

        repository_support = (
            raw_target.get(
                "repository_support"
            )
        )

        if (
            not isinstance(
                repository_support,
                list,
            )
            or not repository_support
        ):
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal_id
                    ),
                    description=(
                        description
                    ),
                    rejection_stage=(
                        "repository_grounding"
                    ),
                    reason=(
                        "missing_repository_support"
                    ),
                )
            )

            continue

        clean_repository_support: List[
            Dict[str, Any]
        ] = []

        repository_evidence_ids: List[
            str
        ] = []

        repository_failure: Optional[
            RejectedTarget
        ] = None

        for support in repository_support:
            if not isinstance(
                support,
                dict,
            ):
                repository_failure = (
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "repository_support_not_object"
                        ),
                    )
                )

                break

            evidence_id = str(
                support.get(
                    "evidence_id",
                    ""
                )
            ).strip()

            if (
                evidence_id
                not in evidence_by_id
            ):
                repository_failure = (
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "unknown_repository_evidence_id"
                        ),
                        details={
                            "evidence_id": (
                                evidence_id
                            )
                        },
                    )
                )

                break

            source_spans = (
                support.get(
                    "source_spans"
                )
            )

            if (
                not isinstance(
                    source_spans,
                    list,
                )
                or not source_spans
            ):
                repository_failure = (
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "missing_repository_source_spans"
                        ),
                        details={
                            "evidence_id": (
                                evidence_id
                            )
                        },
                    )
                )

                break

            evidence_content = (
                _normalize_whitespace(
                    evidence_by_id[
                        evidence_id
                    ].content
                )
            )

            clean_source_spans: List[
                str
            ] = []

            invalid_source_span: Optional[
                str
            ] = None

            for span in source_spans:
                if not isinstance(
                    span,
                    str,
                ):
                    invalid_source_span = (
                        repr(
                            span
                        )
                    )

                    break

                normalized_span = (
                    _normalize_whitespace(
                        span
                    )
                )

                if (
                    not normalized_span
                    or normalized_span
                    not in evidence_content
                ):
                    invalid_source_span = (
                        normalized_span
                    )

                    break

                clean_source_spans.append(
                    normalized_span
                )

            if (
                invalid_source_span
                is not None
            ):
                repository_failure = (
                    RejectedTarget(
                        proposal_id=(
                            proposal_id
                        ),
                        description=(
                            description
                        ),
                        rejection_stage=(
                            "repository_grounding"
                        ),
                        reason=(
                            "repository_span_not_found"
                        ),
                        details={
                            "evidence_id": (
                                evidence_id
                            ),
                            "invalid_span": (
                                invalid_source_span
                            ),
                        },
                    )
                )

                break

            clean_repository_support.append(
                {
                    "evidence_id": (
                        evidence_id
                    ),
                    "source_spans": (
                        clean_source_spans
                    ),
                }
            )

            if (
                evidence_id
                not in repository_evidence_ids
            ):
                repository_evidence_ids.append(
                    evidence_id
                )

        if (
            repository_failure
            is not None
        ):
            rejected.append(
                repository_failure
            )

            continue

        grounded.append(
            _GroundedTargetProposal(
                proposal_id=(
                    proposal_id
                ),
                description=(
                    description
                ),
                trajectory_spans=(
                    clean_trajectory_spans
                ),
                repository_support=(
                    clean_repository_support
                ),
                repository_evidence_ids=(
                    repository_evidence_ids
                ),
            )
        )

    return (
        proposed_count,
        grounded,
        rejected,
    )


# ============================================================
# Semantic Evidence-Support Verification
# ============================================================

def _build_target_support_prompt(
    proposals: List[
        _GroundedTargetProposal
    ],
) -> str:
    """
    Verify that descriptions do not make claims stronger than
    their exact supporting evidence.
    """

    proposal_blocks: List[
        str
    ] = []

    for proposal in proposals:
        proposal_blocks.append(
            "\n".join(
                [
                    (
                        f"PROPOSAL_ID: "
                        f"{proposal.proposal_id}"
                    ),
                    (
                        f"DESCRIPTION: "
                        f"{proposal.description}"
                    ),
                    "TRAJECTORY_SPANS:",
                    json.dumps(
                        proposal.trajectory_spans,
                        ensure_ascii=False,
                        indent=2,
                    ),
                    "REPOSITORY_SUPPORT:",
                    json.dumps(
                        proposal.repository_support,
                        ensure_ascii=False,
                        indent=2,
                    ),
                ]
            )
        )

    return f"""
Verify each proposed knowledge target.

A target is SUPPORTED only if EVERY substantive claim in its
description is directly established by the supplied trajectory
and repository evidence.

Repository support includes trusted metadata such as PATH and
EVIDENCE_TYPE in addition to source content.

TEMPORAL-STATE GROUNDING RULE:

The supplied repository evidence comes from the clean BASE-COMMIT
repository snapshot.

Base-commit repository evidence establishes pre-execution
repository state. It cannot by itself establish whether an edit
later persisted, failed, was reverted, or changed the final
post-execution repository state.

If a target makes a claim about repository state AFTER an agent
edit, mark it UNSUPPORTED unless the supplied TRAJECTORY_SPANS
contain a concrete observation occurring after that edit that
directly establishes the claimed state.

For example:

Base repository evidence:
    def old_name():

Trajectory:
    the agent edits old_name -> new_name

This does NOT support:
    "The rename failed to persist."

A later trajectory read or search showing old_name still present
after the edit may support such a claim.

Do not use base-commit source content or base-commit negative-search
results as evidence of post-execution state.

FILE-PATH GROUNDING RULE:

If the target description names or attributes a fact to a specific
repository file, that file path must match the PATH metadata of the
supporting repository evidence.

Do NOT treat similar source text from another file as evidence for
a claim about the named file.

For example, evidence from tests/test_session.py does NOT support
a claim specifically about tests/test_teardown.py.

Mark UNSUPPORTED if it:

- adds a causal claim not explicitly established;
- declares a root cause based only on circumstantial evidence;
- infers developer intent;
- proposes or implies the required patch;
- infers that one symbol should replace or alias another;
- contains generic advice rather than factual codebase knowledge;
- contains any substantive unsupported fact.

NEGATIVE / ABSENCE CLAIM RULE:

Any negative textual claim requires explicit repository support
containing:

NEGATIVE_SEARCH_EVIDENCE
QUERY: ...
SCOPE: ...
RESULT: NO_MATCHES

The query and scope must directly support the narrowly stated
textual absence.

For example, given:

QUERY: foo
SCOPE: package_x/__init__.py
RESULT: NO_MATCHES

the evidence may support:

"No textual occurrence of foo was found in
package_x/__init__.py."

It does NOT automatically support:

"package_x cannot expose foo."

Seeing another symbol such as bar is NOT evidence that foo is
absent.

EXCLUSIVITY CLAIM RULE:

Mark a target UNSUPPORTED if it claims:

- "only X is defined";
- "X is the only implementation";
- "there are no other functions";
- "the file contains only X";
- "the repository provides only X";

unless the supplied exact evidence explicitly establishes the
complete relevant scope.

For example:

"def bar():"

supports:

"bar is defined"

but does NOT by itself support:

"bar is the only function defined."

Do not repair or rewrite unsupported targets.

Return exactly:

{{
  "decisions": [
    {{
      "proposal_id": "P1",
      "decision": "SUPPORTED",
      "reason": "brief explanation"
    }}
  ]
}}

PROPOSALS:
----------------
{chr(10).join(proposal_blocks)}
----------------
""".strip()


def _validate_support_decisions(
    parsed: Dict[str, Any],
    proposals: List[
        _GroundedTargetProposal
    ],
) -> Dict[
    str,
    Dict[str, str]
]:
    """
    Validate semantic support decisions.

    Malformed verifier output is treated as a pipeline error.
    """

    decisions = parsed.get(
        "decisions"
    )

    if not isinstance(
        decisions,
        list,
    ):
        raise RuntimeError(
            "Target support verifier must return "
            "'decisions' as a list."
        )

    valid_ids = {
        proposal.proposal_id
        for proposal in proposals
    }

    parsed_decisions: Dict[
        str,
        Dict[str, str]
    ] = {}

    for item in decisions:
        if not isinstance(
            item,
            dict,
        ):
            raise RuntimeError(
                "Every target support decision must be "
                "a JSON object."
            )

        proposal_id = str(
            item.get(
                "proposal_id",
                ""
            )
        ).strip()

        decision = str(
            item.get(
                "decision",
                ""
            )
        ).strip().upper()

        reason = str(
            item.get(
                "reason",
                ""
            )
        ).strip()

        if (
            proposal_id
            not in valid_ids
        ):
            raise RuntimeError(
                "Target support verifier returned unknown "
                f"proposal ID: {proposal_id}"
            )

        if (
            proposal_id
            in parsed_decisions
        ):
            raise RuntimeError(
                "Target support verifier returned duplicate "
                f"decision for {proposal_id}"
            )

        if decision not in {
            "SUPPORTED",
            "UNSUPPORTED",
        }:
            raise RuntimeError(
                "Target support decision must be SUPPORTED or "
                f"UNSUPPORTED, got: {decision}"
            )

        parsed_decisions[
            proposal_id
        ] = {
            "decision": (
                decision
            ),
            "reason": (
                reason
            ),
        }

    missing_ids = (
        valid_ids
        - set(
            parsed_decisions.keys()
        )
    )

    if missing_ids:
        raise RuntimeError(
            "Target support verifier omitted proposals: "
            + ", ".join(
                sorted(
                    missing_ids
                )
            )
        )

    return (
        parsed_decisions
    )


def _semantic_support_filter(
    proposals: List[
        _GroundedTargetProposal
    ],
    llm: FixedLLMClient,
) -> Tuple[
    List[
        _GroundedTargetProposal
    ],
    List[
        RejectedTarget
    ],
]:
    """
    Apply strict semantic evidence-support verification.
    """

    if not proposals:
        return (
            [],
            [],
        )

    parsed = llm.complete_json(
        prompt=_build_target_support_prompt(
            proposals
        ),
        system_prompt=(
            TARGET_SUPPORT_SYSTEM_PROMPT
        ),
    )

    decisions = (
        _validate_support_decisions(
            parsed=(
                parsed
            ),
            proposals=(
                proposals
            ),
        )
    )

    accepted: List[
        _GroundedTargetProposal
    ] = []

    rejected: List[
        RejectedTarget
    ] = []

    for proposal in proposals:
        result = (
            decisions[
                proposal.proposal_id
            ]
        )

        if (
            result[
                "decision"
            ]
            == "SUPPORTED"
        ):
            accepted.append(
                proposal
            )

        else:
            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal.proposal_id
                    ),
                    description=(
                        proposal.description
                    ),
                    rejection_stage=(
                        "semantic_support"
                    ),
                    reason=(
                        "description_not_fully_supported"
                    ),
                    details={
                        "verifier_reason": (
                            result[
                                "reason"
                            ]
                        )
                    },
                )
            )

    return (
        accepted,
        rejected,
    )


# ============================================================
# Build KnowledgeTarget Objects
# ============================================================

def _build_knowledge_targets(
    proposals: List[
        _GroundedTargetProposal
    ],
    gap: ObservedGap,
) -> Tuple[
    List[
        KnowledgeTarget
    ],
    List[
        TargetSupportRecord
    ],
]:
    """
    Convert fully validated proposals into KnowledgeTarget
    objects while preserving their evidence audit records.
    """

    targets: List[
        KnowledgeTarget
    ] = []

    support_records: List[
        TargetSupportRecord
    ] = []

    for index, proposal in enumerate(
        proposals,
        start=1,
    ):
        target_id = (
            f"{gap.gap_id}__KT_{index}"
        )

        targets.append(
            KnowledgeTarget(
                target_id=(
                    target_id
                ),
                gap_id=(
                    gap.gap_id
                ),
                description=(
                    proposal.description
                ),
                trajectory_evidence=(
                    "\n".join(
                        proposal.trajectory_spans
                    )
                ),
                repository_evidence_ids=(
                    list(
                        proposal.repository_evidence_ids
                    )
                ),
            )
        )

        support_records.append(
            TargetSupportRecord(
                target_id=(
                    target_id
                ),
                proposal_id=(
                    proposal.proposal_id
                ),
                trajectory_spans=(
                    list(
                        proposal.trajectory_spans
                    )
                ),
                repository_support=[
                    {
                        "evidence_id": (
                            support[
                                "evidence_id"
                            ]
                        ),
                        "source_spans": (
                            list(
                                support[
                                    "source_spans"
                                ]
                            )
                        ),
                    }
                    for support
                    in proposal.repository_support
                ],
            )
        )

    return (
        targets,
        support_records,
    )


# ============================================================
# Duplicate Detection
# ============================================================

def _build_duplicate_prompt(
    targets: List[
        KnowledgeTarget
    ],
    evidence_items: List[
        RepositoryEvidence
    ],
) -> str:
    """
    Ask the same fixed auxiliary LLM to identify duplicate
    knowledge targets.
    """

    target_blocks: List[
        str
    ] = []

    for target in targets:
        target_blocks.append(
            "\n".join(
                [
                    (
                        f"TARGET_ID: "
                        f"{target.target_id}"
                    ),
                    (
                        f"DESCRIPTION: "
                        f"{target.description}"
                    ),
                    (
                        "REPOSITORY_EVIDENCE_IDS: "
                        + ", ".join(
                            target.repository_evidence_ids
                        )
                    ),
                ]
            )
        )

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    referenced_ids: List[
        str
    ] = []

    for target in targets:
        for evidence_id in (
            target.repository_evidence_ids
        ):
            if (
                evidence_id
                not in referenced_ids
            ):
                referenced_ids.append(
                    evidence_id
                )

    evidence_parts: List[
        str
    ] = []

    for evidence_id in referenced_ids:
        evidence = (
            evidence_by_id[
                evidence_id
            ]
        )

        content = (
            evidence.content
        )

        if (
            len(content)
            > MAX_EVIDENCE_CHARS_PER_ITEM
        ):
            content = (
                content[
                    :MAX_EVIDENCE_CHARS_PER_ITEM
                ]
                + "\n...[TRUNCATED]"
            )

        evidence_parts.append(
            "\n".join(
                [
                    (
                        f"EVIDENCE_ID: "
                        f"{evidence.evidence_id}"
                    ),
                    (
                        f"TYPE: "
                        f"{evidence.evidence_type}"
                    ),
                    (
                        f"PATH: "
                        f"{evidence.path}"
                    ),
                    "CONTENT:",
                    content,
                ]
            )
        )

    return f"""
Determine which existing knowledge targets are duplicates.

Two targets are duplicates ONLY if answering either target requires
the same underlying repository-grounded knowledge.

Similar wording, file, topic, error, or component is NOT enough.

Return duplicate groups only.

Each target may appear in at most one group.

Do not include groups containing only one target.

Return exactly:

{{
  "duplicate_groups": [
    ["KT_1", "KT_3"]
  ]
}}

TARGETS:
----------------
{chr(10).join(target_blocks)}
----------------

SUPPORTING REPOSITORY EVIDENCE:
----------------
{chr(10).join(evidence_parts)}
----------------
""".strip()


def _validate_duplicate_groups(
    parsed: Dict[str, Any],
    targets: List[
        KnowledgeTarget
    ],
) -> List[
    List[str]
]:
    """
    Validate duplicate groups returned by the auxiliary LLM.
    """

    groups = (
        parsed.get(
            "duplicate_groups"
        )
    )

    if not isinstance(
        groups,
        list,
    ):
        raise RuntimeError(
            "'duplicate_groups' must be a list."
        )

    valid_ids = {
        target.target_id
        for target in targets
    }

    already_used = set()

    clean_groups: List[
        List[str]
    ] = []

    for group in groups:
        if not isinstance(
            group,
            list,
        ):
            raise RuntimeError(
                "Every duplicate group must be a list."
            )

        clean_group: List[
            str
        ] = []

        for target_id in group:
            if not isinstance(
                target_id,
                str,
            ):
                raise RuntimeError(
                    "Duplicate target IDs must be strings."
                )

            target_id = (
                target_id.strip()
            )

            if (
                target_id
                not in valid_ids
            ):
                raise RuntimeError(
                    "Duplicate detector returned unknown "
                    f"target ID: {target_id}"
                )

            if (
                target_id
                in already_used
            ):
                raise RuntimeError(
                    "A target appeared in more than one duplicate "
                    f"group: {target_id}"
                )

            if (
                target_id
                not in clean_group
            ):
                clean_group.append(
                    target_id
                )

        if (
            len(
                clean_group
            )
            >= 2
        ):
            clean_groups.append(
                clean_group
            )

            already_used.update(
                clean_group
            )

    return (
        clean_groups
    )


# ============================================================
# Deterministic Duplicate Merge
# ============================================================

def _merge_duplicate_targets(
    targets: List[
        KnowledgeTarget
    ],
    duplicate_groups: List[
        List[str]
    ],
) -> List[
    KnowledgeTarget
]:
    """
    Deterministically merge duplicate targets.

    No new target wording is generated.

    The first target in each duplicate group remains the
    representative description.

    Supporting evidence is unioned.
    """

    target_by_id = {
        target.target_id: target
        for target in targets
    }

    member_to_representative: Dict[
        str,
        str
    ] = {}

    group_by_representative: Dict[
        str,
        List[str]
    ] = {}

    for group in duplicate_groups:
        representative_id = (
            group[0]
        )

        group_by_representative[
            representative_id
        ] = group

        for target_id in group:
            member_to_representative[
                target_id
            ] = (
                representative_id
            )

    merged_targets: List[
        KnowledgeTarget
    ] = []

    processed = set()

    for target in targets:
        if (
            target.target_id
            in processed
        ):
            continue

        representative_id = (
            member_to_representative.get(
                target.target_id
            )
        )

        # ----------------------------------------------------
        # Non-duplicate target
        # ----------------------------------------------------

        if (
            representative_id
            is None
        ):
            merged_targets.append(
                target
            )

            processed.add(
                target.target_id
            )

            continue

        # ----------------------------------------------------
        # Non-representative member
        # ----------------------------------------------------

        if (
            target.target_id
            != representative_id
        ):
            continue

        group = (
            group_by_representative[
                representative_id
            ]
        )

        group_targets = [
            target_by_id[
                target_id
            ]
            for target_id in group
        ]

        evidence_ids: List[
            str
        ] = []

        trajectory_parts: List[
            str
        ] = []

        for group_target in group_targets:
            for evidence_id in (
                group_target.repository_evidence_ids
            ):
                if (
                    evidence_id
                    not in evidence_ids
                ):
                    evidence_ids.append(
                        evidence_id
                    )

            if (
                group_target.trajectory_evidence
                and group_target.trajectory_evidence
                not in trajectory_parts
            ):
                trajectory_parts.append(
                    group_target.trajectory_evidence
                )

            processed.add(
                group_target.target_id
            )

        representative = (
            target_by_id[
                representative_id
            ]
        )

        merged_targets.append(
            KnowledgeTarget(
                target_id=(
                    representative.target_id
                ),
                gap_id=(
                    representative.gap_id
                ),
                description=(
                    representative.description
                ),
                trajectory_evidence=(
                    "\n".join(
                        trajectory_parts
                    )
                ),
                repository_evidence_ids=(
                    evidence_ids
                ),
            )
        )

    return (
        merged_targets
    )



# ============================================================
# Global Cross-Gap Semantic Deduplication
# ============================================================

def deduplicate_targets_globally(
    targets: List[KnowledgeTarget],
    evidence_items: List[RepositoryEvidence],
    llm: FixedLLMClient,
) -> Tuple[
    List[KnowledgeTarget],
    List[List[str]],
]:
    """
    Remove semantic duplicate knowledge targets across observed gaps.

    Per-gap Stage 1C already performs duplicate detection locally.
    This function performs one additional task-level pass after all
    gaps have been processed.

    Duplicate semantics are unchanged:
    two targets are duplicates only when answering either requires
    the same underlying repository-grounded knowledge.

    We keep the earliest target in the original Stage-1 order.
    We intentionally do NOT merge evidence across different gaps,
    because downstream stages resolve repository evidence using the
    representative target's gap_id.
    """

    if len(targets) < 2:
        return list(targets), []

    # Ensure target IDs remain globally unique.
    target_ids = [
        target.target_id
        for target in targets
    ]

    if len(target_ids) != len(set(target_ids)):
        raise RuntimeError(
            "Global target dedup received duplicate target IDs."
        )

    # Ensure every evidence ID referenced by every target is
    # available to the duplicate detector.
    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    missing_evidence_ids: List[str] = []

    for target in targets:
        for evidence_id in target.repository_evidence_ids:
            if (
                evidence_id not in evidence_by_id
                and evidence_id not in missing_evidence_ids
            ):
                missing_evidence_ids.append(
                    evidence_id
                )

    if missing_evidence_ids:
        raise RuntimeError(
            "Global target dedup is missing repository evidence: "
            + ", ".join(
                missing_evidence_ids
            )
        )

    parsed = llm.complete_json(
        prompt=_build_duplicate_prompt(
            targets=targets,
            evidence_items=evidence_items,
        ),
        system_prompt=(
            DUPLICATE_TARGET_SYSTEM_PROMPT
        ),
    )

    duplicate_groups = (
        _validate_duplicate_groups(
            parsed=parsed,
            targets=targets,
        )
    )

    # Deterministic representative:
    # earliest target in original Stage-1 order.
    position = {
        target.target_id: index
        for index, target in enumerate(
            targets
        )
    }

    normalized_groups: List[
        List[str]
    ] = []

    removed_ids = set()

    for group in duplicate_groups:
        ordered_group = sorted(
            group,
            key=lambda target_id: (
                position[target_id]
            ),
        )

        representative_id = (
            ordered_group[0]
        )

        normalized_groups.append(
            ordered_group
        )

        for target_id in (
            ordered_group[1:]
        ):
            if target_id == representative_id:
                continue

            removed_ids.add(
                target_id
            )

    deduplicated_targets = [
        target
        for target in targets
        if target.target_id
        not in removed_ids
    ]

    return (
        deduplicated_targets,
        normalized_groups,
    )


# ============================================================
# Fixed Evidence-Priority Target Cap
# ============================================================

def _target_priority(
    target: KnowledgeTarget,
    evidence_by_id: Dict[
        str,
        RepositoryEvidence
    ],
    config: ExperimentConfig,
) -> int:
    """
    Lower rank means stronger evidence priority.
    """

    priority_lookup = {
        evidence_type: index
        for index, evidence_type in enumerate(
            config.evidence_priority
        )
    }

    default_rank = (
        len(
            config.evidence_priority
        )
    )

    ranks: List[
        int
    ] = []

    for evidence_id in (
        target.repository_evidence_ids
    ):
        evidence = (
            evidence_by_id.get(
                evidence_id
            )
        )

        if evidence is None:
            continue

        ranks.append(
            priority_lookup.get(
                evidence.evidence_type,
                default_rank,
            )
        )

    if not ranks:
        return (
            default_rank
        )

    return min(
        ranks
    )


def _apply_target_cap(
    targets: List[
        KnowledgeTarget
    ],
    evidence_items: List[
        RepositoryEvidence
    ],
    config: ExperimentConfig,
) -> List[
    KnowledgeTarget
]:
    """
    Apply fixed N_max according to evidence priority.

    Original target order is used as deterministic tie-break.

    Existing target IDs are preserved for auditability.
    """

    if (
        len(targets)
        <= config.max_targets_per_gap
    ):
        return list(
            targets
        )

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    indexed_targets = list(
        enumerate(
            targets
        )
    )

    indexed_targets.sort(
        key=lambda pair: (
            _target_priority(
                target=(
                    pair[1]
                ),
                evidence_by_id=(
                    evidence_by_id
                ),
                config=(
                    config
                ),
            ),
            pair[0],
        )
    )

    selected = [
        target
        for _, target in (
            indexed_targets[
                :config.max_targets_per_gap
            ]
        )
    ]

    return (
        selected
    )


# ============================================================
# Public Stage 1C
# ============================================================


# ============================================================
# Deterministic Target-Scope Guard
# ============================================================

def _deterministic_target_scope_filter(
    proposals: List[
        _GroundedTargetProposal
    ],
) -> Tuple[
    List[
        _GroundedTargetProposal
    ],
    List[
        RejectedTarget
    ],
]:
    """
    Enforce separation between:

        execution evidence / trajectory context

    and:

        repository-grounded knowledge target.

    A knowledge-target description should state the repository
    knowledge to probe. It must not narrate the agent's execution,
    refer to trajectory event IDs, or infer whether edits persisted.

    This is deterministic and does not depend on another LLM call.
    """

    accepted: List[
        _GroundedTargetProposal
    ] = []

    rejected: List[
        RejectedTarget
    ] = []

    for proposal in proposals:

        description = (
            proposal.description.strip()
        )

        normalized = " ".join(
            description.lower().split()
        )

        violations: List[str] = []

        # ----------------------------------------------------
        # A. Explicit trajectory event IDs
        #
        # Examples:
        #   E12
        #   E64
        # ----------------------------------------------------

        if re.search(
            r"\bE\d+\b",
            description,
            flags=re.IGNORECASE,
        ):
            violations.append(
                "trajectory_event_id"
            )

        # ----------------------------------------------------
        # B. Execution-narrative language
        #
        # KT descriptions should contain repository knowledge,
        # not descriptions of what the agent did.
        # ----------------------------------------------------

        execution_patterns = {
            "the agent": (
                "agent_execution_reference"
            ),
            "agent's edit": (
                "agent_edit_reference"
            ),
            "agent edit": (
                "agent_edit_reference"
            ),
            "direct edit": (
                "agent_edit_reference"
            ),
            "direct edits": (
                "agent_edit_reference"
            ),
            "the trajectory": (
                "trajectory_reference"
            ),
            "trajectory shows": (
                "trajectory_reference"
            ),
            "after the edit": (
                "post_edit_reference"
            ),
            "after the edits": (
                "post_edit_reference"
            ),
            "after editing": (
                "post_edit_reference"
            ),
            "post-execution": (
                "post_execution_reference"
            ),
            "final repository state": (
                "post_execution_reference"
            ),
        }

        for phrase, violation in (
            execution_patterns.items()
        ):
            if phrase in normalized:
                if violation not in violations:
                    violations.append(
                        violation
                    )

        # ----------------------------------------------------
        # C. Persistence / application conclusions
        # ----------------------------------------------------

        state_claim_patterns = {
            "did not persist": (
                "persistence_claim"
            ),
            "failed to persist": (
                "persistence_claim"
            ),
            "did not successfully": (
                "execution_outcome_claim"
            ),
            "was not successfully": (
                "execution_outcome_claim"
            ),
            "were not successfully": (
                "execution_outcome_claim"
            ),
            "did not change": (
                "execution_outcome_claim"
            ),
            "was not changed": (
                "execution_outcome_claim"
            ),
            "were not changed": (
                "execution_outcome_claim"
            ),
            "failed to apply": (
                "patch_application_claim"
            ),
            "was not applied": (
                "patch_application_claim"
            ),
            "were not applied": (
                "patch_application_claim"
            ),
            "successfully applied": (
                "patch_application_claim"
            ),
            "successfully added": (
                "execution_outcome_claim"
            ),
            "not successfully added": (
                "execution_outcome_claim"
            ),
        }

        for phrase, violation in (
            state_claim_patterns.items()
        ):
            if phrase in normalized:
                if violation not in violations:
                    violations.append(
                        violation
                    )

        # ----------------------------------------------------
        # D. Reject or keep
        # ----------------------------------------------------

        if violations:

            rejected.append(
                RejectedTarget(
                    proposal_id=(
                        proposal.proposal_id
                    ),
                    description=(
                        proposal.description
                    ),
                    rejection_stage=(
                        "target_scope"
                    ),
                    reason=(
                        "execution_dependent_target_description"
                    ),
                    details={
                        "violations": (
                            violations
                        ),
                    },
                )
            )

            continue

        accepted.append(
            proposal
        )

    return (
        accepted,
        rejected,
    )



def construct_knowledge_targets(
    task_description: str,
    gap: ObservedGap,
    retrieval_result: EvidenceRetrievalResult,
    llm: Optional[
        FixedLLMClient
    ] = None,
    config: ExperimentConfig = CONFIG,
) -> TargetConstructionResult:
    """
    Stage 1C.

    Flow:

        gap
        + trajectory evidence
        + repository evidence
                ↓
        LLM target proposals
                ↓
        exact trajectory-span grounding
                ↓
        exact repository-span grounding
                ↓
        semantic support verification
                ↓
        deterministic target-scope guard
                ↓
        rejection logging
                ↓
        duplicate detection
                ↓
        deterministic merge
                ↓
        fixed N_max evidence-priority cap
                ↓
        final KT_k
    """

    task_description = (
        task_description.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if (
        retrieval_result.gap_id
        != gap.gap_id
    ):
        raise ValueError(
            "retrieval_result and gap refer to different gap IDs."
        )

    evidence_items = (
        retrieval_result.evidence
    )

    if not evidence_items:
        return (
            TargetConstructionResult(
                gap_id=(
                    gap.gap_id
                ),
                proposed_target_count=0,
                grounding_valid_count=0,
                generated_targets=[],
                rejected_targets=[],
                support_records=[],
                merged_targets=[],
                selected_targets=[],
                duplicate_groups=[],
            )
        )

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    # --------------------------------------------------------
    # 1. Generate target proposals
    # --------------------------------------------------------

    parsed = llm.complete_json(
        prompt=_build_target_construction_prompt(
            task_description=(
                task_description
            ),
            gap=(
                gap
            ),
            evidence_items=(
                evidence_items
            ),
        ),
        system_prompt=(
            TARGET_CONSTRUCTION_SYSTEM_PROMPT
        ),
    )

    # --------------------------------------------------------
    # 2. Deterministic exact grounding
    # --------------------------------------------------------

    (
        proposed_count,
        grounded_proposals,
        grounding_rejections,
    ) = _validate_target_proposals(
        parsed=(
            parsed
        ),
        gap=(
            gap
        ),
        evidence_items=(
            evidence_items
        ),
    )

    grounding_valid_count = (
        len(
            grounded_proposals
        )
    )

    # --------------------------------------------------------
    # 3. Semantic evidence-support verification
    # --------------------------------------------------------

    (
        supported_proposals,
        semantic_rejections,
    ) = _semantic_support_filter(
        proposals=(
            grounded_proposals
        ),
        llm=(
            llm
        ),
    )

    # --------------------------------------------------------
    # 3B. Deterministic target-scope guard
    #
    # A validated KT must describe repository knowledge only.
    # Execution narrative remains in trajectory provenance and
    # must not leak into the target description.
    # --------------------------------------------------------

    (
        supported_proposals,
        target_scope_rejections,
    ) = _deterministic_target_scope_filter(
        proposals=(
            supported_proposals
        ),
    )

    rejected_targets = (
        grounding_rejections
        + semantic_rejections
        + target_scope_rejections
    )

    # --------------------------------------------------------
    # 4. Build validated targets
    # --------------------------------------------------------

    (
        generated_targets,
        support_records,
    ) = _build_knowledge_targets(
        proposals=(
            supported_proposals
        ),
        gap=(
            gap
        ),
    )

    if not generated_targets:
        return (
            TargetConstructionResult(
                gap_id=(
                    gap.gap_id
                ),
                proposed_target_count=(
                    proposed_count
                ),
                grounding_valid_count=(
                    grounding_valid_count
                ),
                generated_targets=[],
                rejected_targets=(
                    rejected_targets
                ),
                support_records=[],
                merged_targets=[],
                selected_targets=[],
                duplicate_groups=[],
            )
        )

    # --------------------------------------------------------
    # 5. Duplicate detection
    # --------------------------------------------------------

    if (
        len(
            generated_targets
        )
        >= 2
    ):
        duplicate_output = (
            llm.complete_json(
                prompt=_build_duplicate_prompt(
                    targets=(
                        generated_targets
                    ),
                    evidence_items=(
                        evidence_items
                    ),
                ),
                system_prompt=(
                    DUPLICATE_TARGET_SYSTEM_PROMPT
                ),
            )
        )

        duplicate_groups = (
            _validate_duplicate_groups(
                parsed=(
                    duplicate_output
                ),
                targets=(
                    generated_targets
                ),
            )
        )

    else:
        duplicate_groups = []

    # --------------------------------------------------------
    # 6. Deterministic duplicate merge
    # --------------------------------------------------------

    merged_targets = (
        _merge_duplicate_targets(
            targets=(
                generated_targets
            ),
            duplicate_groups=(
                duplicate_groups
            ),
        )
    )

    # --------------------------------------------------------
    # 7. Fixed N_max evidence-priority cap
    # --------------------------------------------------------

    selected_targets = (
        _apply_target_cap(
            targets=(
                merged_targets
            ),
            evidence_items=(
                evidence_items
            ),
            config=(
                config
            ),
        )
    )

    return (
        TargetConstructionResult(
            gap_id=(
                gap.gap_id
            ),
            proposed_target_count=(
                proposed_count
            ),
            grounding_valid_count=(
                grounding_valid_count
            ),
            generated_targets=(
                generated_targets
            ),
            rejected_targets=(
                rejected_targets
            ),
            support_records=(
                support_records
            ),
            merged_targets=(
                merged_targets
            ),
            selected_targets=(
                selected_targets
            ),
            duplicate_groups=(
                duplicate_groups
            ),
        )
    )