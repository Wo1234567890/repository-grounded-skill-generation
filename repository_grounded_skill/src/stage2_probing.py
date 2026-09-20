import hashlib
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from src.clients.llm_client import FixedLLMClient
from src.config import CONFIG, ExperimentConfig
from src.models import (
    DiagnosticQuestion,
    KnowledgeTarget,
    RepositoryEvidence,
)


# ============================================================
# Constants
# ============================================================

MAX_EVIDENCE_CHARS_PER_ITEM = 8000


# ============================================================
# Shared Helpers
# ============================================================

def _normalize_whitespace(
    text: str,
) -> str:
    """
    Normalize whitespace while preserving wording.

    Example:

        "def bar():\\n    return 1"

    becomes:

        "def bar(): return 1"

    This lets exact evidence checks tolerate formatting and
    line-break differences without allowing paraphrases.
    """

    return " ".join(
        text.split()
    ).strip()


def _strip_repository_line_numbers(
    text: str,
) -> str:
    """
    Remove line-number prefixes added by RepositoryTools.read_file.

    Example:

        1: def bar():
        2:     return 1

    becomes:

        def bar():
            return 1

    The line numbers are retrieval metadata rather than actual
    repository source content.

    This function removes only the first leading numeric prefix
    from each line.
    """

    cleaned_lines: List[str] = []

    for line in text.splitlines():

        stripped = line.lstrip()

        prefix, separator, remainder = (
            stripped.partition(":")
        )

        if (
            separator
            and prefix.isdigit()
        ):
            cleaned_lines.append(
                remainder.lstrip()
            )

        else:
            cleaned_lines.append(
                line
            )

    return "\n".join(
        cleaned_lines
    )


def _option_labels(
    count: int,
) -> List[str]:
    """
    Produce deterministic multiple-choice labels.

    Example:

        5 -> ["A", "B", "C", "D", "E"]
    """

    if count < 1:
        raise ValueError(
            "Option count must be >= 1."
        )

    if count > 26:
        raise ValueError(
            "Option count cannot exceed 26."
        )

    return [
        chr(
            ord("A") + index
        )
        for index in range(
            count
        )
    ]


# ============================================================
# Stage 2A Audit Structures
# ============================================================

@dataclass
class QuestionSupportRecord:
    """
    Exact repository evidence supporting the reference answer.
    """

    question_id: str
    target_id: str

    repository_support: List[
        Dict[str, Any]
    ]

    verifier_reason: str


@dataclass
class DiagnosticQuestionConstructionResult:
    """
    Complete Stage 2A result for one knowledge target.
    """

    target_id: str

    question: DiagnosticQuestion

    support_record: (
        QuestionSupportRecord
    )


@dataclass
class _GroundedQuestionProposal:
    """
    Internal question representation after deterministic
    structure and deterministic evidence-ID validation, but before semantic
    question verification.
    """

    question: str

    options: List[
        Dict[str, str]
    ]

    correct_option: str

    repository_support: List[
        Dict[str, Any]
    ]

    repository_evidence_ids: List[
        str
    ]


# ============================================================
# Stage 2A
# Diagnostic Question Generation
# ============================================================

