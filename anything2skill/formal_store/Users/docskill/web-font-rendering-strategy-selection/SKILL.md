---
id: "5d54ebac-052c-525f-b1ac-d6c81c8e8b19"
name: "Web Font Rendering Strategy Selection"
description: "Capture and log LLM interaction events including prompts, completions, token usage, timestamps, errors, and tool usage to enable debugging and monitoring of LLM provider activity."
version: "0.1.1"
tags:
  - "llm_integration"
  - "observability"
  - "debugging"
  - "event_logging"
  - "monitoring"
triggers:
  - "Web fonts are being downloaded and a fallback rendering strategy must be selected"
  - "Font loading timing is a performance or user experience concern"
  - "Layout shift during font swap needs to be minimized"
---

# Web Font Rendering Strategy Selection

Capture and log LLM interaction events including prompts, completions, token usage, timestamps, errors, and tool usage to enable debugging and monitoring of LLM provider activity.

## Prompt

When an LLM provider is active and processing requests, implement event tracking to capture: prompts sent to the LLM, completions received, token usage metrics, request/response timestamps, any errors encountered, and tool usage if applicable. Log these events in a structured format accessible for later debugging and auditing.

## Objective

Track and log LLM events for observability
## Applicable Signals

- Provider handle_response() method is invoked
- Prompt is prepared for LLM
- Completion is returned from LLM
- Token count is available
- Tool call is made by LLM

## Contraindications

- Event logging is disabled by configuration
- Performance-critical paths where logging overhead is unacceptable
- Sensitive data handling contexts where logging may violate privacy constraints

## Workflow Steps

- {'step': 1, 'action': 'Intercept LLM request before sending', 'detail': 'Capture prompt text, model identifier, and request timestamp'}
- {'step': 2, 'action': 'Log prompt event', 'detail': 'Record prompt content, metadata, and timestamp in structured format'}
- {'step': 3, 'action': 'Intercept LLM response', 'detail': 'Capture completion text, token usage, and response timestamp'}
- {'step': 4, 'action': 'Log completion event', 'detail': 'Record completion content, token counts, and timestamp'}
- {'step': 5, 'action': 'Track tool usage if applicable', 'detail': 'Log any tool calls made by the LLM with parameters and results'}
- {'step': 6, 'action': 'Capture errors', 'detail': 'Log any errors or exceptions with error type, message, and timestamp'}

## Constraints

- Must capture events without blocking LLM request/response flow
- Logged data must be structured and queryable
- Timestamps must be consistent and precise

## Cautions

- Ensure sensitive information (API keys, personal data in prompts) is not logged or is redacted
- Monitor logging overhead to avoid performance degradation

## Output Contract

- All LLM interactions (prompts, completions, token usage, timestamps, errors, tool usage) are logged in a structured, queryable format and accessible for debugging and auditing purposes.

## Triggers

- Web fonts are being downloaded and a fallback rendering strategy must be selected
- Font loading timing is a performance or user experience concern
- Layout shift during font swap needs to be minimized
