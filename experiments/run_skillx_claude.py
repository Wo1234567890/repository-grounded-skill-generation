import argparse
import asyncio
import os

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

import SkillX.pipeline as skillx_pipeline
from SkillX.prompts.registry import PromptRegistry
from experiments.prompts.skillsbench_filter import SKILLSBENCH_GENERAL_FILTER


class ClaudeLLM:
    def __init__(
        self,
        model="claude-haiku-4-5-20251001",
        max_tokens=10240,
        temperature=0.9,
        timeout=60,
        **kwargs
    ):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")

        self.client = ChatAnthropic(
            model=model,
            api_key=api_key,
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=timeout,
        )

    def _convert_messages(self, messages):
        converted = []
        for msg in messages:
            if isinstance(msg, tuple):
                role, content = msg
                if role == "system":
                    converted.append(SystemMessage(content=content))
                elif role in ("human", "user"):
                    converted.append(HumanMessage(content=content))
                elif role in ("assistant", "ai"):
                    converted.append(AIMessage(content=content))
                else:
                    converted.append(HumanMessage(content=content))
            else:
                converted.append(msg)
        return converted

    async def ainvoke(
        self,
        messages,
        regex_pattern=None,
        regex_extractor=None,
        **kwargs
    ):
        import re

        converted = self._convert_messages(messages)

        for _ in range(10):
            response = await self.client.ainvoke(converted)
            text = response.content

            if regex_extractor is not None:
                if regex_extractor(text) is None:
                    await asyncio.sleep(3)
                    continue

            elif regex_pattern is not None:
                if not re.search(regex_pattern, text):
                    await asyncio.sleep(3)
                    continue

            return text

        raise RuntimeError("Claude output validation failed after 10 attempts")

    def invoke(
        self,
        messages,
        regex_pattern=None,
        regex_extractor=None,
        **kwargs
    ):
        return asyncio.run(
            self.ainvoke(
                messages,
                regex_pattern=regex_pattern,
                regex_extractor=regex_extractor,
                **kwargs
            )
        )


# Use Claude as the LLM backend while keeping the SkillX pipeline unchanged.
skillx_pipeline.LLM = ClaudeLLM

# Register one benchmark-level SWE filter for all SkillsBench tasks.
# This replaces the API-oriented default GeneralFilter prompt only.
PromptRegistry.register(
    "general_filter",
    "skillsbench",
    SKILLSBENCH_GENERAL_FILTER,
)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    parser.add_argument("--trajectory", required=True)
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    output_dir = (
        args.output_dir
        if args.output_dir
        else f"experiments/outputs/{args.task}/skillx_swe_final"
    )

    await skillx_pipeline.run_pipeline(
        trajectories_path=args.trajectory,
        output_dir=output_dir,
        model="claude-haiku-4-5-20251001",
        benchmark="skillsbench",
        skill_type="functional",
        plan_strategy="shortest",
        num_epochs=1,
        filter_threshold=0.999,
        batch_size=10,
        max_concurrent=5,
        filter_timing="pre_merge",
        enable_expansion=False,
    )


if __name__ == "__main__":
    asyncio.run(main())
