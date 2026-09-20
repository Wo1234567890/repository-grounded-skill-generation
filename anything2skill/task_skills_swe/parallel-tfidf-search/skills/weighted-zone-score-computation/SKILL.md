---
id: "8466bfb2-cbec-5b4f-b679-b4476dbf2c51"
name: "Weighted Zone Score Computation"
description: "Calculate aggregate statistics (count, min, max, mean, median, variance, standard deviation, quantiles, rank, mode, extent, cumulative sum) over an iterable of numeric values. Use when you need to derive single-value or index-based summaries from a dataset for analysis, visualization, or reporting."
version: "0.1.0"
tags:
  - "data_aggregation"
  - "statistical_computation"
  - "numeric_analysis"
  - "d3_array"
  - "summary_statistics"
triggers:
  - "document has multiple zones (title, body, abstract, etc.)"
  - "zone weights are known or learned from training data"
  - "Boolean match signals per zone are available"
examples:
  - input: "d3.mean([1, 2, 3, 4, 5])"
    output: "3"
    notes: "Arithmetic mean of five integers"
  - input: "d3.median([10, 20, 30, 40, 50])"
    output: "30"
    notes: "Median (0.5-quantile) of sorted array"
  - input: "d3.variance([2, 4, 6, 8])"
    output: "5"
    notes: "Variance measuring spread around mean"
---

# Weighted Zone Score Computation

Calculate aggregate statistics (count, min, max, mean, median, variance, standard deviation, quantiles, rank, mode, extent, cumulative sum) over an iterable of numeric values. Use when you need to derive single-value or index-based summaries from a dataset for analysis, visualization, or reporting.

## Prompt

Select the appropriate summary statistic function based on your data and analysis goal. Pass a numeric iterable (array or similar) to the chosen function. For index-based results (minIndex, maxIndex, leastIndex, greatestIndex, medianIndex, quantileIndex), the function returns the position; for value-based results (min, max, mean, median, variance, deviation, sum, mode, extent, quantile, rank, cumsum), it returns the computed value. Handle empty iterables gracefully—most functions return undefined or null in such cases.

## Objective

Derive summary statistics from numeric iterables
## Applicable Signals

- Need to compute descriptive statistics on numeric arrays
- Preparing data for visualization or reporting
- Extracting single-value summaries from datasets
- Analyzing distribution properties (mean, median, variance, quantiles)

## Contraindications

- Do not use for non-numeric data (strings, objects, mixed types)
- Do not use for hypothesis testing or inferential statistics
- Do not use for streaming data requiring incremental updates without recomputation
- Do not use when you need multi-dimensional or grouped statistics without preprocessing

## Intervention Moves

- Call d3.count to count valid numeric values
- Call d3.min or d3.minIndex to find minimum value or its position
- Call d3.max or d3.maxIndex to find maximum value or its position
- Call d3.mean to compute arithmetic mean
- Call d3.median or d3.medianIndex to find median or its position
- Call d3.variance or d3.deviation to measure spread
- Call d3.sum to compute total
- Call d3.mode to find most common value
- Call d3.extent to get min and max together
- Call d3.quantile or d3.quantileIndex for custom quantiles
- Call d3.rank to compute rank order
- Call d3.cumsum to compute cumulative sum

## Workflow Steps

- {'step': 1, 'action': 'Validate input iterable contains numeric values', 'notes': 'Filter or preprocess if needed'}
- {'step': 2, 'action': 'Select the appropriate summary statistic function based on analysis goal', 'notes': 'Choose from count, min, max, mean, median, variance, deviation, sum, mode, extent, quantile, rank, cumsum, or index variants'}
- {'step': 3, 'action': 'Call the selected d3 function with the iterable and any required parameters', 'notes': 'For quantile functions, provide the quantile value (0–1); for rank, provide the iterable'}
- {'step': 4, 'action': 'Capture the returned value or index', 'notes': 'Value-based functions return numeric results; index-based functions return positions'}
- {'step': 5, 'action': 'Use the result for downstream visualization, reporting, or further analysis', 'notes': 'Pass to chart scales, display in UI, or feed into subsequent computations'}

## Constraints

- Input must be an iterable of numeric values
- Empty iterables may return undefined or null depending on the function
- Non-numeric values in the iterable are typically skipped or cause errors
- Some functions (e.g., quantileSorted) require pre-sorted input

## Cautions

- Verify input data is numeric before calling; filter or validate if necessary
- Be aware of NaN and Infinity handling in your dataset
- For quantile functions, ensure the quantile parameter is in the range [0, 1]
- quantileSorted expects a sorted array; unsorted input will produce incorrect results

## Output Contract

- Returns a single numeric value (for value-based functions: count, min, max, mean, median, variance, deviation, sum, mode, quantile, cumsum) or a numeric index (for index-based functions: minIndex, maxIndex, leastIndex, greatestIndex, medianIndex, quantileIndex). For extent, returns a two-element array [min, max]. For rank, returns an array of rank values. Returns undefined or null if input is empty or invalid.

## Example Executions

### Example 1

- Input: d3.mean([1, 2, 3, 4, 5])
- Output: 3
- Notes: Arithmetic mean of five integers

### Example 2

- Input: d3.median([10, 20, 30, 40, 50])
- Output: 30
- Notes: Median (0.5-quantile) of sorted array

### Example 3

- Input: d3.variance([2, 4, 6, 8])
- Output: 5
- Notes: Variance measuring spread around mean

## Triggers

- document has multiple zones (title, body, abstract, etc.)
- zone weights are known or learned from training data
- Boolean match signals per zone are available

## Examples

### Example 1

Input:

  d3.mean([1, 2, 3, 4, 5])

Output:

  3

Notes:

  Arithmetic mean of five integers

### Example 2

Input:

  d3.median([10, 20, 30, 40, 50])

Output:

  30

Notes:

  Median (0.5-quantile) of sorted array

### Example 3

Input:

  d3.variance([2, 4, 6, 8])

Output:

  5

Notes:

  Variance measuring spread around mean
