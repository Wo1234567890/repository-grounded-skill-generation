---
id: "ba5eb02b-fe16-5890-9e8b-ae1603bd4178"
name: "Trace State Finalization"
description: "Close an active trace and record its final state (success, failure, or custom status). Handles optional trace context and ensures all active session spans are properly terminated."
version: "0.1.0"
tags:
  - "trace_management"
  - "debugging"
  - "agent_execution"
  - "span_lifecycle"
triggers:
  - "Agent execution completes"
  - "Trace must be marked as success, failure, or custom status"
  - "Session spans need termination"
---

# Trace State Finalization

Close an active trace and record its final state (success, failure, or custom status). Handles optional trace context and ensures all active session spans are properly terminated.

## Prompt

Call end_trace() to finalize the current trace. Provide an optional trace_context; if omitted, all active session spans will be ended. Specify end_state as TraceState.SUCCESS, TraceState.FAILURE, a StatusCode, or a custom string. The function will close the trace root span and record the terminal state.

## Objective

Finalize trace execution and record terminal state
## Applicable Signals

- Agent task finished
- Final outcome determined
- Active trace context exists

## Contraindications

- Trace is already closed
- No active trace context
- End state is not yet determined

## Workflow Steps

- Determine the final state (success, failure, or custom status code)
- Retrieve or confirm the active trace context (optional; if None, all active spans end)
- Call end_trace(trace_context=<context>, end_state=<state>)
- Verify trace root span is closed and state is recorded

## Constraints

- end_state must be one of: TraceState enum value, StatusCode, or string
- If trace_context is None, all active session spans will be terminated

## Cautions

- Calling end_trace on an already-closed trace may raise an error
- Ensure end_state accurately reflects the actual outcome before finalization

## Output Contract

- Trace root span closed; end_state recorded in trace metadata; all active session spans terminated; function returns None

## Triggers

- Agent execution completes
- Trace must be marked as success, failure, or custom status
- Session spans need termination