QUESTION_GENERATION_SYSTEM_PROMPT = """
You are the fixed auxiliary LLM used to generate canonical
diagnostic questions for repository-grounded knowledge probing.

Your task is to transform ONE validated knowledge target into ONE
canonical diagnostic question.

The question will later be used to test whether a target coding
agent can DEMONSTRATE and APPLY the repository-specific knowledge
represented by the knowledge target.

IMPORTANT:

1. Generate exactly ONE question.

2. Prefer a multiple-choice question.

3. The question must test the specific repository-grounded
   knowledge target, not generic software-engineering knowledge.

4. The correct answer must be directly justified by the supplied
   repository evidence.

5. Do NOT provide or mention candidate knowledge K_i.

6. Do NOT mention that this is a probing experiment.

7. Do NOT ask whether the agent "knows" something.

8. The question should normally require APPLICATION of the
   knowledge target to a concrete task-relevant situation.

   Prefer testing one of:
   - what behavior should be expected;
   - what diagnosis follows from the repository state;
   - which execution decision is justified;
   - which next action is appropriate;
   - what consequence follows from a repository-specific fact;
   - how two relevant repository facts interact.

9. Do NOT reduce the probe to direct repository fact lookup when
   the target can be tested through application.

   Avoid questions whose main task is merely:
   - recalling a literal value;
   - identifying a literal path;
   - repeating a configuration field;
   - stating what one source line says;
   - selecting which statement is directly supported by the
     repository;
   - reporting what a repository search found.

10. A literal repository fact may appear in the question or answer
    options when it is necessary context, but answering correctly
    should require using that fact rather than merely locating or
    repeating it.

11. Do NOT require the agent to write a patch or full
    implementation. Test the knowledge needed to make the relevant
    decision, diagnosis, prediction, or next action.

12. The question stem must NOT reveal the correct answer.

13. Distractors must represent plausible competing reasoning or
    actions for the SAME situation.

14. Do NOT make distractors primarily from fabricated repository
    files, values, paths, APIs, or configurations just so they can
    be eliminated by lookup.

15. Exactly one answer option must be correct according to the
    supplied repository evidence.

16. Every repository fact required to justify the correct answer
    must cite one or more repository EVIDENCE_IDs from the supplied
    evidence.

17. Return only existing repository EVIDENCE_ID values for evidence
    grounding. Do not copy, paraphrase, or reconstruct source spans
    in the evidence-ID field.

18. Do not use external repository facts.

19. Do not use gold patches, benchmark test patches, hidden tests,
    human solution patches, or other solution-specific information.

20. Do not introduce stronger causal, exclusivity, or semantic
    claims than the supplied evidence supports.

21. A negative-search result supports only the textual absence
    established by its query and scope.

22. The question should test demonstrated repository knowledge,
    not memorization of the exact wording of the knowledge target.

23. If a knowledge target is itself a simple repository fact,
    construct a small task-relevant scenario in which that fact
    affects a decision, expected behavior, diagnosis, or next
    action. Only fall back to direct factual recall when no
    evidence-grounded application can be formed without adding
    unsupported assumptions.
""".strip()


def _format_repository_evidence(
    target: KnowledgeTarget,
    evidence_items: List[
        RepositoryEvidence
    ],
) -> str:
    """
    Format only repository evidence associated with the target.
    """

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    parts: List[str] = []

    for evidence_id in (
        target.repository_evidence_ids
    ):

        evidence = (
            evidence_by_id.get(
                evidence_id
            )
        )

        if evidence is None:
            raise RuntimeError(
                "Knowledge target references unavailable "
                f"repository evidence: {evidence_id}"
            )

        content = (
            evidence.content
        )

        if (
            len(content)
            > MAX_EVIDENCE_CHARS_PER_ITEM
        ):
            content = (
                content[
                    :MAX_EVIDENCE_CHARS_PER_ITEM
                ]
                + "\n...[TRUNCATED]"
            )

        parts.append(
            "\n".join(
                [
                    (
                        f"EVIDENCE_ID: "
                        f"{evidence.evidence_id}"
                    ),
                    (
                        f"TYPE: "
                        f"{evidence.evidence_type}"
                    ),
                    (
                        f"PATH: "
                        f"{evidence.path}"
                    ),
                    "CONTENT:",
                    content,
                ]
            )
        )

    return "\n\n".join(
        parts
    )


