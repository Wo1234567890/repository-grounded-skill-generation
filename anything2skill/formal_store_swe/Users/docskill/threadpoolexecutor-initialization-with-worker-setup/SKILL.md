---
id: "5599899d-93fe-5947-af9f-b0d9a014440f"
name: "ThreadPoolExecutor Initialization with Worker Setup"
description: "Configure ThreadPoolExecutor with initializer and initargs to run setup code once per worker thread at startup. Handles resource allocation, logging, or thread-local state initialization with exception safety."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "ThreadPoolExecutor"
  - "worker_setup"
  - "initialization"
  - "thread_safety"
  - "resource_allocation"
triggers:
  - "Each worker thread requires shared state setup before executing tasks"
  - "Need to allocate per-thread resources (database connections, caches, handlers)"
  - "Logging or instrumentation must be initialized per worker"
examples:
  - input: "initializer=setup_db, initargs=('connection_string',), max_workers=4"
    output: "Each of 4 worker threads calls setup_db('connection_string') once at startup; workers then execute submitted tasks with initialized state"
    notes: "Typical use case for database connection pooling per worker"
  - input: "initializer raises ValueError during startup"
    output: "All pending jobs raise BrokenThreadPool; executor.submit() rejects new submissions"
    notes: "Failure mode: initialization exception propagates to all jobs"
---

# ThreadPoolExecutor Initialization with Worker Setup

Configure ThreadPoolExecutor with initializer and initargs to run setup code once per worker thread at startup. Handles resource allocation, logging, or thread-local state initialization with exception safety.

## Prompt

Pass an initializer callable and initargs tuple to ThreadPoolExecutor constructor. The initializer runs once at the start of each worker thread before any tasks execute. If initializer raises an exception, all pending jobs will raise BrokenThreadPool and further submissions are rejected.

## Objective

Initialize worker thread state and resources before task execution
## Applicable Signals

- Executor creation with max_workers > 1
- Tasks depend on thread-local state or resources
- Setup cost is amortized across many tasks

## Contraindications

- No per-worker setup needed
- Initialization is task-specific rather than thread-specific
- Setup must vary per task (use task wrapper instead)

## Workflow Steps

- Define initializer callable with signature matching initargs
- Create ThreadPoolExecutor with initializer and initargs parameters
- Submit tasks; initializer runs once per worker before first task
- Handle BrokenThreadPool exception if initializer fails

## Constraints

- Initializer must be callable and accept only initargs
- initargs must be a tuple of arguments to pass to initializer
- Initializer exception blocks all pending and future submissions

## Cautions

- If initializer raises an exception, all currently pending jobs raise BrokenThreadPool
- Any attempt to submit more jobs after initializer failure is rejected
- Initializer runs in worker thread context; use thread-safe operations only

## Output Contract

- Initializer callable executes exactly once per worker thread at startup. On success, worker is ready for task execution. On failure, all pending jobs raise BrokenThreadPool and executor rejects further submissions.

## Example Executions

### Example 1

- Input: initializer=setup_db, initargs=('connection_string',), max_workers=4
- Output: Each of 4 worker threads calls setup_db('connection_string') once at startup; workers then execute submitted tasks with initialized state
- Notes: Typical use case for database connection pooling per worker

### Example 2

- Input: initializer raises ValueError during startup
- Output: All pending jobs raise BrokenThreadPool; executor.submit() rejects new submissions
- Notes: Failure mode: initialization exception propagates to all jobs

## Triggers

- Each worker thread requires shared state setup before executing tasks
- Need to allocate per-thread resources (database connections, caches, handlers)
- Logging or instrumentation must be initialized per worker

## Examples

### Example 1

Input:

  initializer=setup_db, initargs=('connection_string',), max_workers=4

Output:

  Each of 4 worker threads calls setup_db('connection_string') once at startup; workers then execute submitted tasks with initialized state

Notes:

  Typical use case for database connection pooling per worker

### Example 2

Input:

  initializer raises ValueError during startup

Output:

  All pending jobs raise BrokenThreadPool; executor.submit() rejects new submissions

Notes:

  Failure mode: initialization exception propagates to all jobs
