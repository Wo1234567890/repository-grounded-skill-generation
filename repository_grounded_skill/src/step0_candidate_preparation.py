import re
from typing import List, Optional

from src.clients.llm_client import FixedLLMClient
from src.models import CandidateKnowledge


# ============================================================
# Step 0: Candidate Knowledge Preparation
# ============================================================

DECOMPOSITION_SYSTEM_PROMPT = """
You are the fixed auxiliary LLM used in a research pipeline for
repository-grounded knowledge probing.

Your ONLY task is to decompose an existing generated
software-engineering skill into relatively atomic candidate
knowledge units.

This is an EXTRACTIVE decomposition task.

You MUST NOT:
- add new knowledge;
- paraphrase the original knowledge;
- correct the original skill;
- make implicit information explicit;
- infer repository-specific facts;
- evaluate usefulness;
- evaluate redundancy;
- make KEEP/REMOVE decisions.

Every candidate unit must be constructed only from text that is
already explicitly present in the original generated skill.
""".strip()


# ============================================================
# Helpers
# ============================================================

def _normalize_whitespace(
    text: str,
) -> str:
    """
    Normalize whitespace while preserving wording.

    This allows source spans containing newlines to be compared
    against model-returned spans that may appear on one line.
    """

    return re.sub(
        r"\s+",
        " ",
        text,
    ).strip()


def _build_decomposition_prompt(
    skill_text: str,
) -> str:
    """
    Construct the extractive atomic-decomposition prompt.
    """

    return f"""
Decompose the generated skill below into relatively atomic
candidate knowledge units K_i.

IMPORTANT:
This is an EXTRACTIVE task.

For every unit, return one or more SOURCE SPANS copied directly
from the generated skill.

Do not rewrite, paraphrase, improve, clarify, or extend them.

Atomicity rules:

1. Each unit should represent one main piece of software-engineering
   knowledge.

2. If one sentence contains multiple independent pieces of knowledge
   that could be useful separately, they may be split into separate
   source spans.

3. If multiple adjacent sentences are required to express one
   coherent piece of knowledge, they may belong to the same unit.

4. Do not create heading-only units.

5. Do not split merely because the source uses bullet points,
   headings, or separate sentences.

6. Preserve all meaningful knowledge from the generated skill.
   Do not remove information merely because it seems unimportant.

7. Do not add connecting explanations that are absent from the
   original skill.

8. Do not judge whether the target agent already knows the knowledge.

9. Do not judge whether the repository already contains the knowledge.

10. Do not perform target matching or KEEP/REMOVE decisions.

Return exactly this JSON structure:

{{
  "units": [
    {{
      "source_spans": [
        "exact text copied from the generated skill"
      ]
    }},
    {{
      "source_spans": [
        "another exact source span"
      ]
    }}
  ]
}}

GENERATED SKILL:
----------------
{skill_text}
----------------
""".strip()


def _validate_and_extract_units(
    parsed: dict,
    original_skill: str,
) -> List[str]:
    """
    Validate that every returned candidate consists only of text
    already present in the original generated skill.

    This prevents Step 0 from introducing new knowledge.
    """

    if "units" not in parsed:
        raise RuntimeError(
            "Step 0 decomposition JSON does not contain 'units'."
        )

    units = parsed["units"]

    if not isinstance(units, list):
        raise RuntimeError(
            "Step 0 field 'units' must be a list."
        )

    if not units:
        raise RuntimeError(
            "Step 0 produced zero candidate knowledge units."
        )

    normalized_original = _normalize_whitespace(
        original_skill
    )

    candidate_texts: List[str] = []

    for unit_index, unit in enumerate(
        units,
        start=1,
    ):
        if not isinstance(unit, dict):
            raise RuntimeError(
                f"Step 0 unit {unit_index} must be a JSON object."
            )

        spans = unit.get(
            "source_spans"
        )

        if not isinstance(
            spans,
            list,
        ):
            raise RuntimeError(
                f"Step 0 unit {unit_index} must contain "
                "'source_spans' as a list."
            )

        if not spans:
            raise RuntimeError(
                f"Step 0 unit {unit_index} contains no source spans."
            )

        validated_spans: List[str] = []

        for span_index, span in enumerate(
            spans,
            start=1,
        ):
            if not isinstance(
                span,
                str,
            ):
                raise RuntimeError(
                    f"Step 0 unit {unit_index}, "
                    f"span {span_index} is not text."
                )

            normalized_span = _normalize_whitespace(
                span
            )

            if not normalized_span:
                raise RuntimeError(
                    f"Step 0 unit {unit_index}, "
                    f"span {span_index} is empty."
                )

            # ------------------------------------------------
            # Critical grounding check
            # ------------------------------------------------

            if normalized_span not in normalized_original:
                raise RuntimeError(
                    "\nStep 0 grounding validation failed.\n"
                    f"Unit: {unit_index}\n"
                    f"Span: {span_index}\n\n"
                    "The auxiliary LLM returned text that does not "
                    "exist in the original generated skill:\n\n"
                    f"{normalized_span}\n"
                )

            validated_spans.append(
                normalized_span
            )

        # A candidate may contain multiple source spans when
        # those spans jointly express one atomic knowledge unit.
        candidate_text = " ".join(
            validated_spans
        ).strip()

        if candidate_text:
            candidate_texts.append(
                candidate_text
            )

    if not candidate_texts:
        raise RuntimeError(
            "Step 0 produced zero valid candidate knowledge units."
        )

    return candidate_texts


