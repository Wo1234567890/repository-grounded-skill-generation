---
id: "4b65ad1e-5b45-5e0c-9d24-c0707b70d5d5"
name: "Area Edge Line Extraction"
description: "Extract individual edge lines (baseline, topline, or radial edges) from a configured area generator for separate rendering or styling."
version: "0.1.0"
tags:
  - "d3"
  - "area-chart"
  - "line-extraction"
  - "edge-rendering"
  - "shape-decomposition"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "need to render area edges separately"
  - "apply different stroke styles to baseline vs. topline"
  - "extract radial edge lines for independent styling"
examples:
  - input: "area generator configured with x, y0, y1 accessors; need to render baseline separately"
    output: "line generator from area.lineY0() that renders the baseline (y0 values) as a line path"
    notes: "baseline can now be styled with a different stroke color or width than the topline"
  - input: "areaRadial generator configured with angle, innerRadius, outerRadius accessors; need to extract inner edge"
    output: "line generator from areaRadial.lineInnerRadius() that renders the inner radial edge"
    notes: "inner edge can be rendered with independent styling in a separate pass"
---

# Area Edge Line Extraction

Extract individual edge lines (baseline, topline, or radial edges) from a configured area generator for separate rendering or styling.

## Prompt

Call the appropriate edge line method on your area or areaRadial generator to derive a line generator for one specific edge. Use lineX0, lineY0, lineX1, lineY1 for Cartesian areas, or lineStartAngle, lineInnerRadius, lineEndAngle, lineOuterRadius for radial areas. The returned line generator can then be invoked with your dataset to render that edge independently.

## Objective

derive a line generator from an area generator for one specific edge
## Applicable Signals

- area generator is configured and ready
- edge styling requirement differs from full area
- separate rendering pass for one or more edges is planned

## Contraindications

- rendering full area shape without edge decomposition
- edges do not need separate styling or rendering
- area generator not yet instantiated or configured

## Workflow Steps

- {'step': 1, 'action': 'Identify which edge(s) you need to extract: baseline (x0, y0), topline (x1, y1), or radial edges (startAngle, innerRadius, endAngle, outerRadius).'}
- {'step': 2, 'action': 'Call the corresponding edge line method on your configured area or areaRadial generator (e.g., area.lineX0(), areaRadial.lineInnerRadius()).'}
- {'step': 3, 'action': 'Invoke the returned line generator with your dataset to render the edge independently.'}
- {'step': 4, 'action': 'Apply custom styling (stroke, color, width) to the rendered edge as needed.'}

## Constraints

- edge line method must be called on a valid area or areaRadial generator
- dataset passed to derived line generator must match the original area dataset structure
- edge line generator inherits curve and context settings from parent area generator

## Cautions

- derived line generators share state with parent area; modifying parent configuration after extraction may affect edge rendering
- ensure dataset consistency between area and extracted edge line invocations

## Output Contract

- Returns a line generator object corresponding to one area edge, ready to render that edge independently with custom styling or in a separate rendering pass.

## Example Therapist Responses

### Example 1

- Client/Input: area generator configured with x, y0, y1 accessors; need to render baseline separately
- Therapist/Output: line generator from area.lineY0() that renders the baseline (y0 values) as a line path
- Notes: baseline can now be styled with a different stroke color or width than the topline

### Example 2

- Client/Input: areaRadial generator configured with angle, innerRadius, outerRadius accessors; need to extract inner edge
- Therapist/Output: line generator from areaRadial.lineInnerRadius() that renders the inner radial edge
- Notes: inner edge can be rendered with independent styling in a separate pass

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- need to render area edges separately
- apply different stroke styles to baseline vs. topline
- extract radial edge lines for independent styling

## Examples

### Example 1

Input:

  area generator configured with x, y0, y1 accessors; need to render baseline separately

Output:

  line generator from area.lineY0() that renders the baseline (y0 values) as a line path

Notes:

  baseline can now be styled with a different stroke color or width than the topline

### Example 2

Input:

  areaRadial generator configured with angle, innerRadius, outerRadius accessors; need to extract inner edge

Output:

  line generator from areaRadial.lineInnerRadius() that renders the inner radial edge

Notes:

  inner edge can be rendered with independent styling in a separate pass
