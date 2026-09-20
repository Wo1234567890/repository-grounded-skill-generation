---
id: "5b237ffe-8a31-54dd-9a54-1764ef74b89d"
name: "Configure parametric easing variant"
description: "Set optional parameters (exponent for polynomial, amplitude and period for elastic, overshoot for back) to customize easing curve behavior before animation application."
version: "0.1.0"
tags:
  - "animation"
  - "easing"
  - "parameter_configuration"
  - "curve_tuning"
  - "d3-ease"
triggers:
  - "Easing function supports parameterization (poly, elastic, or back family)"
  - "Default easing curve shape does not match animation intent"
  - "Fine-tuning of animation acceleration or deceleration curve is required"
examples:
  - input: "easing family: poly, desired exponent: 3"
    output: "d3.easePoly.exponent(3) returns configured polynomial easing function"
    notes: "Cubic polynomial easing with exponent 3"
  - input: "easing family: elastic, desired amplitude: 1.5, period: 0.4"
    output: "d3.easeElastic.amplitude(1.5).period(0.4) returns configured elastic easing function"
    notes: "Chained parameter configuration for elastic easing"
  - input: "easing family: back, desired overshoot: 2"
    output: "d3.easeBack.overshoot(2) returns configured back easing function"
    notes: "Anticipatory easing with increased overshoot"
---

# Configure parametric easing variant

Set optional parameters (exponent for polynomial, amplitude and period for elastic, overshoot for back) to customize easing curve behavior before animation application.

## Prompt

Identify the easing family being used. If it supports parameterization (poly, elastic, or back), call the appropriate parameter setter method with the desired value. Verify the configured easing function object is returned and ready for time normalization input.

## Objective

Adjust easing curve parameters to match animation intent
## Applicable Signals

- poly.exponent method available
- elastic.amplitude method available
- elastic.period method available
- back.overshoot method available

## Contraindications

- Using non-parametric easing functions (easeLinear, easeQuadIn, easeCubicOut, easeSinIn, easeExpOut, easeCircleIn, etc.)
- Easing variant does not expose parameter setter methods
- Animation curve shape is already acceptable with default parameters

## Workflow Steps

- Identify the easing family (poly, elastic, or back)
- Verify the easing variant exposes the required parameter method
- Call the parameter setter with the desired value (exponent, amplitude, period, or overshoot)
- Confirm the configured easing function object is returned
- Pass the configured function to animation time normalization

## Constraints

- Parameter configuration must occur before passing easing function to animation time normalization
- Only poly, elastic, and back easing families support parameterization
- Parameter values must be within valid ranges for the easing family

## Output Contract

- Configured easing function object with custom parameters, ready for time normalization input in animation sequence

## Example Therapist Responses

### Example 1

- Client/Input: easing family: poly, desired exponent: 3
- Therapist/Output: d3.easePoly.exponent(3) returns configured polynomial easing function
- Notes: Cubic polynomial easing with exponent 3

### Example 2

- Client/Input: easing family: elastic, desired amplitude: 1.5, period: 0.4
- Therapist/Output: d3.easeElastic.amplitude(1.5).period(0.4) returns configured elastic easing function
- Notes: Chained parameter configuration for elastic easing

### Example 3

- Client/Input: easing family: back, desired overshoot: 2
- Therapist/Output: d3.easeBack.overshoot(2) returns configured back easing function
- Notes: Anticipatory easing with increased overshoot

## Triggers

- Easing function supports parameterization (poly, elastic, or back family)
- Default easing curve shape does not match animation intent
- Fine-tuning of animation acceleration or deceleration curve is required

## Examples

### Example 1

Input:

  easing family: poly, desired exponent: 3

Output:

  d3.easePoly.exponent(3) returns configured polynomial easing function

Notes:

  Cubic polynomial easing with exponent 3

### Example 2

Input:

  easing family: elastic, desired amplitude: 1.5, period: 0.4

Output:

  d3.easeElastic.amplitude(1.5).period(0.4) returns configured elastic easing function

Notes:

  Chained parameter configuration for elastic easing

### Example 3

Input:

  easing family: back, desired overshoot: 2

Output:

  d3.easeBack.overshoot(2) returns configured back easing function

Notes:

  Anticipatory easing with increased overshoot
