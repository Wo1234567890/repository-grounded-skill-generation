from typing import Any, Dict, List, Optional, Sequence

from src.clients.llm_client import FixedLLMClient
from src.models import (
    CandidateKnowledge,
    FinalSkillStatement,
    InterventionResult,
    KnowledgeTarget,
    RepresentativeCandidate,
    RepositoryEvidence,
)


# ============================================================
# Configuration
# ============================================================

MAX_EVIDENCE_CHARS_PER_ITEM = 8000


# ============================================================
# Stage 4A:
# Representative Candidate Selection
# ============================================================

def select_representative_candidate(
    target_id: str,
    candidates: Sequence[
        CandidateKnowledge
    ],
    intervention_results: Sequence[
        InterventionResult
    ],
) -> Optional[
    RepresentativeCandidate
]:
    """
    Select one representative K_i* for one knowledge target.

    Only candidates satisfying:

        delta_{i,k} = 1

    are eligible.

    If multiple candidates resolve the same target, choose the
    candidate with the smallest token_count.

    If token counts are equal, candidate_id is used as a fixed
    deterministic tie-break.

    No candidate combinations are considered.

    Returns None when no candidate resolves the target.
    """

    if not isinstance(
        target_id,
        str,
    ):
        raise TypeError(
            "target_id must be a string."
        )

    target_id = (
        target_id.strip()
    )

    if not target_id:
        raise ValueError(
            "target_id cannot be empty."
        )

    # --------------------------------------------------------
    # Candidate lookup
    # --------------------------------------------------------

    candidate_by_id: Dict[
        str,
        CandidateKnowledge
    ] = {}

    for candidate in candidates:

        candidate_id = (
            candidate.candidate_id
        )

        if (
            candidate_id
            in candidate_by_id
        ):
            raise ValueError(
                "Duplicate candidate ID: "
                f"{candidate_id}"
            )

        if (
            candidate.token_count
            < 0
        ):
            raise ValueError(
                "Candidate token_count cannot be negative."
            )

        candidate_by_id[
            candidate_id
        ] = candidate

    # --------------------------------------------------------
    # Collect successful interventions for this target
    # --------------------------------------------------------

    effective_candidate_ids: List[
        str
    ] = []

    seen_results = set()

    for result in (
        intervention_results
    ):

        if (
            result.target_id
            != target_id
        ):
            continue

        key = (
            result.candidate_id,
            result.target_id,
        )

        if key in seen_results:
            raise ValueError(
                "Duplicate intervention result for "
                f"candidate={result.candidate_id}, "
                f"target={result.target_id}"
            )

        seen_results.add(
            key
        )

        if (
            result.candidate_id
            not in candidate_by_id
        ):
            raise ValueError(
                "Intervention result refers to an "
                "unknown candidate ID: "
                f"{result.candidate_id}"
            )

        # ----------------------------------------------------
        # The only effectiveness criterion:
        #
        # delta_{i,k} = 1
        # ----------------------------------------------------

        if (
            result.delta
            == 1
        ):
            effective_candidate_ids.append(
                result.candidate_id
            )

    # --------------------------------------------------------
    # No candidate resolved this target.
    # --------------------------------------------------------

    if not effective_candidate_ids:
        return None

    # --------------------------------------------------------
    # Minimality:
    #
    # fewest tokens first.
    #
    # candidate_id is only a deterministic tie-break when
    # token counts are equal.
    # --------------------------------------------------------

    selected_candidate = min(
        (
            candidate_by_id[
                candidate_id
            ]
            for candidate_id
            in effective_candidate_ids
        ),
        key=lambda candidate: (
            candidate.token_count,
            candidate.candidate_id,
        ),
    )

    return (
        RepresentativeCandidate(
            target_id=(
                target_id
            ),
            candidate_id=(
                selected_candidate.candidate_id
            ),
            token_count=(
                selected_candidate.token_count
            ),
        )
    )


# ============================================================
# Stage 4B:
# Evidence Formatting
# ============================================================

def _get_target_repository_evidence(
    target: KnowledgeTarget,
    repository_evidence: Sequence[
        RepositoryEvidence
    ],
) -> List[
    RepositoryEvidence
]:
    """
    Recover exactly the repository evidence associated with KT_k.

    Evidence order follows target.repository_evidence_ids.

    Missing target evidence is treated as an implementation error
    rather than silently ignored.
    """

    evidence_by_id: Dict[
        str,
        RepositoryEvidence
    ] = {}

    for evidence in (
        repository_evidence
    ):

        if (
            evidence.evidence_id
            in evidence_by_id
        ):
            raise ValueError(
                "Duplicate repository evidence ID: "
                f"{evidence.evidence_id}"
            )

        evidence_by_id[
            evidence.evidence_id
        ] = evidence

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
            raise ValueError(
                "Knowledge target refers to repository "
                "evidence that was not supplied: "
                f"{evidence_id}"
            )

        selected.append(
            evidence_by_id[
                evidence_id
            ]
        )

    if not selected:
        raise ValueError(
            "Evidence-grounded recomposition requires "
            "at least one repository evidence item."
        )

    return selected


