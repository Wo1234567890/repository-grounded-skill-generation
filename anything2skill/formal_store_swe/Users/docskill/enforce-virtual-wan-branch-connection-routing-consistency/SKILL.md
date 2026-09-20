---
id: "05a1fa80-ae1b-56f6-8fde-d087fb1185a7"
name: "Enforce Virtual WAN Branch Connection Routing Consistency"
description: "Detect and recover from abrupt worker process termination in ProcessPoolExecutor by catching BrokenProcessPool exception, logging the failure, discarding the broken executor, and implementing recovery or escalation logic to prevent freeze or deadlock."
version: "0.1.1"
tags:
  - "concurrent.futures"
  - "ProcessPoolExecutor"
  - "exception_handling"
  - "worker_process"
  - "deadlock_prevention"
  - "safety_guardrail"
triggers:
  - "Configuring branch connections in Virtual WAN"
  - "Adding or modifying Point-to-site, Site-to-site, or ExpressRoute connections"
  - "Reviewing existing branch routing configuration"
examples:
  - input: "ProcessPoolExecutor with 4 workers; one worker process crashes during executor.map(is_prime, PRIMES)"
    output: "BrokenProcessPool caught; executor discarded; exception logged with worker PID and task count; caller receives exception or retry signal"
    notes: "Prevents silent freeze; allows graceful degradation or retry"
---

# Enforce Virtual WAN Branch Connection Routing Consistency

Detect and recover from abrupt worker process termination in ProcessPoolExecutor by catching BrokenProcessPool exception, logging the failure, discarding the broken executor, and implementing recovery or escalation logic to prevent freeze or deadlock.

## Prompt

When using ProcessPoolExecutor, wrap executor operations (executor.map(), executor.submit(), future.result()) in a try-except block to catch BrokenProcessPool. Upon exception: (1) log the error with worker context and pending task count, (2) discard the current executor instance via shutdown(wait=False) or context manager exit, (3) either recreate the executor and retry or escalate to caller. Do not suppress the exception silently or attempt to reuse futures from the broken executor.

## Objective

Prevent undefined behavior (freeze, deadlock) when worker processes crash unexpectedly in ProcessPoolExecutor.
## Applicable Signals

- BrokenProcessPool exception raised during executor.map(), executor.submit(), or future.result() calls
- Executor or futures operations would otherwise freeze or deadlock
- Worker process terminates abnormally without explicit shutdown

## Contraindications

- Using ThreadPoolExecutor (does not raise BrokenProcessPool)
- Process termination is expected and already handled by application logic
- Executor is used in a context where recreation is not feasible
- Catching generic Exception instead of BrokenProcessPool specifically

## Intervention Moves

- Wrap ProcessPoolExecutor operations in try-except block targeting BrokenProcessPool
- Log exception with worker process context and pending task state
- Discard executor instance via shutdown(wait=False) or context manager exit
- Implement recovery path: recreate executor with backoff strategy or escalate to caller

## Workflow Steps

- {'step': 1, 'action': 'Wrap ProcessPoolExecutor operations in try-except block', 'detail': 'Enclose executor.map(), executor.submit(), or future.result() calls'}
- {'step': 2, 'action': 'Catch BrokenProcessPool exception', 'detail': 'Catch concurrent.futures.BrokenProcessPool specifically; do not catch generic Exception'}
- {'step': 3, 'action': 'Log exception with context', 'detail': 'Record worker process failure, executor state, and pending tasks'}
- {'step': 4, 'action': 'Discard executor instance', 'detail': 'Exit context manager or call executor.shutdown(wait=False)'}
- {'step': 5, 'action': 'Decide recovery path', 'detail': 'Either recreate executor with backoff strategy and retry, or escalate to caller'}

## Constraints

- Must catch BrokenProcessPool explicitly; do not catch generic Exception
- Executor instance must be discarded after exception is caught
- Caller must be prepared to retry or handle escalation
- Do not attempt to reuse futures from a broken executor

## Cautions

- BrokenProcessPool behavior changed in Python 3.3; earlier versions had undefined behavior
- Recreating executor may be expensive; consider backoff or escalation strategy
- Do not attempt to reuse futures from a broken executor
- Ensure no frozen or deadlocked threads remain after executor discard

## Output Contract

- BrokenProcessPool exception is caught and logged with worker context; executor is discarded; no frozen or deadlocked threads remain; caller receives either a new executor instance, a retry signal, or an escalation signal.

## Example Executions

### Example 1

- Input: ProcessPoolExecutor with 4 workers; one worker process crashes during executor.map(is_prime, PRIMES)
- Output: BrokenProcessPool caught; executor discarded; exception logged with worker PID and task count; caller receives exception or retry signal
- Notes: Prevents silent freeze; allows graceful degradation or retry

## Triggers

- Configuring branch connections in Virtual WAN
- Adding or modifying Point-to-site, Site-to-site, or ExpressRoute connections
- Reviewing existing branch routing configuration

## Examples

### Example 1

Input:

  ProcessPoolExecutor with 4 workers; one worker process crashes during executor.map(is_prime, PRIMES)

Output:

  BrokenProcessPool caught; executor discarded; exception logged with worker PID and task count; caller receives exception or retry signal

Notes:

  Prevents silent freeze; allows graceful degradation or retry
