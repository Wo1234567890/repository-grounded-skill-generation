---
id: "42f8bf1d-74f2-5e93-a334-30a1b523596d"
name: "Array Transform Operations"
description: "Reusable micro-operations for deriving new arrays through Cartesian products, merging, pairing, transposition, and filtering. Use when you need to restructure or combine multiple iterables into a single derived array."
version: "0.1.0"
tags:
  - "array"
  - "transform"
  - "reshape"
  - "functional"
  - "data_preparation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Input is one or more iterables requiring restructuring"
  - "Output must be a new array with combined or reshaped elements"
  - "Caller needs Cartesian product, merge, pairing, transposition, or filtering"
---

# Array Transform Operations

Reusable micro-operations for deriving new arrays through Cartesian products, merging, pairing, transposition, and filtering. Use when you need to restructure or combine multiple iterables into a single derived array.

## Prompt

Apply one or more array transformation primitives to reshape or combine input iterables. Select the appropriate operation: d3.cross for Cartesian product, d3.merge to combine multiple iterables, d3.pairs for adjacent element pairs, d3.transpose to flip rows and columns, d3.zip for variable-length transposition, d3.filter to select elements, d3.map to apply a function, or d3.reduce to aggregate values. Return the new array with the transformed structure.

## Objective

Transform and restructure iterables into new arrays
## Applicable Signals

- Multiple arrays need to be combined into one
- Array structure must be transposed or reorganized
- Element-wise filtering or mapping is required
- Adjacent pairs or cross-product relationships are needed

## Contraindications

- Data is already in the target shape
- Operation is not array-to-array transformation
- Caller needs in-place mutation rather than new array derivation

## Workflow Steps

- {'step': 1, 'action': 'Identify the input iterables and their current structure'}
- {'step': 2, 'action': 'Select the appropriate transformation operation based on desired output shape'}
- {'step': 3, 'action': 'Apply the operation (cross, merge, pairs, transpose, zip, filter, map, or reduce)'}
- {'step': 4, 'action': 'Verify the output array has the expected structure and element count'}

## Constraints

- Input must be iterable (array, set, or similar)
- Output is always a new array; original input is not modified
- Operation completes in a single pass or standard algorithmic time

## Cautions

- Cartesian product can produce large arrays; verify input sizes
- Transposition assumes rectangular input for d3.transpose
- Filter and map operations depend on predicate or function correctness

## Output Contract

- New array with transformed structure: Cartesian product of inputs, merged elements, adjacent pairs, transposed rows/columns, filtered values, or mapped/reduced results. Caller receives a single array ready for downstream processing.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Input is one or more iterables requiring restructuring
- Output must be a new array with combined or reshaped elements
- Caller needs Cartesian product, merge, pairing, transposition, or filtering
