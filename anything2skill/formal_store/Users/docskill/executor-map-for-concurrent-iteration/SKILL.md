---
id: "7e395db8-c585-5606-af32-0046c573bbc4"
name: "Executor Map for Concurrent Iteration"
description: "Apply a function to multiple iterables concurrently using Executor.map(), with optional timeout and chunksize control. Returns results in order, with timeout and exception handling."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "parallel_execution"
  - "executor"
  - "map"
  - "timeout"
  - "batch_processing"
triggers:
  - "Multiple items need processing with the same function"
  - "Results must be collected in the same order as input iterables"
  - "Timeout protection is required for result retrieval"
examples:
  - input: "executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5, chunksize=2)"
    output: "Iterator yielding [1024, 3486784401, 1099511627776] in order"
    notes: "Three concurrent pow() calls with 5-second timeout per result; chunksize=2 batches items"
---

# Executor Map for Concurrent Iteration

Apply a function to multiple iterables concurrently using Executor.map(), with optional timeout and chunksize control. Returns results in order, with timeout and exception handling.

## Prompt

Use Executor.map(fn, *iterables, timeout=None, chunksize=1) to execute fn asynchronously over multiple iterables. Results are collected immediately and returned in order. Set timeout to limit wait time per result; set chunksize to batch items for processing. Handle TimeoutError if a result is not available within the timeout window. Any exception raised by fn will be re-raised when that result is retrieved from the iterator.

## Objective

Execute a function over multiple iterables concurrently and retrieve results in order with timeout and exception handling
## Applicable Signals

- Batch processing workload
- Concurrent execution desired
- Ordered result collection required

## Contraindications

- Lazy evaluation is required (use iterator without immediate collection)
- Results must be processed as they complete rather than in order (use as_completed instead)
- Fine-grained per-item exception handling is needed

## Workflow Steps

- Create or obtain an Executor instance (ThreadPoolExecutor or ProcessPoolExecutor)
- Call executor.map(fn, *iterables, timeout=timeout_value, chunksize=chunksize_value)
- Iterate over the returned iterator to retrieve results
- Handle TimeoutError if result is not available within timeout window
- Handle any exception raised by fn when result is retrieved
- Ensure executor is properly shut down after use

## Constraints

- Iterables are collected immediately, not lazily
- Results are returned in input order regardless of completion order
- timeout applies to the wait for each result, not the entire operation
- chunksize batches items for concurrent execution (default 1)

## Cautions

- TimeoutError is raised when __next__() is called and result is not available after timeout seconds
- Any exception from fn is re-raised when its result is retrieved, not at submission time
- Executor must not be shut down before iteration completes

## Output Contract

- Iterator that yields results in the same order as input iterables. Raises TimeoutError if __next__() is called and result is not available after timeout seconds from the original map() call. Raises any exception from fn when that result is retrieved from the iterator.

## Example Therapist Responses

### Example 1

- Client/Input: executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5, chunksize=2)
- Therapist/Output: Iterator yielding [1024, 3486784401, 1099511627776] in order
- Notes: Three concurrent pow() calls with 5-second timeout per result; chunksize=2 batches items

## Triggers

- Multiple items need processing with the same function
- Results must be collected in the same order as input iterables
- Timeout protection is required for result retrieval

## Examples

### Example 1

Input:

  executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5, chunksize=2)

Output:

  Iterator yielding [1024, 3486784401, 1099511627776] in order

Notes:

  Three concurrent pow() calls with 5-second timeout per result; chunksize=2 batches items
