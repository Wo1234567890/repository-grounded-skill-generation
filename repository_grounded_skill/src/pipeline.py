from __future__ import annotations

import hashlib
import json
import pickle
import shutil
import subprocess
import tempfile

from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
)

from src.clients.llm_client import FixedLLMClient
from src.config import CONFIG, ExperimentConfig

from src.models import (
    BaselineProbeResult,
    CandidateKnowledge,
    CandidateTargetMatch,
    DiagnosticQuestion,
    FinalSkillStatement,
    InterventionResult,
    KnowledgeTarget,
    ObservedGap,
    RepresentativeCandidate,
    RepositoryEvidence,
    RepositoryRedundancyResult,
)

from src.step0_candidate_preparation import (
    prepare_candidate_knowledge,
)

from src.stage1_target_construction import (
    EvidenceRetrievalResult,
    RepositorySnapshotInfo,
    TargetConstructionResult,
    construct_knowledge_targets,
    deduplicate_targets_globally,
    discover_observed_gaps,
    retrieve_repository_evidence,
    verify_repository_snapshot,
)

from src.stage2_probing import (
    DiagnosticQuestionConstructionResult,
    generate_diagnostic_question,
)

from src.stage2_baseline_probing.baseline_runner import (
    run_baseline_probe,
)

from src.stage3_repository_redundancy.repository_redundancy import (
    evaluate_repository_redundancy,
)

from src.stage3_candidate_matching.candidate_matching import (
    evaluate_candidate_target_match,
)

from src.stage3_intervention import (
    run_knowledge_intervention,
)

from src.stage4_recomposition import (
    recompose_final_skill_statement,
    select_representative_candidate,
)



# ============================================================
# Pipeline Checkpoint / Resume
# ============================================================

PIPELINE_CHECKPOINT_SCHEMA_VERSION = 1


def _stable_sha256(
    value: Any,
) -> str:
    """
    Stable SHA-256 for JSON-compatible experiment inputs.
    """

    serialized = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def _method_code_sha256() -> str:
    """
    Hash all Python source files under src/.

    This prevents a checkpoint created under one method
    implementation from being silently reused after code changes.
    """

    src_root = (
        Path(__file__)
        .resolve()
        .parent
    )

    digest = hashlib.sha256()

    source_files = sorted(
        src_root.rglob("*.py"),
        key=lambda p: str(
            p.relative_to(
                src_root
            )
        ),
    )

    for source_file in source_files:

        relative = str(
            source_file.relative_to(
                src_root
            )
        )

        digest.update(
            relative.encode("utf-8")
        )

        digest.update(
            b"\0"
        )

        digest.update(
            source_file.read_bytes()
        )

        digest.update(
            b"\0"
        )

    return digest.hexdigest()


def _normalize_checkpoint_metadata(
    metadata: Optional[
        Mapping[str, Any]
    ],
) -> Dict[str, Any]:

    if metadata is None:
        return {}

    # Round-trip through JSON so Path objects and similar values
    # become stable strings.
    return json.loads(
        json.dumps(
            dict(metadata),
            ensure_ascii=False,
            sort_keys=True,
            default=str,
        )
    )


def _build_pipeline_checkpoint_identity(
    repository_path: str,
    expected_base_commit: str,
    task_description: str,
    candidate_skills: Mapping[
        str,
        str,
    ],
    precomputed_trajectory: List[
        Dict[str, Any]
    ],
    config: ExperimentConfig,
    metadata: Optional[
        Mapping[str, Any]
    ],
) -> Dict[str, Any]:
    """
    Build a strict identity for one frozen experiment input.
    """

    config_payload = (
        vars(config)
        if hasattr(
            config,
            "__dict__",
        )
        else repr(config)
    )

    identity = {
        "schema_version": (
            PIPELINE_CHECKPOINT_SCHEMA_VERSION
        ),
        "repository_path": str(
            Path(
                repository_path
            )
            .expanduser()
            .resolve()
        ),
        "expected_base_commit": (
            expected_base_commit
        ),
        "task_description_sha256": (
            _stable_sha256(
                task_description
            )
        ),
        "candidate_skills_sha256": (
            _stable_sha256(
                dict(
                    candidate_skills
                )
            )
        ),
        "trajectory_sha256": (
            _stable_sha256(
                precomputed_trajectory
            )
        ),
        "config_sha256": (
            _stable_sha256(
                config_payload
            )
        ),
        "method_code_sha256": (
            _method_code_sha256()
        ),
        "metadata": (
            _normalize_checkpoint_metadata(
                metadata
            )
        ),
    }

    identity[
        "fingerprint"
    ] = _stable_sha256(
        identity
    )

    return identity


def _checkpoint_meta_path(
    checkpoint_path: Path,
) -> Path:

    return checkpoint_path.with_name(
        checkpoint_path.name
        + ".meta.json"
    )


