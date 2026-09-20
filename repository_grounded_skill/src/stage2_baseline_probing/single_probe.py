from dataclasses import dataclass
from typing import Callable, Optional

from src.models import DiagnosticQuestion


# ============================================================
# Result Structure
# ============================================================

@dataclass
class SingleBaselineProbeResult:
    """
    Result of ONE baseline knowledge probe.

    This stage records:

        Q_k
          ↓
        target coding agent
          ↓
        one raw response

    Majority voting is handled later.
    """

    target_id: str
    question_id: str

    prompt: str

    raw_answer: str

    parsed_answer: Optional[str]


# ============================================================
# Baseline Probe Instruction
# ============================================================

BASELINE_PROBE_INSTRUCTION = """
Answer the following question using the task description and
repository context available in this run.

You may inspect the repository when needed.

Do not modify repository files.
Do not apply a patch.
Do not create new files.

This is a multiple-choice question.

Select exactly one option.

End your response with exactly:

ANSWER: <OPTION>

For example:

ANSWER: B
""".strip()


# ============================================================
# Prompt Construction
# ============================================================

def build_baseline_probe_prompt(
    task_description: str,
    question: DiagnosticQuestion,
) -> str:
    """
    Construct the prompt given to the TARGET CODING AGENT.

    The target agent receives:

        - original task description
        - canonical diagnostic question
        - answer options

    The prompt does NOT contain:

        - reference answer
        - repository evidence collected by Stage 1
        - candidate K_i
        - final skill
    """

    task_description = (
        task_description.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if not question.question.strip():
        raise ValueError(
            "Diagnostic question cannot be empty."
        )

    if (
        question.answer_type
        != "multiple_choice"
    ):
        raise ValueError(
            "Single baseline probing currently supports "
            "multiple-choice questions only."
        )

    if not question.options:
        raise ValueError(
            "Diagnostic question must contain answer options."
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
# MCQ Label Extraction
# ============================================================

def _valid_option_labels(
    question: DiagnosticQuestion,
) -> set[str]:
    """
    Extract valid labels from formatted options.

    Example:

        [
            "A. bar",
            "B. foo",
            "C. baz",
        ]

    becomes:

        {"A", "B", "C"}
    """

    labels: set[str] = set()

    for option in question.options:

        if not isinstance(
            option,
            str,
        ):
            continue

        option = (
            option.strip()
        )

        if (
            len(option) >= 2
            and option[0].isalpha()
            and option[1] == "."
        ):
            labels.add(
                option[0].upper()
            )

    return labels


# ============================================================
# Deterministic Answer Parsing
# ============================================================

def _parse_mcq_answer(
    raw_answer: str,
    valid_labels: set[str],
) -> Optional[str]:
    """
    Parse an explicit final answer of the form:

        ANSWER: A

    The parser is conservative.

    It does NOT infer an answer from free-form reasoning.

    It requires exactly one valid explicit ANSWER line.

    Invalid or ambiguous output returns None.
    """

    if not isinstance(
        raw_answer,
        str,
    ):
        return None

    lines = [
        line.strip()
        for line in raw_answer.splitlines()
        if line.strip()
    ]

    matching_answers = []

    for line in lines:

        upper_line = (
            line.upper()
        )

        if not upper_line.startswith(
            "ANSWER:"
        ):
            continue

        value = (
            upper_line[
                len("ANSWER:"):
            ]
            .strip()
        )

        if (
            len(value) == 1
            and value in valid_labels
        ):
            matching_answers.append(
                value
            )

    # Exactly one explicit valid answer is required.
    if (
        len(matching_answers)
        != 1
    ):
        return None

    return (
        matching_answers[0]
    )


# ============================================================
# Single Baseline Probe
# ============================================================

def run_single_baseline_probe(
    task_description: str,
    question: DiagnosticQuestion,
    agent_runner: Callable[
        [str],
        str,
    ],
) -> SingleBaselineProbeResult:
    """
    Run ONE baseline probe against the target coding agent.

    Experimental condition:

        Target Agent receives:

            Task + Repository + Q_k

        No K_i is provided.

    The target-agent implementation is supplied through
    agent_runner.

    This function must NOT call FixedLLMClient.

    Correct / Incorrect scoring is handled separately.
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
            "Could not determine valid MCQ option labels."
        )

    prompt = (
        build_baseline_probe_prompt(
            task_description=(
                task_description
            ),
            question=(
                question
            ),
        )
    )

    # --------------------------------------------------------
    # TARGET CODING AGENT CALL
    # --------------------------------------------------------

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
            "Target agent runner must return a string response."
        )

    raw_answer = (
        raw_answer.strip()
    )

    if not raw_answer:
        raise RuntimeError(
            "Target coding agent returned an empty response."
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