def _build_question_generation_prompt(
    task_description: str,
    target: KnowledgeTarget,
    evidence_items: List[
        RepositoryEvidence
    ],
    config: ExperimentConfig,
) -> str:
    """
    Build the canonical question-generation prompt using stable
    repository EVIDENCE_IDs rather than copied source spans.
    """

    labels = (
        _option_labels(
            config.mcq_option_count
        )
    )

    evidence_text = (
        _format_repository_evidence(
            target=target,
            evidence_items=(
                evidence_items
            ),
        )
    )

    option_schema = ",\n".join(
        [
            (
                f'        {{"label": "{label}", '
                f'"text": "option text"}}'
            )
            for label in labels
        ]
    )

    return f"""
Generate ONE canonical multiple-choice diagnostic question for the
knowledge target below.

The question must test whether the target coding agent can determine
the repository-specific knowledge represented by the target under
its normal repository context.

Use exactly {config.mcq_option_count} answer options.

Required labels:

{", ".join(labels)}

The correct answer must be uniquely justified by repository evidence.

The question should require the agent to APPLY the knowledge target
to a concrete task-relevant situation.

The main challenge should be reasoning about what follows from the
repository-specific knowledge, rather than simply locating or
repeating a repository fact.

Do NOT simply copy the knowledge target into the question stem in
a way that gives away the correct answer.

Avoid direct lookup-style questions such as:

- What value is defined in this configuration?
- What path appears in this file?
- What does this source line say?
- Which statement is directly supported by the repository?
- What did a targeted repository search establish?

Instead, prefer questions such as:

- Given this repository state, what behavior should the agent
  expect when the relevant operation is executed?
- Given the visible source and test behavior, which diagnosis best
  explains the observed problem?
- Which next action follows from the repository-specific constraint
  represented by this target?
- If the relevant repository condition holds, which consequence is
  expected for this task?
- Which interpretation correctly combines the relevant source,
  configuration, dependency, or test behavior?

Do NOT require a patch or full implementation.

If a literal value, symbol, path, or configuration setting is
important, use it as evidence needed for the reasoning problem
rather than making retrieval of that literal fact the whole task.

Use plausible distractors representing competing diagnoses,
consequences, decisions, or actions for the same situation.

Do not fabricate unrelated repository facts merely to create
incorrect options.

All answer option texts must be pairwise distinct.
Never repeat the same complete option text in two different answer
choices.

Do not make one option obviously correct merely because all other
options are nonsensical.

For the reference answer, cite one or more repository EVIDENCE_IDs.

Use ONLY evidence IDs already associated with this knowledge target:

{", ".join(target.repository_evidence_ids)}

Do NOT copy repository source spans.
Do NOT invent new evidence IDs.

Return exactly:

{{
  "question": "one canonical diagnostic question",
  "options": [
{option_schema}
  ],
  "correct_option": "{labels[0]}",
  "repository_evidence_ids": [
    "{target.repository_evidence_ids[0]}"
  ]
}}

TASK:
----------------
{task_description}
----------------

KNOWLEDGE TARGET:
----------------
TARGET_ID: {target.target_id}

{target.description}
----------------

REPOSITORY EVIDENCE:
----------------
{evidence_text}
----------------
""".strip()


# ============================================================
# Deterministic Question Validation
# ============================================================

