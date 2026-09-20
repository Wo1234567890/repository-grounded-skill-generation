---
id: "a3e2f109-bce4-589c-8d16-668135711221"
name: "Curve Interpolation Selection"
description: "Select and configure an appropriate curve interpolation method based on desired shape continuity and tangent behavior. Supports basis, cardinal, Catmull–Rom, monotone, natural, step, and linear splines with optional tension and alpha parameter tuning."
version: "0.1.0"
tags:
  - "d3"
  - "curve"
  - "interpolation"
  - "spline"
  - "shape_rendering"
  - "path_generation"
triggers:
  - "Preparing to render a continuous curve or path from discrete points"
  - "Need to balance smoothness, monotonicity preservation, or closed-loop behavior"
  - "Configuring shape interpolation before point addition"
---

# Curve Interpolation Selection

Select and configure an appropriate curve interpolation method based on desired shape continuity and tangent behavior. Supports basis, cardinal, Catmull–Rom, monotone, natural, step, and linear splines with optional tension and alpha parameter tuning.

## Prompt

Choose a curve interpolation type that matches your shape requirements. Basis splines offer smooth curves with endpoint repetition; cardinal and Catmull–Rom splines provide tunable tension/alpha for control over curvature; monotone splines preserve monotonicity in one axis; natural splines provide smooth cubic interpolation; step functions create piecewise constant transitions; linear produces polylines. Configure tension (cardinal) or alpha (Catmull–Rom) parameters if fine-tuning curvature is needed. Return the configured curve interpolator object ready to process point sequences.

## Objective

Choose curve type and set tension/alpha parameters for smooth shape rendering
## Applicable Signals

- Input: sequence of discrete points requiring smooth interpolation
- Input: requirement for closed vs. open curve
- Input: need to preserve monotonicity in x or y axis
- Input: desired curvature tension or smoothness level

## Contraindications

- Working with discrete point markers only (no interpolation needed)
- Rendering straight line segments without shape continuity
- No shape continuity or smoothing required
- Real-time performance constraints where simpler linear interpolation suffices

## Workflow Steps

- {'step': 1, 'action': 'Assess shape requirements', 'detail': 'Determine if closed loop, open curve, or piecewise constant behavior is needed'}
- {'step': 2, 'action': 'Evaluate continuity and tangent constraints', 'detail': 'Decide if horizontal/vertical tangents (Bump), monotonicity preservation (Monotone), or general smoothness (Basis, Cardinal, Catmull–Rom, Natural) is required'}
- {'step': 3, 'action': 'Select curve type', 'detail': 'Choose from d3.curveBasis, d3.curveCardinal, d3.curveCatmullRom, d3.curveMonotoneX, d3.curveMonotoneY, d3.curveNatural, d3.curveStep, d3.curveLinear, or their Closed/Open variants'}
- {'step': 4, 'action': 'Configure optional parameters', 'detail': 'If cardinal spline, set tension via cardinal.tension(value); if Catmull–Rom, set alpha via catmullRom.alpha(value)'}
- {'step': 5, 'action': 'Return configured interpolator', 'detail': 'Pass the curve object to downstream point-addition or rendering operations'}

## Constraints

- Tension parameter (cardinal splines) typically ranges 0–1
- Alpha parameter (Catmull–Rom) typically ranges 0–1
- Closed variants require matching start and end points
- Monotone splines require input points to be monotonic in the specified axis

## Cautions

- Closed curve variants require input points to form a closed loop; open variants do not repeat endpoints
- Monotone splines enforce monotonicity; non-monotonic input may produce unexpected results
- Tension and alpha values outside typical ranges (0–1) may produce extreme curvature or instability

## Output Contract

- Curve interpolator object configured with selected method and tension/alpha parameters, ready to accept point sequences via lineStart, lineEnd, point, areaStart, areaEnd methods

## Triggers

- Preparing to render a continuous curve or path from discrete points
- Need to balance smoothness, monotonicity preservation, or closed-loop behavior
- Configuring shape interpolation before point addition
