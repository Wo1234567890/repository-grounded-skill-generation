---
id: "f3f0deb0-649b-524b-8771-326c429468d5"
name: "Quantile-Based Sequential Scale Setup"
description: "Create a sequential scale using quantile-based domain transformation to map data percentiles directly to interpolator output. Ensures equal visual weight across non-uniform data distributions and provides access to quantile breakpoints."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "sequential"
  - "quantile"
  - "data_mapping"
  - "visualization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to ensure equal visual weight across data distribution"
  - "Data has non-uniform or skewed distribution"
  - "Want to inspect quantile breakpoints used by the scale"
  - "Mapping percentiles to color or position interpolators"
examples:
  - input: "Data array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; Interpolator: d3.interpolateViridis"
    output: "scale = d3.scaleSequentialQuantile().domain([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).interpolator(d3.interpolateViridis); scale.quantiles() returns [1, 3.25, 5.5, 7.75, 10]; scale(5) returns a color from the Viridis scale."
    notes: "Quantiles divide the domain into equal-count buckets; each bucket maps to a proportional segment of the interpolator."
  - input: "Skewed data: [1, 1, 1, 2, 10, 100]; Interpolator: d3.interpolateRdYlBu"
    output: "scale.quantiles() returns breakpoints that cluster near the dense region (e.g., [1, 1, 1.5, 10, 100]); scale(1) and scale(1.5) map to similar colors despite different domain values."
    notes: "Quantile-based scaling ensures that the dense cluster of 1s receives proportional visual representation."
---

# Quantile-Based Sequential Scale Setup

Create a sequential scale using quantile-based domain transformation to map data percentiles directly to interpolator output. Ensures equal visual weight across non-uniform data distributions and provides access to quantile breakpoints.

## Prompt

Use d3.scaleSequentialQuantile to create a scale that transforms a continuous domain into quantile-based buckets, then map those buckets to a continuous interpolator. Call quantiles() to retrieve the domain breakpoints used by the scale. This is useful when you want each visual segment of the interpolator to represent an equal count of data points rather than equal domain intervals.

## Objective

Apply quantile transform to sequential scale and retrieve quantile breakpoints
## Applicable Signals

- Data distribution is non-uniform
- Visual encoding should reflect data density equally
- Quantile-based bucketing is required
- Introspection of scale domain breakpoints is needed

## Contraindications

- Domain values are already uniformly distributed
- Linear or logarithmic mapping is explicitly required
- Quantile computation overhead is unacceptable for real-time updates
- Scale must preserve exact domain-to-output linearity

## Workflow Steps

- {'step': 1, 'action': 'Create a quantile-based sequential scale using d3.scaleSequentialQuantile()', 'detail': 'Instantiate the scale with no initial domain; the domain will be set in the next step.'}
- {'step': 2, 'action': 'Set the domain using .domain(array) with your data values', 'detail': 'Pass an array of numeric values; the scale will compute quantile breakpoints internally.'}
- {'step': 3, 'action': 'Set the interpolator using .interpolator(fn) or .range()', 'detail': 'Provide a function that maps [0, 1] to your desired output (e.g., color scale, position).'}
- {'step': 4, 'action': 'Retrieve quantile breakpoints using .quantiles()', 'detail': 'Call this accessor to inspect the domain values that define quantile boundaries; useful for legends or debugging.'}
- {'step': 5, 'action': 'Apply the scale to your data', 'detail': 'Call scale(value) for each data point to get the interpolated output.'}

## Constraints

- Input domain must be a continuous array of numeric values
- Interpolator must accept normalized [0, 1] input range
- Quantile computation is performed once at scale creation; domain changes require scale recreation

## Cautions

- Quantile computation can be expensive for very large datasets; consider pre-computing or sampling if performance is critical
- The quantiles() accessor returns the computed breakpoints; modifying this array externally will not update the scale

## Output Contract

- Returns a quantile-based sequential scale object with methods: domain(array), interpolator(fn), range(array), rangeRound(array), quantiles(). Calling quantiles() returns an array of domain breakpoints representing the computed quantile boundaries. Calling scale(value) returns the interpolated output for a given domain value.

## Example Therapist Responses

### Example 1

- Client/Input: Data array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; Interpolator: d3.interpolateViridis
- Therapist/Output: scale = d3.scaleSequentialQuantile().domain([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).interpolator(d3.interpolateViridis); scale.quantiles() returns [1, 3.25, 5.5, 7.75, 10]; scale(5) returns a color from the Viridis scale.
- Notes: Quantiles divide the domain into equal-count buckets; each bucket maps to a proportional segment of the interpolator.

### Example 2

- Client/Input: Skewed data: [1, 1, 1, 2, 10, 100]; Interpolator: d3.interpolateRdYlBu
- Therapist/Output: scale.quantiles() returns breakpoints that cluster near the dense region (e.g., [1, 1, 1.5, 10, 100]); scale(1) and scale(1.5) map to similar colors despite different domain values.
- Notes: Quantile-based scaling ensures that the dense cluster of 1s receives proportional visual representation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to ensure equal visual weight across data distribution
- Data has non-uniform or skewed distribution
- Want to inspect quantile breakpoints used by the scale
- Mapping percentiles to color or position interpolators

## Examples

### Example 1

Input:

  Data array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; Interpolator: d3.interpolateViridis

Output:

  scale = d3.scaleSequentialQuantile().domain([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).interpolator(d3.interpolateViridis); scale.quantiles() returns [1, 3.25, 5.5, 7.75, 10]; scale(5) returns a color from the Viridis scale.

Notes:

  Quantiles divide the domain into equal-count buckets; each bucket maps to a proportional segment of the interpolator.

### Example 2

Input:

  Skewed data: [1, 1, 1, 2, 10, 100]; Interpolator: d3.interpolateRdYlBu

Output:

  scale.quantiles() returns breakpoints that cluster near the dense region (e.g., [1, 1, 1.5, 10, 100]); scale(1) and scale(1.5) map to similar colors despite different domain values.

Notes:

  Quantile-based scaling ensures that the dense cluster of 1s receives proportional visual representation.
