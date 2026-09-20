from src.models import (
    DiagnosticQuestion,
    ProbeTrial,
)

from src.stage2_baseline_probing.single_probe import (
    SingleBaselineProbeResult,
)


# ============================================================
# Single-Trial Scoring
# ============================================================

def score_single_probe(
    trial_index: int,
    question: DiagnosticQuestion,
    probe_result: SingleBaselineProbeResult,
) -> ProbeTrial:
    """
    Deterministically score one target-agent baseline probe.

    For the current MCQ protocol:

        parsed_answer == reference_answer
            -> correct

        parsed_answer != reference_answer
            -> incorrect

        parsed_answer is None
            -> incorrect

    No LLM judge is required for MCQ scoring.
    """

    if trial_index < 1:
        raise ValueError(
            "trial_index must be >= 1."
        )

    if (
        probe_result.target_id
        != question.target_id
    ):
        raise ValueError(
            "Probe result and diagnostic question "
            "refer to different target IDs."
        )

    if (
        probe_result.question_id
        != question.question_id
    ):
        raise ValueError(
            "Probe result and diagnostic question "
            "refer to different question IDs."
        )

    if (
        question.answer_type
        != "multiple_choice"
    ):
        raise ValueError(
            "Current deterministic scoring supports "
            "multiple-choice questions only."
        )

    reference_answer = (
        question.reference_answer
        .strip()
        .upper()
    )

    parsed_answer = (
        probe_result.parsed_answer
    )

    if parsed_answer is not None:
        parsed_answer = (
            parsed_answer
            .strip()
            .upper()
        )

    is_correct = (
        parsed_answer
        is not None
        and parsed_answer
        == reference_answer
    )

    return ProbeTrial(
        trial_index=trial_index,
        answer=(
            parsed_answer
            if parsed_answer is not None
            else probe_result.raw_answer
        ),
        is_correct=is_correct,
    )