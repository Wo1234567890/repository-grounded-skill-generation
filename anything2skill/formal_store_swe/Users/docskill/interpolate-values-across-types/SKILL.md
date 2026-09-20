---
id: "0a67fc3d-72f2-5ebb-9f1c-8d8a5b6b2b56"
name: "Interpolate Values Across Types"
description: "Transform and blend numeric, color, string, array, and object values smoothly between start and end states. Use when you need continuous transitions or intermediate representations in visualization or animation contexts."
version: "0.1.0"
tags:
  - "interpolation"
  - "animation"
  - "value_blending"
  - "transition"
  - "visualization"
triggers:
  - "Animating visual properties, blending color palettes, or generating intermediate states between two values"
examples:
  - input: "start=0, end=100, factor=0.5"
    output: "50"
    notes: "Numeric interpolation at midpoint"
  - input: "start='rgb(255,0,0)', end='rgb(0,0,255)', factor=0.5"
    output: "rgb(127,0,127)"
    notes: "Color interpolation between red and blue"
  - input: "start=[0,0], end=[100,100], factor=0.25"
    output: "[25,25]"
    notes: "Array interpolation at quarter point"
---

# Interpolate Values Across Types

Transform and blend numeric, color, string, array, and object values smoothly between start and end states. Use when you need continuous transitions or intermediate representations in visualization or animation contexts.

## Prompt

Given a start value and end value of any supported type (number, color, string, array, or object), generate an intermediate value at a specified interpolation factor (0.0–1.0). Factor 0.0 returns the start value; factor 1.0 returns the end value; intermediate factors produce blended results.

## Objective

Generate intermediate values during interpolation
## Applicable Signals

- Animating visual properties (position, size, opacity)
- Blending color palettes or gradients
- Generating intermediate states between two values
- Smooth transitions in time-series or frame-based rendering

## Contraindications

- Discrete categorical transitions where interpolation is not meaningful
- One-time static value mapping without animation or blending
- Cases where the start and end values are of incompatible types

## Workflow Steps

- Accept start value, end value, and interpolation factor (0.0–1.0)
- Detect or infer the type of the values (number, color, string, array, object)
- Apply type-specific interpolation logic
- Return the intermediate value at the specified factor

## Constraints

- Interpolation factor must be a numeric value between 0.0 and 1.0
- Start and end values should be of compatible or identical types for predictable results
- Output type matches the input value type

## Output Contract

- A single intermediate value of the same type as the input values, positioned proportionally between start and end according to the interpolation factor. Ready for rendering, animation frame application, or further processing.

## Example Executions

### Example 1

- Input: start=0, end=100, factor=0.5
- Output: 50
- Notes: Numeric interpolation at midpoint

### Example 2

- Input: start='rgb(255,0,0)', end='rgb(0,0,255)', factor=0.5
- Output: rgb(127,0,127)
- Notes: Color interpolation between red and blue

### Example 3

- Input: start=[0,0], end=[100,100], factor=0.25
- Output: [25,25]
- Notes: Array interpolation at quarter point

## Triggers

- Animating visual properties, blending color palettes, or generating intermediate states between two values

## Examples

### Example 1

Input:

  start=0, end=100, factor=0.5

Output:

  50

Notes:

  Numeric interpolation at midpoint

### Example 2

Input:

  start='rgb(255,0,0)', end='rgb(0,0,255)', factor=0.5

Output:

  rgb(127,0,127)

Notes:

  Color interpolation between red and blue

### Example 3

Input:

  start=[0,0], end=[100,100], factor=0.25

Output:

  [25,25]

Notes:

  Array interpolation at quarter point
