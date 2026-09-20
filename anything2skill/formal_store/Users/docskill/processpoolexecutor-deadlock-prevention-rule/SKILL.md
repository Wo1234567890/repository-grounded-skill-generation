---
id: "20fcfee5-f751-568f-bc84-e74bdd47026d"
name: "ProcessPoolExecutor Deadlock Prevention Rule"
description: "Enforce constraint that Executor or Future methods must not be called from within callables submitted to ProcessPoolExecutor to prevent deadlock."
version: "0.1.0"
tags:
  - "deadlock_prevention"
  - "process_pool"
  - "concurrent.futures"
  - "safety_constraint"
  - "python_parallelism"
triggers:
  - "Code review of functions submitted to ProcessPoolExecutor"
  - "Design phase for parallel task decomposition using process pools"
  - "Debugging deadlock or hang in ProcessPoolExecutor workflows"
examples:
  - input: "Function submitted to ProcessPoolExecutor that calls executor.submit() internally"
    output: "Deadlock detected; refactor to remove nested executor call or use ThreadPoolExecutor"
    notes: "Nested submit() call causes worker to wait for pool lock held by main process"
  - input: "Function submitted to ProcessPoolExecutor that calls future.result() to wait for another task"
    output: "Deadlock detected; move result() call outside the callable or restructure task dependency"
    notes: "Worker process blocks on result() while main process may be waiting for this worker"
---

# ProcessPoolExecutor Deadlock Prevention Rule

Enforce constraint that Executor or Future methods must not be called from within callables submitted to ProcessPoolExecutor to prevent deadlock.

## Prompt

When designing or reviewing callable functions for ProcessPoolExecutor submission, verify that the function body does not call Executor.submit(), Future.result(), Future.cancel(), or any other Executor/Future methods. Such nested calls will cause deadlock in the worker process.

## Objective

Prevent deadlock in process pool execution
## Applicable Signals

- Function is being submitted to ProcessPoolExecutor via executor.submit() or executor.map()
- Code review or static analysis of process pool task implementations

## Contraindications

- ThreadPoolExecutor usage (lower deadlock risk due to shared memory model)
- Single-process or synchronous execution contexts
- Interactive interpreter (ProcessPoolExecutor requires importable __main__ module)

## Intervention Moves

- Scan callable function body for Executor method calls (submit, map, shutdown)
- Scan callable function body for Future method calls (result, cancel, done, exception)
- If found, refactor to move blocking calls outside the callable or use ThreadPoolExecutor instead

## Constraints

- Rule applies only to ProcessPoolExecutor, not ThreadPoolExecutor
- Constraint is architectural; violation causes hard deadlock, not graceful failure

## Cautions

- Deadlock may not manifest immediately; it occurs when worker process attempts to acquire pool lock while main process waits for worker result
- Indirect calls to Executor/Future methods (via helper functions) also trigger deadlock

## Output Contract

- Callable function submitted to ProcessPoolExecutor contains no direct or indirect calls to Executor.submit(), Executor.map(), Future.result(), Future.cancel(), Future.done(), or Future.exception(). Verification artifact: code review checklist or static analysis report confirming absence of these method calls in function body.

## Example Therapist Responses

### Example 1

- Client/Input: Function submitted to ProcessPoolExecutor that calls executor.submit() internally
- Therapist/Output: Deadlock detected; refactor to remove nested executor call or use ThreadPoolExecutor
- Notes: Nested submit() call causes worker to wait for pool lock held by main process

### Example 2

- Client/Input: Function submitted to ProcessPoolExecutor that calls future.result() to wait for another task
- Therapist/Output: Deadlock detected; move result() call outside the callable or restructure task dependency
- Notes: Worker process blocks on result() while main process may be waiting for this worker

## Triggers

- Code review of functions submitted to ProcessPoolExecutor
- Design phase for parallel task decomposition using process pools
- Debugging deadlock or hang in ProcessPoolExecutor workflows

## Examples

### Example 1

Input:

  Function submitted to ProcessPoolExecutor that calls executor.submit() internally

Output:

  Deadlock detected; refactor to remove nested executor call or use ThreadPoolExecutor

Notes:

  Nested submit() call causes worker to wait for pool lock held by main process

### Example 2

Input:

  Function submitted to ProcessPoolExecutor that calls future.result() to wait for another task

Output:

  Deadlock detected; move result() call outside the callable or restructure task dependency

Notes:

  Worker process blocks on result() while main process may be waiting for this worker
