---
id: "bf3921a5-3c68-51d8-a37b-8ed443154762"
name: "Search sorted array by value"
description: "Quickly locate a target value in a pre-sorted array using binary search, returning insertion index or exact match position."
version: "0.1.0"
tags:
  - "binary_search"
  - "sorted_array"
  - "lookup"
  - "O(log n)"
triggers:
  - "array is sorted; need O(log n) lookup performance; searching for single or multiple values"
---

# Search sorted array by value

Quickly locate a target value in a pre-sorted array using binary search, returning insertion index or exact match position.

## Prompt

Use binary search to find a value in a sorted array. Provide the array, target value, and optional value accessor. Returns the index of an exact match or the insertion point where the value would maintain sort order.

## Objective

find value in sorted array
## Applicable Signals

- array is sorted in ascending order
- need O(log n) lookup performance
- searching for single or multiple values in array
- need insertion point for maintaining sort order

## Contraindications

- array is unsorted or partially sorted
- linear search performance is acceptable
- array is very small (fewer than 10 elements)
- frequent array mutations between searches

## Workflow Steps

- Accept sorted array, target value, and optional value accessor function
- Apply binary search algorithm to locate target or insertion point
- Return index of exact match or insertion index

## Constraints

- input array must be sorted before invocation
- value accessor must be consistent with sort order
- comparison function must match the sort criteria used

## Cautions

- verify array is sorted; unsorted input produces incorrect results
- if using custom value accessor, ensure it matches the sort key

## Output Contract

- Returns integer index: exact match position if value exists in array, or insertion point (0 to array.length) where value would be inserted to maintain sort order.

## Triggers

- array is sorted; need O(log n) lookup performance; searching for single or multiple values
