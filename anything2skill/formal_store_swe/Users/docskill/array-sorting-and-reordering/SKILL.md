---
id: "9ce9edca-fca6-5daf-99a1-d159c581e06a"
name: "Array Sorting and Reordering"
description: "Reusable micro-operations for sorting, permuting, and shuffling arrays of values using natural order comparisons, index-based reordering, or randomization."
version: "0.1.0"
tags:
  - "array_manipulation"
  - "sorting"
  - "permutation"
  - "data_preparation"
triggers:
  - "Need to sort values in natural ascending or descending order"
  - "Need to reorder array elements according to an index list"
  - "Need to reverse array element sequence"
  - "Need to randomize array element order"
examples:
  - input: "Array: [3, 1, 4, 1, 5]; Operation: ascending"
    output: "[1, 1, 3, 4, 5]"
    notes: "Natural ascending order sort"
  - input: "Array: [3, 1, 4, 1, 5]; Indexes: [4, 3, 2, 1, 0]; Operation: permute"
    output: "[5, 1, 4, 1, 3]"
    notes: "Reorder by index list"
  - input: "Array: [1, 2, 3, 4, 5]; Operation: shuffle"
    output: "[3, 1, 5, 2, 4] (or other random permutation)"
    notes: "Randomized order; result varies per invocation"
---

# Array Sorting and Reordering

Reusable micro-operations for sorting, permuting, and shuffling arrays of values using natural order comparisons, index-based reordering, or randomization.

## Prompt

Use this skill to transform array element order. Choose the operation based on your goal: ascending/descending for natural order sorting, permute for index-based reordering, reverse for order inversion, or shuffle for randomization. Input arrays and optional index lists; output is the transformed array.

## Objective

Sort or reorder array elements
## Applicable Signals

- Input is an array or iterable of values
- Caller needs deterministic or randomized reordering
- Natural order comparison is sufficient (no custom comparator required)

## Contraindications

- Do not use for non-array data structures (e.g., objects, maps without conversion)
- Do not use for statistical aggregation or summarization tasks
- Do not use when custom sort criteria beyond natural order are required
- Do not use for domain-specific ordering (e.g., topological sort, priority-based sort)

## Intervention Moves

- ascending: compute natural order of two values and sort accordingly
- descending: compute reverse natural order of two values and sort accordingly
- permute: reorder iterable elements according to an iterable of indexes
- quickselect: reorder array of numbers (partial sort optimization)
- reverse: invert the order of values in array
- shuffle: randomize the order of iterable elements

## Constraints

- Input must be an array or iterable
- Natural order comparison must be applicable to input values
- Index list for permute must be valid (within array bounds)
- Shuffle operations produce non-deterministic output

## Cautions

- Shuffle and randomization operations are non-deterministic; use seeded randomization if reproducibility is required
- quickselect modifies array in-place; preserve original if needed
- Large arrays may have performance implications; consider algorithm complexity for your use case

## Output Contract

- Returns a sorted, permuted, reversed, or shuffled array in the requested order or randomized state. Output is an array of the same element type as input.

## Example Executions

### Example 1

- Input: Array: [3, 1, 4, 1, 5]; Operation: ascending
- Output: [1, 1, 3, 4, 5]
- Notes: Natural ascending order sort

### Example 2

- Input: Array: [3, 1, 4, 1, 5]; Indexes: [4, 3, 2, 1, 0]; Operation: permute
- Output: [5, 1, 4, 1, 3]
- Notes: Reorder by index list

### Example 3

- Input: Array: [1, 2, 3, 4, 5]; Operation: shuffle
- Output: [3, 1, 5, 2, 4] (or other random permutation)
- Notes: Randomized order; result varies per invocation

## Triggers

- Need to sort values in natural ascending or descending order
- Need to reorder array elements according to an index list
- Need to reverse array element sequence
- Need to randomize array element order

## Examples

### Example 1

Input:

  Array: [3, 1, 4, 1, 5]; Operation: ascending

Output:

  [1, 1, 3, 4, 5]

Notes:

  Natural ascending order sort

### Example 2

Input:

  Array: [3, 1, 4, 1, 5]; Indexes: [4, 3, 2, 1, 0]; Operation: permute

Output:

  [5, 1, 4, 1, 3]

Notes:

  Reorder by index list

### Example 3

Input:

  Array: [1, 2, 3, 4, 5]; Operation: shuffle

Output:

  [3, 1, 5, 2, 4] (or other random permutation)

Notes:

  Randomized order; result varies per invocation
