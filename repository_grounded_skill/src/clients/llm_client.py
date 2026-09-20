import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

from anthropic import Anthropic
from dotenv import load_dotenv


# ============================================================
# Project / Environment
# ============================================================

# repository_grounded_skill/
# ├── .env
# └── src/
#     └── clients/
#         └── llm_client.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]

ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_PATH)


# ============================================================
# Response Model
# ============================================================

@dataclass
class LLMResponse:
    """
    Result returned by one auxiliary LLM API call.
    """

    text: str
    input_tokens: int = 0
    output_tokens: int = 0
    raw: Any = None


# ============================================================
# Fixed Auxiliary LLM
# ============================================================

class FixedLLMClient:
    """
    Fixed auxiliary LLM used by the repository-grounded
    knowledge probing method.

    IMPORTANT:
    This is NOT the target coding agent.

    This auxiliary LLM is used for:
    - knowledge target identification
    - duplicate-target detection / merging
    - diagnostic question generation
    - reference-answer generation
    - repository redundancy judgment
    - candidate-target matching
    - evidence-grounded recomposition

    The target coding agent uses a separate API key and a
    separate implementation.
    """

    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        max_tokens: int = 4096,
    ):
        # Auxiliary LLM uses its own API key.
        api_key = os.getenv("ANTHROPIC_AUX_API_KEY")

        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_AUX_API_KEY was not found.\n"
                f"Expected it in: {ENV_PATH}"
            )

        self.client = Anthropic(
            api_key=api_key
        )

        self.model = model
        self.max_tokens = max_tokens

    # ========================================================
    # Plain Text Completion
    # ========================================================

    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> LLMResponse:
        """
        Run one independent auxiliary LLM call.

        No conversational state is reused between calls.
        """

        request: Dict[str, Any] = {
            "model": self.model,
            "max_tokens": (
                max_tokens
                if max_tokens is not None
                else self.max_tokens
            ),
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        if system_prompt:
            request["system"] = system_prompt

        message = self.client.messages.create(
            **request
        )

        # Collect all text blocks from the response.
        text_parts = []

        for block in message.content:
            block_text = getattr(
                block,
                "text",
                None,
            )

            if block_text:
                text_parts.append(block_text)

        text = "\n".join(
            text_parts
        ).strip()

        # Token usage.
        usage = getattr(
            message,
            "usage",
            None,
        )

        input_tokens = 0
        output_tokens = 0

        if usage is not None:
            input_tokens = getattr(
                usage,
                "input_tokens",
                0,
            )

            output_tokens = getattr(
                usage,
                "output_tokens",
                0,
            )

        return LLMResponse(
            text=text,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            raw=message,
        )

    # ========================================================
    # JSON Completion
    # ========================================================

    def complete_json(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Run one auxiliary LLM call and require valid JSON output.

        Used for method decisions such as:
        - duplicate / non-duplicate
        - PROVIDED / NOT_PROVIDED
        - MATCH / NO_MATCH
        """

        json_instruction = """
Return ONLY one valid JSON object.

Do not use Markdown code fences.
Do not include explanations before the JSON.
Do not include explanations after the JSON.
"""

        response = self.complete(
            prompt=prompt + "\n" + json_instruction,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
        )

        raw_text = response.text.strip()

        try:
            parsed = json.loads(raw_text)

        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "Auxiliary LLM returned invalid JSON.\n\n"
                f"OUTPUT:\n{raw_text}"
            ) from exc

        if not isinstance(parsed, dict):
            raise RuntimeError(
                "Auxiliary LLM JSON output must be an object.\n\n"
                f"OUTPUT:\n{raw_text}"
            )

        return parsed