from typing import Any, Callable, Optional

from src.config import CONFIG
from src.models import (
    BaselineProbeResult,
    CandidateKnowledge,
    CandidateTargetMatch,
    DiagnosticQuestion,
    InterventionResult,
    RepositoryRedundancyResult,
)

from src.stage2_baseline_probing.scoring import (
    score_single_probe,
)

from src.stage2_baseline_probing.single_probe import (
    BASELINE_PROBE_INSTRUCTION,
    SingleBaselineProbeResult,
    _parse_mcq_answer,
    _valid_option_labels,
)


# ============================================================
# Intervention Prompt
# ============================================================

def build_intervention_probe_prompt(
    task_description: str,
    question: DiagnosticQuestion,
    candidate: CandidateKnowledge,
) -> str:
    """
    Build the Stage 3C intervention prompt.

    The baseline and intervention conditions use:

        - same task;
        - same repository;
        - same target agent;
        - same read-only tools;
        - same diagnostic question;
        - same answer options.

    The intervention condition adds only K_i.
    """

    task_description = (
        task_description.strip()
    )

    candidate_text = (
        candidate.text.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if not candidate_text:
        raise ValueError(
            "Candidate knowledge cannot be empty."
        )

    if (
        question.answer_type
        != "multiple_choice"
    ):
        raise ValueError(
            "Intervention probing currently supports "
            "multiple-choice questions only."
        )

    if not question.options:
        raise ValueError(
            "Diagnostic question must contain options."
        )

    options_text = "\n".join(
        question.options
    )

    return f"""
{BASELINE_PROBE_INSTRUCTION}

TASK:
----------------
{task_description}
----------------

ADDITIONAL KNOWLEDGE:
----------------
{candidate_text}
----------------

QUESTION:
----------------
{question.question}
----------------

OPTIONS:
----------------
{options_text}
----------------
""".strip()


# ============================================================
# Single Intervention Probe
# ============================================================

def run_single_intervention_probe(
    task_description: str,
    question: DiagnosticQuestion,
    candidate: CandidateKnowledge,
    agent_runner: Callable[
        [str],
        str,
    ],
) -> SingleBaselineProbeResult:
    """
    Run ONE intervention probe.

    This is structurally equivalent to one Stage 2 baseline probe,
    except that candidate knowledge K_i is additionally supplied.

    The returned SingleBaselineProbeResult is reused as the generic
    container for:

        prompt
        raw_answer
        parsed_answer

    Correctness is still determined by the same deterministic
    Stage 2 scoring function.
    """

    if not callable(
        agent_runner
    ):
        raise TypeError(
            "agent_runner must be callable."
        )

    valid_labels = (
        _valid_option_labels(
            question
        )
    )

    if not valid_labels:
        raise RuntimeError(
            "Could not determine valid MCQ labels."
        )

    prompt = (
        build_intervention_probe_prompt(
            task_description=(
                task_description
            ),
            question=(
                question
            ),
            candidate=(
                candidate
            ),
        )
    )

    raw_answer = (
        agent_runner(
            prompt
        )
    )

    if not isinstance(
        raw_answer,
        str,
    ):
        raise RuntimeError(
            "Target agent must return a string response."
        )

    raw_answer = (
        raw_answer.strip()
    )

    if not raw_answer:
        raise RuntimeError(
            "Target agent returned an empty intervention "
            "response."
        )

    parsed_answer = (
        _parse_mcq_answer(
            raw_answer=(
                raw_answer
            ),
            valid_labels=(
                valid_labels
            ),
        )
    )

    return (
        SingleBaselineProbeResult(
            target_id=(
                question.target_id
            ),
            question_id=(
                question.question_id
            ),
            prompt=(
                prompt
            ),
            raw_answer=(
                raw_answer
            ),
            parsed_answer=(
                parsed_answer
            ),
        )
    )


# ============================================================
# Stage 3C Intervention Runner
# ============================================================

def run_knowledge_intervention(
    agent: Any,
    repository_path: str,
    task_description: str,
    question: DiagnosticQuestion,
    candidate: CandidateKnowledge,
    target_match: CandidateTargetMatch,
    baseline_result: BaselineProbeResult,
    repository_redundancy: RepositoryRedundancyResult,
    repetitions: Optional[int] = None,
) -> InterventionResult:
    """
    Run independent knowledge intervention for one (K_i, KT_k).

    Stage gates
    -----------

    Intervention is permitted only when:

        1. B_k = 0
        2. RepositoryProvides(KT_k) = NO
        3. Match(K_i, KT_k) = YES

    Experimental comparison
    -----------------------

    Baseline:

        Task + Repository + Q_k

    Intervention:

        Task + Repository + Q_k + K_i

    Everything else should remain fixed.

    The intervention is repeated r times using fresh read-only
    target-agent sessions.

    Majority voting produces:

        B_k^{K_i}

    InterventionResult.delta then implements:

        delta_{i,k} = 1

    iff:

        B_k = 0
        and
        B_k^{K_i} = 1
    """

    # ========================================================
    # Resolve repetitions
    # ========================================================

    if repetitions is None:
        repetitions = (
            CONFIG.probe_repetitions
        )

    if not isinstance(
        repetitions,
        int,
    ):
        raise TypeError(
            "repetitions must be an integer."
        )

    if repetitions < 1:
        raise ValueError(
            "repetitions must be >= 1."
        )

    if repetitions % 2 == 0:
        raise ValueError(
            "repetitions must be odd so majority voting "
            "cannot tie."
        )

    # ========================================================
    # Candidate validation
    # ========================================================

    if not isinstance(
        candidate.text,
        str,
    ):
        raise ValueError(
            "Candidate knowledge text must be a string."
        )

    if not candidate.text.strip():
        raise ValueError(
            "Candidate knowledge text cannot be empty."
        )

    # ========================================================
    # ID consistency
    # ========================================================

    if (
        question.target_id
        != baseline_result.target_id
    ):
        raise ValueError(
            "Question and baseline result refer to "
            "different target IDs."
        )

    if (
        question.question_id
        != baseline_result.question_id
    ):
        raise ValueError(
            "Question and baseline result refer to "
            "different question IDs."
        )

    if (
        target_match.target_id
        != question.target_id
    ):
        raise ValueError(
            "Candidate-target match and question refer "
            "to different target IDs."
        )

    if (
        repository_redundancy.target_id
        != question.target_id
    ):
        raise ValueError(
            "Repository redundancy result and question "
            "refer to different target IDs."
        )

    if (
        target_match.candidate_id
        != candidate.candidate_id
    ):
        raise ValueError(
            "Candidate-target match and candidate refer "
            "to different candidate IDs."
        )

    # ========================================================
    # Stage Gate 1:
    #
    # B_k must be 0.
    # ========================================================

    if not (
        baseline_result.agent_needs
    ):
        raise ValueError(
            "Knowledge intervention must not run for a "
            "baseline-passed target."
        )

    # ========================================================
    # Stage Gate 2:
    #
    # RepositoryProvides must be NO.
    # ========================================================

    if (
        repository_redundancy.is_provided
    ):
        raise ValueError(
            "Knowledge intervention must not run when "
            "RepositoryProvides(KT_k)=YES."
        )

    # ========================================================
    # Stage Gate 3:
    #
    # Candidate-target match must be YES.
    # ========================================================

    if not (
        target_match.is_match
    ):
        raise ValueError(
            "Knowledge intervention must not run for "
            "a candidate with Match(K_i, KT_k)=NO."
        )

    # ========================================================
    # Target-agent interface
    # ========================================================

    if not hasattr(
        agent,
        "run_read_only_fresh_session",
    ):
        raise TypeError(
            "Target agent must implement "
            "run_read_only_fresh_session()."
        )

    if not callable(
        agent.run_read_only_fresh_session
    ):
        raise TypeError(
            "agent.run_read_only_fresh_session "
            "must be callable."
        )

    # ========================================================
    # Independent intervention trials
    # ========================================================

    intervention_trials = []

    for trial_index in range(
        1,
        repetitions + 1,
    ):

        # ----------------------------------------------------
        # Adapter:
        #
        # prompt -> real target-agent answer
        # ----------------------------------------------------

        def agent_runner(
            prompt: str,
        ) -> str:

            run_result = (
                agent.run_read_only_fresh_session(
                    repository_path=(
                        repository_path
                    ),
                    prompt=(
                        prompt
                    ),
                )
            )

            if not run_result.success:
                raise RuntimeError(
                    "Target-agent intervention run failed.\n"
                    f"Trial: {trial_index}\n"
                    f"Error: {run_result.error}"
                )

            # ----------------------------------------------
            # If metadata is available, verify that the
            # target agent really used read-only probing.
            # ----------------------------------------------

            metadata = (
                run_result.metadata
                or {}
            )

            mode = (
                metadata.get(
                    "mode"
                )
            )

            if (
                mode is not None
                and mode
                != "read_only_probe"
            ):
                raise RuntimeError(
                    "Intervention target agent did not run "
                    "in read_only_probe mode."
                )

            allowed_tools = (
                metadata.get(
                    "allowed_tools"
                )
            )

            if (
                allowed_tools
                is not None
            ):
                allowed_tools = set(
                    allowed_tools
                )

                forbidden = {
                    "write_file",
                    "run_command",
                }

                if (
                    allowed_tools
                    & forbidden
                ):
                    raise RuntimeError(
                        "Intervention run exposed "
                        "write-capable tools."
                    )

            if not isinstance(
                run_result.final_answer,
                str,
            ):
                raise RuntimeError(
                    "Target agent returned a non-string "
                    "final_answer."
                )

            return (
                run_result.final_answer
            )

        # ----------------------------------------------------
        # Same Q_k, but now K_i is provided.
        # ----------------------------------------------------

        single_probe = (
            run_single_intervention_probe(
                task_description=(
                    task_description
                ),
                question=(
                    question
                ),
                candidate=(
                    candidate
                ),
                agent_runner=(
                    agent_runner
                ),
            )
        )

        # ----------------------------------------------------
        # Same deterministic MCQ scoring as baseline.
        # ----------------------------------------------------

        trial = (
            score_single_probe(
                trial_index=(
                    trial_index
                ),
                question=(
                    question
                ),
                probe_result=(
                    single_probe
                ),
            )
        )

        intervention_trials.append(
            trial
        )

    # ========================================================
    # Majority Vote
    # ========================================================

    correct_count = sum(
        1
        for trial
        in intervention_trials
        if trial.is_correct
    )

    majority_threshold = (
        repetitions // 2
        + 1
    )

    intervention_majority_correct = (
        correct_count
        >= majority_threshold
    )

    # ========================================================
    # Final Intervention Result
    # ========================================================

    return (
        InterventionResult(
            candidate_id=(
                candidate.candidate_id
            ),
            target_id=(
                question.target_id
            ),
            question_id=(
                question.question_id
            ),
            baseline_majority_correct=(
                baseline_result.majority_correct
            ),
            intervention_trials=(
                intervention_trials
            ),
            intervention_majority_correct=(
                intervention_majority_correct
            ),
        )
    )