def _validate_question_proposal(
    parsed: Dict[str, Any],
    target: KnowledgeTarget,
    evidence_items: List[
        RepositoryEvidence
    ],
    config: ExperimentConfig,
) -> _GroundedQuestionProposal:
    """
    Deterministically validate:

    - question structure;
    - exact number of options;
    - deterministic option labels;
    - unique option text;
    - valid correct-option label;
    - valid repository evidence IDs;
    - deterministic reference-answer evidence grounding.

    Malformed questions fail explicitly.

    We do NOT silently discard the knowledge target.
    """

    # --------------------------------------------------------
    # Question
    # --------------------------------------------------------

    question = (
        parsed.get(
            "question"
        )
    )

    if (
        not isinstance(
            question,
            str,
        )
        or not question.strip()
    ):
        raise RuntimeError(
            "Stage 2A generated no valid question."
        )

    question = (
        question.strip()
    )

    # --------------------------------------------------------
    # Options
    # --------------------------------------------------------

    raw_options = (
        parsed.get(
            "options"
        )
    )

    if not isinstance(
        raw_options,
        list,
    ):
        raise RuntimeError(
            "Stage 2A 'options' must be a list."
        )

    if (
        len(raw_options)
        != config.mcq_option_count
    ):
        raise RuntimeError(
            "Stage 2A generated the wrong number "
            "of answer options.\n"
            f"Expected: {config.mcq_option_count}\n"
            f"Received: {len(raw_options)}"
        )

    expected_labels = (
        _option_labels(
            config.mcq_option_count
        )
    )

    clean_options: List[
        Dict[str, str]
    ] = []

    seen_texts = set()

    for index, raw_option in enumerate(
        raw_options
    ):

        if not isinstance(
            raw_option,
            dict,
        ):
            raise RuntimeError(
                f"Option {index + 1} must be a JSON object."
            )

        label = str(
            raw_option.get(
                "label",
                ""
            )
        ).strip().upper()

        text = str(
            raw_option.get(
                "text",
                ""
            )
        ).strip()

        expected_label = (
            expected_labels[
                index
            ]
        )

        if (
            label
            != expected_label
        ):
            raise RuntimeError(
                "Stage 2A option labels must appear in "
                "deterministic order.\n"
                f"Expected: {expected_label}\n"
                f"Received: {label}"
            )

        if not text:
            raise RuntimeError(
                f"Option {label} has no text."
            )

        normalized_text = (
            _normalize_whitespace(
                text
            ).lower()
        )

        if (
            normalized_text
            in seen_texts
        ):
            raise RuntimeError(
                "Stage 2A generated duplicate answer "
                f"option text: {text}"
            )

        seen_texts.add(
            normalized_text
        )

        clean_options.append(
            {
                "label": (
                    label
                ),
                "text": (
                    text
                ),
            }
        )

    # --------------------------------------------------------
    # Correct option
    # --------------------------------------------------------

    correct_option = str(
        parsed.get(
            "correct_option",
            ""
        )
    ).strip().upper()

    if (
        correct_option
        not in expected_labels
    ):
        raise RuntimeError(
            "Stage 2A returned an invalid correct option: "
            f"{correct_option}"
        )

    # --------------------------------------------------------
    # Repository support
    # --------------------------------------------------------

    repository_support = (
        parsed.get(
            "repository_support"
        )
    )

    # --------------------------------------------------------
    # ID-grounded reference-answer evidence
    #
    # New generations return repository_evidence_ids only.
    # Python resolves those IDs back to the original trusted
    # repository evidence before the existing validation logic.
    # --------------------------------------------------------

    if repository_support is None:

        raw_evidence_ids = (
            parsed.get(
                "repository_evidence_ids"
            )
        )

        if (
            not isinstance(
                raw_evidence_ids,
                list,
            )
            or not raw_evidence_ids
        ):
            raise RuntimeError(
                "Stage 2A reference answer must contain "
                "repository_evidence_ids."
            )

        local_evidence_by_id = {
            evidence.evidence_id: evidence
            for evidence in evidence_items
        }

        allowed_target_evidence_ids = set(
            target.repository_evidence_ids
        )

        clean_evidence_ids: List[
            str
        ] = []

        for raw_evidence_id in raw_evidence_ids:

            if not isinstance(
                raw_evidence_id,
                str,
            ):
                raise RuntimeError(
                    "Stage 2A repository evidence IDs "
                    "must be strings."
                )

            evidence_id = (
                raw_evidence_id.strip()
            )

            if not evidence_id:
                raise RuntimeError(
                    "Stage 2A returned an empty "
                    "repository evidence ID."
                )

            if (
                evidence_id
                not in allowed_target_evidence_ids
            ):
                raise RuntimeError(
                    "Stage 2A used repository evidence outside "
                    "the knowledge target.\n"
                    f"Evidence ID: {evidence_id}"
                )

            if (
                evidence_id
                not in local_evidence_by_id
            ):
                raise RuntimeError(
                    "Stage 2A referenced unavailable "
                    f"repository evidence: {evidence_id}"
                )

            if evidence_id not in clean_evidence_ids:
                clean_evidence_ids.append(
                    evidence_id
                )

        repository_support = [
            {
                "evidence_id": evidence_id,
                "path": (
                    local_evidence_by_id[
                        evidence_id
                    ].path
                ),
                "evidence_type": (
                    local_evidence_by_id[
                        evidence_id
                    ].evidence_type
                ),
                "source_spans": [
                    local_evidence_by_id[
                        evidence_id
                    ].content
                ],
            }
            for evidence_id in clean_evidence_ids
        ]

    if (
        not isinstance(
            repository_support,
            list,
        )
        or not repository_support
    ):
        raise RuntimeError(
            "Stage 2A reference answer must contain "
            "repository_support."
        )

    evidence_by_id = {
        evidence.evidence_id: evidence
        for evidence in evidence_items
    }

    allowed_evidence_ids = set(
        target.repository_evidence_ids
    )

    clean_support: List[
        Dict[str, Any]
    ] = []

    used_evidence_ids: List[
        str
    ] = []

    for support_index, support in enumerate(
        repository_support,
        start=1,
    ):

        if not isinstance(
            support,
            dict,
        ):
            raise RuntimeError(
                "Question reference support item "
                f"{support_index} must be an object."
            )

        evidence_id = str(
            support.get(
                "evidence_id",
                ""
            )
        ).strip()

        if (
            evidence_id
            not in allowed_evidence_ids
        ):
            raise RuntimeError(
                "Stage 2A used repository evidence outside "
                "the knowledge target.\n"
                f"Evidence ID: {evidence_id}"
            )

        if (
            evidence_id
            not in evidence_by_id
        ):
            raise RuntimeError(
                "Stage 2A referenced unavailable "
                f"repository evidence: {evidence_id}"
            )

        source_spans = (
            support.get(
                "source_spans"
            )
        )

        if (
            not isinstance(
                source_spans,
                list,
            )
            or not source_spans
        ):
            raise RuntimeError(
                "Stage 2A reference support must include "
                "at least one exact source span."
            )

        # ----------------------------------------------------
        # Important:
        #
        # We construct TWO evidence views:
        #
        # 1. raw normalized evidence
        # 2. normalized repository source with read_file line
        #    number metadata removed
        #
        # Either may support the exact span.
        # ----------------------------------------------------

        raw_evidence_content = (
            evidence_by_id[
                evidence_id
            ].content
        )

        normalized_evidence = (
            _normalize_whitespace(
                raw_evidence_content
            )
        )

        normalized_source_evidence = (
            _normalize_whitespace(
                _strip_repository_line_numbers(
                    raw_evidence_content
                )
            )
        )

        clean_spans: List[
            str
        ] = []

        for span in source_spans:

            if not isinstance(
                span,
                str,
            ):
                raise RuntimeError(
                    "Stage 2A source spans must be strings."
                )

            normalized_span = (
                _normalize_whitespace(
                    span
                )
            )

            if not normalized_span:
                raise RuntimeError(
                    "Stage 2A received an empty "
                    "repository source span."
                )

            span_found = (
                normalized_span
                in normalized_evidence
                or normalized_span
                in normalized_source_evidence
            )

            if not span_found:
                raise RuntimeError(
                    "Stage 2A reference-answer evidence span "
                    "was not found in the cited repository "
                    "evidence.\n"
                    f"Evidence ID: {evidence_id}\n"
                    f"Span: {normalized_span}"
                )

            clean_spans.append(
                normalized_span
            )

        clean_support.append(
            {
                "evidence_id": (
                    evidence_id
                ),
                "source_spans": (
                    clean_spans
                ),
            }
        )

        if (
            evidence_id
            not in used_evidence_ids
        ):
            used_evidence_ids.append(
                evidence_id
            )

    return (
        _GroundedQuestionProposal(
            question=(
                question
            ),
            options=(
                clean_options
            ),
            correct_option=(
                correct_option
            ),
            repository_support=(
                clean_support
            ),
            repository_evidence_ids=(
                used_evidence_ids
            ),
        )
    )



