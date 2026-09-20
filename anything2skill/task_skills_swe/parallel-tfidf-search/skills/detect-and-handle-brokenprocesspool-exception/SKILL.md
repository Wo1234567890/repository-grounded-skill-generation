---
id: "07979eac-f1a1-5bda-8fb4-e448888f946c"
name: "Detect and Handle BrokenProcessPool Exception"
description: "Catch BrokenProcessPool exceptions raised when a ProcessPoolExecutor worker terminates abnormally (killed externally, crash, or resource exhaustion). Implement recovery or escalation to restore task execution capability."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "ProcessPoolExecutor"
  - "exception_handling"
  - "worker_failure"
  - "recovery"
  - "escalation"
triggers:
  - "ProcessPoolExecutor worker terminates abnormally during task execution"
  - "External process kill or crash detected"
  - "Resource exhaustion causes worker termination"
---

# Detect and Handle BrokenProcessPool Exception

Catch BrokenProcessPool exceptions raised when a ProcessPoolExecutor worker terminates abnormally (killed externally, crash, or resource exhaustion). Implement recovery or escalation to restore task execution capability.

## Prompt

When a ProcessPoolExecutor worker terminates in a non-clean fashion, a BrokenProcessPool exception is raised. Catch this exception, log the failure with worker identity and termination cause, determine an appropriate recovery strategy (task resubmission, pool restart, or escalation), and execute the recovery action or escalate to the caller.

## Objective

Safely handle process pool worker termination failures and restore execution capability
## Applicable Signals

- BrokenProcessPool exception raised by concurrent.futures.process module
- Worker process exit code indicates non-clean termination

## Contraindications

- Worker termination is intentional and should not trigger recovery
- No escalation or recovery action is required by design
- Caller explicitly handles pool lifecycle and does not expect automatic recovery

## Intervention Moves

- Catch BrokenProcessPool exception from ProcessPoolExecutor.submit() or result retrieval
- Log exception details including worker identity, timestamp, affected task, and exception message
- Validate pool state before attempting recovery
- Execute recovery action: resubmit task to new pool, restart pool, or escalate upstream

## Workflow Steps

- {'step': 1, 'action': 'Catch BrokenProcessPool exception', 'detail': 'Use try-except block around ProcessPoolExecutor.submit() or result retrieval to intercept exception from concurrent.futures.process module'}
- {'step': 2, 'action': 'Log exception details', 'detail': 'Record timestamp, affected task identity, worker information, and exception message for diagnostics and audit trail'}
- {'step': 3, 'action': 'Determine recovery strategy', 'detail': 'Analyze failure pattern and choose between task resubmission, pool restart, or escalation based on context and failure frequency'}
- {'step': 4, 'action': 'Execute recovery or escalate', 'detail': 'Resubmit task to new pool instance, restart pool, or raise exception upstream with context preserved'}

## Constraints

- Exception is derived from BrokenExecutor; catch at appropriate hierarchy level
- Recovery action must be idempotent to avoid duplicate task execution
- Pool state must be validated before resubmitting tasks
- Do not silently ignore BrokenProcessPool; always log and escalate or recover

## Cautions

- Resubmitting tasks without pool restart may fail; validate pool health first
- External process kills may indicate system-level issues; escalate if repeated
- Ensure recovery logic does not mask underlying resource or configuration problems

## Output Contract

- Exception caught and logged with full context. Recovery action initiated (task resubmission, pool restart, or escalation to caller). Caller receives either successful task result after recovery or re-raised exception with diagnostic context preserved.

## Triggers

- ProcessPoolExecutor worker terminates abnormally during task execution
- External process kill or crash detected
- Resource exhaustion causes worker termination
