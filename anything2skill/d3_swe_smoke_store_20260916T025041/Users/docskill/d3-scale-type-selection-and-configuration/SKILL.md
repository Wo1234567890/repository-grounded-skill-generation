---
id: "1e8e2de6-6c13-51de-9bb0-cca1b066994e"
name: "D3 Scale Type Selection and Configuration"
description: "Choose the appropriate scale type (linear, time, log, ordinal, band, sequential, diverging, quantile, etc.) based on data domain and range requirements, then configure its domain and range mappings to enable correct visual encoding."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "data-encoding"
  - "visual-mapping"
  - "quantitative"
  - "categorical"
triggers:
  - "Preparing to encode quantitative or categorical data into visual channels"
  - "Need to map data domain to visual range (axes, colors, sizes)"
  - "Scale type selection depends on data type and desired visual effect"
---

# D3 Scale Type Selection and Configuration

Choose the appropriate scale type (linear, time, log, ordinal, band, sequential, diverging, quantile, etc.) based on data domain and range requirements, then configure its domain and range mappings to enable correct visual encoding.

## Prompt

Select a scale type matching your data characteristics: use linear for continuous numeric data, time for temporal data, log for exponential ranges, ordinal for categorical data, band for categorical with spacing, sequential/diverging for color encoding, and quantile/quantize for binned mappings. Configure the scale's domain (input data extent) and range (output visual extent) to establish the transformation function.

## Objective

Map data values to visual encoding (position, color, size) using the correct scale transformation
## Applicable Signals

- Data preparation phase before element binding
- Visual channel assignment (position, color, size, opacity)
- Data type identified (numeric, temporal, categorical)

## Contraindications

- Working with raw SVG or canvas without data binding
- Scale is already instantiated and only needs value updates
- Direct pixel-level rendering without data transformation

## Workflow Steps

- Identify data type: continuous (numeric, temporal) or categorical
- Select scale type: linear, time, log, pow, symlog, ordinal, band, point, sequential, diverging, quantile, quantize, or threshold
- Define domain: input data minimum and maximum (or category list)
- Define range: output visual extent (pixel range, color array, size range)
- Instantiate and configure the scale function
- Validate scale output against expected visual encoding

## Constraints

- Domain must match input data extent
- Range must match output visual extent
- Scale type must align with data type (continuous vs. categorical)

## Output Contract

- A configured scale function that correctly maps input data domain to output visual range with appropriate transformation, ready for use in data binding and visual element updates

## Triggers

- Preparing to encode quantitative or categorical data into visual channels
- Need to map data domain to visual range (axes, colors, sizes)
- Scale type selection depends on data type and desired visual effect