def _atomic_write_bytes(
    path: Path,
    data: bytes,
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = path.with_name(
        path.name
        + ".tmp"
    )

    temp_path.write_bytes(
        data
    )

    temp_path.replace(
        path
    )


def _atomic_write_text(
    path: Path,
    text: str,
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = path.with_name(
        path.name
        + ".tmp"
    )

    temp_path.write_text(
        text,
        encoding="utf-8",
    )

    temp_path.replace(
        path
    )


def _save_pipeline_checkpoint(
    checkpoint_path: Path,
    identity: Dict[
        str,
        Any,
    ],
    state: Dict[
        str,
        Any,
    ],
    next_target_id: Optional[
        str
    ],
) -> None:
    """
    Save complete resumable Stage-1 + target progress.

    Pickle is used only as a local technical resume format.
    Human-readable identity/progress is stored separately in JSON.
    """

    payload = {
        "schema_version": (
            PIPELINE_CHECKPOINT_SCHEMA_VERSION
        ),
        "identity_fingerprint": (
            identity[
                "fingerprint"
            ]
        ),
        "state": state,
    }

    serialized = pickle.dumps(
        payload,
        protocol=(
            pickle.HIGHEST_PROTOCOL
        ),
    )

    _atomic_write_bytes(
        checkpoint_path,
        serialized,
    )

    target_records = (
        state.get(
            "target_records",
            [],
        )
    )

    meta = {
        "schema_version": (
            PIPELINE_CHECKPOINT_SCHEMA_VERSION
        ),
        "identity": identity,
        "completed_target_ids": [
            record.target_id
            for record
            in target_records
        ],
        "completed_target_count": (
            len(
                target_records
            )
        ),
        "total_target_count": (
            len(
                state.get(
                    "all_targets",
                    [],
                )
            )
        ),
        "next_target_id": (
            next_target_id
        ),
    }

    _atomic_write_text(
        _checkpoint_meta_path(
            checkpoint_path
        ),
        json.dumps(
            meta,
            indent=2,
            ensure_ascii=False,
            default=str,
        ),
    )


def _load_pipeline_checkpoint(
    checkpoint_path: Path,
    expected_identity: Dict[
        str,
        Any,
    ],
) -> Dict[str, Any]:
    """
    Load a checkpoint only when its frozen experiment identity
    exactly matches the current invocation.
    """

    meta_path = (
        _checkpoint_meta_path(
            checkpoint_path
        )
    )

    if not meta_path.exists():
        raise RuntimeError(
            "Checkpoint pickle exists but checkpoint metadata "
            "is missing.\n"
            f"Checkpoint: {checkpoint_path}\n"
            f"Metadata:   {meta_path}"
        )

    meta = json.loads(
        meta_path.read_text(
            encoding="utf-8"
        )
    )

    stored_identity = (
        meta.get(
            "identity",
            {}
        )
    )

    stored_fingerprint = (
        stored_identity.get(
            "fingerprint"
        )
    )

    expected_fingerprint = (
        expected_identity.get(
            "fingerprint"
        )
    )

    if (
        stored_fingerprint
        != expected_fingerprint
    ):
        raise RuntimeError(
            "Checkpoint identity mismatch.\n"
            "The checkpoint was created from different "
            "experiment inputs or method code.\n\n"
            f"Checkpoint fingerprint: {stored_fingerprint}\n"
            f"Current fingerprint:    {expected_fingerprint}\n\n"
            "Delete the checkpoint only if you intentionally "
            "want to start a fresh run."
        )

    payload = pickle.loads(
        checkpoint_path.read_bytes()
    )

    if (
        payload.get(
            "schema_version"
        )
        != PIPELINE_CHECKPOINT_SCHEMA_VERSION
    ):
        raise RuntimeError(
            "Unsupported pipeline checkpoint schema version."
        )

    if (
        payload.get(
            "identity_fingerprint"
        )
        != expected_fingerprint
    ):
        raise RuntimeError(
            "Checkpoint pickle and metadata identity do not match."
        )

    state = payload.get(
        "state"
    )

    if not isinstance(
        state,
        dict,
    ):
        raise RuntimeError(
            "Checkpoint state is invalid."
        )

    return state


# ============================================================
# Target terminal states
# ============================================================

STATUS_AGENT_ALREADY_KNOWS = "AGENT_ALREADY_KNOWS"
STATUS_REPOSITORY_PROVIDED = "REPOSITORY_PROVIDED"
STATUS_NO_MATCHING_CANDIDATE = "NO_MATCHING_CANDIDATE"
STATUS_NO_EFFECTIVE_CANDIDATE = "NO_EFFECTIVE_CANDIDATE"
STATUS_RESOLVED = "RESOLVED"


# ============================================================
# Per-target pipeline record
# ============================================================

@dataclass
class TargetPipelineRecord:
    """
    Complete pipeline record for one knowledge target KT_k.

    status is one of:

        AGENT_ALREADY_KNOWS
        REPOSITORY_PROVIDED
        NO_MATCHING_CANDIDATE
        NO_EFFECTIVE_CANDIDATE
        RESOLVED
    """

    gap_id: str
    target_id: str
    status: str

    question_construction: Optional[
        DiagnosticQuestionConstructionResult
    ] = None

    question: Optional[
        DiagnosticQuestion
    ] = None

    baseline_result: Optional[
        BaselineProbeResult
    ] = None

    repository_redundancy: Optional[
        RepositoryRedundancyResult
    ] = None

    candidate_matches: List[
        CandidateTargetMatch
    ] = field(
        default_factory=list
    )

    intervention_results: List[
        InterventionResult
    ] = field(
        default_factory=list
    )

    representative: Optional[
        RepresentativeCandidate
    ] = None

    final_statement: Optional[
        FinalSkillStatement
    ] = None


# ============================================================
# Complete pipeline result
# ============================================================

@dataclass
class PipelineResult:
    """
    Complete result of one repository-grounded skill run.
    """

    snapshot: RepositorySnapshotInfo

    candidates: List[
        CandidateKnowledge
    ]

    no_skill_run: Any

    gaps: List[
        ObservedGap
    ]

    evidence_by_gap: Dict[
        str,
        EvidenceRetrievalResult
    ]

    target_construction_by_gap: Dict[
        str,
        TargetConstructionResult
    ]

    targets: List[
        KnowledgeTarget
    ]

    target_records: List[
        TargetPipelineRecord
    ]

    final_statements: List[
        FinalSkillStatement
    ]

    final_skill: str


# ============================================================
# Small extraction helpers
#
# These isolate the orchestration layer from internal audit fields
# inside Stage 1 / Stage 2 construction-result objects.
# ============================================================

def _extract_repository_evidence(
    retrieval_result: EvidenceRetrievalResult,
) -> List[
    RepositoryEvidence
]:
    """
    Extract repository evidence from EvidenceRetrievalResult.

    Preferred public field names are tried first.

    If the result dataclass changes internally, fail explicitly
    instead of silently using the wrong data.
    """

    preferred_names = (
        "evidence_items",
        "repository_evidence",
        "evidence",
        "items",
    )

    for name in preferred_names:

        if not hasattr(
            retrieval_result,
            name,
        ):
            continue

        value = getattr(
            retrieval_result,
            name,
        )

        if isinstance(
            value,
            (list, tuple),
        ):

            if all(
                isinstance(
                    item,
                    RepositoryEvidence,
                )
                for item in value
            ):
                return list(
                    value
                )

    raise RuntimeError(
        "Could not extract RepositoryEvidence items from "
        "EvidenceRetrievalResult. "
        f"Available fields: "
        f"{list(getattr(retrieval_result, '__dataclass_fields__', {}).keys())}"
    )


def _extract_selected_targets(
    result: TargetConstructionResult,
) -> List[
    KnowledgeTarget
]:
    """
    Extract the final selected Stage 1 targets.

    We deliberately do not use generated/rejected/intermediate
    targets.
    """

    preferred_names = (
        "selected_targets",
        "selected",
        "targets",
        "knowledge_targets",
    )

    for name in preferred_names:

        if not hasattr(
            result,
            name,
        ):
            continue

        value = getattr(
            result,
            name,
        )

        if isinstance(
            value,
            (list, tuple),
        ):

            if all(
                isinstance(
                    item,
                    KnowledgeTarget,
                )
                for item in value
            ):
                return list(
                    value
                )

    raise RuntimeError(
        "Could not extract selected KnowledgeTarget items "
        "from TargetConstructionResult. "
        f"Available fields: "
        f"{list(getattr(result, '__dataclass_fields__', {}).keys())}"
    )


def _extract_diagnostic_question(
    result: DiagnosticQuestionConstructionResult,
) -> DiagnosticQuestion:
    """
    Extract the validated canonical Q_k from Stage 2A.
    """

    preferred_names = (
        "question",
        "diagnostic_question",
    )

    for name in preferred_names:

        if not hasattr(
            result,
            name,
        ):
            continue

        value = getattr(
            result,
            name,
        )

        if isinstance(
            value,
            DiagnosticQuestion,
        ):
            return value

    raise RuntimeError(
        "Could not extract DiagnosticQuestion from "
        "DiagnosticQuestionConstructionResult. "
        f"Available fields: "
        f"{list(getattr(result, '__dataclass_fields__', {}).keys())}"
    )


# ============================================================
# Target-specific repository evidence
# ============================================================

def _evidence_for_target(
    target: KnowledgeTarget,
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> List[
    RepositoryEvidence
]:
    """
    Return E_k in the exact order recorded by KT_k.
    """

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence
        in evidence_items
    }

    selected: List[
        RepositoryEvidence
    ] = []

    for evidence_id in (
        target.repository_evidence_ids
    ):

        if (
            evidence_id
            not in evidence_by_id
        ):
            raise RuntimeError(
                f"Target {target.target_id} refers to "
                f"missing repository evidence "
                f"{evidence_id}."
            )

        selected.append(
            evidence_by_id[
                evidence_id
            ]
        )

    return selected


# ============================================================
# Git helpers
# ============================================================

def _run_git(
    repository_path: str,
    args: Sequence[str],
    check: bool = True,
) -> subprocess.CompletedProcess:
    """
    Run git without shell=True.
    """

    command = [
        "git",
        "-C",
        repository_path,
        *args,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if (
        check
        and result.returncode != 0
    ):
        raise RuntimeError(
            "Git command failed:\n"
            f"{' '.join(command)}\n\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    return result


@contextmanager
def _temporary_no_skill_worktree(
    repository_path: str,
    expected_base_commit: str,
) -> Iterator[str]:
    """
    Create an isolated writable worktree for the no-skill run.

    Why:
        the no-skill coding agent is allowed to modify files.

        Stage 1 repository evidence, however, must come from the
        untouched base_commit snapshot.

    Therefore the no-skill execution must not contaminate the
    repository used by later repository-grounded stages.
    """

    parent_dir = tempfile.mkdtemp(
        prefix="repo_grounded_no_skill_"
    )

    worktree_path = (
        Path(parent_dir)
        / "worktree"
    )

    try:

        _run_git(
            repository_path=(
                repository_path
            ),
            args=[
                "worktree",
                "add",
                "--detach",
                str(worktree_path),
                expected_base_commit,
            ],
        )

        yield str(
            worktree_path
        )

    finally:

        _run_git(
            repository_path=(
                repository_path
            ),
            args=[
                "worktree",
                "remove",
                "--force",
                str(worktree_path),
            ],
            check=False,
        )

        _run_git(
            repository_path=(
                repository_path
            ),
            args=[
                "worktree",
                "prune",
            ],
            check=False,
        )

        shutil.rmtree(
            parent_dir,
            ignore_errors=True,
        )


# ============================================================
# Step 0:
# Prepare all candidate knowledge
# ============================================================

def _prepare_all_candidates(
    candidate_skills: Mapping[
        str,
        str
    ],
    llm: FixedLLMClient,
) -> List[
    CandidateKnowledge
]:
    """
    Decompose all source skills into atomic K_i units.

    Candidate IDs are normalized globally so different source
    skills cannot accidentally produce duplicate K_1/K_2 IDs.
    """

    if not candidate_skills:
        raise ValueError(
            "candidate_skills cannot be empty."
        )

    raw_candidates: List[
        CandidateKnowledge
    ] = []

    for (
        source_skill,
        skill_text,
    ) in candidate_skills.items():

        if not isinstance(
            source_skill,
            str,
        ):
            raise TypeError(
                "Candidate skill source names must be strings."
            )

        if not isinstance(
            skill_text,
            str,
        ):
            raise TypeError(
                "Candidate skill text must be a string."
            )

        if not skill_text.strip():
            continue

        units = (
            prepare_candidate_knowledge(
                skill_text=(
                    skill_text
                ),
                source_skill=(
                    source_skill
                ),
                llm=(
                    llm
                ),
            )
        )

        raw_candidates.extend(
            units
        )

    if not raw_candidates:
        raise RuntimeError(
            "Step 0 produced no candidate knowledge units."
        )

    # --------------------------------------------------------
    # Global deterministic IDs.
    # --------------------------------------------------------

    candidates: List[
        CandidateKnowledge
    ] = []

    for index, unit in enumerate(
        raw_candidates,
        start=1,
    ):

        candidates.append(
            CandidateKnowledge(
                candidate_id=(
                    f"K_{index}"
                ),
                text=(
                    unit.text
                ),
                source_skill=(
                    unit.source_skill
                ),
                token_count=(
                    unit.token_count
                ),
            )
        )

    return candidates


# ============================================================
# No-skill run
# ============================================================

def _run_no_skill_execution(
    agent: Any,
    repository_path: str,
    expected_base_commit: str,
    task_description: str,
) -> Any:
    """
    Run the target coding agent once without any skill.

    This uses a temporary writable git worktree.

    The original base repository remains clean and is later used
    for repository-grounded evidence and read-only probing.
    """

    if not hasattr(
        agent,
        "run_fresh_session",
    ):
        raise TypeError(
            "Target agent must implement run_fresh_session()."
        )

    with _temporary_no_skill_worktree(
        repository_path=(
            repository_path
        ),
        expected_base_commit=(
            expected_base_commit
        ),
    ) as worktree_path:

        result = (
            agent.run_fresh_session(
                repository_path=(
                    worktree_path
                ),
                prompt=(
                    task_description
                ),
            )
        )

    if not getattr(
        result,
        "success",
        False,
    ):
        raise RuntimeError(
            "No-skill target-agent execution failed.\n"
            f"Error: {getattr(result, 'error', None)}"
        )

    trajectory = getattr(
        result,
        "trajectory",
        None,
    )

    if not isinstance(
        trajectory,
        list,
    ):
        raise RuntimeError(
            "No-skill target-agent result does not contain "
            "a valid trajectory list."
        )

    return result


# ============================================================
# Final residual-skill assembly
# ============================================================

def _assemble_final_skill(
    statements: Sequence[
        FinalSkillStatement
    ],
) -> str:
    """
    Combine s_k statements in target-processing order.

    No additional LLM rewriting is performed here.
    """

    if not statements:
        return ""

    return "\n".join(
        f"- {statement.text.strip()}"
        for statement
        in statements
    )


# ============================================================
# Main Pipeline
# ============================================================

def run_repository_grounded_pipeline(
    agent: Any,
    repository_path: str,
    expected_base_commit: str,
    task_description: str,
    candidate_skills: Mapping[
        str,
        str
    ],
    aux_llm: Optional[
        FixedLLMClient
    ] = None,
    config: ExperimentConfig = CONFIG,
    verbose: bool = True,
    precomputed_trajectory: Optional[
        List[Dict[str, Any]]
    ] = None,
    checkpoint_path: Optional[str] = None,
    checkpoint_metadata: Optional[
        Mapping[str, Any]
    ] = None,
    resume_from_checkpoint: bool = True,

) -> PipelineResult:
    """
    Run the complete repository-grounded residual-skill pipeline.

    Flow
    ----

    Step 0
        Candidate knowledge preparation

    No-skill trajectory
        Obtain execution trajectory tau either from a fresh
        no-skill execution or from a precomputed benchmark run.

    Stage 1
        Gap discovery
        Repository evidence retrieval
        Knowledge-target construction

    Stage 2
        Diagnostic-question generation
        Shared baseline probing

    Stage 3A
        Repository redundancy

    Stage 3B
        Candidate-target matching

    Stage 3C
        Independent knowledge intervention

    Stage 4
        Representative selection
        Evidence-grounded recomposition

    Final
        Concatenate resolved s_k statements in target order.
    """

    # ========================================================
    # Basic validation
    # ========================================================

    repository_path = str(
        Path(repository_path)
        .expanduser()
        .resolve()
    )

    task_description = (
        task_description.strip()
    )

    expected_base_commit = (
        expected_base_commit.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if not expected_base_commit:
        raise ValueError(
            "expected_base_commit cannot be empty."
        )

    if aux_llm is None:
        aux_llm = (
            FixedLLMClient()
        )

    def log(
        message: str,
    ) -> None:

        if verbose:
            print(
                message,
                flush=True,
            )

    # ========================================================
    # Snapshot guard
    # ========================================================

    log(
        "[Pipeline] Verify base repository snapshot"
    )

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

    # ========================================================
    # Checkpoint initialization
    # ========================================================

    checkpoint_file: Optional[
        Path
    ] = None

    checkpoint_identity: Optional[
        Dict[str, Any]
    ] = None

    checkpoint_state: Optional[
        Dict[str, Any]
    ] = None

    if checkpoint_path is not None:

        if precomputed_trajectory is None:
            raise ValueError(
                "Checkpoint/resume currently requires "
                "precomputed_trajectory so the frozen trajectory "
                "identity can be verified before resuming."
            )

        checkpoint_file = (
            Path(
                checkpoint_path
            )
            .expanduser()
            .resolve()
        )

        checkpoint_identity = (
            _build_pipeline_checkpoint_identity(
                repository_path=(
                    repository_path
                ),
                expected_base_commit=(
                    expected_base_commit
                ),
                task_description=(
                    task_description
                ),
                candidate_skills=(
                    candidate_skills
                ),
                precomputed_trajectory=(
                    precomputed_trajectory
                ),
                config=(
                    config
                ),
                metadata=(
                    checkpoint_metadata
                ),
            )
        )

        if (
            resume_from_checkpoint
            and checkpoint_file.exists()
        ):
            checkpoint_state = (
                _load_pipeline_checkpoint(
                    checkpoint_path=(
                        checkpoint_file
                    ),
                    expected_identity=(
                        checkpoint_identity
                    ),
                )
            )

            log(
                "[Checkpoint] Valid checkpoint loaded"
            )

    # ========================================================
    # Resume frozen Step 0 + Stage 1
    # ========================================================

    if checkpoint_state is not None:

        candidates = list(
            checkpoint_state[
                "candidates"
            ]
        )

        gaps = list(
            checkpoint_state[
                "gaps"
            ]
        )

        evidence_by_gap = dict(
            checkpoint_state[
                "evidence_by_gap"
            ]
        )

        target_construction_by_gap = dict(
            checkpoint_state[
                "target_construction_by_gap"
            ]
        )

        all_targets = list(
            checkpoint_state[
                "all_targets"
            ]
        )

        # This experiment uses a fixed precomputed trajectory.
        trajectory = list(
            precomputed_trajectory
        )

        no_skill_run = None

        evidence_items_by_gap = {
            gap_id: (
                _extract_repository_evidence(
                    retrieval_result
                )
            )
            for (
                gap_id,
                retrieval_result,
            )
            in evidence_by_gap.items()
        }

        log(
            f"[Checkpoint] Reuse frozen Step 0/Stage 1: "
            f"{len(candidates)} candidates, "
            f"{len(gaps)} gaps, "
            f"{len(all_targets)} targets"
        )

    else:

        # ========================================================
        # Step 0
        # ========================================================

        log(
            "[Pipeline] Step 0: prepare candidate knowledge"
        )

        candidates = (
            _prepare_all_candidates(
                candidate_skills=(
                    candidate_skills
                ),
                llm=(
                    aux_llm
                ),
            )
        )

        log(
            f"[Pipeline] Step 0 produced "
            f"{len(candidates)} candidate units"
        )

        # ========================================================
        # No-skill trajectory
        # ========================================================

        if precomputed_trajectory is not None:

            log(
                "[Pipeline] Use precomputed no-skill trajectory"
            )

            if not isinstance(
                precomputed_trajectory,
                list,
            ):
                raise TypeError(
                    "precomputed_trajectory must be a list."
                )

            if not precomputed_trajectory:
                raise ValueError(
                    "precomputed_trajectory cannot be empty."
                )

            if not all(
                isinstance(event, dict)
                for event in precomputed_trajectory
            ):
                raise TypeError(
                    "Every precomputed trajectory event "
                    "must be a dictionary."
                )

            trajectory = list(
                precomputed_trajectory
            )

            no_skill_run = None

        else:

            log(
                "[Pipeline] Run no-skill target-agent execution"
            )

            no_skill_run = (
                _run_no_skill_execution(
                    agent=(
                        agent
                    ),
                    repository_path=(
                        repository_path
                    ),
                    expected_base_commit=(
                        expected_base_commit
                    ),
                    task_description=(
                        task_description
                    ),
                )
            )

            trajectory = (
                no_skill_run.trajectory
            )

        # --------------------------------------------------------
        # Verify original base repository is still untouched.
        # --------------------------------------------------------

        verify_repository_snapshot(
            repository_path=(
                repository_path
            ),
            expected_base_commit=(
                expected_base_commit
            ),
        )

        # ========================================================
        # Stage 1A:
        # Observed gaps
        # ========================================================

        log(
            "[Pipeline] Stage 1A: discover observed gaps"
        )

        gaps = (
            discover_observed_gaps(
                task_description=(
                    task_description
                ),
                trajectory=(
                    trajectory
                ),
                llm=(
                    aux_llm
                ),
            )
        )

        log(
            f"[Pipeline] Stage 1A found "
            f"{len(gaps)} observed gaps"
        )

        # ========================================================
        # Stage 1B + 1C
        # ========================================================

        evidence_by_gap: Dict[
            str,
            EvidenceRetrievalResult
        ] = {}

        target_construction_by_gap: Dict[
            str,
            TargetConstructionResult
        ] = {}

        all_targets: List[
            KnowledgeTarget
        ] = []

        evidence_items_by_gap: Dict[
            str,
            List[RepositoryEvidence]
        ] = {}

        seen_target_ids = set()

        for gap in gaps:

            log(
                f"[Pipeline] Stage 1B: retrieve evidence "
                f"for {gap.gap_id}"
            )

            retrieval_result = (
                retrieve_repository_evidence(
                    repository_path=(
                        repository_path
                    ),
                    task_description=(
                        task_description
                    ),
                    gap=(
                        gap
                    ),
                    expected_base_commit=(
                        expected_base_commit
                    ),
                    llm=(
                        aux_llm
                    ),
                )
            )

            evidence_by_gap[
                gap.gap_id
            ] = retrieval_result

            evidence_items = (
                _extract_repository_evidence(
                    retrieval_result
                )
            )

            evidence_items_by_gap[
                gap.gap_id
            ] = evidence_items

            log(
                f"[Pipeline] Stage 1C: construct targets "
                f"for {gap.gap_id}"
            )

            target_result = (
                construct_knowledge_targets(
                    task_description=(
                        task_description
                    ),
                    gap=(
                        gap
                    ),
                    retrieval_result=(
                        retrieval_result
                    ),
                    llm=(
                        aux_llm
                    ),
                    config=(
                        config
                    ),
                )
            )

            target_construction_by_gap[
                gap.gap_id
            ] = target_result

            selected_targets = (
                _extract_selected_targets(
                    target_result
                )
            )

            for target in (
                selected_targets
            ):

                if (
                    target.target_id
                    in seen_target_ids
                ):
                    raise RuntimeError(
                        "Duplicate target ID across gaps: "
                        f"{target.target_id}"
                    )

                if (
                    target.gap_id
                    != gap.gap_id
                ):
                    raise RuntimeError(
                        f"Target {target.target_id} has "
                        f"gap_id={target.gap_id}, expected "
                        f"{gap.gap_id}."
                    )

                seen_target_ids.add(
                    target.target_id
                )

                all_targets.append(
                    target
                )

        # ====================================================
        # Stage 1D: global cross-gap semantic deduplication
        # ====================================================

        global_evidence_items: List[
            RepositoryEvidence
        ] = []

        seen_global_evidence_ids = set()

        for gap in gaps:
            for evidence_item in (
                evidence_items_by_gap.get(
                    gap.gap_id,
                    [],
                )
            ):
                if (
                    evidence_item.evidence_id
                    in seen_global_evidence_ids
                ):
                    continue

                seen_global_evidence_ids.add(
                    evidence_item.evidence_id
                )

                global_evidence_items.append(
                    evidence_item
                )

        targets_before_global_dedup = (
            len(all_targets)
        )

        (
            all_targets,
            global_duplicate_groups,
        ) = deduplicate_targets_globally(
            targets=all_targets,
            evidence_items=(
                global_evidence_items
            ),
            llm=aux_llm,
        )

        log(
            f"[Pipeline] Stage 1 global dedup: "
            f"{targets_before_global_dedup} -> "
            f"{len(all_targets)} targets "
            f"({len(global_duplicate_groups)} "
            f"duplicate groups)"
        )

        log(
            f"[Pipeline] Stage 1 produced "
            f"{len(all_targets)} selected targets"
        )

    # ========================================================
    # Stage 2 → Stage 4:
    # Process targets in fixed Stage 1 order.
    # ========================================================

    if checkpoint_state is not None:

        target_records: List[
            TargetPipelineRecord
        ] = list(
            checkpoint_state.get(
                "target_records",
                [],
            )
        )

        final_statements: List[
            FinalSkillStatement
        ] = list(
            checkpoint_state.get(
                "final_statements",
                [],
            )
        )

    else:

        target_records: List[
            TargetPipelineRecord
        ] = []

        final_statements: List[
            FinalSkillStatement
        ] = []

    candidate_by_id = {
        candidate.candidate_id: candidate
        for candidate
        in candidates
    }

    def _save_current_progress_checkpoint(
        next_target_id: Optional[
            str
        ],
    ) -> None:

        if (
            checkpoint_file is None
            or checkpoint_identity is None
        ):
            return

        checkpoint_payload = {
            "candidates": list(
                candidates
            ),
            "gaps": list(
                gaps
            ),
            "evidence_by_gap": dict(
                evidence_by_gap
            ),
            "target_construction_by_gap": dict(
                target_construction_by_gap
            ),
            "all_targets": list(
                all_targets
            ),
            "target_records": list(
                target_records
            ),
            "final_statements": list(
                final_statements
            ),
        }

        _save_pipeline_checkpoint(
            checkpoint_path=(
                checkpoint_file
            ),
            identity=(
                checkpoint_identity
            ),
            state=(
                checkpoint_payload
            ),
            next_target_id=(
                next_target_id
            ),
        )

        log(
            f"[Checkpoint] Saved "
            f"{len(target_records)}/"
            f"{len(all_targets)} completed targets"
        )


    completed_target_ids = {
        record.target_id
        for record in target_records
    }

    valid_target_ids = {
        target.target_id
        for target in all_targets
    }

    unknown_completed_ids = (
        completed_target_ids
        - valid_target_ids
    )

    if unknown_completed_ids:
        raise RuntimeError(
            "Checkpoint contains completed target IDs that "
            "are not present in the frozen Stage 1 target set: "
            f"{sorted(unknown_completed_ids)}"
        )

    for target_index, target in enumerate(
        all_targets,
        start=1,
    ):

        if (
            target.target_id
            in completed_target_ids
        ):
            log(
                f"[Pipeline] Target "
                f"{target_index}/{len(all_targets)}: "
                f"{target.target_id} "
                "[RESUME: already completed]"
            )
            continue

        # Save all PREVIOUS completed targets before starting
        # the next target. If this target fails technically,
        # a rerun resumes exactly here.
        _save_current_progress_checkpoint(
            next_target_id=(
                target.target_id
            )
        )

        log(
            f"[Pipeline] Target "
            f"{target_index}/{len(all_targets)}: "
            f"{target.target_id}"
        )

        if (
            target.gap_id
            not in evidence_items_by_gap
        ):
            raise RuntimeError(
                f"No repository evidence collection "
                f"for target {target.target_id}."
            )

        gap_evidence = (
            evidence_items_by_gap[
                target.gap_id
            ]
        )

        target_evidence = (
            _evidence_for_target(
                target=(
                    target
                ),
                evidence_items=(
                    gap_evidence
                ),
            )
        )

        # ====================================================
        # Stage 2A:
        # Q_k
        # ====================================================

        log(
            f"  [Stage 2A] Generate diagnostic question"
        )

        question_construction = (
            generate_diagnostic_question(
                task_description=(
                    task_description
                ),
                target=(
                    target
                ),
                evidence_items=(
                    target_evidence
                ),
                llm=(
                    aux_llm
                ),
                config=(
                    config
                ),
            )
        )

        question = (
            _extract_diagnostic_question(
                question_construction
            )
        )

        # ====================================================
        # Stage 2B:
        # Shared baseline B_k
        # ====================================================

        log(
            f"  [Stage 2B] Baseline probing "
            f"r={config.probe_repetitions}"
        )

        baseline_result = (
            run_baseline_probe(
                agent=(
                    agent
                ),
                repository_path=(
                    repository_path
                ),
                task_description=(
                    task_description
                ),
                question=(
                    question
                ),
                repetitions=(
                    config.probe_repetitions
                ),
            )
        )

        # ====================================================
        # Gate:
        #
        # B_k = 1
        #
        # Agent already demonstrates target knowledge.
        # ====================================================

        if not (
            baseline_result.agent_needs
        ):

            log(
                "  [STOP] AGENT_ALREADY_KNOWS"
            )

            target_records.append(
                TargetPipelineRecord(
                    gap_id=(
                        target.gap_id
                    ),
                    target_id=(
                        target.target_id
                    ),
                    status=(
                        STATUS_AGENT_ALREADY_KNOWS
                    ),
                    question_construction=(
                        question_construction
                    ),
                    question=(
                        question
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                )
            )

            continue

        # ====================================================
        # Stage 3A:
        # RepositoryProvides(KT_k)
        # ====================================================

        log(
            "  [Stage 3A] Repository redundancy"
        )

        repository_result = (
            evaluate_repository_redundancy(
                target=(
                    target
                ),
                baseline_result=(
                    baseline_result
                ),
                repository_evidence=(
                    target_evidence
                ),
                llm=(
                    aux_llm
                ),
            )
        )

        # ====================================================
        # Gate:
        #
        # RepositoryProvides = YES
        # ====================================================

        if (
            repository_result.is_provided
        ):

            log(
                "  [STOP] REPOSITORY_PROVIDED"
            )

            target_records.append(
                TargetPipelineRecord(
                    gap_id=(
                        target.gap_id
                    ),
                    target_id=(
                        target.target_id
                    ),
                    status=(
                        STATUS_REPOSITORY_PROVIDED
                    ),
                    question_construction=(
                        question_construction
                    ),
                    question=(
                        question
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                    repository_redundancy=(
                        repository_result
                    ),
                )
            )

            continue

        # ====================================================
        # Stage 3B:
        # Candidate ↔ Target matching
        # ====================================================

        log(
            "  [Stage 3B] Candidate-target matching"
        )

        candidate_matches: List[
            CandidateTargetMatch
        ] = []

        matched_candidates: List[
            CandidateKnowledge
        ] = []

        for candidate in candidates:

            match = (
                evaluate_candidate_target_match(
                    candidate=(
                        candidate
                    ),
                    target=(
                        target
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                    repository_redundancy=(
                        repository_result
                    ),
                    llm=(
                        aux_llm
                    ),
                )
            )

            candidate_matches.append(
                match
            )

            if (
                match.is_match
            ):
                matched_candidates.append(
                    candidate
                )

        # ====================================================
        # Gate:
        #
        # No candidate contains sufficient target knowledge.
        # ====================================================

        if not matched_candidates:

            log(
                "  [STOP] NO_MATCHING_CANDIDATE"
            )

            target_records.append(
                TargetPipelineRecord(
                    gap_id=(
                        target.gap_id
                    ),
                    target_id=(
                        target.target_id
                    ),
                    status=(
                        STATUS_NO_MATCHING_CANDIDATE
                    ),
                    question_construction=(
                        question_construction
                    ),
                    question=(
                        question
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                    repository_redundancy=(
                        repository_result
                    ),
                    candidate_matches=(
                        candidate_matches
                    ),
                )
            )

            continue

        # ====================================================
        # Stage 3C:
        # Independent intervention
        # ====================================================

        log(
            f"  [Stage 3C] Intervention on "
            f"{len(matched_candidates)} matched candidates"
        )

        match_by_candidate = {
            match.candidate_id: match
            for match
            in candidate_matches
            if match.is_match
        }

        intervention_results: List[
            InterventionResult
        ] = []

        for candidate in (
            matched_candidates
        ):

            intervention = (
                run_knowledge_intervention(
                    agent=(
                        agent
                    ),
                    repository_path=(
                        repository_path
                    ),
                    task_description=(
                        task_description
                    ),
                    question=(
                        question
                    ),
                    candidate=(
                        candidate
                    ),
                    target_match=(
                        match_by_candidate[
                            candidate.candidate_id
                        ]
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                    repository_redundancy=(
                        repository_result
                    ),
                    repetitions=(
                        config.probe_repetitions
                    ),
                )
            )

            intervention_results.append(
                intervention
            )

        # ====================================================
        # Stage 4A:
        # Representative selection
        # ====================================================

        log(
            "  [Stage 4A] Representative selection"
        )

        representative = (
            select_representative_candidate(
                target_id=(
                    target.target_id
                ),
                candidates=(
                    candidates
                ),
                intervention_results=(
                    intervention_results
                ),
            )
        )

        # ====================================================
        # Gate:
        #
        # Matches existed, but no delta=1 candidate.
        # ====================================================

        if (
            representative
            is None
        ):

            log(
                "  [STOP] NO_EFFECTIVE_CANDIDATE"
            )

            target_records.append(
                TargetPipelineRecord(
                    gap_id=(
                        target.gap_id
                    ),
                    target_id=(
                        target.target_id
                    ),
                    status=(
                        STATUS_NO_EFFECTIVE_CANDIDATE
                    ),
                    question_construction=(
                        question_construction
                    ),
                    question=(
                        question
                    ),
                    baseline_result=(
                        baseline_result
                    ),
                    repository_redundancy=(
                        repository_result
                    ),
                    candidate_matches=(
                        candidate_matches
                    ),
                    intervention_results=(
                        intervention_results
                    ),
                )
            )

            continue

        # ====================================================
        # Resolve selected K_i* and intervention
        # ====================================================

        selected_candidate = (
            candidate_by_id[
                representative.candidate_id
            ]
        )

        selected_intervention = None

        for result in (
            intervention_results
        ):

            if (
                result.candidate_id
                == representative.candidate_id
                and
                result.target_id
                == representative.target_id
                and
                result.delta
                == 1
            ):
                selected_intervention = (
                    result
                )
                break

        if (
            selected_intervention
            is None
        ):
            raise RuntimeError(
                "Representative candidate does not have "
                "a corresponding delta=1 intervention result."
            )

        # ====================================================
        # Stage 4B:
        # Evidence-grounded recomposition
        # ====================================================

        log(
            "  [Stage 4B] Evidence-grounded recomposition"
        )

        final_statement = (
            recompose_final_skill_statement(
                target=(
                    target
                ),
                candidate=(
                    selected_candidate
                ),
                representative=(
                    representative
                ),
                intervention_result=(
                    selected_intervention
                ),
                repository_evidence=(
                    target_evidence
                ),
                llm=(
                    aux_llm
                ),
            )
        )

        final_statements.append(
            final_statement
        )

        log(
            "  [RESOLVED]"
        )

        target_records.append(
            TargetPipelineRecord(
                gap_id=(
                    target.gap_id
                ),
                target_id=(
                    target.target_id
                ),
                status=(
                    STATUS_RESOLVED
                ),
                question_construction=(
                    question_construction
                ),
                question=(
                    question
                ),
                baseline_result=(
                    baseline_result
                ),
                repository_redundancy=(
                    repository_result
                ),
                candidate_matches=(
                    candidate_matches
                ),
                intervention_results=(
                    intervention_results
                ),
                representative=(
                    representative
                ),
                final_statement=(
                    final_statement
                ),
            )
        )

    # --------------------------------------------------------
    # Final completed-target checkpoint
    # --------------------------------------------------------

    _save_current_progress_checkpoint(
        next_target_id=None
    )

    # ========================================================
    # Final residual skill
    # ========================================================

    final_skill = (
        _assemble_final_skill(
            final_statements
        )
    )

    resolved_count = sum(
        1
        for record
        in target_records
        if record.status
        == STATUS_RESOLVED
    )

    log(
        f"[Pipeline] Finished: "
        f"{resolved_count}/"
        f"{len(target_records)} targets resolved"
    )

    return (
        PipelineResult(
            snapshot=(
                snapshot
            ),
            candidates=(
                candidates
            ),
            no_skill_run=(
                no_skill_run
            ),
            gaps=(
                gaps
            ),
            evidence_by_gap=(
                evidence_by_gap
            ),
            target_construction_by_gap=(
                target_construction_by_gap
            ),
            targets=(
                all_targets
            ),
            target_records=(
                target_records
            ),
            final_statements=(
                final_statements
            ),
            final_skill=(
                final_skill
            ),
        )
    )