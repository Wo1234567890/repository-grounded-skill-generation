---
id: "cd376aff-27f0-551f-be8f-d2eb384c145a"
name: "ProcessPoolExecutor Initialization with Worker Setup"
description: "Initialize a ProcessPoolExecutor with optional per-worker initializer callable and arguments. Properly handle initializer exceptions that trigger BrokenProcessPool state and worker process lifecycle."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "process_pool"
  - "parallelism"
  - "cpu_bound"
  - "worker_initialization"
  - "multiprocessing"
triggers:
  - "Need to execute CPU-bound tasks that require true parallelism and GIL release"
  - "Per-worker setup required (e.g., database connections, resource allocation, state initialization)"
  - "Multiple independent tasks can run in separate processes"
examples:
  - input: "initializer=setup_worker, initargs=('db_config.json',), max_workers=4"
    output: "ProcessPoolExecutor with 4 worker processes, each having called setup_worker('db_config.json') at startup"
    notes: "Typical use case for database connection pooling per worker"
  - input: "initializer=None, max_workers=None (defaults to min(32, cpu_count + 4))"
    output: "ProcessPoolExecutor with default worker count, no per-worker initialization"
    notes: "Suitable for stateless CPU-bound tasks"
---

# ProcessPoolExecutor Initialization with Worker Setup

Initialize a ProcessPoolExecutor with optional per-worker initializer callable and arguments. Properly handle initializer exceptions that trigger BrokenProcessPool state and worker process lifecycle.

## Prompt

Create a ProcessPoolExecutor instance by specifying max_workers, mp_context, and an optional initializer callable with initargs. The initializer runs once at the start of each worker process. If the initializer raises an exception, all pending jobs will raise BrokenProcessPool and further job submissions will fail. Ensure the __main__ module is importable by worker subprocesses and avoid calling Executor or Future methods from within submitted callables to prevent deadlock.

## Objective

Set up a process pool executor with per-worker initialization and error handling for CPU-bound parallel tasks
## Applicable Signals

- CPU-bound workload identified
- Initializer setup needed for worker processes
- Main module is importable by subprocesses

## Contraindications

- Interactive interpreter context (main module not importable by worker subprocesses)
- Calling Executor or Future methods from within submitted callables (deadlock risk)
- I/O-bound tasks better suited to ThreadPoolExecutor
- Initializer that raises exceptions will break the entire pool

## Workflow Steps

- {'step': 1, 'action': 'Define initializer callable (optional) that accepts initargs', 'detail': 'This function runs once per worker process at startup'}
- {'step': 2, 'action': 'Create ProcessPoolExecutor with max_workers, mp_context, initializer, and initargs', 'detail': 'max_workers defaults to min(32, os.cpu_count() + 4); mp_context controls multiprocessing start method'}
- {'step': 3, 'action': 'Submit tasks via executor.submit() or executor.map() from main process only', 'detail': 'Do not call executor methods from within submitted callables'}
- {'step': 4, 'action': 'Handle BrokenProcessPool exception if initializer fails', 'detail': 'Catch exception and implement recovery or graceful shutdown'}
- {'step': 5, 'action': 'Use context manager (with statement) to ensure proper cleanup', 'detail': 'Ensures executor.shutdown(wait=True) is called'}

## Constraints

- The __main__ module must be importable by worker subprocesses
- Do not invoke Executor.submit(), Executor.map(), or Future methods from inside a callable submitted to ProcessPoolExecutor
- Initializer exceptions propagate as BrokenProcessPool to all pending and future jobs

## Cautions

- Initializer runs once per worker process at startup; use for one-time setup only
- If initializer fails, the pool enters broken state and cannot accept new jobs
- Ensure initargs tuple is picklable for subprocess transmission

## Output Contract

- ProcessPoolExecutor instance with worker processes initialized; initializer callable executed once per worker process with provided initargs; pool ready to accept task submissions via submit() or map(); BrokenProcessPool exception raised if initializer fails on any worker

## Example Executions

### Example 1

- Input: initializer=setup_worker, initargs=('db_config.json',), max_workers=4
- Output: ProcessPoolExecutor with 4 worker processes, each having called setup_worker('db_config.json') at startup
- Notes: Typical use case for database connection pooling per worker

### Example 2

- Input: initializer=None, max_workers=None (defaults to min(32, cpu_count + 4))
- Output: ProcessPoolExecutor with default worker count, no per-worker initialization
- Notes: Suitable for stateless CPU-bound tasks

## Triggers

- Need to execute CPU-bound tasks that require true parallelism and GIL release
- Per-worker setup required (e.g., database connections, resource allocation, state initialization)
- Multiple independent tasks can run in separate processes

## Examples

### Example 1

Input:

  initializer=setup_worker, initargs=('db_config.json',), max_workers=4

Output:

  ProcessPoolExecutor with 4 worker processes, each having called setup_worker('db_config.json') at startup

Notes:

  Typical use case for database connection pooling per worker

### Example 2

Input:

  initializer=None, max_workers=None (defaults to min(32, cpu_count + 4))

Output:

  ProcessPoolExecutor with default worker count, no per-worker initialization

Notes:

  Suitable for stateless CPU-bound tasks
