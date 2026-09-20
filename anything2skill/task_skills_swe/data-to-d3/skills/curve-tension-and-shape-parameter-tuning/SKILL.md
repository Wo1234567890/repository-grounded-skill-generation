---
id: "cfee6ac1-7b4d-5ef2-b967-818ad4fa46bd"
name: "Curve tension and shape parameter tuning"
description: "Adjust curve shape properties such as bundle tension (beta), cardinal spline tension, or Catmull–Rom alpha to fine-tune interpolation behavior and visual appearance."
version: "0.1.0"
tags:
  - "curve_interpolation"
  - "parameter_tuning"
  - "shape_refinement"
  - "d3_curves"
triggers:
  - "Curve output is too tight, too loose, or does not match desired aesthetic; need to adjust tension or alpha on cardinal, bundle, or Catmull–Rom curves."
---

# Curve tension and shape parameter tuning

Adjust curve shape properties such as bundle tension (beta), cardinal spline tension, or Catmull–Rom alpha to fine-tune interpolation behavior and visual appearance.

## Prompt

Select the appropriate parameter setter for your curve type: use bundle.beta for bundle curves, cardinal.tension for cardinal curves, or catmullRom.alpha for Catmull–Rom curves. Apply the parameter adjustment after curve selection and before rendering to achieve the desired shape.

## Objective

Tune curve shape parameters to refine interpolation behavior
## Applicable Signals

- Curve output is too tight or too loose
- Visual appearance does not match desired aesthetic
- Need to adjust tension on cardinal or bundle curves
- Need to adjust alpha on Catmull–Rom curves

## Contraindications

- Using linear, step, or natural curves (which have no tunable parameters)
- Curve shape is already acceptable
- No visual feedback available to validate adjustment

## Intervention Moves

- Set bundle.beta to control bundle curve tension
- Set cardinal.tension to control cardinal spline tension
- Set catmullRom.alpha to control Catmull–Rom parameter

## Constraints

- Parameter adjustment must occur after curve type selection
- Parameter adjustment must occur before final rendering
- Only applicable to cardinal, bundle, and Catmull–Rom curve families

## Cautions

- Extreme parameter values may produce unexpected or degenerate shapes
- Parameter effects are curve-family-specific; cardinal.tension does not apply to bundle curves

## Output Contract

- Curve re-rendered with adjusted tension or alpha parameter, producing visually distinct shape change observable in output.

## Triggers

- Curve output is too tight, too loose, or does not match desired aesthetic; need to adjust tension or alpha on cardinal, bundle, or Catmull–Rom curves.