# ============================================================
# Deterministic Option Permutation
# ============================================================

def _deterministically_permute_options(
    target: KnowledgeTarget,
    proposal: _GroundedQuestionProposal,
) -> _GroundedQuestionProposal:
    """
    Remove answer-position bias without introducing randomness.

    The auxiliary LLM may consistently place the correct answer
    under the same label (for example A). After deterministic
    question validation, Python reorders the option texts using a
    stable hash derived from the target ID and original option
    label.

    The same target/question therefore receives the same option
    permutation, while the correct answer is not structurally tied
    to label A.
    """

    if len(proposal.options) <= 1:
        return proposal

    original_correct = (
        proposal.correct_option
    )

    ranked = []

    for option in proposal.options:

        original_label = (
            option["label"]
        )

        key_material = (
            f"{target.target_id}|"
            f"{original_label}"
        )

        digest = hashlib.sha256(
            key_material.encode("utf-8")
        ).hexdigest()

        ranked.append(
            (
                digest,
                original_label,
                option["text"],
            )
        )

    ranked.sort(
        key=lambda item: item[0]
    )

    new_labels = (
        _option_labels(
            len(ranked)
        )
    )

    new_options = []

    new_correct_option = None

    for new_label, (
        _digest,
        original_label,
        option_text,
    ) in zip(
        new_labels,
        ranked,
    ):

        new_options.append(
            {
                "label": new_label,
                "text": option_text,
            }
        )

        if (
            original_label
            == original_correct
        ):
            new_correct_option = (
                new_label
            )

    if new_correct_option is None:
        raise RuntimeError(
            "Could not recover correct option after "
            "deterministic permutation."
        )

    return _GroundedQuestionProposal(
        question=(
            proposal.question
        ),
        options=(
            new_options
        ),
        correct_option=(
            new_correct_option
        ),
        repository_support=(
            proposal.repository_support
        ),
        repository_evidence_ids=(
            proposal.repository_evidence_ids
        ),
    )


