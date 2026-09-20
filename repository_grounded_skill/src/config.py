from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class ExperimentConfig:
    """
    Fixed experimental settings for Repository-Grounded
    Knowledge Probing.

    IMPORTANT:
    The values below are development defaults only.
    Before the final evaluation, they must be frozen using
    pilot/development tasks that are disjoint from the
    evaluation set.
    """

    # Maximum number of knowledge targets retained per gap.
    max_targets_per_gap: int = 3

    # Number of independent probe trials.
    # Must be odd so majority voting cannot tie.
    probe_repetitions: int = 3

    # Number of options for multiple-choice diagnostic questions.
    # The method uses 4-5 plausible options to reduce guessing.
    mcq_option_count: int = 5

    # Fixed evidence priority used when:
    # N_targets > N_max
    evidence_priority: List[str] = field(
        default_factory=lambda: [
            "failing_test",
            "explicit_constraint",
            "source_code",
            "documentation",
        ]
    )

    def __post_init__(self):
        if self.max_targets_per_gap < 1:
            raise ValueError(
                "max_targets_per_gap must be at least 1."
            )

        if self.probe_repetitions < 1:
            raise ValueError(
                "probe_repetitions must be at least 1."
            )

        if self.probe_repetitions % 2 == 0:
            raise ValueError(
                "probe_repetitions must be odd for majority voting."
            )

        if self.mcq_option_count < 4:
            raise ValueError(
                "mcq_option_count should be at least 4 "
                "to reduce chance-level guessing."
            )


CONFIG = ExperimentConfig()