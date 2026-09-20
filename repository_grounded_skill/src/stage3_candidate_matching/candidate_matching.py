from typing import Any, Dict, Optional

from src.clients.llm_client import FixedLLMClient
from src.models import (
    BaselineProbeResult,
    CandidateKnowledge,
    CandidateTargetMatch,
    KnowledgeTarget,
    RepositoryRedundancyResult,
)


# ============================================================
# Auxiliary LLM Prompt
# ============================================================

CANDIDATE_MATCHING_SYSTEM_PROMPT = """
You are evaluating whether one candidate knowledge unit K_i
contains the knowledge needed to address one specific
repository-grounded knowledge target KT_k.

This is a candidate-to-target matching judgment.

The question is NOT whether the candidate is merely related to
the same topic.

Return MATCH only when the candidate itself contains sufficient
information to address the specific knowledge target.

Important distinctions:

MATCH:
- the candidate directly states the required rule, constraint,
  behavior, procedure, or relationship;
- the candidate contains enough information that providing it to
  the target agent could plausibly help answer a diagnostic
  question about this target.

NO MATCH:
- the candidate is only topically related;
- the candidate mentions the same file, library, framework, or
  component but does not contain the required knowledge;
- the candidate is too vague;
- the candidate discusses a different problem;
- the candidate only gives generic software-engineering advice;
- the candidate would require substantial new inference to obtain
  the target knowledge.

Do not judge whether the target agent already knows the knowledge.
That was measured by baseline probing.

Do not judge whether the repository already provides the knowledge.
That was evaluated separately.

Do not predict whether intervention will succeed.
That will be experimentally tested later.

Be conservative.

Return JSON only.
""".strip()


# ============================================================
# Prompt Construction
# ============================================================

def _build_candidate_matching_prompt(
    candidate: CandidateKnowledge,
    target: KnowledgeTarget,
) -> str:
    """
    Construct the semantic candidate-target matching prompt.

    The knowledge target is already repository-grounded by Stage 1,
    so this stage evaluates whether K_i actually contains the
    knowledge represented by KT_k.
    """

    return f"""
KNOWLEDGE TARGET
================

TARGET ID:
{target.target_id}

TARGET DESCRIPTION:
{target.description}


CANDIDATE KNOWLEDGE
===================

CANDIDATE ID:
{candidate.candidate_id}

SOURCE SKILL:
{candidate.source_skill}

CANDIDATE TEXT:
{candidate.text}


TASK
====

Determine whether the candidate knowledge contains sufficient
information to address the knowledge target.

A positive MATCH requires more than topical similarity.

Ask:

"If this candidate were supplied to the target coding agent,
does the candidate itself communicate the specific knowledge
represented by KT_k?"

Return exactly this JSON structure:

{{
  "is_match": true or false,
  "rationale": "brief explanation"
}}
""".strip()


# ============================================================
# Deterministic Validation
# ============================================================

def _validate_candidate_matching_output(
    parsed: Dict[str, Any],
) -> tuple[
    bool,
    str,
]:
    """
    Deterministically validate auxiliary-LLM output.

    Python validates structure.

    The auxiliary LLM performs the semantic judgment.
    """

    if not isinstance(
        parsed,
        dict,
    ):
        raise RuntimeError(
            "Candidate matching judge did not return "
            "a JSON object."
        )

    if (
        "is_match"
        not in parsed
    ):
        raise RuntimeError(
            "Candidate matching output is missing "
            "'is_match'."
        )

    is_match = (
        parsed[
            "is_match"
        ]
    )

    if not isinstance(
        is_match,
        bool,
    ):
        raise RuntimeError(
            "'is_match' must be a boolean."
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

    if not rationale:
        raise RuntimeError(
            "Candidate matching output must include "
            "a non-empty rationale."
        )

    return (
        is_match,
        rationale,
    )


# ============================================================
# Public Stage 3B Function
# ============================================================

def evaluate_candidate_target_match(
    candidate: CandidateKnowledge,
    target: KnowledgeTarget,
    baseline_result: BaselineProbeResult,
    repository_redundancy: RepositoryRedundancyResult,
    llm: Optional[
        FixedLLMClient
    ] = None,
) -> CandidateTargetMatch:
    """
    Evaluate MATCH / NO MATCH between K_i and KT_k.

    Stage gate
    ----------

    This function may run only when:

        B_k = 0

    and:

        RepositoryProvides(KT_k) = NO

    Therefore:

        AgentNeeds(KT_k) = True
        AND
        repository does not already explicitly provide KT_k.

    Semantic rule
    -------------

    MATCH means the candidate itself contains sufficient knowledge
    to address the specific target.

    Mere topical similarity is insufficient.

    This stage does NOT establish usefulness.

    Actual causal usefulness is tested later through independent
    intervention using the target coding agent.
    """

    # --------------------------------------------------------
    # Basic candidate validation
    # --------------------------------------------------------

    if not isinstance(
        candidate.text,
        str,
    ):
        raise ValueError(
            "Candidate knowledge text must be a string."
        )

    if not (
        candidate.text.strip()
    ):
        raise ValueError(
            "Candidate knowledge text cannot be empty."
        )

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

    if (
        target.target_id
        != repository_redundancy.target_id
    ):
        raise ValueError(
            "Knowledge target and repository redundancy "
            "result have different target IDs."
        )

    # --------------------------------------------------------
    # Stage 2 gate:
    #
    # B_k must be 0.
    # --------------------------------------------------------

    if not (
        baseline_result.agent_needs
    ):
        raise ValueError(
            "Candidate-target matching should only run for "
            "baseline-failed targets where "
            "AgentNeeds(KT_k)=True."
        )

    # --------------------------------------------------------
    # Stage 3A gate:
    #
    # RepositoryProvides must be NO.
    # --------------------------------------------------------

    if (
        repository_redundancy.is_provided
    ):
        raise ValueError(
            "Candidate-target matching must not run when "
            "RepositoryProvides(KT_k)=YES."
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
                _build_candidate_matching_prompt(
                    candidate=(
                        candidate
                    ),
                    target=(
                        target
                    ),
                )
            ),
            system_prompt=(
                CANDIDATE_MATCHING_SYSTEM_PROMPT
            ),
        )
    )

    (
        is_match,
        rationale,
    ) = (
        _validate_candidate_matching_output(
            parsed
        )
    )

    return (
        CandidateTargetMatch(
            candidate_id=(
                candidate.candidate_id
            ),
            target_id=(
                target.target_id
            ),
            is_match=(
                is_match
            ),
            rationale=(
                rationale
            ),
        )
    )