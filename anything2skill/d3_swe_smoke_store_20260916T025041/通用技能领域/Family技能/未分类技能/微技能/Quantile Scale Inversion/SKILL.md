---
id: "49af3de1-3a4d-59e2-99a5-8d30fe360f4d"
name: "Quantile Scale Inversion"
description: "Reverse-map a range value back to its corresponding domain interval using invertExtent. Use when you need to identify which input domain values produced a given output range value, such as in interactive tooltips or data filtering."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "quantile"
  - "inversion"
  - "reverse_lookup"
  - "interactive"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "You have a range value (e.g., from user interaction or visual element) and need to find the corresponding domain interval; implementing interactive selection or drill-down."
---

# Quantile Scale Inversion

Reverse-map a range value back to its corresponding domain interval using invertExtent. Use when you need to identify which input domain values produced a given output range value, such as in interactive tooltips or data filtering.

## Prompt

Call invertExtent(rangeValue) on a configured quantile scale to retrieve the domain interval [min, max] that maps to the given range value. The result is a two-element array representing the input domain bounds corresponding to the output range value.

## Objective

Invert a quantile scale output to retrieve the input domain interval
## Applicable Signals

- User interaction with a visual element mapped to a quantile scale
- Need to identify source data range from a rendered output value
- Interactive selection or drill-down workflow requiring domain bounds

## Contraindications

- Scale has not been configured with both domain and range
- You only need forward mapping (domain to range)
- You require exact single-value lookup rather than an interval

## Intervention Moves

- Call invertExtent(rangeValue) on the quantile scale instance
- Extract the returned [minDomain, maxDomain] array
- Use the domain interval for filtering, highlighting, or downstream queries

## Constraints

- The quantile scale must be fully initialized before calling invertExtent
- The rangeValue must be within or near the configured output range
- invertExtent returns an interval, not a single point

## Cautions

- If rangeValue is outside the scale's range, the result may be undefined or an edge interval
- Quantile scales discretize the domain; invertExtent returns the interval for that quantile bin

## Output Contract

- An array [minDomain, maxDomain] representing the input interval that maps to the given range value; undefined if the range value is not in the scale's output range.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- You have a range value (e.g., from user interaction or visual element) and need to find the corresponding domain interval; implementing interactive selection or drill-down.
