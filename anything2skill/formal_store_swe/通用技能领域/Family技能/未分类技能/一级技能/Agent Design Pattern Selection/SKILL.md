---
id: "8d51b78f-5e60-50aa-8e1e-da272d48debc"
name: "Agent Design Pattern Selection"
description: "Identify and reference appropriate agent design patterns for a given use case. Provides access to catalog of reusable patterns across multiple frameworks (LangChain, CrewAI, OpenAI Agents, SmolAgents, Google Gemini, LiteLLM, Watsonx, xAI) covering single-agent and multi-agent scenarios, tool orchestration, human-in-the-loop workflows, and domain-specific conversions."
version: "0.1.0"
tags:
  - "agent_design"
  - "pattern_reference"
  - "best_practices"
  - "template"
  - "multi_framework"
  - "langchain"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Designing a new agent from scratch"
  - "Need to understand common agent patterns and best practices"
  - "Looking for a template or example for a specific use case"
---

# Agent Design Pattern Selection

Identify and reference appropriate agent design patterns for a given use case. Provides access to catalog of reusable patterns across multiple frameworks (LangChain, CrewAI, OpenAI Agents, SmolAgents, Google Gemini, LiteLLM, Watsonx, xAI) covering single-agent and multi-agent scenarios, tool orchestration, human-in-the-loop workflows, and domain-specific conversions.

## Prompt

When designing a new agent, consult this reference to identify applicable patterns. Review the pattern description, examine the provided example code, and adapt the template to your use case. Patterns cover single-agent and multi-agent scenarios.

## Objective

Reference and select appropriate agent design pattern for a given use case
## Applicable Signals

- Agent architecture decision point
- No existing pattern selected
- Design phase active

## Contraindications

- Pattern already selected and implementation underway
- Designing a novel or experimental agent architecture
- No design guidance needed; implementation-only phase

## Constraints

- Reference asset; does not execute workflows directly
- Patterns are templates; adaptation to specific requirements is caller responsibility
- Examples assume familiarity with underlying frameworks (LangChain, CrewAI, OpenAI Agents, SmolAgents, Google Gemini, LiteLLM, Watsonx, xAI)

## Output Contract

- Caller receives pattern description, applicable use cases, example code reference, and guidance on when to apply the pattern.
- Caller is responsible for selecting and adapting the pattern to their specific requirements.
- Patterns available include: customer service automation, job workflow automation, markdown validation, text-to-SQL conversion, multi-tool orchestration, web search, human-in-the-loop approval, multi-agent coordination, and streaming text generation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Designing a new agent from scratch
- Need to understand common agent patterns and best practices
- Looking for a template or example for a specific use case
