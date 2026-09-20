---
id: "5cd9dd89-33be-5dbc-b873-956a3f118dda"
name: "Interpolate Values Across Types"
description: "Transform and blend numeric, color, string, array, and object values smoothly between start and end states. Generates intermediate values for animations, transitions, and data-driven visualizations requiring continuous value progression across heterogeneous data types."
version: "0.1.0"
tags:
  - "interpolation"
  - "animation"
  - "transition"
  - "value_blending"
  - "multi_type"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Building animations or transitions requiring smooth value progression"
  - "Creating color gradients or morphing effects"
  - "Generating intermediate states in data-driven visualizations"
  - "Blending heterogeneous data types between two endpoints"
examples:
  - input: "start=0, end=100, parameter=0.5"
    output: "50"
    notes: "Numeric interpolation at midpoint"
  - input: "start='red', end='blue', parameter=0.5"
    output: "Intermediate color (e.g., purple or magenta)"
    notes: "Color interpolation in perceptual color space"
  - input: "start=[0, 0], end=[100, 100], parameter=0.25"
    output: "[25, 25]"
    notes: "Array interpolation element-wise"
---

# Interpolate Values Across Types

Transform and blend numeric, color, string, array, and object values smoothly between start and end states. Generates intermediate values for animations, transitions, and data-driven visualizations requiring continuous value progression across heterogeneous data types.

## Prompt

Create an interpolator function that accepts a normalized parameter (0–1) and returns intermediate values of the same type as the input. Use this skill when you need smooth transitions between two states of any supported type: numbers, colors, strings, arrays, or objects.

## Objective

Generate intermediate values for animation, transition, or blending workflows
## Applicable Signals

- Animation or transition workflow initiated
- Continuous value progression required
- Multi-type data blending requested
- Normalized parameter (0–1) available as input

## Contraindications

- Discrete categorical mapping or classification
- One-time static value assignment without progression
- Non-continuous state changes or step-based transitions
- Unsupported data types (e.g., custom objects without serialization)

## Workflow Steps

- {'step': 1, 'action': 'Identify input type (number, color, string, array, or object)', 'rationale': 'Determines which interpolation strategy to apply'}
- {'step': 2, 'action': 'Validate start and end values for type compatibility', 'rationale': 'Prevents runtime errors and ensures predictable output'}
- {'step': 3, 'action': 'Create interpolator function with normalized parameter (0–1) as input', 'rationale': 'Enables caller to control progression through the transition'}
- {'step': 4, 'action': 'Return intermediate value at the specified parameter position', 'rationale': 'Provides the blended or transitional value for the current frame or state'}

## Constraints

- Input start and end values must be of compatible types
- Normalized parameter must be in range [0, 1]
- Output type must match input type
- Interpolation function must be deterministic and stateless

## Cautions

- Ensure start and end values are of the same type to avoid type coercion errors
- For complex nested objects, verify that all nested values support interpolation
- Performance may degrade with very large arrays or deeply nested structures

## Output Contract

- Callable interpolator function that accepts a normalized parameter (0–1) and returns an intermediate value of the same type as the input start and end values. At parameter 0, returns start value; at parameter 1, returns end value; at intermediate values, returns smoothly blended result.

## Example Therapist Responses

### Example 1

- Client/Input: start=0, end=100, parameter=0.5
- Therapist/Output: 50
- Notes: Numeric interpolation at midpoint

### Example 2

- Client/Input: start='red', end='blue', parameter=0.5
- Therapist/Output: Intermediate color (e.g., purple or magenta)
- Notes: Color interpolation in perceptual color space

### Example 3

- Client/Input: start=[0, 0], end=[100, 100], parameter=0.25
- Therapist/Output: [25, 25]
- Notes: Array interpolation element-wise

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building animations or transitions requiring smooth value progression
- Creating color gradients or morphing effects
- Generating intermediate states in data-driven visualizations
- Blending heterogeneous data types between two endpoints

## Examples

### Example 1

Input:

  start=0, end=100, parameter=0.5

Output:

  50

Notes:

  Numeric interpolation at midpoint

### Example 2

Input:

  start='red', end='blue', parameter=0.5

Output:

  Intermediate color (e.g., purple or magenta)

Notes:

  Color interpolation in perceptual color space

### Example 3

Input:

  start=[0, 0], end=[100, 100], parameter=0.25

Output:

  [25, 25]

Notes:

  Array interpolation element-wise
