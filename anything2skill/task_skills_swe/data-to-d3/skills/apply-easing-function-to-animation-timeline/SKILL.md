---
id: "94082bf4-4c85-5157-8175-5c49e31557e4"
name: "Apply easing function to animation timeline"
description: "Select and apply an easing function to a normalized time value (0–1) to produce a smooth, non-linear motion curve for animation. Supports linear, polynomial, quadratic, cubic, sinusoidal, exponential, circular, elastic, back, and bounce easing modes."
version: "0.1.0"
tags:
  - "animation"
  - "easing"
  - "timing"
  - "motion"
  - "interpolation"
triggers:
  - "animating visual properties (position, opacity, scale)"
  - "normalized time value (0–1) is available"
  - "smooth non-linear motion is required"
---

# Apply easing function to animation timeline

Select and apply an easing function to a normalized time value (0–1) to produce a smooth, non-linear motion curve for animation. Supports linear, polynomial, quadratic, cubic, sinusoidal, exponential, circular, elastic, back, and bounce easing modes.

## Prompt

Given a normalized time value between 0 and 1, select an appropriate easing function based on the desired motion effect (e.g., easeLinear for constant speed, easeQuadIn for acceleration, easeBounceOut for bounce effect). Apply the easing function to transform the time value. Return the eased time value (still in 0–1 range) for use in downstream interpolation.

## Objective

transform normalized time value using selected easing curve
## Applicable Signals

- animation frame tick with elapsed time
- time normalization complete (0 ≤ t ≤ 1)
- easing mode specified or selected

## Contraindications

- animation is instantaneous or discrete (no time progression)
- no time normalization available
- easing is not required for the visual effect

## Workflow Steps

- Receive normalized time value t (0 ≤ t ≤ 1)
- Select easing function based on desired motion effect
- Apply easing function: eased_t = easing_function(t)
- Return eased_t for interpolation into target property

## Constraints

- input time value must be in range [0, 1]
- easing function must be selected before application
- output must remain in range [0, 1] for safe interpolation

## Cautions

- elastic and bounce easing may overshoot or undershoot; verify amplitude and period parameters if customization is needed
- easing function selection affects perceived motion quality; test with target visual property

## Output Contract

- Eased time value in range [0, 1], ready for interpolation into target animation property (position, opacity, scale, etc.)

## Triggers

- animating visual properties (position, opacity, scale)
- normalized time value (0–1) is available
- smooth non-linear motion is required
