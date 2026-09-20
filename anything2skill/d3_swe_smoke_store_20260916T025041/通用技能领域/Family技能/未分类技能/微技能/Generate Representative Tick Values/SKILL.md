---
id: "5bc830c7-42a5-578b-85bb-676fe577ace8"
name: "Generate Representative Tick Values"
description: "Produce a set of evenly-spaced or representative numeric values from a continuous interval for axis labeling or scale subdivision."
version: "0.1.0"
tags:
  - "tick_generation"
  - "axis_labeling"
  - "scale_subdivision"
  - "visualization_prep"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "You need to label an axis, create a legend scale, or subdivide a continuous numeric range into readable intervals."
---

# Generate Representative Tick Values

Produce a set of evenly-spaced or representative numeric values from a continuous interval for axis labeling or scale subdivision.

## Prompt

Given a continuous numeric interval (min, max), generate an array of tick values at regular or optimized spacing suitable for axis labels or scale reference points. The output should be human-readable and span the full interval.

## Objective

Generate tick values for visualization or scale representation
## Applicable Signals

- Need to label an axis with representative values
- Creating a legend scale or color scale
- Subdividing a continuous numeric range into readable intervals
- Preparing visualization scaffolding

## Contraindications

- Tick values are already provided by upstream process
- Data is categorical or non-numeric
- Interval is non-continuous or undefined

## Workflow Steps

- Accept interval bounds (min, max) and optional tick count or spacing preference
- Calculate or select evenly-spaced or optimized tick positions
- Return array of numeric tick values

## Constraints

- Input must be a valid continuous numeric interval with defined min and max
- Output tick values must fall within or span the input interval
- Spacing should be regular or follow a standard optimization heuristic

## Cautions

- Ensure tick count is reasonable for readability (typically 3–10 ticks)
- Verify output values are human-readable (e.g., round numbers, standard increments)

## Output Contract

- An array of numeric tick values spanning the input interval at regular or optimized spacing, suitable for downstream axis rendering or scale labeling.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- You need to label an axis, create a legend scale, or subdivide a continuous numeric range into readable intervals.
