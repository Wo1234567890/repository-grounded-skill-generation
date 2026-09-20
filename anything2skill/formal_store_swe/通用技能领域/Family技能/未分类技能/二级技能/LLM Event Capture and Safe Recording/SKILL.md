---
id: "d455d61a-a585-56d3-b134-16e49b8d6cb2"
name: "LLM Event Capture and Safe Recording"
description: "Captures LLM request-response lifecycle events (parameters, outputs, timestamps) and safely records them to a session, with automatic error event generation on exception."
version: "0.1.0"
tags:
  - "event_logging"
  - "llm_interaction"
  - "debugging"
  - "audit_trail"
  - "error_handling"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "LLM call completes and response is available"
  - "Need to log full interaction (prompt, parameters, response output) for debugging or audit trails"
  - "Session is active and available for event recording"
examples:
  - input: "{'response': 'OpenAI response object with model_dump() method', 'kwargs': {'messages': [{'role': 'user', 'content': 'What is 2+2?'}], 'model': 'gpt-4', 'temperature': 0.7}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}"
    output: "LLMEvent recorded with returns={...}, prompt=[...], params={...}"
    notes: "Normal path: response processed and event recorded successfully"
  - input: "{'response': 'response object', 'kwargs': {'messages': [{'role': 'user', 'content': 'test'}]}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}"
    output: "ErrorEvent recorded with exception details"
    notes: "Exception path: model_dump() or other processing fails, ErrorEvent captures the failure"
---

# LLM Event Capture and Safe Recording

Captures LLM request-response lifecycle events (parameters, outputs, timestamps) and safely records them to a session, with automatic error event generation on exception.

## Prompt

When an LLM call completes, construct an LLMEvent with the initialization timestamp and request parameters. Extract the response output via model_dump() and assign to the event's returns field. Populate the prompt field from the request messages. Attempt to record the event to the session via _safe_record(). If any exception occurs during processing, construct an ErrorEvent with the trigger_event and exception, and record that instead.

## Objective

Record LLM interactions with structured event data and error handling
## Applicable Signals

- response object received from LLM
- init_timestamp available from call start
- kwargs containing request messages and parameters
- session object is not None

## Contraindications

- Session is None or unavailable—use fallback logging mechanism instead
- Event is not LLM-related—do not force into LLMEvent structure
- Response object does not support model_dump() method

## Workflow Steps

- {'step': 1, 'action': 'Construct LLMEvent', 'detail': 'Create LLMEvent object with init_timestamp and params=kwargs'}
- {'step': 2, 'action': 'Extract response data', 'detail': 'Call response.model_dump() and assign to llm_event.returns'}
- {'step': 3, 'action': 'Extract prompt', 'detail': "Assign kwargs['messages'] to llm_event.prompt"}
- {'step': 4, 'action': 'Record event', 'detail': 'Call _safe_record(session, llm_event)'}
- {'step': 5, 'action': 'Handle exception', 'detail': 'On any exception, construct ErrorEvent(trigger_event=llm_event, exception=e) and call _safe_record(session, error_event)'}

## Constraints

- init_timestamp must be set before event construction
- kwargs must contain 'messages' key for prompt extraction
- session parameter must be passed to _safe_record()
- Exception handling must always attempt ErrorEvent recording

## Cautions

- If _safe_record() fails, the error may be silently swallowed depending on implementation; verify logging backend is operational
- Large response payloads from model_dump() may consume significant memory; consider truncation for high-volume scenarios

## Output Contract

- LLMEvent object with populated returns, prompt, and params fields successfully recorded to session; or ErrorEvent recorded if exception occurs during processing. Caller receives confirmation that event was persisted or error was logged.

## Example Executions

### Example 1

- Input: {'response': 'OpenAI response object with model_dump() method', 'kwargs': {'messages': [{'role': 'user', 'content': 'What is 2+2?'}], 'model': 'gpt-4', 'temperature': 0.7}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}
- Output: LLMEvent recorded with returns={...}, prompt=[...], params={...}
- Notes: Normal path: response processed and event recorded successfully

### Example 2

- Input: {'response': 'response object', 'kwargs': {'messages': [{'role': 'user', 'content': 'test'}]}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}
- Output: ErrorEvent recorded with exception details
- Notes: Exception path: model_dump() or other processing fails, ErrorEvent captures the failure

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- LLM call completes and response is available
- Need to log full interaction (prompt, parameters, response output) for debugging or audit trails
- Session is active and available for event recording

## Examples

### Example 1

Input:

  {'response': 'OpenAI response object with model_dump() method', 'kwargs': {'messages': [{'role': 'user', 'content': 'What is 2+2?'}], 'model': 'gpt-4', 'temperature': 0.7}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}

Output:

  LLMEvent recorded with returns={...}, prompt=[...], params={...}

Notes:

  Normal path: response processed and event recorded successfully

### Example 2

Input:

  {'response': 'response object', 'kwargs': {'messages': [{'role': 'user', 'content': 'test'}]}, 'init_timestamp': 1699564800.123, 'session': 'active_session_object'}

Output:

  ErrorEvent recorded with exception details

Notes:

  Exception path: model_dump() or other processing fails, ErrorEvent captures the failure
