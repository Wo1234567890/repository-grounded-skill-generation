---
id: "e5016e77-d942-5283-a78c-c9aecc6bfd1e"
name: "Sequential Scale Configuration"
description: "Create and configure a sequential scale that maps continuous quantitative data to a fixed interpolator output, with support for linear, logarithmic, power, and quantile transforms."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "sequential"
  - "interpolation"
  - "data_mapping"
  - "visualization"
triggers:
  - "Need to encode continuous quantitative values into visual output using a single interpolator function"
  - "Building heatmaps, choropleth maps, or gradient visualizations"
  - "Mapping numerical data to a smooth color or position range"
---

# Sequential Scale Configuration

Create and configure a sequential scale that maps continuous quantitative data to a fixed interpolator output, with support for linear, logarithmic, power, and quantile transforms.

## Prompt

Use d3.scaleSequential or one of its variants (Log, Pow, Sqrt, Symlog, Quantile) to create a scale. Set the interpolator function via sequential.interpolator(). Configure the output range using sequential.range() for floating-point output or sequential.rangeRound() for integer output with rounding enabled. The resulting scale object accepts domain values and returns interpolated output.

## Objective

Map continuous domain to interpolated range via sequential scale
## Applicable Signals

- Continuous quantitative domain available
- Single interpolator function defined or available
- Output range is fixed and known

## Contraindications

- Mapping categorical or ordinal data
- Using diverging or threshold scales instead
- Output requires discrete color bands rather than continuous interpolation

## Workflow Steps

- {'step': 1, 'action': 'Create sequential scale', 'detail': 'Call d3.scaleSequential() or variant (Log, Pow, Sqrt, Symlog, Quantile) based on transform requirement'}
- {'step': 2, 'action': 'Set interpolator', 'detail': 'Call sequential.interpolator(function) to define the output mapping function'}
- {'step': 3, 'action': 'Configure output range', 'detail': 'Call sequential.range(array) for floating-point or sequential.rangeRound(array) for integer output'}
- {'step': 4, 'action': 'Return configured scale', 'detail': 'Scale object is ready to accept domain values and return interpolated output'}

## Constraints

- Domain must be continuous and quantitative
- Interpolator function must be compatible with scale output type
- Range must be fixed before scale is used

## Cautions

- Ensure interpolator function signature matches expected input/output types
- Use rangeRound() only when integer output is required; range() for floating-point
- Quantile variant requires quantiles array to be set via sequentialQuantile.quantiles()

## Output Contract

- A configured scale object that accepts domain values and returns interpolated output values within the specified range. The scale is immediately callable and produces continuous output.

## Triggers

- Need to encode continuous quantitative values into visual output using a single interpolator function
- Building heatmaps, choropleth maps, or gradient visualizations
- Mapping numerical data to a smooth color or position range
