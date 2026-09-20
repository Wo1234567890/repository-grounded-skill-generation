from typing import Any, Dict, List, Optional, Sequence

from src.clients.llm_client import FixedLLMClient
from src.models import (
    BaselineProbeResult,
    KnowledgeTarget,
    RepositoryEvidence,
    RepositoryRedundancyResult,
)


# ============================================================
# Configuration
# ============================================================

MAX_EVIDENCE_CHARS_PER_ITEM = 8000


# Evidence types that are allowed to SUPPORT a positive
# RepositoryProvides judgment.
#
# Important:
#
# source_code and failing_test may help understand the target,
# but they cannot by themselves establish that the repository
# explicitly provides the knowledge.
#
# Configuration/dependency constraints should have been
# represented by Stage 1 as explicit_constraint when they
# explicitly state a requirement.
ELIGIBLE_PROVISION_EVIDENCE_TYPES = {
    "explicit_constraint",
    "documentation",
}


# ============================================================
# Auxiliary LLM Prompt
# ============================================================

REPOSITORY_REDUNDANCY_SYSTEM_PROMPT = """
You are evaluating whether a software repository EXPLICITLY provides
a particular piece of knowledge required by a coding agent.

This is a repository-redundancy judgment.

You must distinguish between:

1. knowledge that is explicitly available to the agent through
   repository instructions, documentation, or explicit configuration
   constraints;

and

2. knowledge that could merely be inferred from source-code behavior,
   tests, implementation details, or indirect evidence.

A target is RepositoryProvides = YES only when the repository
explicitly communicates substantially equivalent knowledge.

Examples of evidence that MAY support YES:

- AGENTS.md instructions;
- repository README instructions;
- contributor/developer documentation;
- explicit configuration constraints;
- explicit dependency/version requirements;
- other repository text that directly states the relevant guidance.

Evidence that MUST NOT by itself support YES:

- a failing test;
- observed runtime behavior;
- source code from which the knowledge must be inferred;
- the fact that an implementation happens to behave a certain way;
- absence of a symbol in source code;
- the execution trajectory.

Source code and tests may be used only as context for understanding
the target. They are not sufficient evidence that the repository
explicitly provides the knowledge.

Be conservative.

Do not decide whether the AGENT knows the target. That has already
been measured by baseline probing.

Do not decide whether candidate knowledge is useful. That will be
tested later through intervention.

Return JSON only.
""".strip()


# ============================================================
# Evidence Formatting
# ============================================================

