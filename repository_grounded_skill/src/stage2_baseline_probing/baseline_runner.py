from typing import Any, Optional

from src.config import CONFIG
from src.models import (
    BaselineProbeResult,
    DiagnosticQuestion,
)

from src.stage2_baseline_probing.scoring import (
    score_single_probe,
)

from src.stage2_baseline_probing.single_probe import (
    run_single_baseline_probe,
)


# ============================================================
# Baseline Probe Runner
# ============================================================

def run_baseline_probe(
    agent: Any,
    repository_path: str,
    task_description: str,
    question: DiagnosticQuestion,
    repetitions: Optional[int] = None,
) -> BaselineProbeResult:
    """
    Run the shared baseline probe for one knowledge target.

    Experimental condition
    ----------------------

    For the SAME diagnostic question Q_k:

        - same target-agent model;
        - same task description;
        - same repository;
        - same question;
        - same read-only tool set;
        - no candidate knowledge K_i;

    we run r independent fresh target-agent sessions.

    Each session produces one ProbeTrial.

    Majority vote determines B_k:

        B_k = 1
            if a strict majority of trials are correct

        B_k = 0
            otherwise

    Because r must be odd, ties are impossible.
    """

    # --------------------------------------------------------
    # Resolve r
    # --------------------------------------------------------

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
            "cannot end in a tie."
        )

    # --------------------------------------------------------
    # Validate target agent interface
    # --------------------------------------------------------

    if not hasattr(
        agent,
        "run_read_only_fresh_session",
    ):
        raise TypeError(
            "Target agent must implement "
            "run_read_only_fresh_session()."
        )

    probe_method = getattr(
        agent,
        "run_read_only_fresh_session",
    )

    if not callable(
        probe_method
    ):
        raise TypeError(
            "agent.run_read_only_fresh_session "
            "must be callable."
        )

    # --------------------------------------------------------
    # Run independent trials
    # --------------------------------------------------------

    trials = []

    for trial_index in range(
        1,
        repetitions + 1,
    ):

        # ----------------------------------------------------
        # Adapter required by run_single_baseline_probe:
        #
        #     prompt -> raw answer string
        #
        # Each invocation below calls
        # run_read_only_fresh_session(), which creates a
        # completely fresh target-agent context.
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
                    "Target-agent baseline probe failed.\n"
                    f"Trial: {trial_index}\n"
                    f"Error: {run_result.error}"
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
        # Run one fresh baseline probe
        # ----------------------------------------------------

        single_probe = (
            run_single_baseline_probe(
                task_description=(
                    task_description
                ),
                question=(
                    question
                ),
                agent_runner=(
                    agent_runner
                ),
            )
        )

        # ----------------------------------------------------
        # Deterministic MCQ scoring
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

        trials.append(
            trial
        )

    # --------------------------------------------------------
    # Majority Vote
    # --------------------------------------------------------

    correct_count = sum(
        1
        for trial in trials
        if trial.is_correct
    )

    majority_threshold = (
        repetitions // 2
        + 1
    )

    majority_correct = (
        correct_count
        >= majority_threshold
    )

    # --------------------------------------------------------
    # Final baseline result B_k
    # --------------------------------------------------------

    return (
        BaselineProbeResult(
            target_id=(
                question.target_id
            ),
            question_id=(
                question.question_id
            ),
            trials=(
                trials
            ),
            majority_correct=(
                majority_correct
            ),
        )
    )