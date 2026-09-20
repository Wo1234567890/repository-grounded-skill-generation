---
id: "a5de0627-0e80-5765-baa7-fd826622d7b5"
name: "Linear Scale Construction and Configuration"
description: "Create and configure a quantitative linear scale by setting domain, range, and interpolation properties. Use when mapping continuous input values to continuous output values for visualization or data transformation."
version: "0.1.0"
tags:
  - "d3"
  - "scale"
  - "quantitative"
  - "mapping"
  - "visualization"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "need to map continuous domain values to continuous output range"
  - "building visualization axes or data encodings"
  - "preparing quantitative data for visual representation"
examples:
  - input: "domain=[0, 100], range=[0, 960]"
    output: "scale(50) returns 480; scale(0) returns 0; scale(100) returns 960"
    notes: "Basic linear mapping for visualization width."
  - input: "domain=[0, 1], rangeRound=[0, 255]"
    output: "scale(0.5) returns 128 (integer); scale(0.25) returns 64"
    notes: "Integer output for color channel encoding."
---

# Linear Scale Construction and Configuration

Create and configure a quantitative linear scale by setting domain, range, and interpolation properties. Use when mapping continuous input values to continuous output values for visualization or data transformation.

## Prompt

1. Create a linear scale using d3.scaleLinear().
2. Set the input domain using linear.domain([min, max]).
3. Set the output range using linear.range([min, max]) or linear.rangeRound([min, max]) for integer output.
4. Optionally configure interpolation using linear.interpolate(interpolator).
5. Verify the scale is ready by testing a sample domain value through the scale function.
6. Return the configured scale object for downstream value mapping.

## Objective

establish a reusable linear scale with domain-to-range mapping
## Applicable Signals

- input data is continuous and quantitative
- output requires linear transformation
- scale will be reused across multiple value mappings

## Contraindications

- domain is categorical or ordinal
- scale is identity or radial
- working with power or logarithmic transformations
- input values are discrete or non-numeric

## Workflow Steps

- {'step': 1, 'action': 'Create scale', 'detail': 'Invoke d3.scaleLinear() to instantiate a new linear scale.'}
- {'step': 2, 'action': 'Set domain', 'detail': 'Call linear.domain([minValue, maxValue]) with numeric bounds.'}
- {'step': 3, 'action': 'Set range', 'detail': 'Call linear.range([minOutput, maxOutput]) or linear.rangeRound([minOutput, maxOutput]).'}
- {'step': 4, 'action': 'Configure interpolation (optional)', 'detail': 'Call linear.interpolate(interpolatorFunction) if custom interpolation is needed.'}
- {'step': 5, 'action': 'Validate', 'detail': 'Test scale(testValue) with a sample domain value to confirm output is in expected range.'}
- {'step': 6, 'action': 'Return scale', 'detail': 'Return the configured scale object for use in value mapping operations.'}

## Constraints

- domain must be numeric and continuous
- range must be defined before scale is used for mapping
- interpolator must be compatible with range value types

## Cautions

- Ensure domain values span the full input data range to avoid clipping or extrapolation artifacts.
- Use rangeRound() only when integer output is required; standard range() offers finer precision.
- Test scale with boundary and mid-range values before deployment.

## Output Contract

- A configured linear scale object ready for value mapping. The scale accepts domain values and returns corresponding range values. The scale object supports chaining and can be queried for domain, range, and interpolation properties.

## Example Therapist Responses

### Example 1

- Client/Input: domain=[0, 100], range=[0, 960]
- Therapist/Output: scale(50) returns 480; scale(0) returns 0; scale(100) returns 960
- Notes: Basic linear mapping for visualization width.

### Example 2

- Client/Input: domain=[0, 1], rangeRound=[0, 255]
- Therapist/Output: scale(0.5) returns 128 (integer); scale(0.25) returns 64
- Notes: Integer output for color channel encoding.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- need to map continuous domain values to continuous output range
- building visualization axes or data encodings
- preparing quantitative data for visual representation

## Examples

### Example 1

Input:

  domain=[0, 100], range=[0, 960]

Output:

  scale(50) returns 480; scale(0) returns 0; scale(100) returns 960

Notes:

  Basic linear mapping for visualization width.

### Example 2

Input:

  domain=[0, 1], rangeRound=[0, 255]

Output:

  scale(0.5) returns 128 (integer); scale(0.25) returns 64

Notes:

  Integer output for color channel encoding.