def _format_repository_evidence(
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> str:
    """
    Format target-specific repository evidence for recomposition.
    """

    blocks: List[str] = []

    for evidence in (
        evidence_items
    ):

        content = (
            evidence.content
            or ""
        )

        content = content[
            :MAX_EVIDENCE_CHARS_PER_ITEM
        ]

        block = f"""
EVIDENCE ID: {evidence.evidence_id}
TYPE: {evidence.evidence_type}
PATH: {evidence.path}

CONTENT:
{content}
""".strip()

        blocks.append(
            block
        )

    return "\n\n".join(
        blocks
    )


# ============================================================
# Recomposition Prompt
# ============================================================

RECOMPOSITION_SYSTEM_PROMPT = """
You are constructing one minimal residual-skill statement for a
software-engineering coding agent.

The knowledge target has already been repository-grounded.

The candidate knowledge has already passed controlled intervention,
meaning it helped resolve this target.

Your job is ONLY to recompose the validated candidate knowledge into
a concise repository-specific skill statement.

Important rules:

1. Preserve the useful knowledge contained in the candidate.

2. Include only knowledge needed for the supplied knowledge target.

3. Use repository evidence to ground repository-specific names,
   locations, constraints, APIs, files, or behavior.

4. Do not add knowledge that is unsupported by either:
   - the validated candidate knowledge; or
   - the supplied repository evidence.

5. Do not introduce unrelated generic software-engineering advice.

6. Do not broaden the statement beyond the supplied target.

7. Do not invent requirements, APIs, dependencies, tests, paths,
   commands, or behavior.

8. Do not mention:
   - probing;
   - candidate knowledge;
   - intervention;
   - knowledge targets;
   - delta;
   - the experiment.

9. The output should read like a normal concise skill instruction
   that could be given directly to a coding agent.

10. repository_evidence_ids must contain only evidence IDs that were
    actually used to ground the final statement.

Be conservative.

Return JSON only.
""".strip()


def _build_recomposition_prompt(
    target: KnowledgeTarget,
    candidate: CandidateKnowledge,
    representative: RepresentativeCandidate,
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> str:
    """
    Build the evidence-grounded recomposition prompt.
    """

    evidence_text = (
        _format_repository_evidence(
            evidence_items
        )
    )

    allowed_evidence_ids = [
        evidence.evidence_id
        for evidence
        in evidence_items
    ]

    return f"""
KNOWLEDGE TARGET
================

TARGET ID:
{target.target_id}

TARGET DESCRIPTION:
{target.description}


VALIDATED REPRESENTATIVE KNOWLEDGE
==================================

CANDIDATE ID:
{candidate.candidate_id}

SOURCE SKILL:
{candidate.source_skill}

CANDIDATE TEXT:
{candidate.text}


REPOSITORY EVIDENCE
===================

{evidence_text}


ALLOWED REPOSITORY EVIDENCE IDS
===============================

{allowed_evidence_ids}


TASK
====

Rewrite the validated candidate knowledge into one concise
repository-specific skill statement s_k.

The final statement must:

- retain the knowledge that resolved the target;
- remain specific to the supplied target;
- use repository evidence only to ground repository-specific context;
- add no unsupported information;
- avoid unrelated advice;
- be suitable for inclusion directly in the final residual skill.

Return exactly this JSON structure:

{{
  "text": "final skill statement",
  "repository_evidence_ids": ["evidence_id", "..."]
}}
""".strip()


# ============================================================
# Deterministic Recomposition Validation
# ============================================================

def _validate_recomposition_output(
    parsed: Dict[
        str,
        Any
    ],
    allowed_evidence_ids: Sequence[
        str
    ],
) -> tuple[
    str,
    List[str],
]:
    """
    Validate mechanical properties of recomposition output.

    Semantic recomposition remains an auxiliary-LLM operation.

    Python does NOT independently judge whether the wording is
    semantically ideal; it verifies the output structure and prevents
    evidence-ID leakage.
    """

    if not isinstance(
        parsed,
        dict,
    ):
        raise RuntimeError(
            "Recomposition did not return a JSON object."
        )

    text = (
        parsed.get(
            "text"
        )
    )

    if not isinstance(
        text,
        str,
    ):
        raise RuntimeError(
            "Recomposition output 'text' must be a string."
        )

    text = (
        text.strip()
    )

    if not text:
        raise RuntimeError(
            "Recomposition output text cannot be empty."
        )

    repository_evidence_ids = (
        parsed.get(
            "repository_evidence_ids"
        )
    )

    if not isinstance(
        repository_evidence_ids,
        list,
    ):
        raise RuntimeError(
            "'repository_evidence_ids' must be a list."
        )

    normalized_ids: List[
        str
    ] = []

    allowed = set(
        allowed_evidence_ids
    )

    for evidence_id in (
        repository_evidence_ids
    ):

        if not isinstance(
            evidence_id,
            str,
        ):
            raise RuntimeError(
                "Every repository evidence ID must "
                "be a string."
            )

        evidence_id = (
            evidence_id.strip()
        )

        if not evidence_id:
            raise RuntimeError(
                "Repository evidence IDs cannot be empty."
            )

        if (
            evidence_id
            not in allowed
        ):
            raise RuntimeError(
                "Recomposition cited repository evidence "
                "outside the target evidence set: "
                f"{evidence_id}"
            )

        if (
            evidence_id
            not in normalized_ids
        ):
            normalized_ids.append(
                evidence_id
            )

    if not normalized_ids:
        raise RuntimeError(
            "Evidence-grounded recomposition must cite "
            "at least one repository evidence item."
        )

    return (
        text,
        normalized_ids,
    )


# ============================================================
# Public Recomposition Function
# ============================================================

def recompose_final_skill_statement(
    target: KnowledgeTarget,
    candidate: CandidateKnowledge,
    representative: RepresentativeCandidate,
    intervention_result: InterventionResult,
    repository_evidence: Sequence[
        RepositoryEvidence
    ],
    llm: Optional[
        FixedLLMClient
    ] = None,
) -> FinalSkillStatement:
    """
    Recompose one validated representative candidate K_i* into s_k.

    Required conditions:

        - candidate matches representative;
        - representative belongs to target;
        - intervention result belongs to same (K_i, KT_k);
        - delta_{i,k} = 1.

    The auxiliary LLM performs evidence-grounded recomposition.

    Python validates IDs, stage conditions, and evidence references.
    """

    # --------------------------------------------------------
    # ID consistency
    # --------------------------------------------------------

    if (
        representative.target_id
        != target.target_id
    ):
        raise ValueError(
            "Representative and knowledge target have "
            "different target IDs."
        )

    if (
        representative.candidate_id
        != candidate.candidate_id
    ):
        raise ValueError(
            "Representative and candidate have "
            "different candidate IDs."
        )

    if (
        intervention_result.target_id
        != target.target_id
    ):
        raise ValueError(
            "Intervention result and knowledge target have "
            "different target IDs."
        )

    if (
        intervention_result.candidate_id
        != candidate.candidate_id
    ):
        raise ValueError(
            "Intervention result and candidate have "
            "different candidate IDs."
        )

    # --------------------------------------------------------
    # Representative token count must correspond to candidate
    # --------------------------------------------------------

    if (
        representative.token_count
        != candidate.token_count
    ):
        raise ValueError(
            "Representative token_count does not match "
            "the selected candidate."
        )

    # --------------------------------------------------------
    # Only experimentally effective candidates may be
    # recomposed.
    # --------------------------------------------------------

    if (
        intervention_result.delta
        != 1
    ):
        raise ValueError(
            "Only candidates with delta_{i,k}=1 may be "
            "recomposed into the residual skill."
        )

    # --------------------------------------------------------
    # Recover E_k
    # --------------------------------------------------------

    evidence_items = (
        _get_target_repository_evidence(
            target=(
                target
            ),
            repository_evidence=(
                repository_evidence
            ),
        )
    )

    allowed_evidence_ids = [
        evidence.evidence_id
        for evidence
        in evidence_items
    ]

    # --------------------------------------------------------
    # Fixed Auxiliary LLM
    # --------------------------------------------------------

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    parsed = (
        llm.complete_json(
            prompt=(
                _build_recomposition_prompt(
                    target=(
                        target
                    ),
                    candidate=(
                        candidate
                    ),
                    representative=(
                        representative
                    ),
                    evidence_items=(
                        evidence_items
                    ),
                )
            ),
            system_prompt=(
                RECOMPOSITION_SYSTEM_PROMPT
            ),
        )
    )

    (
        text,
        repository_evidence_ids,
    ) = (
        _validate_recomposition_output(
            parsed=(
                parsed
            ),
            allowed_evidence_ids=(
                allowed_evidence_ids
            ),
        )
    )

    return (
        FinalSkillStatement(
            target_id=(
                target.target_id
            ),
            candidate_id=(
                candidate.candidate_id
            ),
            text=(
                text
            ),
            repository_evidence_ids=(
                repository_evidence_ids
            ),
        )
    )