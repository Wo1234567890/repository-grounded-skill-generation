---
id: "668f2259-9ad6-5193-b5b0-d334405e5cbf"
name: "Exit Handler Registration for Trace Cleanup"
description: "Register a single atexit handler to ensure trace cleanup occurs on process termination, preventing duplicate handler registration through idempotent flag checking."
version: "0.1.0"
tags:
  - "lifecycle"
  - "cleanup"
  - "idempotent"
  - "resource_management"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Client or session initialization begins"
  - "Trace context setup required"
---

# Exit Handler Registration for Trace Cleanup

Register a single atexit handler to ensure trace cleanup occurs on process termination, preventing duplicate handler registration through idempotent flag checking.

## Prompt

Check the _atexit_registered flag. If False, register the _end_init_trace_atexit callback with atexit.register() and set the flag to True. This ensures the handler is registered exactly once, even if initialization is called multiple times.

## Objective

Ensure deterministic cleanup of trace resources on process exit
## Applicable Signals

- Initialization phase entry
- _atexit_registered flag is False or unset

## Contraindications

- Handler already registered (_atexit_registered is True)
- Process cleanup not required or disabled
- Multiple concurrent initialization calls (use flag to serialize)

## Intervention Moves

- Check global _atexit_registered flag
- If False, call atexit.register(_end_init_trace_atexit)
- Set _atexit_registered to True

## Workflow Steps

- {'step': 1, 'action': 'Check global _atexit_registered flag', 'condition': 'Flag exists and is accessible'}
- {'step': 2, 'action': 'If flag is False, call atexit.register(_end_init_trace_atexit)', 'condition': 'Handler not yet registered'}
- {'step': 3, 'action': 'Set _atexit_registered to True', 'condition': 'Registration successful'}

## Constraints

- Must check flag before registration to prevent duplicates
- Flag must be module-level global to persist across calls
- Registration must occur exactly once per process lifetime

## Cautions

- If flag check is bypassed, duplicate handlers may accumulate
- Ensure _end_init_trace_atexit callback is defined and callable before registration

## Output Contract

- Handler registered exactly once; _atexit_registered flag set to True; _end_init_trace_atexit will be invoked on process termination.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Client or session initialization begins
- Trace context setup required
