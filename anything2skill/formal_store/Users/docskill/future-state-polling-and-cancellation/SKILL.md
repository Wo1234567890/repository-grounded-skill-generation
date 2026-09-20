---
id: "b1c7e545-b288-5698-96f2-bd145626c8d9"
name: "Future State Polling and Cancellation"
description: "Query and manage the lifecycle state of asynchronous task execution using Future methods. Inspect whether a task is running, completed, or cancelled, and attempt early cancellation before execution begins."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "Future"
  - "task_lifecycle"
  - "cancellation"
  - "polling"
  - "async_control"
triggers:
  - "Need to check if task is running, done, or cancelled"
  - "Want to attempt early cancellation before task starts"
  - "Require task lifecycle visibility for routing decisions"
---

# Future State Polling and Cancellation

Query and manage the lifecycle state of asynchronous task execution using Future methods. Inspect whether a task is running, completed, or cancelled, and attempt early cancellation before execution begins.

## Prompt

Use Future.cancel(), cancelled(), running(), and done() methods to inspect task state and attempt cancellation. Call cancel() only before task execution starts; it returns False if the task is already running or finished. Use cancelled() to check if cancellation succeeded, running() to check if task is currently executing, and done() to check if task has completed.

## Objective

Inspect and control individual Future task state
## Applicable Signals

- Task submitted to executor but result not yet needed
- Conditional logic depends on task execution state
- Resource constraints require selective task cancellation

## Contraindications

- Task is already running (cancel() will return False)
- Task has finished (state is immutable)
- No need for task lifecycle visibility

## Intervention Moves

- Call cancel() to attempt cancellation (returns True if successful, False if already running or done)
- Call cancelled() to verify cancellation succeeded
- Call running() to check if task is currently executing
- Call done() to check if task has completed

## Workflow Steps

- {'step': 1, 'action': 'Call future.cancel() to attempt cancellation', 'condition': 'Task not yet started', 'output': 'Boolean: True if cancelled, False if already running or done'}
- {'step': 2, 'action': 'Call future.cancelled() to verify cancellation', 'condition': 'After cancel() call', 'output': 'Boolean: True if cancellation succeeded'}
- {'step': 3, 'action': 'Call future.running() to check execution status', 'condition': 'Need to know if task is currently executing', 'output': 'Boolean: True if task is running'}
- {'step': 4, 'action': 'Call future.done() to check completion', 'condition': 'Need to know if task has finished', 'output': 'Boolean: True if task completed or was cancelled'}

## Constraints

- cancel() must be called before task execution begins to succeed
- Future instances must be created by Executor.submit(); do not create directly except for testing
- State queries return boolean values; caller must interpret and route accordingly

## Cautions

- Calling cancel() on a running or finished task returns False; do not assume cancellation succeeded without checking cancelled()
- State is immutable after task completion; repeated polling after done() returns True is redundant

## Output Contract

- Boolean state returned (True/False) indicating cancellation success, running status, or completion. Caller uses returned state to make routing decision for downstream task handling.

## Triggers

- Need to check if task is running, done, or cancelled
- Want to attempt early cancellation before task starts
- Require task lifecycle visibility for routing decisions
