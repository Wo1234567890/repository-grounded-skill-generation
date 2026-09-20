---
id: "8ef64891-bac2-5d37-ada9-4bf8b822efa3"
name: "Pie Generator Configuration"
description: "Configure a pie chart generator by setting value accessor, sort comparators, angular bounds, and arc padding. Each configuration method returns the generator for method chaining."
version: "0.1.0"
tags:
  - "d3"
  - "pie-chart"
  - "configuration"
  - "data-visualization"
  - "chart-setup"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Initializing a new pie generator instance"
  - "Need to customize value extraction from dataset"
  - "Require non-default sort order for pie slices"
  - "Must set custom start angle, end angle, or padding between arcs"
examples:
  - input: "Dataset: [{name: 'A', count: 30}, {name: 'B', count: 20}]; need to extract count field, sort descending, use full circle"
    output: "pie.value(d => d.count).sort((a, b) => b - a).startAngle(0).endAngle(2 * Math.PI)"
    notes: "Method chaining allows fluent configuration"
  - input: "Need donut chart with 0.1 radian padding between slices"
    output: "pie.padAngle(0.1)"
    notes: "Padding is applied symmetrically around each arc"
---

# Pie Generator Configuration

Configure a pie chart generator by setting value accessor, sort comparators, angular bounds, and arc padding. Each configuration method returns the generator for method chaining.

## Prompt

Use pie generator configuration methods to customize how data values are extracted, sorted, and positioned as arc angles. Call configuration methods in sequence before passing data to the pie generator. Each method returns the generator instance to enable chaining.

## Objective

Configure pie generator properties for custom data visualization
## Applicable Signals

- pie generator created but not yet configured
- dataset structure requires custom value accessor
- sort order specification needed for slice ordering
- angular positioning or spacing customization required

## Contraindications

- Using default pie configuration without customization
- Generator already fully configured and locked for execution
- Data already computed; configuration phase complete

## Workflow Steps

- {'step': 1, 'action': 'Create pie generator instance', 'detail': 'Call d3.pie() to instantiate generator'}
- {'step': 2, 'action': 'Set value accessor', 'detail': 'Call pie.value(accessor_function) to specify how to extract numeric values from dataset objects'}
- {'step': 3, 'action': 'Set sort order', 'detail': 'Call pie.sort(comparator) or pie.sortValues(comparator) to define slice ordering'}
- {'step': 4, 'action': 'Set angular bounds', 'detail': 'Call pie.startAngle(angle) and pie.endAngle(angle) to define overall rotation range in radians'}
- {'step': 5, 'action': 'Set arc padding', 'detail': 'Call pie.padAngle(angle) to specify spacing between adjacent arcs in radians'}

## Constraints

- Configuration must occur before data computation
- Each method call returns the generator for chaining
- Angular values must be in radians
- Pad angle must be non-negative

## Cautions

- Ensure value accessor returns numeric values; non-numeric values will cause computation errors
- Start angle and end angle define the angular span; typical range is 0 to 2π
- Pad angle is applied between each pair of adjacent arcs; large values may cause visual overlap

## Output Contract

- Configured pie generator instance with all specified properties set, ready to accept dataset and compute arc angles

## Example Therapist Responses

### Example 1

- Client/Input: Dataset: [{name: 'A', count: 30}, {name: 'B', count: 20}]; need to extract count field, sort descending, use full circle
- Therapist/Output: pie.value(d => d.count).sort((a, b) => b - a).startAngle(0).endAngle(2 * Math.PI)
- Notes: Method chaining allows fluent configuration

### Example 2

- Client/Input: Need donut chart with 0.1 radian padding between slices
- Therapist/Output: pie.padAngle(0.1)
- Notes: Padding is applied symmetrically around each arc

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Initializing a new pie generator instance
- Need to customize value extraction from dataset
- Require non-default sort order for pie slices
- Must set custom start angle, end angle, or padding between arcs

## Examples

### Example 1

Input:

  Dataset: [{name: 'A', count: 30}, {name: 'B', count: 20}]; need to extract count field, sort descending, use full circle

Output:

  pie.value(d => d.count).sort((a, b) => b - a).startAngle(0).endAngle(2 * Math.PI)

Notes:

  Method chaining allows fluent configuration

### Example 2

Input:

  Need donut chart with 0.1 radian padding between slices

Output:

  pie.padAngle(0.1)

Notes:

  Padding is applied symmetrically around each arc
