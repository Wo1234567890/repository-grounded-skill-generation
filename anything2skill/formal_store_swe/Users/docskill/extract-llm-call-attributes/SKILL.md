---
id: "8185c2cc-1c3f-50b8-a5e9-e51dce55aa14"
name: "Extract LLM Call Attributes"
description: "Extract structured attributes (model, tokens, usage) from LLM method calls and return values for telemetry recording. Maps call arguments and responses to OpenTelemetry attribute keys."
version: "0.1.0"
tags:
  - "telemetry"
  - "instrumentation"
  - "opentelemetry"
  - "llm-monitoring"
  - "attribute-extraction"
  - "observability"
triggers:
  - "Intercepting LLM provider method calls (OpenAI, Anthropic, Google GenAI, IBM WatsonX, CrewAI, AG2/AutoGen, etc.)"
  - "Need to extract model name, token usage, or response metadata for observability"
  - "Preparing telemetry data for OpenTelemetry span attachment"
examples:
  - input: "args=None, kwargs={'model': 'gpt-4', 'temperature': 0.7}, return_value=<Response with usage.total_tokens=150>"
    output: "{'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150}"
    notes: "Standard OpenAI-style call with model and usage metadata"
  - input: "args=None, kwargs={'model': 'claude-3'}, return_value=None"
    output: "{'llm.request.model': 'claude-3'}"
    notes: "Return value missing; extract only available kwargs"
---

# Extract LLM Call Attributes

Extract structured attributes (model, tokens, usage) from LLM method calls and return values for telemetry recording. Maps call arguments and responses to OpenTelemetry attribute keys.

## Prompt

Implement an attribute handler that inspects method call arguments (args, kwargs) and return values to populate an AttributeMap dictionary. Extract model name from kwargs, token usage from return_value.usage, and other LLM-specific metadata. Return the populated AttributeMap ready for span attachment.

## Objective

Convert method call metadata into telemetry attributes
## Applicable Signals

- Method call with kwargs containing 'model' parameter
- Return value with 'usage' attribute containing token counts
- LLM provider response object available for inspection

## Contraindications

- Non-LLM method calls or utility functions without LLM semantics
- Return value is None or lacks usage metadata
- Attribute keys do not conform to OpenTelemetry naming conventions

## Workflow Steps

- {'step': 1, 'action': "Check if kwargs is not None and contains 'model' key", 'output': "Extract model name and assign to attributes['llm.request.model']"}
- {'step': 2, 'action': "Check if return_value is not None and has 'usage' attribute", 'output': "Extract total_tokens and assign to attributes['llm.usage.total_tokens']"}
- {'step': 3, 'action': 'Populate any additional LLM-specific attributes from return_value or kwargs', 'output': 'Add keys such as llm.response.finish_reason, llm.request.temperat...'}
- {'step': 4, 'action': 'Return the populated AttributeMap', 'output': 'AttributeMap ready for downstream span attachment'}

## Constraints

- Must validate that kwargs and return_value are not None before accessing nested attributes
- Attribute keys must follow OpenTelemetry semantic conventions (e.g., llm.request.model, llm.usage.total_tokens)
- Handler must return AttributeMap type, not raw dict

## Cautions

- Accessing missing keys in kwargs or return_value without hasattr checks will raise KeyError
- Token counts may be zero or missing in some LLM responses; handle gracefully
- Different LLM providers may use different response structures; validate structure before extraction

## Output Contract

- AttributeMap dictionary with populated OpenTelemetry-compliant keys (llm.request.model, llm.usage.total_tokens, etc.) ready for span attachment. Empty AttributeMap if no extractable metadata is found.

## Example Executions

### Example 1

- Input: args=None, kwargs={'model': 'gpt-4', 'temperature': 0.7}, return_value=<Response with usage.total_tokens=150>
- Output: {'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150}
- Notes: Standard OpenAI-style call with model and usage metadata

### Example 2

- Input: args=None, kwargs={'model': 'claude-3'}, return_value=None
- Output: {'llm.request.model': 'claude-3'}
- Notes: Return value missing; extract only available kwargs

## Triggers

- Intercepting LLM provider method calls (OpenAI, Anthropic, Google GenAI, IBM WatsonX, CrewAI, AG2/AutoGen, etc.)
- Need to extract model name, token usage, or response metadata for observability
- Preparing telemetry data for OpenTelemetry span attachment

## Examples

### Example 1

Input:

  args=None, kwargs={'model': 'gpt-4', 'temperature': 0.7}, return_value=<Response with usage.total_tokens=150>

Output:

  {'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150}

Notes:

  Standard OpenAI-style call with model and usage metadata

### Example 2

Input:

  args=None, kwargs={'model': 'claude-3'}, return_value=None

Output:

  {'llm.request.model': 'claude-3'}

Notes:

  Return value missing; extract only available kwargs
