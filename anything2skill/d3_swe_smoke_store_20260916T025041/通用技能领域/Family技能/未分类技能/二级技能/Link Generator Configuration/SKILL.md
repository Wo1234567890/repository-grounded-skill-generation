---
id: "120baec5-2dd0-5275-9f9a-8b7fc6f38728"
name: "Link Generator Configuration"
description: "Configure and instantiate D3 link generators (vertical, horizontal, or radial) with source, target, and coordinate accessors for rendering smooth cubic Bézier curves between nodes."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "link-generator"
  - "graph-rendering"
  - "accessor-binding"
  - "bezier-curve"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Building node-link diagrams with curved connectors"
  - "Setting up tree layout visualizations"
  - "Configuring force-directed graph rendering"
  - "Preparing data-driven link rendering with accessor-based binding"
---

# Link Generator Configuration

Configure and instantiate D3 link generators (vertical, horizontal, or radial) with source, target, and coordinate accessors for rendering smooth cubic Bézier curves between nodes.

## Prompt

Create a link generator by selecting the appropriate factory (d3.link, d3.linkVertical, d3.linkHorizontal, or d3.linkRadial). Bind source and target accessors to extract node references from data. Set coordinate accessors (x, y for Cartesian; angle, radius for radial). Optionally configure rendering context and output precision. The configured generator accepts a data array and produces SVG path strings or canvas commands.

## Objective

Set up a reusable link generator with custom accessors and rendering options
## Applicable Signals

- Data structure contains source and target node references
- Coordinate system is Cartesian (vertical/horizontal) or polar (radial)
- Rendering target is SVG or canvas context
- Multiple links share the same accessor logic

## Contraindications

- Rendering static SVG paths without accessor-based data binding
- Using pre-computed path strings instead of generator-based rendering
- Single one-off link without reusable accessor pattern

## Workflow Steps

- {'step': 1, 'action': 'Select link generator factory', 'detail': 'Choose d3.link, d3.linkVertical, d3.linkHorizontal, or d3.linkRadial based on layout orientation'}
- {'step': 2, 'action': 'Bind source accessor', 'detail': 'Call link.source(d => d.source) to extract source node from data element'}
- {'step': 3, 'action': 'Bind target accessor', 'detail': 'Call link.target(d => d.target) to extract target node from data element'}
- {'step': 4, 'action': 'Set coordinate accessors', 'detail': 'For Cartesian: link.x(d => d.x) and link.y(d => d.y); for radial: linkRadial.angle(d => d.angle) and linkRadial.radius(d => d.radius)'}
- {'step': 5, 'action': 'Configure optional rendering parameters', 'detail': 'Set link.context(canvasContext) for canvas rendering or link.digits(precision) for numeric precision if needed'}
- {'step': 6, 'action': 'Return configured generator', 'detail': 'Generator is now ready to accept data array and produce path strings or render commands'}

## Constraints

- Source and target accessors must return valid node objects or indices
- Coordinate accessors must return numeric values compatible with the chosen link type
- Context parameter required only for canvas rendering; omit for SVG
- Digits precision applies only to numeric output, not path commands

## Cautions

- Ensure accessor functions handle edge cases (null/undefined nodes)
- Verify coordinate ranges match the intended layout dimensions
- Test rendering context compatibility before production use

## Output Contract

- Configured link generator object with bound accessors, ready to accept data array and produce SVG path strings (via .toString() or direct rendering) or canvas rendering commands. Output is a smooth cubic Bézier curve path between source and target coordinates.

## 子技能目录
- [Link Rendering Context and Precision Control](通用技能领域/Family技能/未分类技能/微技能/Link Rendering Context and Precision Control/SKILL.md) ｜ 适用：Configure the rendering context (canvas or SVG) and output precision for link path generation. This micro-skill optimizes rendering performance and controls numerical precision in generated link paths.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Link Rendering Context and Precision Control` 时，优先调用它。 线索：Switching between canvas and SVG rendering backends, Tuning output file size or numerical precision for large datasets, Optimizing rendering performance for specific output format, d3, link-generation

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building node-link diagrams with curved connectors
- Setting up tree layout visualizations
- Configuring force-directed graph rendering
- Preparing data-driven link rendering with accessor-based binding
