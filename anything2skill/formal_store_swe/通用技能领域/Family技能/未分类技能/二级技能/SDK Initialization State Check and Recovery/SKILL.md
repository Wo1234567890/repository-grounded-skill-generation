---
id: "86a1fa28-94ca-59d8-816c-237d0c8ee660"
name: "SDK Initialization State Check and Recovery"
description: "Validate SDK initialization state before critical tracer operations. Attempt automatic recovery if uninitialized; escalate to error logging and return None if recovery fails. Prevents silent failures and ensures SDK readiness."
version: "0.1.0"
tags:
  - "sdk_lifecycle"
  - "state_validation"
  - "precondition_check"
  - "error_handling"
  - "initialization_guard"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Before any tracer operation; when tracer.initialized status is uncertain; to prevent downstream failures from uninitialized SDK"
---

# SDK Initialization State Check and Recovery

Validate SDK initialization state before critical tracer operations. Attempt automatic recovery if uninitialized; escalate to error logging and return None if recovery fails. Prevents silent failures and ensures SDK readiness.

## Prompt

Check tracer.initialized status. If False, log warning and attempt init() with environment defaults. If init() succeeds and tracer.initialized becomes True, proceed. If init() fails or tracer.initialized remains False after attempt, log error and return None. Do not silently continue with uninitialized SDK.

## Objective

Prevent silent failures and ensure SDK readiness before critical operations
## Applicable Signals

- Before any tracer operation (start_trace, log_event, etc.)
- When tracer.initialized status is uncertain or unknown
- Entry point to operations that depend on SDK readiness

## Contraindications

- SDK initialization is explicitly disabled by user configuration
- Running in a context where auto-initialization is forbidden by policy
- Caller has already verified SDK initialization state upstream

## Intervention Moves

- Check tracer.initialized boolean flag
- Log warning if uninitialized
- Attempt init() with environment variables and defaults
- Re-check tracer.initialized after init() attempt
- Log error and return None if still uninitialized or init() raised exception

## Workflow Steps

- {'step': 1, 'action': 'Check tracer.initialized', 'condition': 'if not tracer.initialized'}
- {'step': 2, 'action': "Log warning: 'AgentOps SDK not initialized. Attempting to initialize with defaults before starting trace.'", 'condition': 'tracer.initialized is False'}
- {'step': 3, 'action': 'Call init() to attempt recovery with environment defaults', 'condition': 'Warning logged'}
- {'step': 4, 'action': 'Re-check tracer.initialized', 'condition': 'init() completed without exception'}
- {'step': 5, 'action': 'Log error and return None', 'condition': 'tracer.initialized still False or init() raised exception'}

## Constraints

- Must not silently proceed with uninitialized SDK
- Must log both warning (pre-recovery) and error (post-failure) states
- Must return None on failure, not raise exception
- Auto-initialization attempt must use environment defaults only

## Cautions

- Auto-initialization may fail if required environment variables are missing
- Exception during init() must be caught and logged; do not propagate
- Caller must handle None return value and decide whether to escalate or retry

## Output Contract

- Returns True if tracer.initialized == True after check or recovery; returns False if recovery failed. Caller receives explicit error log entry on failure. No silent failures.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Before any tracer operation; when tracer.initialized status is uncertain; to prevent downstream failures from uninitialized SDK
