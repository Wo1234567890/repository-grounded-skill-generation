---
id: "e3db3ce1-4c46-5250-8cf3-b6d590656c9e"
name: "ProcessPoolExecutor Worker Lifecycle Configuration"
description: "Register and execute a global atexit handler that safely ends the client's auto-initialized trace context during application shutdown, with error recovery and resource cleanup."
version: "0.1.1"
tags:
  - "shutdown"
  - "trace_management"
  - "resource_cleanup"
  - "atexit_handler"
  - "error_recovery"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to control fork vs. spawn behavior for worker processes"
  - "Require setup code (e.g., database connection) to run in each worker"
  - "Want to limit worker lifetime to prevent memory leaks"
  - "Must ensure consistent worker state across task batches"
examples:
  - input: "Application with auto-initialized trace context; process receives SIGTERM"
    output: "Trace context ended with state='Shutdown'; _client_init_trace_context set to None; _client_legacy_session_for_init_trace set to None; process exits cleanly"
    notes: "Normal shutdown path with active trace"
  - input: "Tracer not initialized or span not recording at shutdown"
    output: "Debug log recorded; trace context and legacy wrapper cleared; no tracer.end_trace() call; process exits cleanly"
    notes: "Graceful degradation when tracer state is incomplete"
  - input: "Exception raised during tracer.end_trace() call"
    output: "Warning logged with exception details; trace context and legacy wrapper still cleared in finally block; process exits cleanly"
    notes: "Error recovery ensures cleanup occurs despite trace termination failure"
---

# ProcessPoolExecutor Worker Lifecycle Configuration

Register and execute a global atexit handler that safely ends the client's auto-initialized trace context during application shutdown, with error recovery and resource cleanup.

## Prompt

When the application is shutting down, invoke the atexit handler to terminate the active trace context. The handler checks if a trace context exists and is recording, then calls the global tracer to end the trace with state 'Shutdown'. If an error occurs during trace termination, log a warning and proceed to cleanup. Finally, clear the trace context and legacy session wrapper references to prevent resource leaks.

## Objective

Ensure trace context is properly terminated on process exit
## Applicable Signals

- Client auto-initialization with trace context active
- Global _client_init_trace_context is not None
- Tracer is initialized and span is recording

## Contraindications

- Manual trace lifecycle control is required by caller
- Trace context is managed externally outside this handler
- Shutdown hooks are already registered by caller
- Tracer is not initialized or span is not recording

## Workflow Steps

- {'step': 1, 'action': 'Check if trace context exists', 'condition': '_client_init_trace_context is not None', 'next': 'step 2 if true, else exit'}
- {'step': 2, 'action': 'Log debug message indicating auto-end of init trace', 'condition': 'Always', 'next': 'step 3'}
- {'step': 3, 'action': 'Verify tracer is initialized and span is recording', 'condition': 'tracer.initialized and _client_init_trace_context.span.is_recording()', 'next': 'step 4 if true, else step 5'}
- {'step': 4, 'action': "Call tracer.end_trace() with end_state='Shutdown'", 'condition': 'Tracer ready', 'next': 'step 5'}
- {'step': 5, 'action': 'Catch any exception and log warning', 'condition': 'Exception raised in steps 3-4', 'next': 'step 6'}
- {'step': 6, 'action': 'Clear trace context and legacy session wrapper', 'condition': 'Always (in finally block)', 'next': 'completion'}

## Constraints

- Handler must be registered only once (use _atexit_registered flag)
- Handler must execute within Python's atexit phase
- Global state (_client_init_trace_context, _client_legacy_session_for_init_trace) must be accessible
- Tracer instance must be available and initialized

## Cautions

- Exceptions during trace termination must be caught and logged; do not propagate during shutdown
- Resource cleanup (setting context to None) must occur in finally block to guarantee execution
- Handler should not raise exceptions that would interrupt process exit

## Output Contract

- Atexit handler is registered globally; on process exit, trace context is set to None; legacy session wrapper is cleared; trace span is ended with state 'Shutdown' if conditions permit; errors are logged but do not interrupt shutdown.

## Example Executions

### Example 1

- Input: Application with auto-initialized trace context; process receives SIGTERM
- Output: Trace context ended with state='Shutdown'; _client_init_trace_context set to None; _client_legacy_session_for_init_trace set to None; process exits cleanly
- Notes: Normal shutdown path with active trace

### Example 2

- Input: Tracer not initialized or span not recording at shutdown
- Output: Debug log recorded; trace context and legacy wrapper cleared; no tracer.end_trace() call; process exits cleanly
- Notes: Graceful degradation when tracer state is incomplete

### Example 3

- Input: Exception raised during tracer.end_trace() call
- Output: Warning logged with exception details; trace context and legacy wrapper still cleared in finally block; process exits cleanly
- Notes: Error recovery ensures cleanup occurs despite trace termination failure

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to control fork vs. spawn behavior for worker processes
- Require setup code (e.g., database connection) to run in each worker
- Want to limit worker lifetime to prevent memory leaks
- Must ensure consistent worker state across task batches

## Examples

### Example 1

Input:

  Application with auto-initialized trace context; process receives SIGTERM

Output:

  Trace context ended with state='Shutdown'; _client_init_trace_context set to None; _client_legacy_session_for_init_trace set to None; process exits cleanly

Notes:

  Normal shutdown path with active trace

### Example 2

Input:

  Tracer not initialized or span not recording at shutdown

Output:

  Debug log recorded; trace context and legacy wrapper cleared; no tracer.end_trace() call; process exits cleanly

Notes:

  Graceful degradation when tracer state is incomplete

### Example 3

Input:

  Exception raised during tracer.end_trace() call

Output:

  Warning logged with exception details; trace context and legacy wrapper still cleared in finally block; process exits cleanly

Notes:

  Error recovery ensures cleanup occurs despite trace termination failure
