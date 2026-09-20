---
id: "c9cf6cff-970b-5e93-8e61-f543e257085e"
name: "Initialize SDK with Fallback"
description: "Automatically initialize the AgentOps SDK using environment variables or defaults if not already initialized, with error logging and graceful failure handling. Ensures the tracer is ready before downstream operations attempt to use it."
version: "0.1.0"
tags:
  - "sdk_setup"
  - "initialization"
  - "fallback"
  - "error_handling"
  - "precondition_check"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "tracer.initialized returns False"
  - "SDK initialization status is unknown or unconfirmed before starting a trace"
---

# Initialize SDK with Fallback

Automatically initialize the AgentOps SDK using environment variables or defaults if not already initialized, with error logging and graceful failure handling. Ensures the tracer is ready before downstream operations attempt to use it.

## Prompt

Check if tracer.initialized is False. If so, attempt init() with environment variables or defaults. Log warnings and errors at each stage. Return success only if tracer.initialized becomes True after init(); otherwise return None and log the failure reason.

## Objective

Ensure SDK is ready before trace operations
## Applicable Signals

- tracer.initialized == False
- Caller attempts trace operation without explicit prior init()

## Contraindications

- Explicit initialization has already been performed and confirmed
- User prefers manual control over initialization timing
- tracer.initialized == True (skip this skill)

## Intervention Moves

- Attempt automatic initialization with environment defaults
- Log diagnostic warnings and errors for troubleshooting
- Gracefully degrade to None return on failure

## Workflow Steps

- {'step': 1, 'action': 'Check tracer.initialized status', 'condition': 'if not tracer.initialized'}
- {'step': 2, 'action': 'Log warning that SDK is not initialized', 'detail': 'logger.warning("AgentOps SDK not initialized. Attempting to initialize with defaults before starting trace.")'}
- {'step': 3, 'action': 'Attempt init() with environment variables or defaults', 'detail': 'Call init() inside try-except block'}
- {'step': 4, 'action': 'Verify tracer.initialized after init()', 'condition': 'if not tracer.initialized after init()'}
- {'step': 5, 'action': 'Log error and return None', 'detail': 'logger.error("SDK initialization failed. Cannot start trace."); return None'}
- {'step': 6, 'action': 'Catch and log exceptions during init()', 'detail': 'except Exception as e: logger.error(f"SDK auto-initialization failed: {e}. Cannot start trace."); return None'}

## Constraints

- Must check tracer.initialized before attempting init()
- Must catch and log exceptions during auto-initialization
- Must not raise exceptions; return None on failure

## Cautions

- Auto-initialization relies on environment variables; ensure they are set if defaults are insufficient
- Logging warnings and errors should not block execution

## Output Contract

- Returns True or success indicator if tracer.initialized == True after initialization; returns None with error logged if initialization fails or cannot be completed. Caller should check return value before proceeding to trace operations.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- tracer.initialized returns False
- SDK initialization status is unknown or unconfirmed before starting a trace
