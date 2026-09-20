---
id: "36d9b519-83c7-57a1-9bbc-fa41a0213aaf"
name: "Register atexit cleanup handler"
description: "Register a single atexit handler to ensure trace cleanup runs at process exit, guarding against duplicate registrations via idempotent flag check."
version: "0.1.0"
tags:
  - "cleanup"
  - "atexit"
  - "idempotent"
  - "initialization"
  - "resource_management"
triggers:
  - "Client initialization; atexit handler not yet registered (_atexit_registered is False)"
---

# Register atexit cleanup handler

Register a single atexit handler to ensure trace cleanup runs at process exit, guarding against duplicate registrations via idempotent flag check.

## Prompt

Check if the atexit handler has already been registered using the _atexit_registered flag. If not registered (flag is False), call atexit.register() with the _end_init_trace_atexit callback and set the flag to True. This ensures the cleanup handler runs exactly once at process termination.

## Objective

Ensure trace cleanup on process termination
## Applicable Signals

- Client initialization phase
- _atexit_registered flag is False
- Process lifecycle management required

## Contraindications

- Handler already registered (_atexit_registered is True)
- Process cleanup not required or disabled
- Multiple concurrent initialization attempts

## Intervention Moves

- Check _atexit_registered global state
- Call atexit.register(_end_init_trace_atexit)
- Set _atexit_registered to True

## Workflow Steps

- {'step': 1, 'action': 'Check global _atexit_registered flag', 'condition': 'Flag must be False to proceed'}
- {'step': 2, 'action': 'Call atexit.register(_end_init_trace_atexit)', 'condition': 'Only if flag is False'}
- {'step': 3, 'action': 'Set _atexit_registered to True', 'condition': 'After successful registration'}

## Constraints

- Must check flag before registration to prevent duplicates
- Registration must occur exactly once per process
- Callback function _end_init_trace_atexit must be defined and callable

## Cautions

- Atexit handlers run in reverse registration order; ensure no circular dependencies with other handlers
- Exceptions in the cleanup callback may prevent subsequent handlers from running

## Output Contract

- _atexit_registered flag set to True; atexit.register() called exactly once with _end_init_trace_atexit callback; cleanup handler guaranteed to execute at process exit

## Triggers

- Client initialization; atexit handler not yet registered (_atexit_registered is False)
