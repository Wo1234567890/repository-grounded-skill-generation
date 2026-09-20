---
id: "d2d734a8-0322-51e2-a503-f256a0d31d5c"
name: "BrokenProcessPool Exception Handling"
description: "Detect and handle BrokenProcessPool exception raised when a worker process in ProcessPoolExecutor terminates abruptly. Prevents undefined behavior such as freezing or deadlock by catching the exception, logging the failure, and ensuring graceful cleanup before escalating to caller. Complements mandatory credential validation at initialization to ensure only properly configured clients enter execution phase."
version: "0.1.1"
tags:
  - "initialization"
  - "credential_validation"
  - "safety_guard"
  - "exception_escalation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "ProcessPoolExecutor in use"
  - "Worker process crashes or terminates unexpectedly"
  - "Operations on executor or futures may freeze"
examples:
  - input: "ProcessPoolExecutor.map() called; worker process terminates abruptly during iteration"
    output: "BrokenProcessPool exception caught, logged with operation context, executor shutdown initiated, exception re-raised to caller"
    notes: "Caller must decide whether to retry with a new executor or fall back to sequential execution"
---

# BrokenProcessPool Exception Handling

Detect and handle BrokenProcessPool exception raised when a worker process in ProcessPoolExecutor terminates abruptly. Prevents undefined behavior such as freezing or deadlock by catching the exception, logging the failure, and ensuring graceful cleanup before escalating to caller. Complements mandatory credential validation at initialization to ensure only properly configured clients enter execution phase.

## Prompt

Check that self.config.api_key is non-empty and non-None. If the API key is missing or empty, raise NoApiKeyException immediately to halt initialization. This is a mandatory guard that must execute before any API calls or session operations.

## Objective

Prevent uninitialized client operation due to missing credentials
## Applicable Signals

- Client initialization is in progress
- Config object has been instantiated
- API key presence must be verified before any API calls

## Contraindications

- API key is optional or deferred in the current execution context
- Client is operating in offline or mock mode
- Credential validation is handled by a parent system or wrapper

## Intervention Moves

- Catch BrokenProcessPool exception at executor operation boundary
- Log exception with context (which operation, which futures affected)
- Trigger executor cleanup (context manager exit or explicit shutdown)
- Escalate failure state to caller for recovery or retry decision

## Workflow Steps

- Identify ProcessPoolExecutor operation boundary (submit, map, or future result access)
- Wrap operation in try-except block targeting BrokenProcessPool
- In except block: log exception with operation context and affected futures
- Initiate executor cleanup (context manager exit or shutdown)
- Re-raise exception or notify caller of pool failure state

## Constraints

- Must be applied at ProcessPoolExecutor operation boundary (submit, map, or future result access)
- Exception must not be silently suppressed; escalation is mandatory
- Executor cleanup must complete before returning control to caller

## Cautions

- BrokenProcessPool indicates worker process failure; recovery may require pool restart or fallback to sequential execution
- Futures submitted before the crash may be lost; caller must handle incomplete results
- Do not attempt to reuse the same executor instance after BrokenProcessPool; create a new one

## Output Contract

- On success: API key is confirmed non-empty in self.config.api_key; execution proceeds to next initialization step. On failure: NoApiKeyException is raised and initialization halts.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- ProcessPoolExecutor in use
- Worker process crashes or terminates unexpectedly
- Operations on executor or futures may freeze

## Examples

### Example 1

Input:

  ProcessPoolExecutor.map() called; worker process terminates abruptly during iteration

Output:

  BrokenProcessPool exception caught, logged with operation context, executor shutdown initiated, exception re-raised to caller

Notes:

  Caller must decide whether to retry with a new executor or fall back to sequential execution
