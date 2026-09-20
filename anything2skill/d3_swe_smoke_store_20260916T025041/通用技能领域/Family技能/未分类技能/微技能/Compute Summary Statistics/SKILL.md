---
id: "9c20b541-1a61-5079-a92d-22c3d99087cd"
name: "Compute Summary Statistics"
description: "Calculate aggregate statistics (count, min, max, mean, median, variance, standard deviation, mode, extent, quantile, cumsum, rank, and index variants) over an iterable of numeric values. Use when you need to derive single-value summaries or aggregate arrays from a dataset."
version: "0.1.0"
tags:
  - "aggregation"
  - "statistics"
  - "reduction"
  - "numeric"
  - "d3-array"
  - "summarize"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Caller has an iterable of numeric values"
  - "Single summary statistic is needed (not multi-step transformation)"
  - "Result should be a scalar, index value, or aggregate array"
examples:
  - input: "iterable=[1, 2, 3, 4, 5], operation='mean'"
    output: "3"
    notes: "Arithmetic mean of five integers"
  - input: "iterable=[10, 20, 15, 30, 25], operation='minIndex'"
    output: "0"
    notes: "Index of minimum value (10 at position 0)"
  - input: "iterable=[5, 5, 3, 5, 2], operation='mode'"
    output: "5"
    notes: "Most common value appears three times"
---

# Compute Summary Statistics

Calculate aggregate statistics (count, min, max, mean, median, variance, standard deviation, mode, extent, quantile, cumsum, rank, and index variants) over an iterable of numeric values. Use when you need to derive single-value summaries or aggregate arrays from a dataset.

## Prompt

Given an iterable of numbers, apply the appropriate summary statistic function to produce a single numeric result, numeric index, or aggregate array. Supported operations include: count (valid numbers), min/max (extreme values), minIndex/maxIndex (position of extremes), least/greatest (element comparison), leastIndex/greatestIndex (position of compared elements), mean/median (central tendency), variance/deviation (spread), mode (most common), extent (min and max together), quantile/quantileIndex/quantileSorted (percentile), cumsum (running total), rank (ordinal position), sum (total), and conditional tests (every, some).

## Objective

Derive aggregate numeric summaries from iterables
## Applicable Signals

- Dataset ready for reduction
- Aggregation requirement identified
- No intermediate filtering or reshaping needed

## Contraindications

- Data contains non-numeric values (use filtering or type conversion first)
- Data is already aggregated or pre-computed
- Multi-pass transformations or conditional logic required beyond reduction

## Workflow Steps

- Validate input is iterable and contains numeric values
- Select appropriate summary function (count, min, max, minIndex, maxIndex, least, leastIndex, greatest, greatestIndex, mean, median, medianIndex, variance, deviation, mode, extent, sum, quantile, quantileIndex, quantileSorted, cumsum, rank, every, or some)
- Apply function to iterable
- Return scalar result, numeric index, or aggregate array

## Constraints

- Input must be iterable
- Numeric values must be valid (null/undefined handling depends on operation)
- Single-pass reduction semantics apply
- quantileSorted requires pre-sorted input

## Cautions

- Empty iterables may return undefined or throw; check preconditions
- Index variants (minIndex, maxIndex, medianIndex, leastIndex, greatestIndex, quantileIndex) return position, not value
- Quantile operations require sorted input or explicit sort step (use quantileSorted for pre-sorted arrays)
- every and some return boolean, not numeric results

## Output Contract

- A single numeric value (e.g., mean=42.5, count=10, variance=15.3, sum=100), a numeric index (e.g., minIndex=3, maxIndex=7, medianIndex=5), a boolean (every/some), or an aggregate array (extent=[min, max], cumsum=[...], rank=[...]) representing the requested statistic.

## Example Therapist Responses

### Example 1

- Client/Input: iterable=[1, 2, 3, 4, 5], operation='mean'
- Therapist/Output: 3
- Notes: Arithmetic mean of five integers

### Example 2

- Client/Input: iterable=[10, 20, 15, 30, 25], operation='minIndex'
- Therapist/Output: 0
- Notes: Index of minimum value (10 at position 0)

### Example 3

- Client/Input: iterable=[5, 5, 3, 5, 2], operation='mode'
- Therapist/Output: 5
- Notes: Most common value appears three times

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Caller has an iterable of numeric values
- Single summary statistic is needed (not multi-step transformation)
- Result should be a scalar, index value, or aggregate array

## Examples

### Example 1

Input:

  iterable=[1, 2, 3, 4, 5], operation='mean'

Output:

  3

Notes:

  Arithmetic mean of five integers

### Example 2

Input:

  iterable=[10, 20, 15, 30, 25], operation='minIndex'

Output:

  0

Notes:

  Index of minimum value (10 at position 0)

### Example 3

Input:

  iterable=[5, 5, 3, 5, 2], operation='mode'

Output:

  5

Notes:

  Most common value appears three times
