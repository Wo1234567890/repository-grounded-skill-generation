---
id: "40060062-3dbc-5b0d-b4dc-a198affc3fb8"
name: "Future Cancellation and State Inspection"
description: "Synchronize current session and trace context state to legacy module globals for backward compatibility. Invoked during client initialization when auto-trace is enabled and legacy code paths must remain functional."
version: "0.1.1"
tags:
  - "backward_compatibility"
  - "state_synchronization"
  - "legacy_integration"
  - "client_initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to conditionally cancel a pending task before it starts execution"
  - "Must check if a task is still running before attempting to access its result"
  - "Implementing timeout-based or event-driven cancellation logic"
  - "Coordinating multiple dependent futures and need to know their execution state"
examples:
  - input: "future = executor.submit(is_prime, 112272535095293); future.cancel()"
    output: "True (if task was pending and successfully cancelled) or False (if task already running or finished)"
    notes: "Attempt to cancel a submitted task before it starts execution"
  - input: "future.running()"
    output: "True (if task is currently executing) or False (if not yet started or already finished)"
    notes: "Check if task is in progress before attempting cancellation"
  - input: "future.done()"
    output: "True (if task has finished in any state) or False (if still pending or running)"
    notes: "Verify task has reached terminal state before proceeding with dependent operations"
---

# Future Cancellation and State Inspection

Synchronize current session and trace context state to legacy module globals for backward compatibility. Invoked during client initialization when auto-trace is enabled and legacy code paths must remain functional.

## Prompt

Update the legacy module's _current_session and _current_trace_context globals with the values from the current client instance. Wrap the import and assignment in a try-except block to gracefully handle cases where the legacy module is not available. Do not raise an error if the import fails; log and continue.

## Objective

Update legacy module globals with current session state to maintain backward compatibility
## Applicable Signals

- auto_start_session flag is True
- Legacy session wrapper exists in current client instance
- Trace context has been initialized

## Contraindications

- Legacy module is not imported or not available
- auto_start_session is False
- Direct session passing is available and preferred

## Workflow Steps

- {'step': 1, 'action': 'Attempt to import agentops.legacy module', 'condition': 'Legacy module integration required'}
- {'step': 2, 'action': 'Assign self._legacy_session_for_init_trace to agentops.legacy._current_session', 'condition': 'Import successful'}
- {'step': 3, 'action': 'Assign self._init_trace_context to agentops.legacy._current_trace_context', 'condition': 'Import successful'}
- {'step': 4, 'action': 'Catch ImportError and pass silently', 'condition': 'Legacy module not available'}

## Constraints

- ImportError must be caught and suppressed; do not propagate
- Assignment must occur only if import succeeds
- State values must be taken from the current client instance, not external sources

## Cautions

- Direct access to another module's globals is not ideal; use only when explicit session passing is not feasible
- Ensure legacy module is in the expected import path before relying on this synchronization

## Output Contract

- Legacy module _current_session and _current_trace_context globals are updated with current client state; ImportError is caught and suppressed without raising; caller receives confirmation that synchronization completed (or was skipped if legacy module unavailable)

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to conditionally cancel a pending task before it starts execution
- Must check if a task is still running before attempting to access its result
- Implementing timeout-based or event-driven cancellation logic
- Coordinating multiple dependent futures and need to know their execution state

## Examples

### Example 1

Input:

  future = executor.submit(is_prime, 112272535095293); future.cancel()

Output:

  True (if task was pending and successfully cancelled) or False (if task already running or finished)

Notes:

  Attempt to cancel a submitted task before it starts execution

### Example 2

Input:

  future.running()

Output:

  True (if task is currently executing) or False (if not yet started or already finished)

Notes:

  Check if task is in progress before attempting cancellation

### Example 3

Input:

  future.done()

Output:

  True (if task has finished in any state) or False (if still pending or running)

Notes:

  Verify task has reached terminal state before proceeding with dependent operations
