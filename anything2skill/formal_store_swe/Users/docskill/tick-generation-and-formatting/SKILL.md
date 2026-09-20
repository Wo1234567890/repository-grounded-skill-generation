---
id: "83da7051-b1d8-5253-970d-a41728748dad"
name: "Tick Generation and Formatting"
description: "Generate representative tick values from a continuous quantitative domain and format them into human-readable strings suitable for axis or legend display. Combines tick computation via scale.ticks() with formatting via scale.tickFormat() to produce display-ready labels."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "axis"
  - "tick"
  - "formatting"
  - "visualization"
triggers:
  - "building chart axes and need human-readable scale labels"
  - "preparing legend or reference marks for visualization"
  - "converting domain values to display-friendly tick strings"
---

# Tick Generation and Formatting

Generate representative tick values from a continuous quantitative domain and format them into human-readable strings suitable for axis or legend display. Combines tick computation via scale.ticks() with formatting via scale.tickFormat() to produce display-ready labels.

## Prompt

1. Retrieve or create a quantitative scale (e.g., d3.scaleLinear) with domain and range configured.
2. Compute representative tick values from the scale domain using linear.ticks(count) where count is the desired number of ticks.
3. Obtain a formatter function via linear.tickFormat(count, specifier) or d3.tickFormat(start, stop, count, specifier).
4. Apply the formatter function to each numeric tick value to produce human-readable strings.
5. Return the array of formatted tick strings ready for axis or legend rendering.

## Objective

produce formatted tick labels suitable for axis or legend display
## Applicable Signals

- scale domain is continuous and quantitative
- axis or legend rendering is in progress
- tick positions and labels must be coordinated

## Contraindications

- ticks are pre-computed or provided externally
- scale domain is categorical or ordinal
- custom tick positions are required outside standard computation

## Workflow Steps

- {'step': 1, 'action': 'Retrieve or create a quantitative scale', 'input': 'scale object with domain and range configured', 'output': 'scale instance (e.g., d3.scaleLinear())'}
- {'step': 2, 'action': 'Compute tick values from domain', 'input': 'scale.ticks(count) where count is desired number of ticks', 'output': 'array of numeric tick values'}
- {'step': 3, 'action': 'Obtain formatter function', 'input': 'scale.tickFormat(count, specifier) or d3.tickFormat(start, stop, count, specifier)', 'output': 'formatter function'}
- {'step': 4, 'action': 'Apply formatter to each tick value', 'input': 'numeric tick array and formatter function', 'output': 'array of formatted tick strings'}
- {'step': 5, 'action': 'Return formatted ticks for rendering', 'input': 'array of formatted strings', 'output': 'array of strings ready for axis or legend display'}

## Constraints

- scale must support .ticks() and .tickFormat() methods
- domain must be continuous and numeric
- output must be an array of formatted strings

## Cautions

- tick count should be reasonable (typically 5–10) to avoid overcrowding
- formatter specifier must match the data type and precision requirements
- ensure scale domain is finalized before computing ticks

## Output Contract

- array of formatted tick strings, each suitable for direct display on an axis label or legend entry; strings are human-readable and respect the scale's domain and formatting rules

## Triggers

- building chart axes and need human-readable scale labels
- preparing legend or reference marks for visualization
- converting domain values to display-friendly tick strings
