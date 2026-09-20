---
id: "3d368414-e8d6-5c86-809b-74c68ac3c3c6"
name: "Executor Lifecycle Management"
description: "Signal executor to release resources after pending futures complete, optionally cancelling unstarted futures. Prevents new submissions after shutdown."
version: "0.1.0"
tags:
  - "executor"
  - "concurrent.futures"
  - "resource_management"
  - "cleanup"
  - "thread_pool"
  - "process_pool"
triggers:
  - "Executor work is complete"
  - "Context manager is exiting"
  - "Need to free thread or process pool resources"
  - "Optionally cancel pending tasks before shutdown"
examples:
  - input: "ThreadPoolExecutor with pending futures; work is complete"
    output: "executor.shutdown(wait=True) blocks until all futures finish, then releases thread pool resources"
    notes: "Typical cleanup pattern when exiting a context or finishing batch processing"
  - input: "ProcessPoolExecutor with unstarted futures; need to abandon pending work"
    output: "executor.shutdown(wait=False, cancel_futures=True) cancels unstarted futures and returns immediately"
    notes: "Use when time-sensitive or when pending work is no longer needed"
---

# Executor Lifecycle Management

Signal executor to release resources after pending futures complete, optionally cancelling unstarted futures. Prevents new submissions after shutdown.

## Prompt

Call shutdown() on the executor when work is complete or the context manager is exiting. Set wait=True to block until pending futures finish; set cancel_futures=True to cancel unstarted tasks. After shutdown, any submit() or map() calls will raise RuntimeError.

## Objective

Cleanly shut down executor and manage resource release
## Applicable Signals

- All submitted tasks have been processed
- No new tasks will be submitted
- Resource cleanup is required

## Contraindications

- Executor already shut down
- Futures are actively running and must not be cancelled
- New tasks need to be submitted (shutdown blocks new submissions)

## Workflow Steps

- {'step': 1, 'action': 'Determine shutdown parameters', 'detail': 'Decide whether to wait for pending futures (wait=True/False) and whether to cancel unstarted futures (cancel_futures=True/False)'}
- {'step': 2, 'action': 'Call executor.shutdown()', 'detail': 'Invoke shutdown(wait=True, cancel_futures=False) or with appropriate parameter values'}
- {'step': 3, 'action': 'Verify no new submissions', 'detail': 'Ensure no code attempts to call submit() or map() after shutdown; such calls will raise RuntimeError'}

## Constraints

- shutdown() must be called on a concrete Executor subclass (ThreadPoolExecutor or ProcessPoolExecutor), not the abstract Executor class
- After shutdown is called, submit() and map() will raise RuntimeError
- If cancel_futures=True, only unstarted futures are cancelled; running or completed futures are unaffected

## Cautions

- Setting wait=False will return immediately without waiting for pending futures to complete
- Setting cancel_futures=True may discard work; use only when safe to abandon pending tasks

## Output Contract

- Executor resources are freed; pending futures are completed (if wait=True) or allowed to finish asynchronously (if wait=False); unstarted futures are cancelled (if cancel_futures=True); any post-shutdown submit() or map() calls raise RuntimeError

## Example Executions

### Example 1

- Input: ThreadPoolExecutor with pending futures; work is complete
- Output: executor.shutdown(wait=True) blocks until all futures finish, then releases thread pool resources
- Notes: Typical cleanup pattern when exiting a context or finishing batch processing

### Example 2

- Input: ProcessPoolExecutor with unstarted futures; need to abandon pending work
- Output: executor.shutdown(wait=False, cancel_futures=True) cancels unstarted futures and returns immediately
- Notes: Use when time-sensitive or when pending work is no longer needed

## Triggers

- Executor work is complete
- Context manager is exiting
- Need to free thread or process pool resources
- Optionally cancel pending tasks before shutdown

## Examples

### Example 1

Input:

  ThreadPoolExecutor with pending futures; work is complete

Output:

  executor.shutdown(wait=True) blocks until all futures finish, then releases thread pool resources

Notes:

  Typical cleanup pattern when exiting a context or finishing batch processing

### Example 2

Input:

  ProcessPoolExecutor with unstarted futures; need to abandon pending work

Output:

  executor.shutdown(wait=False, cancel_futures=True) cancels unstarted futures and returns immediately

Notes:

  Use when time-sensitive or when pending work is no longer needed
