---
id: "2c74694c-d6e4-56da-8163-d8e8be22b489"
name: "Iterate Pattern for Feedback Loops"
description: "Implement feedback loops in DataStream processing by using the iterate() method to conditionally feed a subset of records back into the iteration for repeated processing until a termination condition is met."
version: "0.1.0"
tags:
  - "datastream"
  - "iteration"
  - "feedback_loop"
  - "conditional_processing"
  - "scala"
triggers:
  - "iterative refinement or repeated filtering is needed"
  - "records must be conditionally looped back based on intermediate results"
examples:
  - input: "Stream of integers: [5, 3, 8, 1]"
    output: "After iterate with decrement-and-filter: records that reach <= 0 are output; records > 0 loop back for another decrement"
    notes: "Each record iterates independently until it satisfies the termination condition (value <= 0)"
---

# Iterate Pattern for Feedback Loops

Implement feedback loops in DataStream processing by using the iterate() method to conditionally feed a subset of records back into the iteration for repeated processing until a termination condition is met.

## Prompt

Use iterate() on a DataStream to create a feedback loop. Inside the iteration block, apply transformations (map, filter, etc.) to the incoming records. Split the output into two branches: one for records that should continue iterating (feedback), and one for records that have reached the termination condition (output). The iterate() method returns a DataStream where the feedback branch is automatically looped back.

## Objective

implement_iterative_stream_processing
## Applicable Signals

- iterative refinement or repeated filtering is needed
- records must be conditionally looped back based on intermediate results
- multi-pass processing with state-dependent termination

## Contraindications

- Do not use if infinite loops are possible without proper termination logic
- Do not use if feedback condition is not well-defined or deterministic
- Avoid when the number of iterations is unbounded and termination is uncertain

## Intervention Moves

- Define the iteration block with clear input and output branches
- Apply transformations (map, filter) to refine records in each iteration
- Split output into feedback (continue iterating) and terminal (exit loop) branches
- Ensure termination condition is well-defined to prevent infinite loops

## Workflow Steps

- {'step': 1, 'action': 'Call iterate() on the source DataStream, passing a function that receives the iteration stream'}
- {'step': 2, 'action': 'Inside the iteration block, apply transformations (e.g., map to decrement values, filter to check conditions)'}
- {'step': 3, 'action': 'Split the transformed stream into two branches using filter or other selection logic'}
- {'step': 4, 'action': 'Return a tuple of (feedback_stream, output_stream) from the iteration block'}
- {'step': 5, 'action': 'The feedback_stream is automatically looped back; the output_stream is the final result'}

## Constraints

- Feedback branch must eventually reach a state where all records satisfy the termination condition
- Transformations within the iteration block must be deterministic
- The split output must cleanly separate feedback and terminal records

## Cautions

- Ensure termination logic is sound; poorly designed feedback conditions can cause performance degradation or job failure
- Monitor iteration depth and record throughput to detect unexpected looping behavior

## Output Contract

- iterate() returns a DataStream with the feedback loop established. The output contains all records that satisfied the termination condition. Records in the feedback branch are automatically re-injected into the iteration until they reach the termination condition.

## Example Therapist Responses

### Example 1

- Client/Input: Stream of integers: [5, 3, 8, 1]
- Therapist/Output: After iterate with decrement-and-filter: records that reach <= 0 are output; records > 0 loop back for another decrement
- Notes: Each record iterates independently until it satisfies the termination condition (value <= 0)

## Triggers

- iterative refinement or repeated filtering is needed
- records must be conditionally looped back based on intermediate results

## Examples

### Example 1

Input:

  Stream of integers: [5, 3, 8, 1]

Output:

  After iterate with decrement-and-filter: records that reach <= 0 are output; records > 0 loop back for another decrement

Notes:

  Each record iterates independently until it satisfies the termination condition (value <= 0)
