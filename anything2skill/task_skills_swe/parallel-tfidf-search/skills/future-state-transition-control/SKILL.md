---
id: "89af0319-817d-52d3-90b9-ccb19b7a6372"
name: "Future State Transition Control"
description: "Atomically assign a Future's terminal state (result or exception) exactly once. Use this micro-operation when implementing custom Executor backends or in unit tests that need to manually resolve Future outcomes."
version: "0.1.0"
tags:
  - "futures"
  - "concurrent.futures"
  - "executor"
  - "state_mutation"
  - "python312"
triggers:
  - "Implementing Executor.submit() or testing Future resolution; need to finalize a Future's outcome exactly once"
examples:
  - input: "Custom Executor implementation needs to resolve a Future after task completion"
    output: "Call future.set_result(task_output) to mark the Future as done with the result"
    notes: "Typical use in Executor.submit() implementation"
  - input: "Unit test needs to manually set an exception on a Future"
    output: "Call future.set_exception(ValueError('test error')) to mark the Future as done with an exception"
    notes: "Typical use in testing Future exception handling"
---

# Future State Transition Control

Atomically assign a Future's terminal state (result or exception) exactly once. Use this micro-operation when implementing custom Executor backends or in unit tests that need to manually resolve Future outcomes.

## Prompt

Call either set_result(result) or set_exception(exception) on a Future object exactly once. Do not call both methods on the same Future, and do not call either method after the Future is already done. If the Future is already done, the call will raise InvalidStateError.

## Objective

Atomically assign a Future's terminal state (result or exception)
## Applicable Signals

- Implementing custom Executor.submit() or similar task submission
- Writing unit tests that manually resolve Future outcomes
- Need to finalize a Future's outcome exactly once

## Contraindications

- Future is already done (result or exception already set)
- Calling after Future.set_result() or Future.set_exception() has been invoked
- Attempting to call both set_result() and set_exception() on the same Future

## Intervention Moves

- Call set_result(result) to assign the successful outcome
- Call set_exception(exception) to assign an exception outcome
- Ensure only one of these two methods is called per Future

## Workflow Steps

- {'step': 1, 'action': 'Check that the Future is not already done', 'detail': 'Verify the Future has not had set_result() or set_exception() called previously'}
- {'step': 2, 'action': 'Choose outcome type: result or exception', 'detail': 'Determine whether the task completed successfully or raised an exception'}
- {'step': 3, 'action': 'Call set_result(result) or set_exception(exception)', 'detail': 'Invoke exactly one of these methods with the appropriate outcome'}
- {'step': 4, 'action': 'Verify Future transitions to done state', 'detail': 'Confirm the Future is now done and subsequent calls will raise InvalidStateError'}

## Constraints

- Method can only be called once per Future
- Cannot be called after the Future is already done
- Intended only for Executor implementations and unit tests

## Cautions

- Raises concurrent.futures.InvalidStateError if the Future is already done (Python 3.8+)
- Misuse can leave Futures in inconsistent states if not properly guarded

## Output Contract

- Future transitions to done state with result or exception set; subsequent calls to set_result() or set_exception() raise InvalidStateError; downstream callers can now retrieve the outcome via result() or exception()

## Example Executions

### Example 1

- Input: Custom Executor implementation needs to resolve a Future after task completion
- Output: Call future.set_result(task_output) to mark the Future as done with the result
- Notes: Typical use in Executor.submit() implementation

### Example 2

- Input: Unit test needs to manually set an exception on a Future
- Output: Call future.set_exception(ValueError('test error')) to mark the Future as done with an exception
- Notes: Typical use in testing Future exception handling

## Triggers

- Implementing Executor.submit() or testing Future resolution; need to finalize a Future's outcome exactly once

## Examples

### Example 1

Input:

  Custom Executor implementation needs to resolve a Future after task completion

Output:

  Call future.set_result(task_output) to mark the Future as done with the result

Notes:

  Typical use in Executor.submit() implementation

### Example 2

Input:

  Unit test needs to manually set an exception on a Future

Output:

  Call future.set_exception(ValueError('test error')) to mark the Future as done with an exception

Notes:

  Typical use in testing Future exception handling
