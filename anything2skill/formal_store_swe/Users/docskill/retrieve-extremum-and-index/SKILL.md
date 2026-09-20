---
id: "e412b6c8-b521-58a0-b858-c4201fcb739b"
name: "Retrieve Extremum and Index"
description: "Find the minimum or maximum value in an iterable, or retrieve the index of the extremum. Use when you need to locate the smallest or largest element or its position in a dataset."
version: "0.1.0"
tags:
  - "data_analysis"
  - "lookup"
  - "extremum"
  - "d3_array"
  - "micro_operation"
triggers:
  - "Need to identify the smallest or largest element in a dataset"
  - "Require the position (index) of an extremum for downstream operations"
  - "Selecting outliers or pivot points from unsorted data"
---

# Retrieve Extremum and Index

Find the minimum or maximum value in an iterable, or retrieve the index of the extremum. Use when you need to locate the smallest or largest element or its position in a dataset.

## Prompt

Call the appropriate extremum function on your iterable: d3.min() or d3.max() to get the value, d3.minIndex() or d3.maxIndex() to get the position, d3.least() or d3.greatest() for element comparison, or d3.leastIndex() or d3.greatestIndex() for element position. Pass the iterable and optional accessor function if needed.

## Objective

Locate extremum value or its index in an iterable
## Applicable Signals

- Outlier detection workflow initiated
- Representative element selection required
- Extremum-based filtering or ranking task

## Contraindications

- Data is already sorted; use binary search instead for efficiency
- Handling streaming or unbounded data where full iteration is infeasible
- Performing range queries or multi-element lookups; use aggregate functions instead

## Workflow Steps

- Receive iterable and optional accessor function
- Select appropriate extremum function (min/max/least/greatest or their Index variants)
- Execute linear scan across iterable
- Return extremum value or index position

## Constraints

- Iterable must be non-empty to avoid undefined behavior
- Linear scan complexity; not suitable for very large datasets without preprocessing
- Accessor function (if provided) must return comparable values

## Cautions

- Index-based functions return position in original iterable; verify index validity before use
- Comparison semantics depend on data type; ensure consistent ordering for mixed-type iterables

## Output Contract

- A single numeric value representing either the extremum (min/max value) or its integer index position (minIndex/maxIndex/leastIndex/greatestIndex), suitable for direct use in downstream filtering, selection, or ranking operations.

## Triggers

- Need to identify the smallest or largest element in a dataset
- Require the position (index) of an extremum for downstream operations
- Selecting outliers or pivot points from unsorted data
