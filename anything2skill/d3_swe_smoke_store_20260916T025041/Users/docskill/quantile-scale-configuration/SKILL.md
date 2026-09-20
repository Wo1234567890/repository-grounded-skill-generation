---
id: "228a8871-08eb-566a-8109-8fc6f1368195"
name: "Quantile Scale Configuration"
description: "Set up and configure a quantile scale that maps continuous input domain values to discrete output range values using quantile thresholds. Use when you need to partition data into equal-frequency bins or apply quantile-based color encoding."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "quantile"
  - "data-mapping"
  - "binning"
  - "configuration"
triggers:
  - "Need to map continuous values to discrete output categories based on quantile boundaries"
  - "Data distribution is non-uniform and equal-frequency binning is desired"
  - "Applying quantile-based color encoding or categorical output mapping"
---

# Quantile Scale Configuration

Set up and configure a quantile scale that maps continuous input domain values to discrete output range values using quantile thresholds. Use when you need to partition data into equal-frequency bins or apply quantile-based color encoding.

## Prompt

Create a quantile scale by: (1) instantiate d3.scaleQuantile(), (2) set the input domain with .domain(array), (3) set the output range with .range(array), (4) retrieve quantile thresholds with .quantiles() to verify equal-frequency partitioning, (5) test the scale by passing domain values and observing discrete range outputs.

## Objective

Configure a quantile scale with domain, range, and quantile thresholds
## Applicable Signals

- Input is a continuous numeric array
- Output range is discrete (e.g., color palette, category labels)
- Quantile thresholds must be computed and accessible

## Contraindications

- Linear or logarithmic scaling is required
- Continuous output rather than discrete range values is needed
- Domain values are already categorical

## Workflow Steps

- {'step': 1, 'action': 'Instantiate quantile scale', 'detail': 'Call d3.scaleQuantile() to create a new quantile scale object'}
- {'step': 2, 'action': 'Set input domain', 'detail': 'Call .domain(array) with numeric array to define input value range'}
- {'step': 3, 'action': 'Set output range', 'detail': 'Call .range(array) with discrete output values (colors, labels, etc.)'}
- {'step': 4, 'action': 'Retrieve quantile thresholds', 'detail': 'Call .quantiles() to access computed threshold boundaries'}
- {'step': 5, 'action': 'Test scale mapping', 'detail': 'Pass sample domain values to the scale and verify discrete range outputs'}

## Constraints

- Domain must be a numeric array with sufficient data points to compute quantiles
- Range array length determines the number of quantile bins
- Quantile thresholds are computed automatically; manual threshold specification is not supported

## Cautions

- Small datasets may produce unreliable quantile estimates
- Range array length must be at least 2 to define meaningful quantile boundaries

## Output Contract

- A configured quantile scale object that accepts domain input and returns corresponding range value, with quantile thresholds accessible via .quantiles(). The scale is ready for downstream use in visualization or data transformation pipelines.

## Triggers

- Need to map continuous values to discrete output categories based on quantile boundaries
- Data distribution is non-uniform and equal-frequency binning is desired
- Applying quantile-based color encoding or categorical output mapping
