---
id: "9533f43e-b370-52fc-97e8-f364f1d5fe6a"
name: "Detect and Avoid ThreadPoolExecutor Deadlock"
description: "Identify and prevent deadlock scenarios in ThreadPoolExecutor where a task waits on another task's result within the same pool, or a single-worker pool task submits and waits on a child task."
version: "0.1.0"
tags:
  - "concurrency"
  - "thread_pool"
  - "deadlock_prevention"
  - "task_design"
  - "safety_guardrail"
triggers:
  - "Designing task callables that may call .result() on other futures"
  - "Submitting tasks to a pool with limited workers"
examples:
  - input: "Task callable that calls .result() on another future in the same pool"
    output: "Deadlock detected; refactor to avoid inter-task result waits or use separate executors"
    notes: "Example: wait_on_b() calls b.result() while b is waiting on a.result() in the same 2-worker pool"
  - input: "Single-worker pool submitting a task that internally submits and waits on a child task"
    output: "Deadlock detected; increase max_workers or restructure task hierarchy"
    notes: "Example: max_workers=1 executor submitting wait_on_future() which calls executor.submit(pow, 5, 2).result()"
---

# Detect and Avoid ThreadPoolExecutor Deadlock

Identify and prevent deadlock scenarios in ThreadPoolExecutor where a task waits on another task's result within the same pool, or a single-worker pool task submits and waits on a child task.

## Prompt

Review task callables before submission to ThreadPoolExecutor. Check for any calls to .result() on futures within the callable body. Ensure that if a task waits on another future, sufficient worker threads exist to execute both tasks concurrently. For single-worker pools, never submit a task that internally submits and waits on a child task.

## Objective

Prevent task interdependency deadlocks in thread pool execution
## Applicable Signals

- Designing task callables that may call .result() on other futures
- Submitting tasks to a pool with limited workers
- Using ThreadPoolExecutor with max_workers < number of interdependent tasks

## Contraindications

- Tasks are guaranteed independent with no inter-task result waits
- Using separate executor instances for parent and child tasks
- Pool has sufficient workers to execute all potentially concurrent tasks

## Intervention Moves

- Refactor task callables to eliminate inter-task result waits
- Use separate executor instances for parent and child tasks
- Increase max_workers to accommodate all potentially concurrent tasks
- Restructure task hierarchy to avoid nested submissions with waits

## Workflow Steps

- Inspect task callable source code for .result() calls on futures
- Identify all futures that a given task may wait on
- Count maximum concurrent tasks that may execute simultaneously
- Verify max_workers >= maximum concurrent task count
- For single-worker pools, confirm no task submits and waits on child tasks
- Approve task design or recommend refactoring

## Constraints

- Do not call .result() on a future within a task callable submitted to the same executor
- If a task must wait on another task's result, ensure max_workers >= 2 and account for all concurrent waits
- Single-worker pools (max_workers=1) must never submit a task that internally submits and waits on another task

## Cautions

- Deadlocks may not manifest immediately; they occur only when task scheduling causes a wait-on-wait cycle
- Circular waits between two or more tasks in the same pool will hang indefinitely
- Initializer exceptions in ThreadPoolExecutor will raise BrokenThreadPool on all pending jobs

## Output Contract

- Task design review confirms no circular waits and no result() calls within task callables
- All submitted tasks execute to completion without blocking
- Pool shutdown completes successfully

## Example Executions

### Example 1

- Input: Task callable that calls .result() on another future in the same pool
- Output: Deadlock detected; refactor to avoid inter-task result waits or use separate executors
- Notes: Example: wait_on_b() calls b.result() while b is waiting on a.result() in the same 2-worker pool

### Example 2

- Input: Single-worker pool submitting a task that internally submits and waits on a child task
- Output: Deadlock detected; increase max_workers or restructure task hierarchy
- Notes: Example: max_workers=1 executor submitting wait_on_future() which calls executor.submit(pow, 5, 2).result()

## Triggers

- Designing task callables that may call .result() on other futures
- Submitting tasks to a pool with limited workers

## Examples

### Example 1

Input:

  Task callable that calls .result() on another future in the same pool

Output:

  Deadlock detected; refactor to avoid inter-task result waits or use separate executors

Notes:

  Example: wait_on_b() calls b.result() while b is waiting on a.result() in the same 2-worker pool

### Example 2

Input:

  Single-worker pool submitting a task that internally submits and waits on a child task

Output:

  Deadlock detected; increase max_workers or restructure task hierarchy

Notes:

  Example: max_workers=1 executor submitting wait_on_future() which calls executor.submit(pow, 5, 2).result()
