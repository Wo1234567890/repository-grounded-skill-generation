---
id: "b807967a-43b5-5afd-a7d7-8197a847f5bb"
name: "Threshold Scale Value Lookup"
description: "Query a configured threshold scale to map a domain value to its corresponding range value, or invert to find the domain bounds for a given range value. Use this micro-skill when you need to apply an already-configured threshold scale to transform individual values or retrieve..."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "threshold"
  - "quantization"
  - "value_mapping"
  - "lookup"
triggers:
  - "Need to apply a threshold scale to transform a single value"
  - "Need to apply a threshold scale to transform a batch of values"
  - "Need to find domain range for a given output category"
---

# Threshold Scale Value Lookup

Query a configured threshold scale to map a domain value to its corresponding range value, or invert to find the domain bounds for a given range value. Use this micro-skill when you need to apply an already-configured threshold scale to transform individual values or retrieve...

## Prompt

Given a threshold scale object and an input value, call threshold(value) to retrieve the mapped output, or call threshold.invertExtent(value) to retrieve the domain interval [min, max] corresponding to a range value. Ensure the scale is configured with domain() and range() before querying.

## Objective

Query a threshold scale to map or reverse-map values
## Applicable Signals

- Threshold scale is already configured with domain and range
- Input value is within or near expected domain bounds
- Caller has a pre-built scale object ready for querying

## Contraindications

- Scale is not yet configured with domain() and range()
- Input is outside expected domain bounds and no fallback is defined
- Caller needs to create or modify the scale itself (use scale configuration skill instead)

## Workflow Steps

- {'step': 1, 'action': 'Verify the threshold scale is configured', 'detail': 'Confirm scale.domain() and scale.range() have been set'}
- {'step': 2, 'action': 'Call threshold(value) to map a domain value to range', 'detail': 'Pass the input value; receive the corresponding output category or value'}
- {'step': 3, 'action': 'Optionally call threshold.invertExtent(value) to reverse-map', 'detail': 'Pass a range value; receive [min, max] domain bounds for that output'}
- {'step': 4, 'action': 'Return the mapped value or domain extent to the caller', 'detail': 'Ensure output matches the expected contract (single value or [min, max] array)'}

## Constraints

- Scale must be instantiated and configured before this skill is invoked
- Domain and range must be set on the scale object
- Input values should align with the scale's domain definition

## Cautions

- invertExtent() returns a domain interval; check that the returned array has two elements
- Threshold scales quantize continuous input; values between thresholds map to the same output

## Output Contract

- Returns either a single mapped value (from threshold(value)) or a two-element domain extent array [min, max] (from threshold.invertExtent(value)). Caller receives the quantized output or the domain interval corresponding to the queried range value.

## Triggers

- Need to apply a threshold scale to transform a single value
- Need to apply a threshold scale to transform a batch of values
- Need to find domain range for a given output category
