---
id: "0c6d7ac8-d8d1-54d8-8cbd-55c5a2dac5ec"
name: "Trace context safe termination with fallback"
description: "Safely terminate an active trace span by verifying tracer initialization and span recording status, then end the trace with exception handling and state cleanup. Designed to prevent dangling trace references and unhandled exceptions during shutdown or session termination."
version: "0.1.0"
tags:
  - "trace_management"
  - "resource_cleanup"
  - "shutdown_handler"
  - "defensive_programming"
  - "exception_handling"
triggers:
  - "A trace context exists, tracer is available, and the span is actively recording; shutdown or session end is triggered"
---

# Trace context safe termination with fallback

Safely terminate an active trace span by verifying tracer initialization and span recording status, then end the trace with exception handling and state cleanup. Designed to prevent dangling trace references and unhandled exceptions during shutdown or session termination.

## Prompt

Before ending a trace context: (1) Verify the trace context is not None. (2) Check that the tracer is initialized and the span is actively recording. (3) Call tracer.end_trace() with an appropriate end_state parameter. (4) Catch and log any exceptions without re-raising. (5) In the finally block, nullify both the trace context and any legacy wrapper references to prevent reuse.

## Objective

End a trace context without raising exceptions or leaving dangling references
## Applicable Signals

- Trace context exists and is not None
- Tracer is initialized
- Span is actively recording
- Shutdown or session end is triggered

## Contraindications

- Trace context is None
- Tracer is not initialized
- Span is already closed or not recording
- Trace state is unknown or unverified

## Workflow Steps

- {'step': 1, 'action': 'Check if trace context is not None', 'condition': 'Proceed only if context exists'}
- {'step': 2, 'action': 'Verify tracer.initialized is True and span.is_recording() returns True', 'condition': 'Both conditions must hold before calling end_trace'}
- {'step': 3, 'action': 'Call tracer.end_trace(context, end_state=<state_label>)', 'condition': "All checks passed; use appropriate end_state such as 'Shutdown'"}
- {'step': 4, 'action': 'Catch Exception and log warning without re-raising', 'condition': 'Any exception during end_trace is caught and logged'}
- {'step': 5, 'action': 'In finally block, set trace context and legacy wrapper to None', 'condition': 'Always execute to ensure state cleanup regardless of success or failure'}

## Constraints

- Do not re-raise exceptions; log and suppress to prevent cascade failures
- Always nullify context and legacy wrapper in finally block
- Do not attempt to end trace if tracer is not initialized
- Do not attempt to end trace if span is not recording

## Cautions

- If tracer.end_trace() raises an exception, the trace may be partially ended; log the error and proceed with cleanup
- Ensure end_state parameter is meaningful for downstream analysis (e.g., 'Shutdown', 'Error', 'Complete')

## Output Contract

- Trace context is ended with the specified end_state
- Both trace context and legacy wrapper are set to None
- No unhandled exceptions are propagated to the caller

## Triggers

- A trace context exists, tracer is available, and the span is actively recording; shutdown or session end is triggered
