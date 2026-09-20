---
id: "b807967a-43b5-5afd-a7d7-8197a847f5bb"
name: "Threshold Scale Value Lookup"
description: "Query a configured threshold scale to map a domain value to its corresponding range value, or invert to find the domain extent for a given range value. Use this micro-skill when you need to apply threshold scale transformations to individual values or small batches."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "threshold"
  - "value_mapping"
  - "quantization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to apply a threshold scale to transform a single value"
  - "Need to find domain range for a given output value"
  - "Threshold scale is already configured and ready for queries"
---

# Threshold Scale Value Lookup

Query a configured threshold scale to map a domain value to its corresponding range value, or invert to find the domain extent for a given range value. Use this micro-skill when you need to apply threshold scale transformations to individual values or small batches.

## Prompt

Given a threshold scale and an input value, call threshold(value) to retrieve the mapped output, or call threshold.invertExtent(value) to retrieve the domain bounds [min, max] corresponding to a range value. Ensure the scale is already configured with domain() and range() before invoking this lookup.

## Objective

Query a threshold scale to map or reverse-map values
## Applicable Signals

- Scale configuration complete (domain and range set)
- Single or small-batch value transformation required
- Reverse lookup (range → domain) needed

## Contraindications

- Scale is not yet configured with domain() and range()
- Performing bulk transformations better handled by scale function directly
- Scale type is not threshold

## Workflow Steps

- {'step': 1, 'action': 'Verify threshold scale is configured', 'detail': 'Confirm scale has domain() and range() already set'}
- {'step': 2, 'action': 'Call threshold(value) for forward lookup', 'detail': 'Pass domain value; receive corresponding range value'}
- {'step': 3, 'action': 'Or call threshold.invertExtent(value) for reverse lookup', 'detail': 'Pass range value; receive [min, max] domain extent'}
- {'step': 4, 'action': 'Return result to caller', 'detail': 'Single mapped value or domain extent tuple'}

## Constraints

- Input value must be within or compatible with the scale's domain or range
- Scale must be initialized before calling threshold() or threshold.invertExtent()

## Cautions

- invertExtent() returns a domain extent [min, max]; check that the range value exists in the scale's range before inverting
- Threshold scales quantize continuous input; output is discrete and based on configured thresholds

## Output Contract

- Returns either a single mapped value (domain → range) or a domain extent tuple [min, max] (range → domain). Caller receives the result ready for downstream use or validation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to apply a threshold scale to transform a single value
- Need to find domain range for a given output value
- Threshold scale is already configured and ready for queries
