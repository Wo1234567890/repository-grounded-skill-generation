---
id: "b83453c5-ba47-5052-b5eb-134ded68dfae"
name: "Curve interpolation selection"
description: "Select and configure an appropriate curve interpolation method based on desired shape continuity and tangent behavior. Choose from basis, cardinal, Catmull–Rom, monotone, natural, step, or linear splines, with support for closed and open variants."
version: "0.1.0"
tags:
  - "curve_interpolation"
  - "shape_rendering"
  - "d3_path"
  - "spline_selection"
  - "configuration"
triggers:
  - "Preparing to interpolate points into a continuous curve"
  - "Need to decide between smooth splines, closed curves, or piecewise functions"
  - "Configuring a path or area generator before rendering"
examples:
  - input: "Smooth general-purpose curve needed for line chart"
    output: "d3.curveBasis selected; passed to line generator"
    notes: "Basis spline repeats end points for natural closure"
  - input: "Closed shape required; smooth interpolation preferred"
    output: "d3.curveBasisClosed selected; configured for area rendering"
    notes: "Closed variant ensures loop back to start"
  - input: "Data must remain monotone in x-axis; smooth curve desired"
    output: "d3.curveMonotoneX selected with default parameters"
    notes: "Preserves x-monotonicity while smoothing y values"
---

# Curve interpolation selection

Select and configure an appropriate curve interpolation method based on desired shape continuity and tangent behavior. Choose from basis, cardinal, Catmull–Rom, monotone, natural, step, or linear splines, with support for closed and open variants.

## Prompt

Evaluate the shape continuity requirements and tangent behavior needed for your visualization. Select a curve type from the available interpolators: use basis splines for smooth general-purpose curves, cardinal or Catmull–Rom for controllable tension, monotone variants to preserve axis monotonicity, natural for smooth interpolation without parameters, step functions for piecewise constant data, or linear for simple polylines. Configure tension or alpha parameters if the chosen curve type supports them. Return the configured curve interpolator object ready to receive point data.

## Objective

Choose and configure curve type for shape rendering
## Applicable Signals

- Shape continuity requirement specified
- Tangent behavior preference identified
- Data monotonicity constraint present
- Closed vs. open curve decision needed

## Contraindications

- Already committed to a specific curve type
- Rendering discrete points without interpolation
- Working with non-2D data
- Curve type is dynamically determined by external system

## Workflow Steps

- {'step': 1, 'action': 'Identify shape continuity requirement', 'detail': 'Determine if smooth curves, piecewise constant, or simple polylines are needed'}
- {'step': 2, 'action': 'Assess tangent behavior', 'detail': 'Decide if horizontal (BumpX), vertical (BumpY), or automatic tangents are required'}
- {'step': 3, 'action': 'Check for monotonicity constraint', 'detail': 'If data must remain monotone in x or y, select MonotoneX or MonotoneY'}
- {'step': 4, 'action': 'Determine if curve must be closed', 'detail': 'Select Closed variant if shape must loop back to start point'}
- {'step': 5, 'action': 'Select base curve type', 'detail': 'Choose from Basis, Cardinal, CatmullRom, Natural, Step, or Linear'}
- {'step': 6, 'action': 'Configure optional parameters', 'detail': 'Set tension (Cardinal, Bundle) or alpha (CatmullRom) if applicable'}
- {'step': 7, 'action': 'Return configured interpolator', 'detail': 'Pass curve object to path or area generator'}

## Constraints

- Curve selection must precede point addition
- Tension and alpha parameters are curve-type-specific
- Closed variants require compatible point sequences

## Cautions

- Cardinal and Catmull–Rom splines require tension/alpha tuning for desired smoothness
- Monotone variants preserve monotonicity only in the specified axis
- Step functions produce discontinuous derivatives at segment boundaries

## Output Contract

- Curve interpolator object (e.g., d3.curveBasis, d3.curveCardinal with tension set, d3.curveMonotoneX) selected, configured, and ready to receive point data via lineStart, point, and lineEnd calls.

## Example Executions

### Example 1

- Input: Smooth general-purpose curve needed for line chart
- Output: d3.curveBasis selected; passed to line generator
- Notes: Basis spline repeats end points for natural closure

### Example 2

- Input: Closed shape required; smooth interpolation preferred
- Output: d3.curveBasisClosed selected; configured for area rendering
- Notes: Closed variant ensures loop back to start

### Example 3

- Input: Data must remain monotone in x-axis; smooth curve desired
- Output: d3.curveMonotoneX selected with default parameters
- Notes: Preserves x-monotonicity while smoothing y values

## Triggers

- Preparing to interpolate points into a continuous curve
- Need to decide between smooth splines, closed curves, or piecewise functions
- Configuring a path or area generator before rendering

## Examples

### Example 1

Input:

  Smooth general-purpose curve needed for line chart

Output:

  d3.curveBasis selected; passed to line generator

Notes:

  Basis spline repeats end points for natural closure

### Example 2

Input:

  Closed shape required; smooth interpolation preferred

Output:

  d3.curveBasisClosed selected; configured for area rendering

Notes:

  Closed variant ensures loop back to start

### Example 3

Input:

  Data must remain monotone in x-axis; smooth curve desired

Output:

  d3.curveMonotoneX selected with default parameters

Notes:

  Preserves x-monotonicity while smoothing y values
