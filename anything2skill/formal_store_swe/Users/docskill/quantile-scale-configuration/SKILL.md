---
id: "228a8871-08eb-566a-8109-8fc6f1368195"
name: "Quantile Scale Configuration"
description: "Set up and configure a quantile scale that maps a continuous input domain to discrete output range values using quantile thresholds. Use when you need to partition data into equal-frequency bins or apply quantile-based color encoding."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "quantile"
  - "data_mapping"
  - "binning"
  - "configuration"
triggers:
  - "Need to map continuous data to discrete output values using equal-frequency partitioning"
  - "Data distribution is non-uniform and quantile-based binning is desired"
  - "Applying quantile-based color encoding or categorical output mapping"
---

# Quantile Scale Configuration

Set up and configure a quantile scale that maps a continuous input domain to discrete output range values using quantile thresholds. Use when you need to partition data into equal-frequency bins or apply quantile-based color encoding.

## Prompt

Create a quantile scale by: (1) instantiate d3.scaleQuantile(), (2) set the input domain using .domain([...]), (3) set the output range using .range([...]), (4) verify quantile thresholds via .quantiles(). The scale will automatically compute quantile boundaries and map domain values to range outputs. Use .invertExtent(rangeValue) to reverse-map a range value back to its domain interval. Call .copy() to create an independent copy of the configured scale.

## Objective

Configure a quantile scale with domain, range, and quantile thresholds
## Applicable Signals

- Continuous numeric domain available
- Discrete output range defined
- Equal-frequency binning requirement identified

## Contraindications

- Linear or logarithmic scaling is more appropriate for the use case
- Domain values are already categorical
- Quantile thresholds are unknown or cannot be computed from the data

## Workflow Steps

- {'step': 1, 'action': 'Instantiate quantile scale', 'detail': 'Call d3.scaleQuantile() to create a new quantile scale instance'}
- {'step': 2, 'action': 'Set input domain', 'detail': 'Call .domain(array) with continuous numeric values to define the input range'}
- {'step': 3, 'action': 'Set output range', 'detail': 'Call .range(array) with discrete output values (colors, categories, etc.)'}
- {'step': 4, 'action': 'Verify quantile thresholds', 'detail': 'Call .quantiles() to inspect computed threshold boundaries between bins'}
- {'step': 5, 'action': 'Test scale transformation', 'detail': 'Apply scale to sample domain values and confirm output matches expected range values'}

## Constraints

- Domain must be a continuous numeric array
- Range must have discrete output values matching or exceeding quantile bin count
- Quantile computation requires sufficient data points for meaningful thresholds

## Cautions

- Quantile thresholds are computed automatically; verify .quantiles() output matches expected bin boundaries
- Small datasets may produce unexpected or sparse quantile thresholds
- Changing domain or range after configuration recomputes quantiles; preserve original scale with .copy() if needed

## Output Contract

- A configured quantile scale object with domain, range, and quantile thresholds set; ready to transform input values to output range values. The scale is callable as a function and supports .invertExtent() for reverse mapping and .copy() for duplication.

## Triggers

- Need to map continuous data to discrete output values using equal-frequency partitioning
- Data distribution is non-uniform and quantile-based binning is desired
- Applying quantile-based color encoding or categorical output mapping
