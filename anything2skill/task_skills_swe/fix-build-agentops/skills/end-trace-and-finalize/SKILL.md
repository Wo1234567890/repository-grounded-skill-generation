---
id: "2bc6e1f0-1a41-5924-96e3-a05d149f1f9e"
name: "End Trace and Finalize"
description: "Terminates the current trace (root span) and finalizes its state. If no trace context is provided, closes all active session spans. Use when completing a debugging session or marking trace completion status."
version: "0.1.0"
tags:
  - "trace_lifecycle"
  - "debugging"
  - "session_management"
  - "span_termination"
triggers:
  - "Completing a trace session"
  - "Finalizing agent operation monitoring"
  - "Closing all active spans"
---

# End Trace and Finalize

Terminates the current trace (root span) and finalizes its state. If no trace context is provided, closes all active session spans. Use when completing a debugging session or marking trace completion status.

## Prompt

Call end_trace() to finalize the current trace with a specified end state. Provide an optional trace_context to target a specific trace; if omitted, all active session spans are closed. Set end_state to TraceState.SUCCESS, TraceState.FAILURE, a custom StatusCode, or a string status. The trace and all its spans are marked complete and no longer accept new events.

## Objective

finalize trace lifecycle
## Applicable Signals

- Agent task completion
- Debugging session end
- Explicit trace closure request

## Contraindications

- Trace has already been ended
- Only updating metadata without closing the session

## Workflow Steps

- Verify trace is still active (not already ended)
- Resolve trace_context: use provided context or default to all active session spans
- Set end_state to specified value (default: TraceState.SUCCESS)
- Finalize trace and close all associated spans
- Return confirmation of finalization

## Constraints

- trace_context must be Optional[TraceContext] or None
- end_state must be TraceState, StatusCode, or string
- Once end_trace() is called, the trace cannot accept new spans or events

## Cautions

- Calling end_trace() on an already-ended trace may raise an error or be silently ignored depending on implementation.
- If trace_context is None, all active session spans are terminated; ensure this is the intended behavior.

## Output Contract

- Trace finalized with specified end state (SUCCESS, FAILURE, or custom StatusCode); all spans closed and trace marked complete.

## Triggers

- Completing a trace session
- Finalizing agent operation monitoring
- Closing all active spans
