---
id: "3a5d5495-e130-5d76-915b-5f9fab29f2fa"
name: "Token Usage Extraction and Attribution"
description: "Extract token usage metrics from LLM/API responses and record them as span attributes for observability and cost tracking. Parses response metadata using TokenUsageExtractor and applies prompt/completion token counts to active instrumentation spans."
version: "0.1.0"
tags:
  - "token_counting"
  - "metrics"
  - "observability"
  - "cost_tracking"
  - "span_attributes"
triggers:
  - "LLM or API response is received and token usage must be tracked for observability or billing"
examples:
  - input: "API response object with usage field: {\"choices\": [...], \"usage\": {\"prompt_tokens\": 100, \"completion_tokens\": 50}}"
    output: "Span attributes set: span.attributes[\"prompt_tokens\"] = 100, span.attributes[\"completion_tokens\"] = 50"
    notes: "Standard OpenAI-style response format"
---

# Token Usage Extraction and Attribution

Extract token usage metrics from LLM/API responses and record them as span attributes for observability and cost tracking. Parses response metadata using TokenUsageExtractor and applies prompt/completion token counts to active instrumentation spans.

## Prompt

When an LLM or API response is received, use TokenUsageExtractor.extract_from_response(response) to parse token counts, then call set_token_usage_attributes(span, response) to record prompt_tokens and completion_tokens as span attributes. This ensures consistent token usage tracking across all instrumented operations.

## Objective

Capture and record token usage from LLM responses into instrumentation spans
## Applicable Signals

- LLM or API response received
- Token usage metadata present in response
- Span context active and ready for attribute assignment

## Contraindications

- Response does not contain token usage metadata
- Token tracking is not required for the operation
- No active span context available

## Intervention Moves

- Extract token usage from response using TokenUsageExtractor.extract_from_response()
- Set extracted token counts on span using set_token_usage_attributes(span, response)
- Verify span attributes include prompt_tokens and completion_tokens

## Workflow Steps

- {'step': 1, 'action': 'Receive LLM or API response object', 'condition': 'Response is available and contains potential token usage data'}
- {'step': 2, 'action': 'Call TokenUsageExtractor.extract_from_response(response)', 'condition': 'Response object is compatible with extractor'}
- {'step': 3, 'action': 'Call set_token_usage_attributes(span, response)', 'condition': 'Extraction succeeded and span context is active'}
- {'step': 4, 'action': 'Verify span attributes contain prompt_tokens and completion_tokens', 'condition': 'Attribute assignment completed'}

## Constraints

- Response object must be compatible with TokenUsageExtractor
- Span must be active and writable at time of attribute assignment
- Token values must be numeric and non-negative

## Cautions

- Ensure response object structure matches expected format before extraction
- Verify span is still in scope before setting attributes
- Handle cases where token counts may be missing or zero

## Output Contract

- Span attributes updated with prompt_tokens and completion_tokens values extracted from response; token usage is now recorded for downstream observability and billing systems

## Example Therapist Responses

### Example 1

- Client/Input: API response object with usage field: {"choices": [...], "usage": {"prompt_tokens": 100, "completion_tokens": 50}}
- Therapist/Output: Span attributes set: span.attributes["prompt_tokens"] = 100, span.attributes["completion_tokens"] = 50
- Notes: Standard OpenAI-style response format

## Triggers

- LLM or API response is received and token usage must be tracked for observability or billing

## Examples

### Example 1

Input:

  API response object with usage field: {"choices": [...], "usage": {"prompt_tokens": 100, "completion_tokens": 50}}

Output:

  Span attributes set: span.attributes["prompt_tokens"] = 100, span.attributes["completion_tokens"] = 50

Notes:

  Standard OpenAI-style response format
