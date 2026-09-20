---
id: "fca6e09e-14bf-5af8-ba2d-0b6dccb05d58"
name: "Threshold Scale Configuration"
description: "Create and configure a threshold scale that maps continuous domain values to discrete range values. Use this skill when you need to quantize continuous input into discrete output categories for visualizations like choropleth maps or categorical color assignments."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "threshold"
  - "quantization"
  - "categorical"
  - "visualization"
triggers:
  - "Need to map continuous input values to discrete output categories"
  - "Building a choropleth or categorical visualization"
  - "Quantizing continuous data into predefined buckets"
---

# Threshold Scale Configuration

Create and configure a threshold scale that maps continuous domain values to discrete range values. Use this skill when you need to quantize continuous input into discrete output categories for visualizations like choropleth maps or categorical color assignments.

## Prompt

1. Create a threshold scale using d3.scaleThreshold().
2. Set the input domain using threshold.domain() with an array of threshold boundary values in ascending order.
3. Set the output range using threshold.range() with an array of discrete output values (e.g., colors or categories).
4. Optionally create a copy of the scale using threshold.copy() for reuse.
5. Use threshold() to transform input values, or threshold.invertExtent() to reverse-map range values back to domain intervals.

## Objective

Configure a quantizing threshold scale for data visualization
## Applicable Signals

- Data has continuous domain but requires discrete range output
- Visualization requires categorical color or value assignment
- Threshold boundaries are known in advance

## Contraindications

- Continuous output mapping is required
- Linear or logarithmic scaling is more appropriate
- Domain values are already categorical
- Fine-grained interpolation between values is needed

## Workflow Steps

- {'step': 1, 'action': 'Instantiate scale', 'detail': 'Call d3.scaleThreshold() to create a new threshold scale object'}
- {'step': 2, 'action': 'Configure domain', 'detail': 'Call threshold.domain([value1, value2, ...]) with sorted numeric boundaries'}
- {'step': 3, 'action': 'Configure range', 'detail': 'Call threshold.range([output1, output2, ...]) with discrete output values'}
- {'step': 4, 'action': 'Validate and test', 'detail': 'Call threshold(inputValue) to verify mapping; use invertExtent(rangeValue) to check reverse mapping'}
- {'step': 5, 'action': 'Optional: clone for reuse', 'detail': 'Call threshold.copy() if the scale configuration needs to be reused elsewhere'}

## Constraints

- Domain must be an array of numeric threshold values in ascending order
- Range array length must be domain length plus one
- Threshold scale is unidirectional by default; use invertExtent() for reverse mapping

## Cautions

- Domain values must be strictly ascending; unsorted domains produce undefined behavior
- Range length must equal domain length plus one (n thresholds produce n+1 output categories)
- Threshold scales do not interpolate; values outside domain bounds map to the nearest range endpoint

## Output Contract

- A configured threshold scale object with domain and range set, ready to transform input values. The scale is callable as a function and supports invertExtent() for reverse lookups.

## Triggers

- Need to map continuous input values to discrete output categories
- Building a choropleth or categorical visualization
- Quantizing continuous data into predefined buckets
