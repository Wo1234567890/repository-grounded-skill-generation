---
id: "3a7c2fc9-94f3-58e3-af8a-f9bcde8462e7"
name: "ThreadPoolExecutor Deadlock Avoidance"
description: "Detect and prevent circular wait conditions where futures block on other futures' results within the same ThreadPoolExecutor. Identifies scenarios where a limited number of worker threads can become exhausted if a submitted task calls .result() on another future in the same pool."
version: "0.1.0"
tags:
  - "concurrency"
  - "deadlock"
  - "thread_pool"
  - "futures"
  - "safety"
  - "design_review"
triggers:
  - "Designing task submission logic where one submitted task may call .result() on another future in the same pool"
examples:
  - input: "Two tasks submitted to ThreadPoolExecutor(max_workers=2): task A calls b.result(), task B calls a.result()."
    output: "Deadlock detected. Recommendation: refactor to use callbacks or submit one task to a separate executor."
    notes: "Circular dependency with insufficient workers."
  - input: "Single task submitted to ThreadPoolExecutor(max_workers=1) that calls executor.submit(pow, 5, 2).result()."
    output: "Deadlock detected. The single worker is blocked waiting for itself. Recommendation: increase max_workers or use non-blocking pattern."
    notes: "Self-blocking scenario with max_workers=1."
---

# ThreadPoolExecutor Deadlock Avoidance

Detect and prevent circular wait conditions where futures block on other futures' results within the same ThreadPoolExecutor. Identifies scenarios where a limited number of worker threads can become exhausted if a submitted task calls .result() on another future in the same pool.

## Prompt

Review task submission logic before execution. Identify any submitted callable that may invoke .result() on another future from the same executor. Check for circular dependencies: task A waiting on task B, and task B waiting on task A. Verify that the number of worker threads is sufficient for all concurrent blocking operations. If a task must wait on another future's result, ensure either (1) the dependent future is submitted to a different executor, (2) the pool has enough workers to run both tasks concurrently, or (3) the task uses a non-blocking pattern such as callbacks or chaining.

## Objective

Prevent deadlock when futures have inter-dependencies within ThreadPoolExecutor
## Applicable Signals

- Task submission logic includes .result() calls on other futures
- Multiple futures are submitted to the same ThreadPoolExecutor
- Task design involves inter-task synchronization or result polling

## Contraindications

- Tasks are independent and do not call .result() on other futures
- Using ProcessPoolExecutor (different concurrency model; deadlock risk is lower but still possible with insufficient workers)
- All futures are submitted to different executors

## Intervention Moves

- Refactor task to avoid blocking on sibling futures; use callbacks or future chaining instead
- Increase max_workers to at least the number of potentially concurrent blocking tasks
- Submit dependent tasks to a separate executor to break the circular wait
- Use non-blocking patterns such as executor.map() or future.add_done_callback()

## Constraints

- Applies only to ThreadPoolExecutor, not ProcessPoolExecutor or other executor types
- Circular dependencies must be detected at design time; runtime detection is difficult
- Increasing max_workers is a mitigation but not a complete solution if task logic is inherently circular

## Cautions

- A single worker thread executing a task that calls .result() on another future will block indefinitely if all other workers are also blocked
- With max_workers=1, any task that calls .result() on a future will deadlock
- Deadlock may not manifest immediately; it depends on task scheduling and timing

## Output Contract

- Task design review confirms no circular waits; all futures can progress without blocking on sibling futures. Documented evidence that either (1) no task calls .result() on another future, (2) dependent futures are in separate executors, or (3) max_workers is sufficient for concurrent blocking operations.

## Example Therapist Responses

### Example 1

- Client/Input: Two tasks submitted to ThreadPoolExecutor(max_workers=2): task A calls b.result(), task B calls a.result().
- Therapist/Output: Deadlock detected. Recommendation: refactor to use callbacks or submit one task to a separate executor.
- Notes: Circular dependency with insufficient workers.

### Example 2

- Client/Input: Single task submitted to ThreadPoolExecutor(max_workers=1) that calls executor.submit(pow, 5, 2).result().
- Therapist/Output: Deadlock detected. The single worker is blocked waiting for itself. Recommendation: increase max_workers or use non-blocking pattern.
- Notes: Self-blocking scenario with max_workers=1.

## Triggers

- Designing task submission logic where one submitted task may call .result() on another future in the same pool

## Examples

### Example 1

Input:

  Two tasks submitted to ThreadPoolExecutor(max_workers=2): task A calls b.result(), task B calls a.result().

Output:

  Deadlock detected. Recommendation: refactor to use callbacks or submit one task to a separate executor.

Notes:

  Circular dependency with insufficient workers.

### Example 2

Input:

  Single task submitted to ThreadPoolExecutor(max_workers=1) that calls executor.submit(pow, 5, 2).result().

Output:

  Deadlock detected. The single worker is blocked waiting for itself. Recommendation: increase max_workers or use non-blocking pattern.

Notes:

  Self-blocking scenario with max_workers=1.
