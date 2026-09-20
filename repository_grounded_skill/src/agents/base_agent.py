from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentRunResult:
    """
    Result returned by one completely fresh target-agent run.
    """

    final_answer: str

    # Full execution trajectory.
    trajectory: List[Dict[str, Any]] = field(default_factory=list)

    # Optional metadata returned by the API/harness.
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Whether the run completed normally.
    success: bool = True

    # Optional error information.
    error: Optional[str] = None


class BaseCodingAgent(ABC):
    """
    Common interface for target coding agents.

    Implementations may use Claude, Codex, or another coding-agent
    backend, but Stage 1-4 should not depend on backend-specific code.

    IMPORTANT:
    Every call below must start from a fresh agent context/session.
    This is required for independent probing trials.
    """

    def __init__(
        self,
        model: str,
        max_turns: int = 50,
    ):
        self.model = model
        self.max_turns = max_turns

    # ========================================================
    # Backend-specific primitive
    # ========================================================

    @abstractmethod
    def run_fresh_session(
        self,
        repository_path: str,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> AgentRunResult:
        """
        Run one completely fresh coding-agent session.

        Every implementation MUST:
        - start a new independent context/session;
        - operate inside repository_path;
        - expose the repository tools required by the agent;
        - return the execution trajectory;
        - return the final textual answer/result.

        No previous session state may be reused.
        """
        raise NotImplementedError

    # ========================================================
    # No-skill task execution
    # ========================================================

    def run_no_skill_task(
        self,
        repository_path: str,
        task_description: str,
        system_prompt: Optional[str] = None,
    ) -> AgentRunResult:
        """
        Run the original software-engineering task without any
        generated skill.

        This produces the no-skill trajectory used by Stage 1.
        """

        prompt = (
            "Solve the following software engineering task.\n\n"
            f"TASK:\n{task_description}"
        )

        return self.run_fresh_session(
            repository_path=repository_path,
            prompt=prompt,
            system_prompt=system_prompt,
        )

    # ========================================================
    # Baseline probing
    # ========================================================

    def run_baseline_probe(
        self,
        repository_path: str,
        task_description: str,
        question: str,
        system_prompt: Optional[str] = None,
    ) -> AgentRunResult:
        """
        Ask one diagnostic question without candidate knowledge K_i.

        The agent retains normal task and repository access.
        """

        prompt = (
            "You are being asked a diagnostic question about the "
            "software engineering task and repository.\n\n"
            f"TASK:\n{task_description}\n\n"
            f"QUESTION:\n{question}\n\n"
            "Answer the question using the repository when needed."
        )

        return self.run_fresh_session(
            repository_path=repository_path,
            prompt=prompt,
            system_prompt=system_prompt,
        )

    # ========================================================
    # Intervention probing
    # ========================================================

    def run_intervention_probe(
        self,
        repository_path: str,
        task_description: str,
        question: str,
        candidate_knowledge: str,
        system_prompt: Optional[str] = None,
    ) -> AgentRunResult:
        """
        Ask the same diagnostic question with candidate knowledge K_i.

        This must use the same agent/repository/task conditions as
        baseline probing. The only experimental difference is that
        K_i is additionally provided.
        """

        prompt = (
            "You are being asked a diagnostic question about the "
            "software engineering task and repository.\n\n"
            f"TASK:\n{task_description}\n\n"
            "CANDIDATE KNOWLEDGE:\n"
            f"{candidate_knowledge}\n\n"
            f"QUESTION:\n{question}\n\n"
            "Answer the question using the repository when needed."
        )

        return self.run_fresh_session(
            repository_path=repository_path,
            prompt=prompt,
            system_prompt=system_prompt,
        )