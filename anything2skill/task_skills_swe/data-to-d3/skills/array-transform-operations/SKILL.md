---
id: "02f13fd3-07cd-5708-a955-c8fdfb10aece"
name: "Array Transform Operations"
description: "Reusable micro-operations for deriving new arrays through Cartesian products, merging, pairing, transposition, filtering, mapping, and reduction. Use when you need to restructure or combine multiple iterables into a single derived array."
version: "0.1.0"
tags:
  - "array"
  - "transform"
  - "functional"
  - "data_preparation"
  - "iterable"
  - "restructure"
triggers:
  - "Input is one or more iterables requiring restructuring"
  - "Need to combine multiple arrays into a single output"
  - "Must derive new array with transformed or filtered elements"
---

# Array Transform Operations

Reusable micro-operations for deriving new arrays through Cartesian products, merging, pairing, transposition, filtering, mapping, and reduction. Use when you need to restructure or combine multiple iterables into a single derived array.

## Prompt

Apply one or more array transformation operations to restructure or combine input iterables. Select the operation that matches your intent: cross (Cartesian product), merge (combine multiple iterables), pairs (adjacent element pairs), transpose (flip rows/columns), zip (transpose variable arrays), filter (select elements), map (transform elements), or reduce (aggregate to single value). Execute the operation and return the new array.

## Objective

Transform and restructure iterables into derived arrays
## Applicable Signals

- Multiple iterables available for combination
- Array structure does not match downstream requirements
- Element-wise transformation or selection needed

## Contraindications

- Data is already in target structure
- Operation is not array-based
- Performance-critical context with very large datasets where lazy evaluation is required

## Workflow Steps

- Identify input iterables and their structure
- Select appropriate transformation operation (cross, merge, pairs, transpose, zip, filter, map, or reduce)
- Apply operation to input(s)
- Validate output array structure and content
- Return new array to caller

## Constraints

- Input must be iterable(s)
- Output must be a new array
- Operation must be deterministic and side-effect free

## Cautions

- Ensure input iterables are compatible with selected operation
- Verify output array dimensions and element types match expectations
- Consider memory implications for large datasets

## Output Contract

- New array with transformed, merged, paired, transposed, filtered, mapped, or reduced elements matching the operation intent. Array is ready for downstream consumption.

## Triggers

- Input is one or more iterables requiring restructuring
- Need to combine multiple arrays into a single output
- Must derive new array with transformed or filtered elements
