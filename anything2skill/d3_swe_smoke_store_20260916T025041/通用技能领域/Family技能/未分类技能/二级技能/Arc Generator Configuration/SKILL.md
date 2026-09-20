---
id: "35f30758-446c-51fe-9b26-fe9ef5810a3c"
name: "Arc Generator Configuration"
description: "Configure and generate circular or annular sectors for pie and donut charts by setting radius, angle, padding, and rendering parameters."
version: "0.1.0"
tags:
  - "d3"
  - "chart"
  - "arc"
  - "pie"
  - "donut"
  - "geometry"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Building pie charts or donut charts"
  - "Need to define arc geometry with custom radius, angles, or padding"
  - "Rendering radial sector visualizations"
---

# Arc Generator Configuration

Configure and generate circular or annular sectors for pie and donut charts by setting radius, angle, padding, and rendering parameters.

## Prompt

Use this skill to create a reusable arc generator for chart visualization. Initialize with d3.arc(), then chain configuration methods to set inner radius, outer radius, start angle, end angle, padding angle, corner radius, rendering context, and output precision. Call the configured generator with datum objects to produce SVG path data for sectors.

## Objective

Create and customize arc shapes for chart visualization
## Applicable Signals

- Chart type is circular or annular sector-based
- Caller has datum objects with angle and radius properties
- SVG path output is required for rendering

## Contraindications

- Rendering non-circular shapes
- Working with linear or rectangular chart types
- No arc or sector geometry required

## Workflow Steps

- {'step': 1, 'action': 'Initialize arc generator', 'detail': 'Call d3.arc() to create a new arc generator instance'}
- {'step': 2, 'action': 'Configure radius parameters', 'detail': 'Set innerRadius() and outerRadius() to define annular geometry; both accept numeric values or accessor functions'}
- {'step': 3, 'action': 'Configure angle parameters', 'detail': 'Set startAngle() and endAngle() to define sector span; both accept numeric values or accessor functions'}
- {'step': 4, 'action': 'Configure padding and corner radius', 'detail': 'Optionally set padAngle(), padRadius(), and cornerRadius() for spacing and rounded corners'}
- {'step': 5, 'action': 'Set rendering context and precision', 'detail': 'Optionally set context() for canvas rendering and digits() for output precision'}
- {'step': 6, 'action': 'Generate arc path data', 'detail': 'Call the configured generator with datum objects to produce SVG path strings or canvas drawing commands'}

## Constraints

- Arc generator must be initialized before configuration
- Radius values must be non-negative
- Start angle and end angle must be numeric
- Padding angle must not exceed the arc span

## Cautions

- Corner radius may produce unexpected results if larger than arc thickness
- Padding radius linearization affects visual spacing between adjacent arcs
- Output precision (digits) affects SVG path string length and rendering accuracy

## Output Contract

- A configured arc generator object capable of producing SVG path data (or canvas drawing commands) for sectors with specified inner/outer radius, start/end angles, corner rounding, and padding. The generator returns a path string or executes canvas operations when invoked with datum objects.

## 子技能目录
- [Arc Centroid Calculation](通用技能领域/Family技能/未分类技能/微技能/Arc Centroid Calculation/SKILL.md) ｜ 适用：Compute the midpoint or centroid of an arc sector for label placement or annotation positioning in pie and donut charts.
- [Arc Rendering Context Configuration](通用技能领域/Family技能/未分类技能/微技能/Arc Rendering Context Configuration/SKILL.md) ｜ 适用：Configure the rendering context (canvas or SVG) and output precision for arc path generation in D3. This micro-skill isolates the output format setup from arc geometry definition, enabling callers to switch rendering targets or adjust numerical precision independently.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Arc Centroid Calculation` 时，优先调用它。 线索：Need to place text labels at the center of pie or donut chart slices, Positioning icons or annotations within arc sectors, Require precise centroid coordinates for element alignment, d3, arc
- 当目标、阶段或方法更接近 `Arc Rendering Context Configuration` 时，优先调用它。 线索：Switching between SVG and canvas rendering targets, Adjusting numerical precision for arc path output, Optimizing file size or rendering performance through digit reduction, d3, arc

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building pie charts or donut charts
- Need to define arc geometry with custom radius, angles, or padding
- Rendering radial sector visualizations
