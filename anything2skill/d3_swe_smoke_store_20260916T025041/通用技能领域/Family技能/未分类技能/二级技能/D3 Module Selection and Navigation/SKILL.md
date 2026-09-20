---
id: "95b45d8c-f58b-55ac-b11a-530eb8338eaa"
name: "D3 Module Selection and Navigation"
description: "Identify and select the appropriate D3 module based on visualization or data-handling task requirements, then navigate to its API documentation and relevant sub-modules."
version: "0.1.0"
tags:
  - "d3"
  - "module_discovery"
  - "visualization_planning"
  - "routing"
  - "api_navigation"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new D3 visualization project or adding a new capability (e.g., need to add color mapping, force simulation, or hierarchical layout)"
---

# D3 Module Selection and Navigation

Identify and select the appropriate D3 module based on visualization or data-handling task requirements, then navigate to its API documentation and relevant sub-modules.

## Prompt

When starting a new D3 project or adding a new capability, consult the D3 module taxonomy to route to the correct module. Match your task (e.g., color mapping, force simulation, hierarchical layout, data transformation) to the appropriate module category: Visualization (d3-scale, d3-selection, d3-shape, d3-geo, d3-hierarchy, d3-force, etc.), Animation (d3-transition, d3-ease, d3-timer), Interaction (d3-brush, d3-drag, d3-zoom), or Data (d3-array, d3-dsv, d3-fetch, d3-format). Once identified, access the module's API documentation and explore its sub-modules or functions.

## Objective

Route user to the correct D3 module for their visualization or data-handling task
## Applicable Signals

- Starting a new D3 visualization project
- Adding a new visualization capability (e.g., color mapping, force simulation, hierarchical layout)
- Need to handle data transformation or array operations
- Require animation or interaction features

## Contraindications

- Already inside a specific module's API documentation
- Executing code within a module; use only at project initiation or when switching modules
- Troubleshooting existing module-specific code

## Workflow Steps

- {'step': 1, 'action': 'Clarify task requirements', 'detail': 'Define what the visualization or data operation needs to accomplish (e.g., scale data, select DOM elements, draw shapes, simulate forces, transform hierarchies)'}
- {'step': 2, 'action': 'Map task to module category', 'detail': 'Match requirements to one of four categories: Visualization (rendering and layout), Animation (timing and transitions), Interaction (user input and brushing), or Data (array operations and file I/O)'}
- {'step': 3, 'action': 'Identify specific module', 'detail': 'Select the appropriate module from the category (e.g., d3-scale for quantitative mapping, d3-hierarchy for tree/cluster layouts, d3-force for physics simulations)'}
- {'step': 4, 'action': 'Access module documentation', 'detail': "Navigate to the module's API index and review available sub-modules and functions"}
- {'step': 5, 'action': 'Explore sub-modules', 'detail': "Review the module's sub-options (e.g., Linear scales, Time scales, Pow scales under d3-scale; or Arcs, Areas, Curves under d3-shape)"}

## Constraints

- Module selection must precede detailed API exploration
- Task requirements must be clearly defined before routing

## Cautions

- Ensure task scope aligns with a single primary module; complex tasks may require multiple modules in sequence

## Output Contract

- User has identified and accessed the correct D3 module documentation and its relevant sub-modules or functions, ready to proceed with API-level implementation.

## 子技能目录
- [Qualify and Resolve XML Namespaces](通用技能领域/Family技能/未分类技能/微技能/Qualify and Resolve XML Namespaces/SKILL.md) ｜ 适用：Resolve prefixed XML names (e.g., 'xlink:href') to their full namespace URIs and access built-in namespace definitions. Use when working with SVG, XML attributes, or DOM elements that require namespace qualification.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Qualify and Resolve XML Namespaces` 时，优先调用它。 线索：Setting or reading SVG/XML attributes with namespace prefixes, Need to look up standard namespace URIs (e.g., xlink, svg, xmlns), Qualifying element or attribute names for DOM or SVG operations, xml, namespace

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new D3 visualization project or adding a new capability (e.g., need to add color mapping, force simulation, or hierarchical layout)