def _count_tokens(
    llm: FixedLLMClient,
    text: str,
) -> int:
    """
    Count candidate length using the Anthropic token-count API.

    The same model is used for every candidate, providing a
    consistent length measure for Stage 4 representative
    selection.
    """

    result = llm.client.messages.count_tokens(
        model=llm.model,
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
    )

    return int(
        result.input_tokens
    )


# ============================================================
# Public Step 0 Function
# ============================================================

def prepare_candidate_knowledge(
    skill_text: str,
    source_skill: str,
    llm: Optional[FixedLLMClient] = None,
) -> List[CandidateKnowledge]:
    """
    Decompose one generated skill into relatively atomic K_i.

    The auxiliary LLM identifies source spans, but the program
    independently verifies that every span is grounded in the
    original generated skill.

    Step 0 performs decomposition only.

    It does NOT:
    - test agent knowledge;
    - inspect repository redundancy;
    - perform target matching;
    - intervene;
    - make KEEP/REMOVE decisions.
    """

    skill_text = skill_text.strip()
    source_skill = source_skill.strip()

    if not skill_text:
        raise ValueError(
            "skill_text cannot be empty."
        )

    if not source_skill:
        raise ValueError(
            "source_skill cannot be empty."
        )

    if llm is None:
        llm = FixedLLMClient()

    # --------------------------------------------------------
    # 1. Ask auxiliary LLM for extractive decomposition
    #    with validation-feedback retry
    # --------------------------------------------------------

    base_prompt = _build_decomposition_prompt(
        skill_text=skill_text,
    )

    max_attempts = 3
    validation_error: Optional[str] = None
    unit_texts: Optional[List[str]] = None

    for attempt in range(
        1,
        max_attempts + 1,
    ):
        if validation_error is None:
            attempt_prompt = base_prompt
        else:
            attempt_prompt = f"""
{base_prompt}

VALIDATION FEEDBACK FROM THE PREVIOUS ATTEMPT
---------------------------------------------
Your previous response failed deterministic Step 0 grounding
validation:

{validation_error}

Regenerate the COMPLETE JSON response from scratch.

Important correction requirements:
- Every source span MUST be copied verbatim from GENERATED SKILL.
- Do NOT paraphrase.
- Do NOT summarize.
- Do NOT rewrite.
- Do NOT add connecting text.
- Do NOT make implicit information explicit.
- Preserve the exact wording of each returned span.
- Return the complete JSON structure again, not only the corrected span.
---------------------------------------------
""".strip()

        parsed = llm.complete_json(
            prompt=attempt_prompt,
            system_prompt=DECOMPOSITION_SYSTEM_PROMPT,
        )

        try:
            unit_texts = _validate_and_extract_units(
                parsed=parsed,
                original_skill=skill_text,
            )
        except RuntimeError as exc:
            validation_error = str(exc)

            if attempt >= max_attempts:
                raise RuntimeError(
                    "\nStep 0 decomposition failed after "
                    f"{max_attempts} attempts.\n"
                    "The deterministic grounding validator was "
                    "kept unchanged.\n\n"
                    "Last validation error:\n"
                    f"{validation_error}"
                ) from exc

            continue

        break

    if unit_texts is None:
        raise RuntimeError(
            "Step 0 decomposition did not produce validated units."
        )

    # --------------------------------------------------------
    # 3. Construct K_i objects
    # --------------------------------------------------------

    candidates: List[
        CandidateKnowledge
    ] = []

    for index, text in enumerate(
        unit_texts,
        start=1,
    ):
        token_count = _count_tokens(
            llm=llm,
            text=text,
        )

        candidate = CandidateKnowledge(
            candidate_id=f"K_{index}",
            text=text,
            source_skill=source_skill,
            token_count=token_count,
        )

        candidates.append(
            candidate
        )

    return candidates