# ============================================================
# Semantic Question Verification
# ============================================================

QUESTION_VERIFIER_SYSTEM_PROMPT = """
You are the strict verifier for canonical diagnostic questions in
a repository-grounded knowledge probing experiment.

Determine whether the proposed multiple-choice question is valid.

A question is VALID only if ALL of the following hold:

1. It tests the supplied knowledge target.

2. It tests repository-specific knowledge rather than generic
   software-engineering knowledge.

3. The question stem does not reveal the correct answer.

4. The declared correct option is directly supported by the
   supplied exact repository evidence.

5. Exactly one option is correct according to that evidence.

6. The distractors are plausible but are not equally supported by
   the evidence.

7. The question does not require gold-patch, benchmark test-patch,
   hidden-test, or other solution-specific information.

8. The question does not ask the target agent merely to repeat the
   wording of the knowledge target.

9. The question does not introduce unsupported causal,
   exclusivity, semantic, or runtime claims.

10. Negative-search evidence is interpreted only within its exact
    query and scope.

11. The question can be answered under normal repository context.

12. The question should diagnose the target knowledge rather than
    test unrelated repository trivia.

This verifier is conservative.

Do not rewrite the question.
Do not alter the declared correct answer.
""".strip()


def _build_question_verifier_prompt(
    target: KnowledgeTarget,
    proposal: _GroundedQuestionProposal,
) -> str:
    """
    Build semantic question-verification prompt.
    """

    return f"""
Verify this canonical diagnostic question.

Repository support contains trusted PATH and EVIDENCE_TYPE metadata
in addition to source content.

FILE-PATH GROUNDING RULE:

If the knowledge target, question stem, answer options, or declared
correct answer attributes a fact to a specific repository file,
that file must match the PATH metadata in the cited repository
support.

Evidence from a different file does not support a file-specific
claim merely because its source text is similar.

The question is VALID only if:
- it tests the supplied knowledge target;
- exactly one option is correct;
- the declared correct option is supported by the evidence;
- all file-specific claims are consistent with evidence PATH;
- it does not introduce unsupported repository facts.

Return exactly:

{{
  "decision": "VALID",
  "reason": "brief explanation"
}}

or:

{{
  "decision": "INVALID",
  "reason": "brief explanation"
}}

KNOWLEDGE TARGET:
----------------
{target.description}
----------------

QUESTION:
----------------
{proposal.question}
----------------

OPTIONS:
----------------
{json.dumps(
    proposal.options,
    ensure_ascii=False,
    indent=2,
)}
----------------

DECLARED CORRECT OPTION:
----------------
{proposal.correct_option}
----------------

EXACT REPOSITORY SUPPORT:
----------------
{json.dumps(
    proposal.repository_support,
    ensure_ascii=False,
    indent=2,
)}
----------------
""".strip()


