---
id: "f2084a63-0d37-52bb-ba37-663e4a2cf660"
name: "DataStream Sink Configuration"
description: "Automatically capture and log LLM API interactions (model, provider, tokens, cost, messages) from supported providers for observability and debugging."
version: "0.1.1"
tags:
  - "llm_monitoring"
  - "api_instrumentation"
  - "observability"
  - "cost_tracking"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Completing a Flink DataStream pipeline; need to write results to text, CSV, sockets, files, or external systems like Kafka"
---

# DataStream Sink Configuration

Automatically capture and log LLM API interactions (model, provider, tokens, cost, messages) from supported providers for observability and debugging.

## Prompt

Initialize AgentOps to track LLM API calls. Configure the instrumentation to collect model name, provider, prompt tokens, completion tokens, estimated cost, and message content for each interaction. Ensure tracking is active across the agent's lifetime and logs are accessible for monitoring and debugging.

## Objective

instrument_llm_interactions
## Applicable Signals

- Setting up LLM agent monitoring
- Need to track API costs across multiple providers
- Need to monitor token usage (prompt and completion)
- Need to debug model behavior or response quality
- Integrating with supported LLM providers (OpenAI, Anthropic, etc.)

## Contraindications

- Local-only inference without external API calls
- Privacy-restricted environments where API logging is prohibited
- Offline-only deployments

## Workflow Steps

- {'step': 1, 'action': 'Import and initialize AgentOps', 'detail': 'Set up AgentOps in the agent codebase to begin tracking'}
- {'step': 2, 'action': 'Configure provider integration', 'detail': 'Connect to supported LLM providers (e.g., OpenAI, Anthropic) via their SDKs'}
- {'step': 3, 'action': 'Enable automatic API call capture', 'detail': 'Activate tracking to collect model, provider, tokens, cost, and message data'}
- {'step': 4, 'action': 'Verify logging output', 'detail': 'Confirm that structured logs or dashboard displays all tracked fields'}

## Constraints

- Requires integration with supported LLM provider SDKs
- Tracking must be initialized before LLM calls are made
- Logging infrastructure must be available and accessible

## Cautions

- Ensure compliance with data privacy regulations before logging message content
- Monitor storage and retention policies for logged API interactions

## Output Contract

- Structured log or dashboard showing model name, provider, prompt tokens, completion tokens, estimated cost, and message content for each LLM API call.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Completing a Flink DataStream pipeline; need to write results to text, CSV, sockets, files, or external systems like Kafka
