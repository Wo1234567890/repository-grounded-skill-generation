---
id: "a4e8dc3e-92b7-57ac-9a86-942f2de4d17a"
name: "Exception-to-ErrorEvent Conversion"
description: "Wraps any exception that occurs during LLM response processing into a structured ErrorEvent linked to the triggering LLMEvent, preserving causality for debugging."
version: "0.1.0"
tags:
  - "error_handling"
  - "exception_wrapping"
  - "debugging"
  - "event_tracing"
  - "causality_preservation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "An exception is raised during LLM event processing and you need to preserve the error context and link it to the originating LLM event"
examples:
  - input: "LLMEvent in progress; exception raised during response.model_dump()"
    output: "ErrorEvent(trigger_event=llm_event, exception=<exception instance>)"
    notes: "Exception is captured and linked to the LLMEvent that triggered it"
---

# Exception-to-ErrorEvent Conversion

Wraps any exception that occurs during LLM response processing into a structured ErrorEvent linked to the triggering LLMEvent, preserving causality for debugging.

## Prompt

When an exception is raised during LLM event processing, capture it and create an ErrorEvent object that references the originating LLMEvent. Pass both the trigger_event (the LLMEvent that was being processed) and the exception to the ErrorEvent constructor, then record it via _safe_record().

## Objective

Convert unhandled exceptions into traceable error events
## Applicable Signals

- Exception raised during LLM response processing
- Need to preserve error context and link to originating LLM event

## Contraindications

- Exception should be re-raised to a higher-level handler
- Exception handling is delegated to caller or outer scope

## Intervention Moves

- Catch exception in except block
- Create ErrorEvent with trigger_event and exception parameters
- Record ErrorEvent via _safe_record()

## Workflow Steps

- {'step': 1, 'action': 'Wrap LLM response processing in try-except block'}
- {'step': 2, 'action': 'In except clause, instantiate ErrorEvent with trigger_event=llm_event and exception=e'}
- {'step': 3, 'action': 'Call _safe_record(session, error_event) to persist the error event'}

## Constraints

- LLMEvent must be available and valid before exception occurs
- session parameter must be passed to _safe_record()
- ErrorEvent constructor must accept trigger_event and exception fields

## Cautions

- Do not suppress exceptions that require escalation or re-raising
- Ensure _safe_record() is idempotent to avoid duplicate error logging

## Output Contract

- ErrorEvent object created with trigger_event and exception fields, ready for recording and downstream debugging.

## Example Executions

### Example 1

- Input: LLMEvent in progress; exception raised during response.model_dump()
- Output: ErrorEvent(trigger_event=llm_event, exception=<exception instance>)
- Notes: Exception is captured and linked to the LLMEvent that triggered it

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- An exception is raised during LLM event processing and you need to preserve the error context and link it to the originating LLM event

## Examples

### Example 1

Input:

  LLMEvent in progress; exception raised during response.model_dump()

Output:

  ErrorEvent(trigger_event=llm_event, exception=<exception instance>)

Notes:

  Exception is captured and linked to the LLMEvent that triggered it
