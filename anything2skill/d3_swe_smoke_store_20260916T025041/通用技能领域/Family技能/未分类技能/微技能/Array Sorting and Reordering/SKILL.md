---
id: "9ce9edca-fca6-5daf-99a1-d159c581e06a"
name: "Array Sorting and Reordering"
description: "Reusable micro-operations for sorting, permuting, and shuffling arrays of values using natural order comparisons, index-based reordering, or randomization."
version: "0.1.0"
tags:
  - "array_manipulation"
  - "sorting"
  - "permutation"
  - "randomization"
  - "data_preparation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to sort values in natural ascending or descending order"
  - "Need to reorder array elements according to an index list"
  - "Need to reverse array element sequence"
  - "Need to randomize array element order"
examples:
  - input: "Array [3, 1, 4, 1, 5]; operation: ascending"
    output: "[1, 1, 3, 4, 5]"
    notes: "Natural ascending order applied"
  - input: "Array [10, 20, 30]; index list [2, 0, 1]; operation: permute"
    output: "[30, 10, 20]"
    notes: "Elements reordered according to index positions"
  - input: "Array [1, 2, 3, 4]; operation: shuffle"
    output: "[3, 1, 4, 2] (or any random permutation)"
    notes: "Element order randomized"
---

# Array Sorting and Reordering

Reusable micro-operations for sorting, permuting, and shuffling arrays of values using natural order comparisons, index-based reordering, or randomization.

## Prompt

Use this skill to transform array element order. Choose the operation based on your goal: ascending/descending for natural order sorting, permute for index-based reordering, reverse for order inversion, or shuffle for randomization. Input must be an iterable; output is the transformed array.

## Objective

Sort or reorder array elements
## Applicable Signals

- Array or iterable input available
- Natural order comparison applicable
- Index-based reordering required
- Randomization or reversal needed

## Contraindications

- Do not use for non-array data structures (e.g., objects, maps without iteration support)
- Do not use for statistical aggregation or summarization tasks
- Do not use when domain-specific sort criteria beyond natural order are required
- Do not use for sorting with custom comparators not based on natural order

## Intervention Moves

- ascending: compute natural order of two values
- descending: compute reverse natural order of two values
- permute: reorder iterable elements according to index list
- quickselect: reorder array of numbers by selection criterion
- reverse: invert element sequence
- shuffle: randomize element order

## Workflow Steps

- {'step': 1, 'action': 'Identify transformation goal', 'detail': 'Determine whether you need sorting (ascending/descending), reordering (permute), reversal, or randomization (shuffle)'}
- {'step': 2, 'action': 'Prepare input', 'detail': 'Ensure input is an iterable array or array-like structure with comparable elements'}
- {'step': 3, 'action': 'Select operation', 'detail': 'Choose ascending, descending, permute, reverse, or shuffle based on goal'}
- {'step': 4, 'action': 'Execute transformation', 'detail': 'Apply selected operation to input array'}
- {'step': 5, 'action': 'Verify output', 'detail': 'Confirm output array matches expected order or randomization state'}

## Constraints

- Input must be an iterable or array-like structure
- Natural order comparison assumes comparable values
- Permute operation requires index list length matching or subset of array length
- Shuffle operations modify element order; original sequence is not preserved unless explicitly copied

## Cautions

- Shuffle and reverse operations are destructive; preserve original array if needed
- quickselect may partially reorder array; use only when partial ordering is acceptable
- Large arrays may have performance implications; consider algorithm complexity for scale

## Output Contract

- Returns transformed array in the requested order: sorted (ascending or descending), permuted by index list, reversed, or shuffled. Output is an iterable in the new sequence; original array state depends on operation (some are in-place, others return new array).

## Example Therapist Responses

### Example 1

- Client/Input: Array [3, 1, 4, 1, 5]; operation: ascending
- Therapist/Output: [1, 1, 3, 4, 5]
- Notes: Natural ascending order applied

### Example 2

- Client/Input: Array [10, 20, 30]; index list [2, 0, 1]; operation: permute
- Therapist/Output: [30, 10, 20]
- Notes: Elements reordered according to index positions

### Example 3

- Client/Input: Array [1, 2, 3, 4]; operation: shuffle
- Therapist/Output: [3, 1, 4, 2] (or any random permutation)
- Notes: Element order randomized

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to sort values in natural ascending or descending order
- Need to reorder array elements according to an index list
- Need to reverse array element sequence
- Need to randomize array element order

## Examples

### Example 1

Input:

  Array [3, 1, 4, 1, 5]; operation: ascending

Output:

  [1, 1, 3, 4, 5]

Notes:

  Natural ascending order applied

### Example 2

Input:

  Array [10, 20, 30]; index list [2, 0, 1]; operation: permute

Output:

  [30, 10, 20]

Notes:

  Elements reordered according to index positions

### Example 3

Input:

  Array [1, 2, 3, 4]; operation: shuffle

Output:

  [3, 1, 4, 2] (or any random permutation)

Notes:

  Element order randomized
