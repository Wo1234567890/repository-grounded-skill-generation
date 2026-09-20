---
id: "2f61409c-487d-5905-bece-063163c72b9e"
name: "LLM Event Capture and Error Handling"
description: "Captures LLM request/response lifecycle events (parameters, outputs, timestamps) and wraps exceptions in error events for safe recording. Use when instrumenting LLM API calls to build an audit trail of interactions and failures."
version: "0.1.0"
tags:
  - "llm_instrumentation"
  - "event_capture"
  - "error_handling"
  - "audit_trail"
  - "structured_logging"
triggers:
  - "LLM API call completes and needs to be recorded"
  - "Exception occurs during response processing"
---

# LLM Event Capture and Error Handling

Captures LLM request/response lifecycle events (parameters, outputs, timestamps) and wraps exceptions in error events for safe recording. Use when instrumenting LLM API calls to build an audit trail of interactions and failures.

## Prompt

When an LLM API call completes or an exception occurs during response processing, create an LLMEvent with init_timestamp and request parameters (kwargs). Extract response data via model_dump() and prompt from kwargs["messages"]. If an exception occurs, wrap it in an ErrorEvent with the trigger_event reference. Call _safe_record(session, event) to persist the event safely.

## Objective

capture_and_record_llm_interactions
## Applicable Signals

- LLM API call completion
- Response object available
- Exception raised during response processing

## Contraindications

- Recording is disabled or not configured
- Session is None and no fallback handler exists
- Response object does not support model_dump() method

## Intervention Moves

- Create LLMEvent with init_timestamp and request parameters
- Extract and assign response data via model_dump()
- Extract and assign prompt from kwargs["messages"]
- Catch exceptions and wrap in ErrorEvent with trigger_event reference
- Call _safe_record(session, event) to persist event

## Workflow Steps

- {'step': 1, 'action': 'Initialize LLMEvent with init_timestamp and kwargs (request parameters)'}
- {'step': 2, 'action': 'Extract response data via response.model_dump() and assign to llm_event.returns'}
- {'step': 3, 'action': 'Extract prompt from kwargs["messages"] and assign to llm_event.prompt'}
- {'step': 4, 'action': 'Perform any additional processing on llm_event'}
- {'step': 5, 'action': 'Call _safe_record(session, llm_event) to persist the event'}
- {'step': 6, 'action': 'On exception: create ErrorEvent with trigger_event=llm_event and exception details'}
- {'step': 7, 'action': 'Call _safe_record(session, error_event) to persist the error'}

## Constraints

- init_timestamp must be set before LLMEvent creation
- kwargs must contain "messages" key for prompt extraction
- session parameter may be None; _safe_record must handle gracefully
- Exception handling must not suppress critical errors needed for escalation

## Cautions

- Ensure _safe_record is implemented to handle None session safely
- Do not lose exception context when wrapping in ErrorEvent
- Verify response.model_dump() does not expose sensitive data before recording

## Output Contract

- LLMEvent or ErrorEvent successfully persisted via _safe_record(); response data, prompt, and exception details (if applicable) captured and recorded for audit trail.

## Triggers

- LLM API call completes and needs to be recorded
- Exception occurs during response processing
