---
id: "1c7e4db5-298c-5ca8-a406-0519cc434ad9"
name: "Select and apply easing function"
description: "Choose an easing function from a family (linear, polynomial, quadratic, cubic, sinusoidal, exponential, circular, elastic, back, or bounce) and apply it to transform normalized animation time (0–1) into an eased progression curve. Use when smooth animation transitions require specific acceleration or deceleration behavior."
version: "0.1.0"
tags:
  - "animation"
  - "easing"
  - "time_normalization"
  - "interpolation"
  - "transition"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Animating visual properties (position, opacity, scale) and need non-linear time progression; normalized time value (0–1) is available"
examples:
  - input: "time=0.5, easing=easeQuadInOut"
    output: "0.5 (quadratic symmetric easing applied)"
    notes: "Quadratic InOut produces smooth acceleration then deceleration"
  - input: "time=0.3, easing=easeElasticOut with amplitude=1.0, period=0.3"
    output: "~0.28 (elastic overshoot applied)"
    notes: "Elastic easing creates rubber-band-like oscillation on exit"
  - input: "time=0.7, easing=easeLinear"
    output: "0.7 (identity function)"
    notes: "Linear easing returns time unchanged; useful as baseline"
---

# Select and apply easing function

Choose an easing function from a family (linear, polynomial, quadratic, cubic, sinusoidal, exponential, circular, elastic, back, or bounce) and apply it to transform normalized animation time (0–1) into an eased progression curve. Use when smooth animation transitions require specific acceleration or deceleration behavior.

## Prompt

Given a normalized time value t ∈ [0, 1] and a target easing family, select the appropriate easing function variant (e.g., easePolyIn, easeQuadOut, easeCubicInOut) and apply it to produce an eased time value. Optionally configure family-specific parameters (e.g., polynomial exponent, elastic amplitude/period, back overshoot) before application.

## Objective

Transform normalized time using selected easing curve
## Applicable Signals

- Animating visual properties (position, opacity, scale, rotation)
- Normalized time value (0–1) is available
- Non-linear time progression is desired
- Smooth acceleration or deceleration curve is required

## Contraindications

- Static rendering without animation
- Time values outside 0–1 range without prior normalization
- Real-time physics simulation requiring frame-independent calculations
- Discrete or step-based animation (use step easing or no easing)

## Intervention Moves

- Select easing family (poly, quad, cubic, sin, exp, circle, elastic, back, bounce, or linear)
- Choose direction variant (In, Out, InOut) if applicable
- Configure family-specific parameters (exponent, amplitude, period, overshoot)
- Apply easing function to normalized time
- Return eased time value for downstream interpolation

## Constraints

- Input time must be normalized to [0, 1]
- Output is always in [0, 1] range
- Easing function must be selected before application
- Family-specific parameters (if used) must be set before calling ease function

## Cautions

- Elastic and bounce easing may overshoot or undershoot; verify visual result
- Back easing with high overshoot can produce unexpected negative intermediate values
- Polynomial exponent must be positive; default is 3 for cubic

## Output Contract

- Eased time value (number in [0, 1]) suitable for interpolating animation keyframes or property values downstream

## Example Therapist Responses

### Example 1

- Client/Input: time=0.5, easing=easeQuadInOut
- Therapist/Output: 0.5 (quadratic symmetric easing applied)
- Notes: Quadratic InOut produces smooth acceleration then deceleration

### Example 2

- Client/Input: time=0.3, easing=easeElasticOut with amplitude=1.0, period=0.3
- Therapist/Output: ~0.28 (elastic overshoot applied)
- Notes: Elastic easing creates rubber-band-like oscillation on exit

### Example 3

- Client/Input: time=0.7, easing=easeLinear
- Therapist/Output: 0.7 (identity function)
- Notes: Linear easing returns time unchanged; useful as baseline

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Animating visual properties (position, opacity, scale) and need non-linear time progression; normalized time value (0–1) is available

## Examples

### Example 1

Input:

  time=0.5, easing=easeQuadInOut

Output:

  0.5 (quadratic symmetric easing applied)

Notes:

  Quadratic InOut produces smooth acceleration then deceleration

### Example 2

Input:

  time=0.3, easing=easeElasticOut with amplitude=1.0, period=0.3

Output:

  ~0.28 (elastic overshoot applied)

Notes:

  Elastic easing creates rubber-band-like oscillation on exit

### Example 3

Input:

  time=0.7, easing=easeLinear

Output:

  0.7 (identity function)

Notes:

  Linear easing returns time unchanged; useful as baseline