def _format_repository_evidence(
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> str:
    """
    Format repository evidence for the auxiliary LLM.

    All supplied evidence is visible for context, but only
    documentation / explicit_constraint evidence may support a
    positive RepositoryProvides judgment.
    """

    if not evidence_items:
        return (
            "(No repository evidence was supplied.)"
        )

    blocks: List[str] = []

    for evidence in evidence_items:

        content = (
            evidence.content
            if evidence.content
            else ""
        )

        content = content[
            :MAX_EVIDENCE_CHARS_PER_ITEM
        ]

        eligible = (
            evidence.evidence_type
            in ELIGIBLE_PROVISION_EVIDENCE_TYPES
        )

        block = f"""
EVIDENCE ID: {evidence.evidence_id}
TYPE: {evidence.evidence_type}
PATH: {evidence.path}
ELIGIBLE TO SUPPORT RepositoryProvides=YES: {eligible}

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
# Prompt Construction
# ============================================================

def _build_repository_redundancy_prompt(
    target: KnowledgeTarget,
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> str:
    """
    Build the repository redundancy judgment prompt.
    """

    evidence_text = (
        _format_repository_evidence(
            evidence_items
        )
    )

    eligible_ids = [
        evidence.evidence_id
        for evidence
        in evidence_items
        if (
            evidence.evidence_type
            in ELIGIBLE_PROVISION_EVIDENCE_TYPES
        )
    ]

    return f"""
KNOWLEDGE TARGET
================

TARGET ID:
{target.target_id}

TARGET DESCRIPTION:
{target.description}


REPOSITORY EVIDENCE
===================

{evidence_text}


ELIGIBLE POSITIVE-SUPPORT EVIDENCE IDS
======================================

{eligible_ids}


TASK
====

Determine whether the repository EXPLICITLY provides the knowledge
described by the target.

RepositoryProvides should be true ONLY if explicit repository
information communicates substantially equivalent knowledge.

Important:

- Do not mark true merely because source code implements the behavior.
- Do not mark true merely because a test expects the behavior.
- Do not mark true because the knowledge can be inferred.
- Do not use execution behavior as evidence of repository provision.
- A positive decision must cite at least one eligible evidence ID.
- Every supporting evidence ID must come from the eligible list above.
- If the repository does not explicitly communicate the target
  knowledge, return false.

Return exactly this JSON structure:

{{
  "is_provided": true or false,
  "supporting_evidence_ids": ["evidence_id", "..."],
  "rationale": "brief explanation"
}}
""".strip()


# ============================================================
# Deterministic Validation
# ============================================================

def _validate_redundancy_output(
    parsed: Dict[
        str,
        Any
    ],
    evidence_items: Sequence[
        RepositoryEvidence
    ],
) -> tuple[
    bool,
    List[str],
    str,
]:
    """
    Deterministically validate the auxiliary LLM judgment.

    Python enforces mechanical constraints.

    The LLM performs only the semantic judgment.
    """

    if not isinstance(
        parsed,
        dict,
    ):
        raise RuntimeError(
            "Repository redundancy judge did not return "
            "a JSON object."
        )

    if (
        "is_provided"
        not in parsed
    ):
        raise RuntimeError(
            "Repository redundancy output is missing "
            "'is_provided'."
        )

    is_provided = (
        parsed[
            "is_provided"
        ]
    )

    if not isinstance(
        is_provided,
        bool,
    ):
        raise RuntimeError(
            "'is_provided' must be a boolean."
        )

    supporting_ids = (
        parsed.get(
            "supporting_evidence_ids",
            [],
        )
    )

    if not isinstance(
        supporting_ids,
        list,
    ):
        raise RuntimeError(
            "'supporting_evidence_ids' must be a list."
        )

    normalized_supporting_ids: List[
        str
    ] = []

    for evidence_id in (
        supporting_ids
    ):

        if not isinstance(
            evidence_id,
            str,
        ):
            raise RuntimeError(
                "Every supporting evidence ID must be a string."
            )

        evidence_id = (
            evidence_id.strip()
        )

        if not evidence_id:
            raise RuntimeError(
                "Supporting evidence IDs cannot be empty."
            )

        if (
            evidence_id
            not in normalized_supporting_ids
        ):
            normalized_supporting_ids.append(
                evidence_id
            )

    rationale = (
        parsed.get(
            "rationale",
            "",
        )
    )

    if not isinstance(
        rationale,
        str,
    ):
        raise RuntimeError(
            "'rationale' must be a string."
        )

    rationale = (
        rationale.strip()
    )

    # --------------------------------------------------------
    # Evidence lookup
    # --------------------------------------------------------

    evidence_by_id = {
        evidence.evidence_id:
        evidence
        for evidence
        in evidence_items
    }

    for evidence_id in (
        normalized_supporting_ids
    ):

        if (
            evidence_id
            not in evidence_by_id
        ):
            raise RuntimeError(
                "Repository redundancy judge cited an "
                "unknown evidence ID: "
                f"{evidence_id}"
            )

    # --------------------------------------------------------
    # Positive judgment requires explicit evidence
    # --------------------------------------------------------

    if is_provided:

        if not normalized_supporting_ids:
            raise RuntimeError(
                "RepositoryProvides=YES requires at least "
                "one supporting evidence ID."
            )

        for evidence_id in (
            normalized_supporting_ids
        ):

            evidence = (
                evidence_by_id[
                    evidence_id
                ]
            )

            if (
                evidence.evidence_type
                not in
                ELIGIBLE_PROVISION_EVIDENCE_TYPES
            ):
                raise RuntimeError(
                    "RepositoryProvides=YES was supported "
                    "by an ineligible evidence type.\n"
                    f"Evidence ID: {evidence_id}\n"
                    f"Evidence type: "
                    f"{evidence.evidence_type}\n"
                    "Only documentation and "
                    "explicit_constraint evidence may "
                    "support a positive repository "
                    "provision judgment."
                )

    # --------------------------------------------------------
    # Negative judgments should not carry positive support
    # --------------------------------------------------------

    else:

        if normalized_supporting_ids:
            raise RuntimeError(
                "RepositoryProvides=NO must not include "
                "supporting_evidence_ids."
            )

    return (
        is_provided,
        normalized_supporting_ids,
        rationale,
    )


# ============================================================
# Public Stage 3A Function
# ============================================================

def evaluate_repository_redundancy(
    target: KnowledgeTarget,
    baseline_result: BaselineProbeResult,
    repository_evidence: Sequence[
        RepositoryEvidence
    ],
    llm: Optional[
        FixedLLMClient
    ] = None,
) -> RepositoryRedundancyResult:
    """
    Evaluate whether KT_k is explicitly provided by the repository.

    Stage gate
    ----------

    This function is intended ONLY for targets where:

        B_k = 0
        AgentNeeds(KT_k) = True

    If the target agent already passed the baseline probe, the target
    should have stopped before Stage 3A.

    Semantic decision
    -----------------

    The fixed auxiliary LLM determines semantic equivalence between
    the target and explicit repository guidance.

    Deterministic Python checks enforce:

        - valid JSON structure;
        - valid evidence IDs;
        - positive judgments require evidence;
        - source-code/test evidence cannot support YES.

    Returns
    -------

    RepositoryRedundancyResult
    """

    # --------------------------------------------------------
    # Target consistency
    # --------------------------------------------------------

    if (
        target.target_id
        != baseline_result.target_id
    ):
        raise ValueError(
            "Knowledge target and baseline result have "
            "different target IDs."
        )

    # --------------------------------------------------------
    # Stage 2 gate
    # --------------------------------------------------------

    if not (
        baseline_result.agent_needs
    ):
        raise ValueError(
            "Stage 3A repository redundancy should only run "
            "for baseline-failed targets where "
            "AgentNeeds(KT_k)=True."
        )

    # --------------------------------------------------------
    # Deduplicate evidence IDs
    # --------------------------------------------------------

    evidence_items: List[
        RepositoryEvidence
    ] = []

    seen_ids = set()

    for evidence in (
        repository_evidence
    ):

        if (
            evidence.evidence_id
            in seen_ids
        ):
            raise ValueError(
                "Duplicate repository evidence ID: "
                f"{evidence.evidence_id}"
            )

        seen_ids.add(
            evidence.evidence_id
        )

        evidence_items.append(
            evidence
        )

    # --------------------------------------------------------
    # Fixed auxiliary LLM
    # --------------------------------------------------------

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    parsed = (
        llm.complete_json(
            prompt=(
                _build_repository_redundancy_prompt(
                    target=(
                        target
                    ),
                    evidence_items=(
                        evidence_items
                    ),
                )
            ),
            system_prompt=(
                REPOSITORY_REDUNDANCY_SYSTEM_PROMPT
            ),
        )
    )

    (
        is_provided,
        supporting_evidence_ids,
        rationale,
    ) = (
        _validate_redundancy_output(
            parsed=(
                parsed
            ),
            evidence_items=(
                evidence_items
            ),
        )
    )

    return (
        RepositoryRedundancyResult(
            target_id=(
                target.target_id
            ),
            is_provided=(
                is_provided
            ),
            supporting_evidence_ids=(
                supporting_evidence_ids
            ),
            rationale=(
                rationale
            ),
        )
    )