def _validate_question_verifier_output(
    parsed: Dict[str, Any],
) -> Tuple[
    bool,
    str,
]:
    """
    Validate semantic question-verifier output.
    """

    decision = str(
        parsed.get(
            "decision",
            ""
        )
    ).strip().upper()

    reason = str(
        parsed.get(
            "reason",
            ""
        )
    ).strip()

    if decision not in {
        "VALID",
        "INVALID",
    }:
        raise RuntimeError(
            "Question verifier must return VALID or INVALID."
        )

    if not reason:
        raise RuntimeError(
            "Question verifier must provide a reason."
        )

    return (
        decision == "VALID",
        reason,
    )


# ============================================================
# Final DiagnosticQuestion Construction
# ============================================================

def _build_diagnostic_question(
    target: KnowledgeTarget,
    proposal: _GroundedQuestionProposal,
) -> DiagnosticQuestion:
    """
    Convert a validated question proposal into the common
    DiagnosticQuestion model.

    For multiple-choice questions:

        reference_answer = correct option LABEL

    Example:

        "C"

    This allows later baseline/intervention scoring to be
    deterministic.
    """

    question_id = (
        f"Q_{target.gap_id}_{target.target_id}"
    )

    formatted_options = [
        (
            f"{option['label']}. "
            f"{option['text']}"
        )
        for option in (
            proposal.options
        )
    ]

    return DiagnosticQuestion(
        question_id=(
            question_id
        ),
        target_id=(
            target.target_id
        ),
        question=(
            proposal.question
        ),
        reference_answer=(
            proposal.correct_option
        ),
        answer_type=(
            "multiple_choice"
        ),
        options=(
            formatted_options
        ),
        repository_evidence_ids=(
            list(
                proposal.repository_evidence_ids
            )
        ),
    )


# ============================================================
# Public Stage 2A Function
# ============================================================

