---
id: "053702a9-da5e-566e-80f2-9759ce838188"
name: "Compute Quantile and Rank"
description: "Calculate quantile values (percentiles) or rank order of elements in a numeric iterable. Use when you need to understand the distribution or relative ordering of data."
version: "0.1.0"
tags:
  - "data_analysis"
  - "statistics"
  - "distribution"
  - "percentile"
  - "ranking"
  - "d3-array"
triggers:
  - "Need to compute percentile thresholds from a dataset"
  - "Require rank order assignment for sorting or comparison"
  - "Analyzing data distribution to identify quartiles or deciles"
examples:
  - input: "iterable=[1, 2, 3, 4, 5], quantile=0.5"
    output: "3 (median)"
    notes: "d3.quantile or d3.median returns the 50th percentile"
  - input: "iterable=[10, 20, 30, 40], quantile=0.75"
    output: "32.5 (75th percentile)"
    notes: "d3.quantile interpolates between values"
  - input: "iterable=[5, 2, 8, 1, 9]"
    output: "[3, 2, 4, 1, 5] (rank order)"
    notes: "d3.rank assigns 1-indexed positions by ascending value"
---

# Compute Quantile and Rank

Calculate quantile values (percentiles) or rank order of elements in a numeric iterable. Use when you need to understand the distribution or relative ordering of data.

## Prompt

Given an iterable of numbers and a quantile parameter (0.0–1.0), compute the corresponding quantile value. Alternatively, compute the rank order (1-indexed position) of elements. For quantile operations, use d3.quantile for unsorted input, d3.quantileSorted for pre-sorted arrays, or d3.quantileIndex for the index. For rank operations, use d3.rank to assign rank positions. Median (0.5-quantile) is available via d3.median or d3.medianIndex.

## Objective

Determine quantile or rank position in a numeric iterable
## Applicable Signals

- Input is a numeric iterable
- Quantile parameter is in range [0.0, 1.0]
- Data is unsorted (use d3.quantile) or pre-sorted (use d3.quantileSorted)

## Contraindications

- Input contains categorical or non-numeric data
- Performing hypothesis testing or statistical inference
- Using d3.quantileSorted on unsorted data without prior sort

## Workflow Steps

- {'step': 1, 'action': 'Validate input iterable contains numeric values', 'note': 'Filter or coerce non-numeric entries if needed'}
- {'step': 2, 'action': 'Choose operation: quantile (percentile) or rank (order)', 'note': 'Quantile requires a parameter p ∈ [0.0, 1.0]; rank does not'}
- {'step': 3, 'action': 'For quantile: select d3.quantile (unsorted), d3.quantileSorted (sorted), or d3.quantileIndex (index)', 'note': 'Pre-sort if using d3.quantileSorted for performance'}
- {'step': 4, 'action': 'For rank: apply d3.rank to assign positions', 'note': 'Returns array of rank values in same order as input'}
- {'step': 5, 'action': 'Return numeric result (quantile value or rank position)', 'note': 'Quantile is a single value; rank is an array'}

## Constraints

- Quantile parameter must be a number between 0.0 and 1.0 inclusive
- Input iterable must contain valid numeric values
- For d3.quantileSorted, input array must be pre-sorted in ascending order

## Cautions

- Rank computation assumes distinct or tied values; ties are handled by average rank
- Quantile on small samples may not reflect true distribution
- Empty or single-element iterables may return undefined or edge-case values

## Output Contract

- A numeric value representing the quantile (0.0–1.0 range) or an integer rank position (1-indexed). For rank, an array of rank values matching input length.

## Example Executions

### Example 1

- Input: iterable=[1, 2, 3, 4, 5], quantile=0.5
- Output: 3 (median)
- Notes: d3.quantile or d3.median returns the 50th percentile

### Example 2

- Input: iterable=[10, 20, 30, 40], quantile=0.75
- Output: 32.5 (75th percentile)
- Notes: d3.quantile interpolates between values

### Example 3

- Input: iterable=[5, 2, 8, 1, 9]
- Output: [3, 2, 4, 1, 5] (rank order)
- Notes: d3.rank assigns 1-indexed positions by ascending value

## Triggers

- Need to compute percentile thresholds from a dataset
- Require rank order assignment for sorting or comparison
- Analyzing data distribution to identify quartiles or deciles

## Examples

### Example 1

Input:

  iterable=[1, 2, 3, 4, 5], quantile=0.5

Output:

  3 (median)

Notes:

  d3.quantile or d3.median returns the 50th percentile

### Example 2

Input:

  iterable=[10, 20, 30, 40], quantile=0.75

Output:

  32.5 (75th percentile)

Notes:

  d3.quantile interpolates between values

### Example 3

Input:

  iterable=[5, 2, 8, 1, 9]

Output:

  [3, 2, 4, 1, 5] (rank order)

Notes:

  d3.rank assigns 1-indexed positions by ascending value
