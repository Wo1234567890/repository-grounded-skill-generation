---
id: "fca6e09e-14bf-5af8-ba2d-0b6dccb05d58"
name: "Threshold Scale Configuration"
description: "Create and configure a threshold scale that maps continuous domain values to discrete range values. Use this skill when you need to quantize continuous input into discrete output categories, such as for choropleth maps or categorical color assignments."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "threshold"
  - "quantization"
  - "visualization"
  - "data-mapping"
triggers:
  - "Need to map continuous input values to discrete output categories or colors; building a choropleth or categorical visualization"
---

# Threshold Scale Configuration

Create and configure a threshold scale that maps continuous domain values to discrete range values. Use this skill when you need to quantize continuous input into discrete output categories, such as for choropleth maps or categorical color assignments.

## Prompt

To configure a threshold scale: (1) Create the scale using d3.scaleThreshold(). (2) Set the input domain using threshold.domain() with an array of threshold values that define boundaries between categories. (3) Set the output range using threshold.range() with an array of discrete values (colors, categories, etc.) matching the number of domain segments. (4) Optionally use threshold.invertExtent() to reverse-map a range value back to its domain interval. (5) Call threshold.copy() if you need an independent copy of the configured scale.

## Objective

Configure a quantizing threshold scale for data visualization
## Applicable Signals

- Need to map continuous input values to discrete output categories
- Building a choropleth or categorical visualization
- Quantizing continuous data into bins or color bands

## Contraindications

- Continuous output mapping is required
- Linear or logarithmic scaling is more appropriate
- Domain values are already categorical

## Workflow Steps

- {'step': 1, 'action': 'Create threshold scale', 'detail': 'Instantiate d3.scaleThreshold() to create a new threshold scale object.'}
- {'step': 2, 'action': 'Set domain', 'detail': 'Call threshold.domain([value1, value2, ...]) with an array of threshold boundary values in ascending order.'}
- {'step': 3, 'action': 'Set range', 'detail': 'Call threshold.range([output1, output2, ...]) with an array of discrete output values (length = domain length + 1).'}
- {'step': 4, 'action': 'Optional: invert mapping', 'detail': 'Use threshold.invertExtent(rangeValue) to retrieve the domain interval [min, max] corresponding to a given range value.'}
- {'step': 5, 'action': 'Optional: copy scale', 'detail': 'Call threshold.copy() to create an independent copy of the configured scale.'}

## Constraints

- Domain array must be sorted in ascending order
- Range array length must equal domain array length plus one
- Each domain value defines a threshold; values below the first threshold map to range[0], values between thresholds map to intermediate range values, and values above the last threshold map to the final range value

## Output Contract

- Returns a configured threshold scale object with domain and range set, ready to transform input values via direct invocation (e.g., scale(inputValue)) or to support reverse lookups via invertExtent().

## Triggers

- Need to map continuous input values to discrete output categories or colors; building a choropleth or categorical visualization
