from dataclasses import dataclass, field
from typing import List, Optional


# ============================================================
# Step 0: Candidate Knowledge
# ============================================================

@dataclass
class CandidateKnowledge:
    """
    One ideally atomic candidate knowledge unit K_i.
    """
    candidate_id: str
    text: str
    source_skill: str
    token_count: int = 0


# ============================================================
# Stage 1: Gap + Repository Evidence + Knowledge Target
# ============================================================

@dataclass
class ObservedGap:
    """
    An observed execution gap g_j from the no-skill trajectory.
    A gap describes what went wrong, but does not assume
    that the agent lacks the corresponding knowledge.
    """
    gap_id: str
    description: str
    local_trajectory: str
    trajectory_evidence: List[str] = field(default_factory=list)


@dataclass
class RepositoryEvidence:
    """
    Repository evidence E_j used to ground a knowledge target.

    explicit_guidance=False:
        evidence is used to infer required knowledge
        (e.g. source code or tests).

    explicit_guidance=True:
        evidence explicitly provides guidance
        (e.g. AGENTS.md or explicit documentation).
    """
    evidence_id: str
    gap_id: str
    evidence_type: str
    path: str
    content: str
    rationale: str
    explicit_guidance: bool = False


@dataclass
class KnowledgeTarget:
    """
    One evidence-grounded knowledge target KT_k.
    """
    target_id: str
    gap_id: str
    description: str
    trajectory_evidence: List[str] = field(default_factory=list)
    repository_evidence_ids: List[str] = field(default_factory=list)


# ============================================================
# Stage 2: Diagnostic Question + Baseline Probing
# ============================================================

@dataclass
class DiagnosticQuestion:
    """
    One canonical diagnostic question Q_k for one KT_k.
    """
    question_id: str
    target_id: str
    question: str
    reference_answer: str

    # "multiple_choice" or "free_text"
    answer_type: str = "multiple_choice"

    # Used for multiple-choice questions.
    options: List[str] = field(default_factory=list)

    # Repository evidence supporting the question/reference answer.
    repository_evidence_ids: List[str] = field(default_factory=list)


@dataclass
class ProbeTrial:
    """
    One independent probe trial.
    """
    trial_index: int
    answer: str
    is_correct: bool


@dataclass
class BaselineProbeResult:
    """
    Majority-vote baseline result B_k.
    """
    target_id: str
    question_id: str
    trials: List[ProbeTrial] = field(default_factory=list)
    majority_correct: bool = False

    @property
    def correct_count(self) -> int:
        return sum(trial.is_correct for trial in self.trials)

    @property
    def agent_needs(self) -> bool:
        """
        AgentNeeds(KT_k) ≡ (B_k = 0)
        """
        return not self.majority_correct


# ============================================================
# Stage 3: Repository Redundancy + Matching + Intervention
# ============================================================

@dataclass
class RepositoryRedundancyResult:
    """
    Whether KT_k is explicitly provided by the repository.
    """
    target_id: str
    is_provided: bool
    supporting_evidence_ids: List[str] = field(default_factory=list)
    rationale: str = ""


@dataclass
class CandidateTargetMatch:
    """
    MATCH / NO MATCH between K_i and KT_k.
    """
    candidate_id: str
    target_id: str
    is_match: bool
    rationale: str = ""


@dataclass
class InterventionResult:
    """
    Target-level intervention result for one (K_i, KT_k) pair.

    delta = 1 only when:
        baseline majority = wrong
        intervention majority = correct
    """
    candidate_id: str
    target_id: str
    question_id: str

    baseline_majority_correct: bool
    intervention_trials: List[ProbeTrial] = field(default_factory=list)
    intervention_majority_correct: bool = False

    @property
    def delta(self) -> int:
        if (
            not self.baseline_majority_correct
            and self.intervention_majority_correct
        ):
            return 1
        return 0


# ============================================================
# Stage 4: Representative + Final Skill
# ============================================================

@dataclass
class RepresentativeCandidate:
    """
    Selected representative K_i* for one resolved target.
    """
    target_id: str
    candidate_id: str
    token_count: int


@dataclass
class FinalSkillStatement:
    """
    Evidence-grounded recomposed statement s_k.
    """
    target_id: str
    candidate_id: str
    text: str
    repository_evidence_ids: List[str] = field(default_factory=list)