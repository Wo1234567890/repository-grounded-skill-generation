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
  - "data_encoding"
  - "visualization"
triggers:
  - "Need to encode continuous quantitative values into visual output using a single interpolator function"
  - "Building heatmaps, choropleth maps, or gradient visualizations"
  - "Mapping numerical data to a smooth color or value gradient"
---

# Sequential Scale Configuration

Create and configure a sequential scale that maps continuous quantitative data to a fixed interpolator output, with support for linear, logarithmic, power, and quantile transforms.

## Prompt

Use d3.scaleSequential or its variants (Log, Pow, Sqrt, Symlog, Quantile) to create a scale. Set the interpolator function via sequential.interpolator(). Configure the output range using sequential.range() for floating-point output or sequential.rangeRound() for integer output with rounding. The scale object accepts domain values and returns interpolated output.

## Objective

Map continuous domain to interpolated range via sequential scale
## Applicable Signals

- Continuous quantitative domain available
- Single interpolator function defined or available
- Output range specified (color scheme, numeric range, etc.)

## Contraindications

- Mapping categorical or ordinal data
- Using diverging or threshold scales
- Output requires discrete color bands rather than continuous interpolation
- Data has multiple distinct value ranges requiring separate scales

## Workflow Steps

- Select scale variant: d3.scaleSequential (linear), scaleSequentialLog, scaleSequentialPow, scaleSequentialSqrt, scaleSequentialSymlog, or scaleSequentialQuantile
- Create scale instance using selected variant
- Set interpolator function via sequential.interpolator(interpolatorFunction)
- Set output range via sequential.range(rangeArray) or sequential.rangeRound(rangeArray)
- Return configured scale object for use in data encoding

## Constraints

- Interpolator must be a function that accepts a normalized value [0, 1] and returns output
- Domain must be continuous and quantitative
- Output range must be compatible with the interpolator function

## Cautions

- Sequential scales assume monotonic mapping; non-monotonic data may produce unexpected results
- rangeRound() applies rounding; use range() for precise floating-point output
- Quantile variant requires quantiles array; other variants use implicit domain transform

## Output Contract

- A configured scale object that accepts domain values and returns interpolated output values within the specified range; scale is immediately usable for encoding data.

## Triggers

- Need to encode continuous quantitative values into visual output using a single interpolator function
- Building heatmaps, choropleth maps, or gradient visualizations
- Mapping numerical data to a smooth color or value gradient
