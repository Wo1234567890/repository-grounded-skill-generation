---
id: "b5944d1a-ddcf-5572-944b-ef169857829b"
name: "Configure easing function parameters"
description: "Set configurable parameters (exponent, amplitude, period, overshoot) on easing function instances to customize the shape and intensity of animation curves."
version: "0.1.0"
tags:
  - "animation"
  - "easing"
  - "parameterization"
  - "curve-customization"
  - "d3-ease"
triggers:
  - "easing function supports tunable parameters"
  - "default curve shape is not suitable for animation intent"
  - "animation setup phase before execution"
---

# Configure easing function parameters

Set configurable parameters (exponent, amplitude, period, overshoot) on easing function instances to customize the shape and intensity of animation curves.

## Prompt

Identify which easing function supports tunable parameters. Apply the appropriate parameter setter (poly.exponent, elastic.amplitude, elastic.period, or back.overshoot) to the easing function instance before passing it to animation execution. Verify the parameter value is within valid range for the easing type.

## Objective

customize easing curve behavior via parameter adjustment
## Applicable Signals

- poly.exponent available on polynomial easing functions
- elastic.amplitude available on elastic easing functions
- elastic.period available on elastic easing functions
- back.overshoot available on anticipatory easing functions

## Contraindications

- easing function has no configurable parameters (e.g., easeLinear)
- animation curve is already finalized
- parameter setter is not defined for the chosen easing type

## Workflow Steps

- Select easing function instance (e.g., d3.easePoly, d3.easeElastic, d3.easeBack)
- Check if easing function supports parameter configuration
- Apply parameter setter with desired value (exponent, amplitude, period, or overshoot)
- Validate parameter application succeeded
- Return configured easing function instance for animation use

## Constraints

- parameter must be compatible with the easing function type
- parameter value must be within valid numeric range
- configuration must occur before animation execution begins

## Cautions

- Not all easing functions support parameters; verify before attempting configuration
- Parameter values may have domain-specific constraints (e.g., exponent > 0, amplitude > 0)

## Output Contract

- Configured easing function instance with custom parameters applied and ready for animation execution.

## Triggers

- easing function supports tunable parameters
- default curve shape is not suitable for animation intent
- animation setup phase before execution
