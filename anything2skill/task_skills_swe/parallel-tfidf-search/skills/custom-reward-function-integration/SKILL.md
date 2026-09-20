---
id: "6f7e5bc6-904e-565f-aba8-be6b82fdcd9c"
name: "Custom Reward Function Integration"
description: "Execute atomic 2D affine transform operations (scale, translate, apply, invert, rescale) on coordinates and scale domains. Use for coordinate system conversions and scale domain adjustments in response to zoom or pan events."
version: "0.1.2"
tags:
  - "d3"
  - "transform"
  - "coordinate-conversion"
  - "zoom"
  - "pan"
  - "affine"
triggers:
  - "Integrating domain-specific or custom reward logic into GRPO training"
  - "Standard reward metrics do not capture desired completion quality"
  - "Need to evaluate completions against custom criteria"
examples:
  - input: "transform object with scale=2, translate=[10, 20]; point [5, 5]"
    output: "[20, 30]"
    notes: "Point is scaled by 2 and translated by [10, 20]"
  - input: "transform object; x-scale with domain [0, 100]"
    output: "New x-scale with domain adjusted to account for zoom transform"
    notes: "Rescaled domain is ready for axis redraw"
  - input: "transform object with scale=2, translate=[10, 20]; point [20, 30]"
    output: "[5, 5]"
    notes: "Inverted point maps back to original data space"
---

# Custom Reward Function Integration

Execute atomic 2D affine transform operations (scale, translate, apply, invert, rescale) on coordinates and scale domains. Use for coordinate system conversions and scale domain adjustments in response to zoom or pan events.

## Prompt

Execute single transform operations: scale a transform by a specified amount; translate a transform by a specified amount; apply the transform to points or coordinates; invert the transform to unapply it; rescale x or y scale domains by applying the transform. Each operation is atomic and reusable across zoom, pan, or custom coordinate conversion workflows.

## Objective

Execute single transform operations (scale, translate, invert, rescale) on coordinates or scales
## Applicable Signals

- zoom.transform() returns a transform object
- User interaction (zoom, pan) updates transform state
- Scale domain adjustment required after viewport change

## Contraindications

- 3D transforms or perspective projections
- Non-affine transformations (e.g., curved warping)
- Transform state is unavailable or null
- Coordinate system is not Cartesian

## Workflow Steps

- {'step': 1, 'action': 'Obtain or create a transform object (e.g., via d3.zoomTransform(element) or d3.zoomIdentity)', 'input': 'Element reference or identity transform'}
- {'step': 2, 'action': 'Select the operation: scale, translate, apply, invert, rescaleX, or rescaleY', 'input': 'Transform object and operation parameters (scale factor, translation vector, point, or scale)'}
- {'step': 3, 'action': 'Execute the operation and capture the result', 'output': 'Transformed coordinate, inverted coordinate, rescaled domain, or modified transform'}
- {'step': 4, 'action': 'Validate output (check for NaN, verify coordinate is in expected range)', 'validation': 'Output is numeric and within expected bounds'}

## Constraints

- Transform must be a valid 2D affine transform object
- Input coordinates must be numeric (x, y) pairs or scale domain values
- Operations assume left-to-right, top-to-bottom screen orientation

## Cautions

- Invert operations may fail or produce NaN if transform is singular (determinant = 0)
- Rescale operations modify scale domain; ensure scale is mutable before applying
- Chaining multiple transforms can accumulate floating-point error; consider recomputing from source when precision is critical

## Output Contract

- Returns a transformed coordinate (point or x/y value), an inverted coordinate, a rescaled scale domain, or a new transform object. The output is guaranteed to be a valid numeric value or object that can be used immediately by downstream rendering or scale operations.

## Example Executions

### Example 1

- Input: transform object with scale=2, translate=[10, 20]; point [5, 5]
- Output: [20, 30]
- Notes: Point is scaled by 2 and translated by [10, 20]

### Example 2

- Input: transform object; x-scale with domain [0, 100]
- Output: New x-scale with domain adjusted to account for zoom transform
- Notes: Rescaled domain is ready for axis redraw

### Example 3

- Input: transform object with scale=2, translate=[10, 20]; point [20, 30]
- Output: [5, 5]
- Notes: Inverted point maps back to original data space

## Triggers

- Integrating domain-specific or custom reward logic into GRPO training
- Standard reward metrics do not capture desired completion quality
- Need to evaluate completions against custom criteria

## Examples

### Example 1

Input:

  transform object with scale=2, translate=[10, 20]; point [5, 5]

Output:

  [20, 30]

Notes:

  Point is scaled by 2 and translated by [10, 20]

### Example 2

Input:

  transform object; x-scale with domain [0, 100]

Output:

  New x-scale with domain adjusted to account for zoom transform

Notes:

  Rescaled domain is ready for axis redraw

### Example 3

Input:

  transform object with scale=2, translate=[10, 20]; point [20, 30]

Output:

  [5, 5]

Notes:

  Inverted point maps back to original data space
