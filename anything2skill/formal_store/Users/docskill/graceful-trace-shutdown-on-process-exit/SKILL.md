---
id: "221b12bc-4082-5dda-ba28-0a8424fb4c0f"
name: "Graceful Trace Shutdown on Process Exit"
description: "Registers and executes a global atexit handler to cleanly end an auto-initialized trace context when the application shuts down, preventing resource leaks and incomplete trace records."
version: "0.1.0"
tags:
  - "lifecycle_management"
  - "cleanup"
  - "shutdown"
  - "trace_context"
  - "atexit_handler"
  - "resource_management"
triggers:
  - "Process termination signal received"
  - "Application exit initiated"
  - "atexit handler invoked by Python runtime"
---

# Graceful Trace Shutdown on Process Exit

Registers and executes a global atexit handler to cleanly end an auto-initialized trace context when the application shuts down, preventing resource leaks and incomplete trace records.

## Prompt

When the process is terminating, check if an auto-initialized trace context exists. If it does and the tracer is initialized with an active recording span, call tracer.end_trace() with end_state='Shutdown'. Wrap the operation in try-except to log warnings on failure. Clear global references to the trace context and legacy session wrapper in the finally block to ensure cleanup occurs regardless of success or failure.

## Objective

End trace context safely during process shutdown
## Applicable Signals

- Auto-initialized trace context exists
- Process is in shutdown phase
- Tracer is initialized and span is recording

## Contraindications

- Trace context is already explicitly ended by user code
- Manual shutdown is preferred over automatic atexit handling
- Tracer is not initialized

## Intervention Moves

- Check if _client_init_trace_context is not None
- Verify tracer.initialized and span.is_recording() before ending
- Call tracer.end_trace() with end_state='Shutdown'
- Clear _client_init_trace_context and _client_legacy_session_for_init_trace references

## Workflow Steps

- {'step': 1, 'action': 'Check if _client_init_trace_context is not None', 'condition': 'Trace context exists'}
- {'step': 2, 'action': 'Log debug message indicating auto-ending of init trace', 'condition': 'Always'}
- {'step': 3, 'action': 'Verify tracer.initialized and _client_init_trace_context.span.is_recording()', 'condition': 'Before attempting to end trace'}
- {'step': 4, 'action': "Call tracer.end_trace(_client_init_trace_context, end_state='Shutdown')", 'condition': 'Tracer is initialized and span is recording'}
- {'step': 5, 'action': 'Catch exceptions and log warning', 'condition': 'Any exception occurs during trace ending'}
- {'step': 6, 'action': 'Clear _client_init_trace_context and _client_legacy_session_for_init_trace', 'condition': 'In finally block, always'}

## Constraints

- Must be registered as a global atexit handler before application shutdown
- Must use try-except-finally to prevent exceptions from propagating to atexit
- Must clear global state in finally block to ensure cleanup

## Cautions

- Atexit handlers run in a limited environment; avoid complex I/O or external calls
- Log warnings instead of raising exceptions to prevent shutdown hangs
- Ensure global references are cleared to avoid dangling pointers

## Output Contract

- Trace context is ended with end_state='Shutdown', global references (_client_init_trace_context and _client_legacy_session_for_init_trace) are set to None, and no exceptions propagate to the atexit handler.

## Triggers

- Process termination signal received
- Application exit initiated
- atexit handler invoked by Python runtime
