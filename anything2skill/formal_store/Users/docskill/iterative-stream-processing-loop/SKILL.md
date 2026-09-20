---
id: "28a7cdfa-a20c-5cb7-9b25-6e229b1ad87d"
name: "Iterative Stream Processing Loop"
description: "Constructs and executes a feedback loop within a DataStream where elements are repeatedly transformed until a termination condition is met, then splits output into continuation and exit paths."
version: "0.1.0"
tags:
  - "stream_iteration"
  - "loop_control"
  - "datastream_api"
  - "feedback_loop"
  - "conditional_termination"
triggers:
  - "Need to apply repeated transformations to stream elements until a stopping condition is met"
  - "Implementing recursive computations or fixed-point algorithms on streaming data"
  - "Elements must be processed multiple times with conditional feedback"
examples:
  - input: "DataStream of integers [5, 3, 8]"
    output: "After subtracting 1 repeatedly until value ≤ 0: exit stream contains [0, 0, 0] (or final non-positive values); continuation stream is empty (no values > 0 remain)"
    notes: "Demonstrates fixed-point iteration: each element is decremented until it reaches zero, then exits"
---

# Iterative Stream Processing Loop

Constructs and executes a feedback loop within a DataStream where elements are repeatedly transformed until a termination condition is met, then splits output into continuation and exit paths.

## Prompt

1. Call `.iterate()` on the input DataStream to create an IterativeStream.
2. Define the loop body by applying transformations (e.g., `map()`) to the IterativeStream.
3. Split the transformed stream into two parts using filters: one that continues the loop (fed back via `closeWith()`), one that exits.
4. Call `iteration.closeWith(continuationStream)` to close the loop and specify the feedback path.
5. Extract the exit stream from the loop body to obtain the final output.
6. Both streams are now available for downstream processing.

## Objective

Set up and manage iterative data transformations with conditional loop closure
## Applicable Signals

- Repeated transformation requirement detected
- Conditional termination logic needed
- Feedback path required for loop continuation

## Contraindications

- Processing unbounded streams without a clear termination criterion
- Handling one-pass transformations that do not require feedback
- When loop overhead outweighs computational benefit
- Scenarios where elements should not be reprocessed

## Intervention Moves

- Invoke `.iterate()` to establish loop context
- Apply transformation logic within loop body
- Use filter to partition stream into continuation and exit branches
- Call `.closeWith()` to bind feedback path

## Workflow Steps

- {'step': 1, 'action': 'Create IterativeStream', 'detail': 'Call `input.iterate()` to obtain an IterativeStream object'}
- {'step': 2, 'action': 'Define loop body', 'detail': 'Apply transformations (map, filter, etc.) to the IterativeStream'}
- {'step': 3, 'action': 'Partition output', 'detail': 'Use filter to split transformed stream into continuation branch (fed back) and exit branch'}
- {'step': 4, 'action': 'Close loop', 'detail': 'Call `iteration.closeWith(continuationBranch)` to establish feedback path'}
- {'step': 5, 'action': 'Extract final output', 'detail': 'Obtain exit branch from loop body for downstream processing'}

## Constraints

- Loop body must be defined before calling `closeWith()`
- Exactly one stream must be passed to `closeWith()` for feedback
- Exit stream must be extracted from the loop body, not from the original input
- Termination condition must be expressible as a filter predicate

## Cautions

- Ensure termination condition is reachable; infinite loops will block execution
- Loop overhead may be significant for high-throughput streams; validate performance impact
- Both continuation and exit branches must be explicitly defined to avoid data loss

## Output Contract

- Two output DataStreams: (1) continuation stream fed back into the loop via `closeWith()`, (2) exit stream containing elements that satisfy the termination condition and exit the loop. Both streams are available for independent downstream operations.

## Example Therapist Responses

### Example 1

- Client/Input: DataStream of integers [5, 3, 8]
- Therapist/Output: After subtracting 1 repeatedly until value ≤ 0: exit stream contains [0, 0, 0] (or final non-positive values); continuation stream is empty (no values > 0 remain)
- Notes: Demonstrates fixed-point iteration: each element is decremented until it reaches zero, then exits

## Triggers

- Need to apply repeated transformations to stream elements until a stopping condition is met
- Implementing recursive computations or fixed-point algorithms on streaming data
- Elements must be processed multiple times with conditional feedback

## Examples

### Example 1

Input:

  DataStream of integers [5, 3, 8]

Output:

  After subtracting 1 repeatedly until value ≤ 0: exit stream contains [0, 0, 0] (or final non-positive values); continuation stream is empty (no values > 0 remain)

Notes:

  Demonstrates fixed-point iteration: each element is decremented until it reaches zero, then exits
