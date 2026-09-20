---
id: "5dd1b2bc-7f4e-5620-b497-1d40d196e251"
name: "Future Exception Inspection with Timeout"
description: "Inspect the exception raised by an asynchronous task without blocking indefinitely. Returns None if the task completed successfully, or raises TimeoutError if the exception is not available within the timeout window."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "Future"
  - "exception_handling"
  - "async_task"
  - "timeout"
  - "error_inspection"
triggers:
  - "Caller needs to determine whether a parallel task raised an exception and must inspect it without re-raising, or must enforce a maximum wait time."
examples:
  - input: "future.exception(timeout=5)"
    output: "Returns exception object if task raised; None if task succeeded; raises TimeoutError if 5 seconds elapsed"
    notes: "Typical use case: check for errors in a background task with a bounded wait"
  - input: "future.exception(timeout=None)"
    output: "Blocks until task completes, then returns exception or None"
    notes: "Use only when indefinite blocking is acceptable"
---

# Future Exception Inspection with Timeout

Inspect the exception raised by an asynchronous task without blocking indefinitely. Returns None if the task completed successfully, or raises TimeoutError if the exception is not available within the timeout window.

## Prompt

Call future.exception(timeout=T) to retrieve the exception object from a completed task. If timeout is None, wait indefinitely. If timeout is a positive number (int or float), wait up to that many seconds. Returns None if the task completed without raising an exception. Raises TimeoutError if the timeout expires before the task completes. Raises CancelledError if the future was cancelled before completion.

## Objective

Safely retrieve exception state from a completed or failed task for error handling and logging
## Applicable Signals

- Caller needs to determine whether a parallel task raised an exception
- Exception must be inspected without re-raising it
- A maximum wait time must be enforced before giving up on exception retrieval

## Contraindications

- The future has not been submitted to an executor
- The caller wants to propagate the exception immediately to the caller
- Synchronous blocking is unacceptable in the execution context

## Workflow Steps

- Obtain a Future object from an Executor (e.g., ThreadPoolExecutor or ProcessPoolExecutor)
- Call future.exception(timeout=T) where T is None or a numeric timeout in seconds
- Handle the return value: None indicates successful completion, or catch TimeoutError/CancelledError

## Constraints

- timeout parameter must be None, int, or float
- timeout must be non-negative if specified
- The future must have been created by an Executor

## Cautions

- If timeout is None, the call will block indefinitely until the task completes
- If the future was cancelled, CancelledError is raised regardless of timeout
- Exceptions raised by the task are returned as objects, not re-raised

## Output Contract

- Returns the exception object if the task raised an exception; returns None if the task completed without raising; raises TimeoutError if timeout expires before completion; raises CancelledError if the future was cancelled.

## Example Therapist Responses

### Example 1

- Client/Input: future.exception(timeout=5)
- Therapist/Output: Returns exception object if task raised; None if task succeeded; raises TimeoutError if 5 seconds elapsed
- Notes: Typical use case: check for errors in a background task with a bounded wait

### Example 2

- Client/Input: future.exception(timeout=None)
- Therapist/Output: Blocks until task completes, then returns exception or None
- Notes: Use only when indefinite blocking is acceptable

## Triggers

- Caller needs to determine whether a parallel task raised an exception and must inspect it without re-raising, or must enforce a maximum wait time.

## Examples

### Example 1

Input:

  future.exception(timeout=5)

Output:

  Returns exception object if task raised; None if task succeeded; raises TimeoutError if 5 seconds elapsed

Notes:

  Typical use case: check for errors in a background task with a bounded wait

### Example 2

Input:

  future.exception(timeout=None)

Output:

  Blocks until task completes, then returns exception or None

Notes:

  Use only when indefinite blocking is acceptable
