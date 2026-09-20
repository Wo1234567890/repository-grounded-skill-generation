---
id: "88ec988c-cb23-50ce-b6e6-eb8aec788c7a"
name: "Attribute Extraction from Method Calls"
description: "Extract telemetry attributes (e.g., model name, token usage) from LLM method arguments and return values using a structured AttributeMap handler. Normalizes observable metadata into OpenTelemetry-compliant keys for downstream observability systems."
version: "0.1.0"
tags:
  - "observability"
  - "telemetry"
  - "instrumentation"
  - "attribute_extraction"
  - "opentelemetry"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "An instrumented LLM method is called; args, kwargs, or return_value contain model, usage, or other observable metadata."
examples:
  - input: "{'args': [], 'kwargs': {'model': 'gpt-4', 'temperature': 0.7}, 'return_value': {'usage': {'total_tokens': 150, 'prompt_tokens': 50, 'completion_tokens': 100}}}"
    output: "{'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150, 'llm.usage.prompt_tokens': 50, 'llm.usage.completion_tokens': 100}"
    notes: "Full extraction from both kwargs and return_value"
  - input: "{'args': [], 'kwargs': {'model': 'claude-3'}, 'return_value': None}"
    output: "{'llm.request.model': 'claude-3'}"
    notes: "Partial extraction when return_value is None"
---

# Attribute Extraction from Method Calls

Extract telemetry attributes (e.g., model name, token usage) from LLM method arguments and return values using a structured AttributeMap handler. Normalizes observable metadata into OpenTelemetry-compliant keys for downstream observability systems.

## Prompt

Implement an attribute handler function that inspects method call arguments, keyword arguments, and return values to extract relevant telemetry data. Map extracted values to OpenTelemetry-compliant attribute keys (e.g., 'llm.request.model', 'llm.usage.total_tokens'). Return an AttributeMap dictionary with all extracted attributes. Handle cases where expected attributes may be missing or None.

## Objective

Capture and normalize LLM request and response metadata for observability
## Applicable Signals

- LLM method call is intercepted during instrumentation
- Method arguments contain model identifier or configuration
- Return value contains usage statistics or metadata
- Span context requires enrichment with call-specific attributes

## Contraindications

- Method call has no relevant metadata to extract
- Return value is None or lacks expected attributes
- Attribute extraction would require deep introspection of complex nested objects

## Intervention Moves

- Check kwargs for 'model' key and extract model name
- Inspect return_value for 'usage' attribute and extract token counts
- Map extracted values to OpenTelemetry-compliant keys
- Return populated AttributeMap or empty dict if no relevant data found

## Workflow Steps

- {'step': 1, 'action': 'Receive args, kwargs, and return_value from instrumented method call'}
- {'step': 2, 'action': 'Initialize empty AttributeMap dictionary'}
- {'step': 3, 'action': "Check kwargs for 'model' key; if present, map to 'llm.request.model'"}
- {'step': 4, 'action': "Check return_value for 'usage' attribute; if present, extract token counts and map to 'llm.usage.*' keys"}
- {'step': 5, 'action': 'Return populated AttributeMap'}

## Constraints

- Handler must accept args, kwargs, and return_value parameters
- Output must be an AttributeMap (dict-like) with string keys
- Keys must follow OpenTelemetry naming conventions (e.g., 'llm.request.*', 'llm.usage.*')
- Handler must not raise exceptions; missing attributes should be skipped gracefully

## Cautions

- Do not assume all expected attributes are present; use defensive checks
- Avoid extracting sensitive data (e.g., API keys, user content) into attributes
- Keep attribute extraction lightweight to minimize instrumentation overhead

## Output Contract

- AttributeMap dictionary with zero or more OpenTelemetry-compliant key-value pairs extracted from the method call. Keys follow patterns such as 'llm.request.model', 'llm.usage.total_tokens', 'llm.usage.prompt_tokens', 'llm.usage.completion_tokens'. Empty dict is valid if no relevant metadata is found.

## Example Therapist Responses

### Example 1

- Client/Input: {'args': [], 'kwargs': {'model': 'gpt-4', 'temperature': 0.7}, 'return_value': {'usage': {'total_tokens': 150, 'prompt_tokens': 50, 'completion_tokens': 100}}}
- Therapist/Output: {'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150, 'llm.usage.prompt_tokens': 50, 'llm.usage.completion_tokens': 100}
- Notes: Full extraction from both kwargs and return_value

### Example 2

- Client/Input: {'args': [], 'kwargs': {'model': 'claude-3'}, 'return_value': None}
- Therapist/Output: {'llm.request.model': 'claude-3'}
- Notes: Partial extraction when return_value is None

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- An instrumented LLM method is called; args, kwargs, or return_value contain model, usage, or other observable metadata.

## Examples

### Example 1

Input:

  {'args': [], 'kwargs': {'model': 'gpt-4', 'temperature': 0.7}, 'return_value': {'usage': {'total_tokens': 150, 'prompt_tokens': 50, 'completion_tokens': 100}}}

Output:

  {'llm.request.model': 'gpt-4', 'llm.usage.total_tokens': 150, 'llm.usage.prompt_tokens': 50, 'llm.usage.completion_tokens': 100}

Notes:

  Full extraction from both kwargs and return_value

### Example 2

Input:

  {'args': [], 'kwargs': {'model': 'claude-3'}, 'return_value': None}

Output:

  {'llm.request.model': 'claude-3'}

Notes:

  Partial extraction when return_value is None
