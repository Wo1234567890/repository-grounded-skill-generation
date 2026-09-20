---
id: "0727e71a-176f-5681-b009-b38cd2eb150a"
name: "Classify Future Timeout and Cancellation Outcomes"
description: "Catch and classify TimeoutError and CancelledError exceptions when calling Future.result(timeout=...) or waiting on Futures with timeout. Route each outcome class (timeout, cancellation, normal completion) to the appropriate handler for recovery, retry, escalation, or cleanup."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "Future"
  - "timeout"
  - "cancellation"
  - "exception_handling"
  - "error_classification"
triggers:
  - "Calling Future.result(timeout=...) or waiting on Futures with timeout; need to distinguish between timeout, cancellation, and normal completion"
examples:
  - input: "Call future.result(timeout=5) on a Future that does not complete within 5 seconds"
    output: "concurrent.futures.TimeoutError is raised; caller catches and decides to retry or escalate"
    notes: "Timeout is the primary failure mode when timeout parameter is set"
  - input: "Call future.result(timeout=10) on a Future that was cancelled via future.cancel()"
    output: "concurrent.futures.CancelledError is raised; caller catches and performs cleanup"
    notes: "Cancellation takes precedence; result() raises CancelledError even if timeout has not elapsed"
  - input: "Call future.result(timeout=None) on a Future that completes normally"
    output: "No exception; result is returned or underlying exception is raised"
    notes: "When timeout=None, no timeout occurs; only the Future's actual outcome is observed"
---

# Classify Future Timeout and Cancellation Outcomes

Catch and classify TimeoutError and CancelledError exceptions when calling Future.result(timeout=...) or waiting on Futures with timeout. Route each outcome class (timeout, cancellation, normal completion) to the appropriate handler for recovery, retry, escalation, or cleanup.

## Prompt

When calling Future.result(timeout=...) or waiting on Futures with a timeout parameter, catch and classify the exception outcome. If TimeoutError is raised, the operation exceeded the timeout threshold. If CancelledError is raised, the Future was cancelled before completion. Route each case to the appropriate handler: timeout cases may warrant retry or escalation; cancellation cases may warrant logging or cleanup. Normal completion (no exception) proceeds without intervention.

## Objective

Classify and handle Future timeout and cancellation outcomes
## Applicable Signals

- Calling Future.result(timeout=...) with a timeout parameter
- Waiting on Futures using concurrent.futures.wait() or as_completed() with timeout
- Need to distinguish between timeout, cancellation, and normal completion

## Contraindications

- No timeout is set on the Future operation
- Future is guaranteed to complete within acceptable time
- Error classification is not needed for the use case

## Intervention Moves

- Catch TimeoutError: log timeout event, decide whether to retry, escalate, or fail gracefully
- Catch CancelledError: log cancellation event, perform cleanup, update caller state
- On normal completion: proceed with result or exception from Future

## Workflow Steps

- {'step': 1, 'action': 'Invoke Future.result(timeout=T) or wait(..., timeout=T)', 'note': 'Set timeout parameter to a positive number or None'}
- {'step': 2, 'action': 'Catch concurrent.futures.TimeoutError', 'note': 'Indicates operation exceeded timeout threshold T'}
- {'step': 3, 'action': 'Catch concurrent.futures.CancelledError', 'note': 'Indicates Future was cancelled before completion'}
- {'step': 4, 'action': 'Route to appropriate handler based on exception type', 'note': 'Timeout → retry/escalate; Cancellation → cleanup/log; Normal → proceed'}

## Constraints

- TimeoutError is a deprecated alias of built-in TimeoutError as of Python 3.11
- CancelledError is raised only if the Future was explicitly cancelled
- Exception handling must occur after the timeout-aware call (e.g., Future.result(timeout=...) or wait(..., timeout=...))

## Cautions

- Do not confuse TimeoutError with other exceptions raised by the Future's underlying work
- Cancellation and timeout are distinct outcomes; apply different recovery strategies
- Ensure timeout value is appropriate for the task; very short timeouts may cause spurious failures

## Output Contract

- Caller identifies the outcome class (timeout, cancellation, or normal completion) and applies the corresponding action. The skill guarantees classification; the caller is responsible for recovery logic.

## Example Executions

### Example 1

- Input: Call future.result(timeout=5) on a Future that does not complete within 5 seconds
- Output: concurrent.futures.TimeoutError is raised; caller catches and decides to retry or escalate
- Notes: Timeout is the primary failure mode when timeout parameter is set

### Example 2

- Input: Call future.result(timeout=10) on a Future that was cancelled via future.cancel()
- Output: concurrent.futures.CancelledError is raised; caller catches and performs cleanup
- Notes: Cancellation takes precedence; result() raises CancelledError even if timeout has not elapsed

### Example 3

- Input: Call future.result(timeout=None) on a Future that completes normally
- Output: No exception; result is returned or underlying exception is raised
- Notes: When timeout=None, no timeout occurs; only the Future's actual outcome is observed

## Triggers

- Calling Future.result(timeout=...) or waiting on Futures with timeout; need to distinguish between timeout, cancellation, and normal completion

## Examples

### Example 1

Input:

  Call future.result(timeout=5) on a Future that does not complete within 5 seconds

Output:

  concurrent.futures.TimeoutError is raised; caller catches and decides to retry or escalate

Notes:

  Timeout is the primary failure mode when timeout parameter is set

### Example 2

Input:

  Call future.result(timeout=10) on a Future that was cancelled via future.cancel()

Output:

  concurrent.futures.CancelledError is raised; caller catches and performs cleanup

Notes:

  Cancellation takes precedence; result() raises CancelledError even if timeout has not elapsed

### Example 3

Input:

  Call future.result(timeout=None) on a Future that completes normally

Output:

  No exception; result is returned or underlying exception is raised

Notes:

  When timeout=None, no timeout occurs; only the Future's actual outcome is observed
