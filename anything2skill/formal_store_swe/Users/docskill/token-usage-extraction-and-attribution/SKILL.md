---
id: "d0c0577d-6e2d-5153-a42c-06b985df0433"
name: "Token Usage Extraction and Attribution"
description: "Extract token usage metrics from API responses and attach them as span attributes for cost and quota tracking. Applies to instrumented LLM or API calls that return token consumption data."
version: "0.1.0"
tags:
  - "instrumentation"
  - "metrics"
  - "token_counting"
  - "span_attributes"
  - "cost_tracking"
  - "quota_management"
triggers:
  - "Response object contains token usage fields (prompt_tokens, completion_tokens); need to track LLM cost or quota per operation"
examples:
  - input: "API response object with fields: {prompt_tokens: 100, completion_tokens: 50, ...}"
    output: "Span attributes set: span.attributes['prompt_tokens'] = 100, span.attributes['completion_tokens'] = 50"
    notes: "Typical LLM API response after completion"
  - input: "Active span context and MetricsRecorder instance"
    output: "Metrics recorded: recorder.record_token_usage(prompt_tokens=100, completion_tokens=50)"
    notes: "Enables aggregated cost tracking across multiple operations"
---

# Token Usage Extraction and Attribution

Extract token usage metrics from API responses and attach them as span attributes for cost and quota tracking. Applies to instrumented LLM or API calls that return token consumption data.

## Prompt

Use TokenUsageExtractor to extract token usage from a response object, then call set_token_usage_attributes to attach prompt_tokens and completion_tokens to the active span. Optionally record metrics via MetricsRecorder for aggregated tracking.

## Objective

Extract and record token usage from a response object onto a span
## Applicable Signals

- Response object contains token usage fields (prompt_tokens, completion_tokens)
- Need to track LLM cost or quota per operation
- Span is active and ready to receive attributes

## Contraindications

- Response does not include token usage data
- Token counting is handled by the API client library itself
- Metrics are aggregated at a higher level without per-operation attribution

## Intervention Moves

- Call TokenUsageExtractor.extract_from_response(response) to parse token counts
- Call set_token_usage_attributes(span, response) to attach metrics to span
- Optionally call MetricsRecorder.record_token_usage(prompt_tokens, completion_tokens) for aggregation

## Workflow Steps

- {'step': 1, 'action': 'Import TokenUsageExtractor and set_token_usage_attributes from agentops.instrumentation.common'}
- {'step': 2, 'action': 'After API call returns, extract token usage: usage = TokenUsageExtractor.extract_from_response(response)'}
- {'step': 3, 'action': 'Attach to active span: set_token_usage_attributes(span, response)'}
- {'step': 4, 'action': 'Optionally record in metrics: recorder.record_token_usage(usage.prompt_tokens, usage.completion_tokens)'}

## Constraints

- Span must be active before calling set_token_usage_attributes
- Response object must be available after API call completes
- Token fields must be present in response structure

## Cautions

- Verify response structure includes token usage fields before extraction
- Ensure span context is not closed before attribute assignment

## Output Contract

- Token usage attributes (prompt_tokens, completion_tokens) are set on the span; metrics are recorded in MetricsRecorder if invoked. Downstream callers can query span attributes for cost calculation and quota enforcement.

## Example Executions

### Example 1

- Input: API response object with fields: {prompt_tokens: 100, completion_tokens: 50, ...}
- Output: Span attributes set: span.attributes['prompt_tokens'] = 100, span.attributes['completion_tokens'] = 50
- Notes: Typical LLM API response after completion

### Example 2

- Input: Active span context and MetricsRecorder instance
- Output: Metrics recorded: recorder.record_token_usage(prompt_tokens=100, completion_tokens=50)
- Notes: Enables aggregated cost tracking across multiple operations

## Triggers

- Response object contains token usage fields (prompt_tokens, completion_tokens); need to track LLM cost or quota per operation

## Examples

### Example 1

Input:

  API response object with fields: {prompt_tokens: 100, completion_tokens: 50, ...}

Output:

  Span attributes set: span.attributes['prompt_tokens'] = 100, span.attributes['completion_tokens'] = 50

Notes:

  Typical LLM API response after completion

### Example 2

Input:

  Active span context and MetricsRecorder instance

Output:

  Metrics recorded: recorder.record_token_usage(prompt_tokens=100, completion_tokens=50)

Notes:

  Enables aggregated cost tracking across multiple operations
