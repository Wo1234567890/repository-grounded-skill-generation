---
id: "726039b4-3da3-57da-a3cf-343fc81b9c57"
name: "Pie Chart Angle Computation"
description: "Generate arc angles from tabular data for pie or donut chart visualization. Configures value mapping, sort order, angular bounds, and inter-arc padding to produce angles ready for SVG rendering."
version: "0.1.0"
tags:
  - "pie_chart"
  - "donut_chart"
  - "angle_computation"
  - "data_visualization"
  - "arc_generation"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to render categorical or part-to-whole data as pie or donut chart; have tabular dataset with numeric values"
---

# Pie Chart Angle Computation

Generate arc angles from tabular data for pie or donut chart visualization. Configures value mapping, sort order, angular bounds, and inter-arc padding to produce angles ready for SVG rendering.

## Prompt

Use this skill when you have a tabular dataset with numeric values and need to compute arc angles for pie or donut chart visualization. Configure the value accessor to extract numeric values, set sort order if needed, define angular bounds (start and end angles), and optionally set padding between arcs. The skill outputs computed angles (start, end, padAngle) for each data element.

## Objective

Transform dataset into pie/donut chart arc angles
## Applicable Signals

- Need to render categorical or part-to-whole data as pie or donut chart
- Have tabular dataset with numeric values
- Preparing data for SVG path rendering

## Contraindications

- Data is continuous or time-series
- Chart type is not pie or donut
- Values are negative or zero-only
- Dataset lacks numeric value column

## Workflow Steps

- {'step': 1, 'action': 'Create pie generator instance', 'detail': 'Initialize d3.pie() to set up the angle computation engine'}
- {'step': 2, 'action': 'Configure value accessor', 'detail': 'Set pie.value() to extract numeric values from each data element'}
- {'step': 3, 'action': 'Set sort order (optional)', 'detail': 'Use pie.sort() or pie.sortValues() to define comparison order; omit for input order'}
- {'step': 4, 'action': 'Define angular bounds', 'detail': 'Set pie.startAngle() and pie.endAngle() to control overall rotation and span (e.g., 0 to 2π for full circle)'}
- {'step': 5, 'action': 'Configure inter-arc padding (optional)', 'detail': 'Set pie.padAngle() to add spacing between adjacent arcs'}
- {'step': 6, 'action': 'Compute angles', 'detail': 'Call pie(dataset) to generate arc angles for each element'}

## Constraints

- All values must be non-negative numbers
- Dataset must be iterable (array or array-like)
- Value accessor must return a number for each element
- Angular bounds must be valid (startAngle < endAngle or equal for zero-span)

## Cautions

- Zero or negative values will be treated as zero and may produce unexpected visual results
- Sorting is applied before angle computation; sort order affects visual layout
- padAngle is applied proportionally; very large padAngle may cause overlapping arcs

## Output Contract

- Returns array of objects, one per input data element, each containing computed start angle, end angle, and padAngle properties ready for SVG arc path generation

## 子技能目录
- [Pie Generator Configuration](通用技能领域/Family技能/未分类技能/微技能/Pie Generator Configuration/SKILL.md) ｜ 适用：Configure a pie chart generator by setting value accessor, sort comparators, angular bounds, and arc padding. Each configuration method returns the generator for method chaining.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Pie Generator Configuration` 时，优先调用它。 线索：Initializing a new pie generator instance, Need to customize value extraction from dataset, Require non-default sort order for pie slices, Must set custom start angle, end angle, or padding between arcs, d3

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to render categorical or part-to-whole data as pie or donut chart; have tabular dataset with numeric values
