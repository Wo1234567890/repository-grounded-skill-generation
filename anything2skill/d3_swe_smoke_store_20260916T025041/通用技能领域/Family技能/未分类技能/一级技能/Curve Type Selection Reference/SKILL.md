---
id: "cde8290a-5028-5b00-a8de-2e29cd699933"
name: "Curve Type Selection Reference"
description: "Canonical reference for selecting appropriate D3 curve interpolation methods based on shape requirements. Provides lookup of curve type properties (closure, continuity, tangent behavior, monotonicity, parameters) to inform curve selection decisions during planning phase."
version: "0.1.0"
tags:
  - "d3"
  - "curve_interpolation"
  - "spline"
  - "reference"
  - "shape_rendering"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Evaluating which curve type best fits shape requirements"
  - "Comparing monotonicity, closure, or tangent behavior"
  - "Documenting curve selection rationale"
examples:
  - input: "Shape requirement: smooth closed curve with natural continuity"
    output: "Select curveCatmullRomClosed or curveBasisClosed; curveCatmullRomClosed offers alpha parameter for control, curveBasisClosed repeats endpoints"
    notes: "Both are closed; choose based on whether endpoint repetition is desired"
  - input: "Shape requirement: preserve monotonicity in x-axis while interpolating y values"
    output: "Select curveMonotoneX; this cubic spline preserves x-monotonicity in y output"
    notes: "Verify data is monotonic in x before selection"
  - input: "Shape requirement: piecewise constant function with step transitions"
    output: "Select curveStep, curveStepAfter, or curveStepBefore depending on step timing preference"
    notes: "All three are piecewise constant; differ only in when the step occurs relative to points"
---

# Curve Type Selection Reference

Canonical reference for selecting appropriate D3 curve interpolation methods based on shape requirements. Provides lookup of curve type properties (closure, continuity, tangent behavior, monotonicity, parameters) to inform curve selection decisions during planning phase.

## Prompt

Use this reference to compare and select appropriate curve interpolation methods. Each curve type has distinct mathematical properties: basis splines repeat endpoints; cardinal and Catmull–Rom splines use tension/alpha parameters; monotone curves preserve monotonicity in one axis; step curves produce piecewise constant functions; natural splines use cubic interpolation without parameters. Consult this catalog when evaluating shape requirements before rendering.

## Objective

Provide lookup and comparison of curve types for informed selection decision
## Applicable Signals

- Evaluating which curve type best fits shape requirements
- Comparing monotonicity, closure, or tangent behavior
- Documenting curve selection rationale
- Selecting between basis, cardinal, Catmull–Rom, monotone, step, or natural curves

## Contraindications

- Do not use when actively rendering curves or executing point sequences
- Do not use when curve type is already determined and execution is underway
- Not applicable for real-time curve rendering without prior selection phase

## Workflow Steps

- {'step': 1, 'action': 'Identify shape requirements', 'detail': 'Determine closure (open/closed), tangent behavior (horizontal/vertical/natural), and monotonicity constraints'}
- {'step': 2, 'action': 'Consult curve catalog', 'detail': 'Review available curve types: Basis (curveBasis, curveBasisClosed, curveBasisOpen), Cardinal (curveCardinal, curveCardinalClosed, curveCardinalOpen), Catmull–Rom (curveCatmullRom, curveCatmullRomClosed, curveCatmullRomOpen), Bump (curveBumpX, curveBumpY), Monotone (curveMonotoneX, curveMonotoneY), Step (curveStep, curveStepAfter, curveStepBefore), Linear (curveLinear, curveLinearClosed), Natural (curveNatural)'}
- {'step': 3, 'action': 'Match properties to requirements', 'detail': 'Cross-reference closure, continuity, tangent behavior, and parameter availability against shape needs'}
- {'step': 4, 'action': 'Document selection rationale', 'detail': 'Record chosen curve type and justification for traceability'}

## Constraints

- This is a reference asset; it does not execute curve rendering
- Lookup and comparison only; parameter tuning requires separate execution skill
- Assumes caller has basic understanding of spline mathematics

## Cautions

- Cardinal and Catmull–Rom splines require tension/alpha parameter tuning; default values may not suit all shapes
- Monotone curves preserve monotonicity in one axis only; verify axis alignment matches data
- Step curves produce discontinuous derivatives; use only for piecewise constant requirements
- Basis splines repeat endpoints; verify this behavior is acceptable for your shape

## Output Contract

- Clear understanding of curve type properties, parameter ranges, and applicability constraints sufficient for informed curve selection decision

## Example Therapist Responses

### Example 1

- Client/Input: Shape requirement: smooth closed curve with natural continuity
- Therapist/Output: Select curveCatmullRomClosed or curveBasisClosed; curveCatmullRomClosed offers alpha parameter for control, curveBasisClosed repeats endpoints
- Notes: Both are closed; choose based on whether endpoint repetition is desired

### Example 2

- Client/Input: Shape requirement: preserve monotonicity in x-axis while interpolating y values
- Therapist/Output: Select curveMonotoneX; this cubic spline preserves x-monotonicity in y output
- Notes: Verify data is monotonic in x before selection

### Example 3

- Client/Input: Shape requirement: piecewise constant function with step transitions
- Therapist/Output: Select curveStep, curveStepAfter, or curveStepBefore depending on step timing preference
- Notes: All three are piecewise constant; differ only in when the step occurs relative to points

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Evaluating which curve type best fits shape requirements
- Comparing monotonicity, closure, or tangent behavior
- Documenting curve selection rationale

## Examples

### Example 1

Input:

  Shape requirement: smooth closed curve with natural continuity

Output:

  Select curveCatmullRomClosed or curveBasisClosed; curveCatmullRomClosed offers alpha parameter for control, curveBasisClosed repeats endpoints

Notes:

  Both are closed; choose based on whether endpoint repetition is desired

### Example 2

Input:

  Shape requirement: preserve monotonicity in x-axis while interpolating y values

Output:

  Select curveMonotoneX; this cubic spline preserves x-monotonicity in y output

Notes:

  Verify data is monotonic in x before selection

### Example 3

Input:

  Shape requirement: piecewise constant function with step transitions

Output:

  Select curveStep, curveStepAfter, or curveStepBefore depending on step timing preference

Notes:

  All three are piecewise constant; differ only in when the step occurs relative to points
