---
id: "e352cfb4-df8f-5d6f-a2b3-15b6196f6265"
name: "D3 Data Binding and Selection Join"
description: "Bind data to DOM elements and manage enter/update/exit selections based on data changes. Synchronizes visual elements with underlying data in D3 visualizations using the data-join pattern."
version: "0.1.0"
tags:
  - "d3"
  - "data-binding"
  - "dom-manipulation"
  - "selection"
  - "enter-update-exit"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to bind data to DOM elements"
  - "Handling new data entries (enter selection)"
  - "Updating existing elements based on data changes"
  - "Removing elements when data is removed (exit selection)"
---

# D3 Data Binding and Selection Join

Bind data to DOM elements and manage enter/update/exit selections based on data changes. Synchronizes visual elements with underlying data in D3 visualizations using the data-join pattern.

## Prompt

Execute the D3 data-join workflow: (1) bind data to elements using selection.data(), (2) use selection.join() to coordinate enter, update, and exit selections, (3) handle new data entries via selection.enter(), (4) update existing elements via the update selection, (5) remove elements via selection.exit(). Optionally use selection.datum() to get or set element data without joining. Ensure all three selections (enter, update, exit) are properly configured before rendering.

## Objective

Synchronize DOM elements with data via selection join operations
## Applicable Signals

- Data array or collection is available
- DOM selection exists and is ready for binding
- Data structure has changed or needs synchronization with visual representation

## Contraindications

- Working with static HTML without dynamic data binding
- Data binding is not required for the use case
- Using non-D3 DOM manipulation libraries or frameworks

## Workflow Steps

- {'step': 1, 'action': 'Obtain or create a D3 selection of target DOM elements', 'detail': 'Use d3.select() or d3.selectAll() to target the container or elements'}
- {'step': 2, 'action': 'Bind data to the selection using selection.data()', 'detail': 'Pass the data array and optionally a key function to establish data-element correspondence'}
- {'step': 3, 'action': 'Coordinate enter, update, and exit selections', 'detail': 'Use selection.join() to merge enter and update, or manually handle selection.enter(), update selection, and selection.exit()'}
- {'step': 4, 'action': 'Configure enter selection', 'detail': 'Append new elements for data without corresponding DOM elements'}
- {'step': 5, 'action': 'Configure update selection', 'detail': 'Modify attributes, styles, or content of elements that already exist'}
- {'step': 6, 'action': 'Configure exit selection', 'detail': 'Remove elements that no longer have corresponding data'}

## Constraints

- Data must be an array or iterable collection
- DOM selection must be valid and accessible
- Key function should be defined if data identity matters across updates

## Cautions

- Ensure enter, update, and exit selections are all handled to avoid orphaned or missing elements
- Use appropriate key functions to maintain data identity during updates
- Be aware of performance implications when binding large datasets

## Output Contract

- DOM elements are correctly bound to data with enter, update, and exit selections properly configured
- Visual representation is synchronized with the underlying data state

## 子技能目录
- [Array Sorting and Reordering](通用技能领域/Family技能/未分类技能/微技能/Array Sorting and Reordering/SKILL.md) ｜ 适用：Reusable micro-operations for sorting, permuting, and shuffling arrays of values using natural order comparisons, index-based reordering, or randomization.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Array Sorting and Reordering` 时，优先调用它。 线索：Need to sort values in natural ascending or descending order, Need to reorder array elements according to an index list, Need to reverse array element sequence, Need to randomize array element order, array_manipulation

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to bind data to DOM elements
- Handling new data entries (enter selection)
- Updating existing elements based on data changes
- Removing elements when data is removed (exit selection)
