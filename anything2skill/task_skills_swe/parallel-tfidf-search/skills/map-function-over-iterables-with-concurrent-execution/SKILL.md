---
id: "eb76c3cc-8009-5f73-a9e4-bbd23480b58d"
name: "Map Function Over Iterables with Concurrent Execution"
description: "Apply a function to multiple iterables concurrently using an executor. Collects iterables immediately, executes the function asynchronously over input sets, and returns an iterator over results with per-result timeout and exception handling."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "batch_processing"
  - "async_execution"
  - "timeout_handling"
  - "exception_propagation"
triggers:
  - "Need to apply one function to many input sets"
  - "Want concurrent execution across multiple iterables"
  - "Require per-result timeout enforcement"
  - "Need exception propagation on result retrieval"
examples:
  - input: "executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5)"
    output: "Iterator yielding 1024, 3486784401, 1099511627776 (or TimeoutError if any result unavailable after 5 seconds)"
    notes: "Applies pow concurrently to three (base, exponent) pairs with 5-second timeout per result"
---

# Map Function Over Iterables with Concurrent Execution

Apply a function to multiple iterables concurrently using an executor. Collects iterables immediately, executes the function asynchronously over input sets, and returns an iterator over results with per-result timeout and exception handling.

## Prompt

Use executor.map(fn, *iterables, timeout=None, chunksize=1) to apply fn concurrently across multiple input sets. The iterables are collected eagerly (not lazily). Results are returned as an iterator; accessing a result via __next__() raises TimeoutError if the result is not available within the timeout window. Exceptions raised by fn calls are propagated when their results are retrieved from the iterator. The chunksize parameter (default 1) controls batching of work items.

## Objective

Execute a function over multiple input sets concurrently with timeout and exception handling per result.
## Applicable Signals

- Batch of homogeneous tasks ready for concurrent processing
- Multiple input iterables available upfront
- Timeout tolerance per result is known

## Contraindications

- Executor has been shut down
- Lazy evaluation of iterables is required
- Single callable execution needed (use submit() instead)
- Results must be collected in order without timeout per result

## Workflow Steps

- Prepare iterables and callable function
- Call executor.map(fn, *iterables, timeout=timeout, chunksize=chunksize)
- Iterate over returned iterator using __next__() or for loop
- Handle TimeoutError if result not available within timeout
- Handle exceptions raised by fn calls during result retrieval

## Constraints

- Iterables are collected immediately, not lazily
- Calls to map() after executor.shutdown() raise RuntimeError
- timeout applies per result retrieval, not to the entire map operation
- chunksize must be a positive integer

## Cautions

- TimeoutError is raised only when __next__() is called on the iterator and the result is not ready
- Exceptions from fn are raised when their results are accessed, not when fn is called
- If cancel_futures=True was used in shutdown(), pending futures may be cancelled before map() completes

## Output Contract

- Returns an iterator over results of fn applied to input sets. Iterator raises TimeoutError if __next__() is called and result is not available after timeout seconds. Exceptions from fn calls are raised when their results are retrieved from the iterator.

## Example Executions

### Example 1

- Input: executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5)
- Output: Iterator yielding 1024, 3486784401, 1099511627776 (or TimeoutError if any result unavailable after 5 seconds)
- Notes: Applies pow concurrently to three (base, exponent) pairs with 5-second timeout per result

## Triggers

- Need to apply one function to many input sets
- Want concurrent execution across multiple iterables
- Require per-result timeout enforcement
- Need exception propagation on result retrieval

## Examples

### Example 1

Input:

  executor.map(pow, [2, 3, 4], [10, 20, 30], timeout=5)

Output:

  Iterator yielding 1024, 3486784401, 1099511627776 (or TimeoutError if any result unavailable after 5 seconds)

Notes:

  Applies pow concurrently to three (base, exponent) pairs with 5-second timeout per result
