---
id: "fbff9862-db86-58a4-9cdc-06e659adf674"
name: "LLM Event Capture and Tracking"
description: "Micro operation to intercept and log LLM interactions including prompts, completions, token usage, timestamps, errors, and tool calls. Invoked within provider handle_response() to record observable LLM behavior for debugging and monitoring."
version: "0.1.0"
tags:
  - "observability"
  - "event_logging"
  - "llm_monitoring"
  - "debugging"
  - "provider_integration"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "LLM provider receives a response from the model"
  - "handle_response() method is invoked on the provider instance"
---

# LLM Event Capture and Tracking

Micro operation to intercept and log LLM interactions including prompts, completions, token usage, timestamps, errors, and tool calls. Invoked within provider handle_response() to record observable LLM behavior for debugging and monitoring.

## Prompt

When an LLM provider receives a response, capture and record the following event metadata: the input prompt, the completion text, token usage counts, request/response timestamps, any errors encountered, and tool invocations if applicable. Store the event record in a structured format accessible to downstream logging and analysis.

## Objective

Capture and record LLM request/response events with full observability metadata
## Applicable Signals

- Response object available from LLM client
- Provider context is active and initialized

## Contraindications

- Do not invoke during pre-request validation phase
- Do not invoke during provider initialization or setup
- Do not invoke during method patching or unpatching logic

## Workflow Steps

- {'step': 1, 'action': 'Extract prompt from request context', 'detail': 'Retrieve the input prompt text that was sent to the LLM'}
- {'step': 2, 'action': 'Extract completion from response', 'detail': 'Retrieve the completion text returned by the LLM'}
- {'step': 3, 'action': 'Record token usage', 'detail': 'Capture prompt tokens, completion tokens, and total tokens if available'}
- {'step': 4, 'action': 'Record timestamps', 'detail': 'Capture request start time and response completion time'}
- {'step': 5, 'action': 'Capture error information', 'detail': 'Log any errors or exceptions encountered during the LLM call'}
- {'step': 6, 'action': 'Track tool usage if applicable', 'detail': 'Record any tool calls or function invocations made by the LLM'}
- {'step': 7, 'action': 'Assemble and store event record', 'detail': 'Combine all captured metadata into a structured event record'}

## Constraints

- Must execute after response is received, not before
- Event record must include all required fields: prompt, completion, token usage, timestamp, error status
- Tool usage tracking is conditional on applicability to the provider

## Cautions

- Ensure token counts are accurate for billing and quota tracking
- Preserve error details without exposing sensitive information
- Handle cases where tool usage is not applicable to the provider

## Output Contract

- Event record object containing: prompt (string), completion (string), token_usage (dict with prompt_tokens, completion_tokens, total_tokens), timestamp_start (ISO 8601), timestamp_end (ISO 8601), error (string or null), tool_calls (list or null). Record is immediately available for logging, monitoring, and downstream analysis.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- LLM provider receives a response from the model
- handle_response() method is invoked on the provider instance