def generate_diagnostic_question(
    task_description: str,
    target: KnowledgeTarget,
    evidence_items: List[
        RepositoryEvidence
    ],
    llm: Optional[
        FixedLLMClient
    ] = None,
    config: ExperimentConfig = CONFIG,
) -> DiagnosticQuestionConstructionResult:
    """
    Stage 2A.

    One validated knowledge target produces one canonical
    diagnostic question:

        KT_k
          ↓
        Q_k + ReferenceAnswer_k

    Semantic work:

        Fixed auxiliary LLM
        - question generation
        - semantic question verification

    Deterministic Python work:

        - option count
        - option ordering
        - duplicate option checking
        - valid evidence IDs
        - deterministic repository evidence-ID grounding

    If question construction fails, the knowledge target is NOT
    silently dropped.

    The pipeline fails explicitly so the experiment can record the
    question-construction failure.
    """

    task_description = (
        task_description.strip()
    )

    if not task_description:
        raise ValueError(
            "task_description cannot be empty."
        )

    if not target.description.strip():
        raise ValueError(
            "Knowledge target description cannot be empty."
        )

    if not target.repository_evidence_ids:
        raise ValueError(
            "Knowledge target must reference repository evidence."
        )

    if llm is None:
        llm = (
            FixedLLMClient()
        )

    # --------------------------------------------------------
    # 1-2. Generate and deterministically validate one
    # canonical question.
    #
    # A malformed LLM generation does not change the method
    # decision. We retry question construction using the same
    # fixed prompt and evidence, up to a fixed number of
    # attempts.
    # --------------------------------------------------------

    max_generation_attempts = 3

    grounded_proposal = None

    last_generation_error = None

    for generation_attempt in range(
        1,
        max_generation_attempts + 1,
    ):

        try:
            generation_prompt = (
                _build_question_generation_prompt(
                    task_description=(
                        task_description
                    ),
                    target=(
                        target
                    ),
                    evidence_items=(
                        evidence_items
                    ),
                    config=(
                        config
                    ),
                )
            )

            # ------------------------------------------------
            # Validator-feedback retry
            #
            # Attempt 1 uses the canonical prompt unchanged.
            #
            # On later attempts, feed back ONLY the technical
            # deterministic-validation failure from the previous
            # generation. This does not add new repository
            # knowledge, change the target, or use probe results.
            # It only asks the auxiliary model to repair malformed
            # question construction.
            # ------------------------------------------------

            if last_generation_error is not None:
                generation_prompt += f"""

RETRY CORRECTION:

Your previous diagnostic-question generation was rejected by the
deterministic validator for this reason:

{last_generation_error}

Regenerate the ENTIRE JSON object from scratch.

Keep the SAME:
- task;
- knowledge target;
- repository evidence;
- repository-grounded meaning of the correct answer.

Repair the technical validation problem.

Important requirements:
- return exactly {config.mcq_option_count} options;
- use the required option labels exactly once each;
- every option text must be pairwise distinct;
- do not repeat the same answer text under different labels;
- do not create options that differ only by capitalization,
  surrounding whitespace, or trivial formatting;
- exactly one option must be correct;
- the correct option must be directly supported by the allowed
  repository evidence;
- all distractors must be genuinely different alternatives.

Return only the complete corrected JSON object.
""".strip()

            parsed = llm.complete_json(
                prompt=(
                    generation_prompt
                ),
                system_prompt=(
                    QUESTION_GENERATION_SYSTEM_PROMPT
                ),
            )

            grounded_proposal = (
                _validate_question_proposal(
                    parsed=(
                        parsed
                    ),
                    target=(
                        target
                    ),
                    evidence_items=(
                        evidence_items
                    ),
                    config=(
                        config
                    ),
                )
            )

            break

        except RuntimeError as exc:
            last_generation_error = exc

            if (
                generation_attempt
                >= max_generation_attempts
            ):
                raise RuntimeError(
                    "Stage 2A failed to generate a "
                    "deterministically valid diagnostic "
                    "question after "
                    f"{max_generation_attempts} attempts.\n"
                    "Last generation error:\n"
                    f"{exc}"
                ) from exc

    if grounded_proposal is None:
        raise RuntimeError(
            "Stage 2A question generation ended without "
            "a grounded proposal.\n"
            f"Last error: {last_generation_error}"
        )

    # --------------------------------------------------------
    # Deterministically remove answer-position bias.
    #
    # The question and answer texts are unchanged. Only the
    # option ordering and labels are reassigned.
    # --------------------------------------------------------

    grounded_proposal = (
        _deterministically_permute_options(
            target=(
                target
            ),
            proposal=(
                grounded_proposal
            ),
        )
    )

    # --------------------------------------------------------
    # 3. Semantic question verification
    # --------------------------------------------------------

    verifier_output = (
        llm.complete_json(
            prompt=_build_question_verifier_prompt(
                target=(
                    target
                ),
                proposal=(
                    grounded_proposal
                ),
            ),
            system_prompt=(
                QUESTION_VERIFIER_SYSTEM_PROMPT
            ),
        )
    )

    (
        valid,
        verifier_reason,
    ) = (
        _validate_question_verifier_output(
            verifier_output
        )
    )

    if not valid:
        raise RuntimeError(
            "Stage 2A canonical diagnostic question "
            "failed semantic verification.\n"
            f"Target: {target.target_id}\n"
            f"Reason: {verifier_reason}"
        )

    # --------------------------------------------------------
    # 4. Build final canonical DiagnosticQuestion
    # --------------------------------------------------------

    diagnostic_question = (
        _build_diagnostic_question(
            target=(
                target
            ),
            proposal=(
                grounded_proposal
            ),
        )
    )

    support_record = (
        QuestionSupportRecord(
            question_id=(
                diagnostic_question.question_id
            ),
            target_id=(
                target.target_id
            ),
            repository_support=(
                grounded_proposal.repository_support
            ),
            verifier_reason=(
                verifier_reason
            ),
        )
    )

    return (
        DiagnosticQuestionConstructionResult(
            target_id=(
                target.target_id
            ),
            question=(
                diagnostic_question
            ),
            support_record=(
                support_record
            ),
        )
    )