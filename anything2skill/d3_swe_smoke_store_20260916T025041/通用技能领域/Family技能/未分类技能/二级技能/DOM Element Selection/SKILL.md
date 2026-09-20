---
id: "6a19ca02-45da-59db-b6ba-fe8d458d0111"
name: "DOM Element Selection"
description: "Select and query DOM elements using CSS selectors and D3 selection methods. Use when building interactive visualizations that require targeted element manipulation."
version: "0.1.0"
tags:
  - "d3"
  - "dom"
  - "selection"
  - "query"
  - "initialization"
  - "visualization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a visualization"
  - "Need to target specific elements"
  - "Preparing elements for data binding"
---

# DOM Element Selection

Select and query DOM elements using CSS selectors and D3 selection methods. Use when building interactive visualizations that require targeted element manipulation.

## Prompt

Use D3 selection methods to locate and reference DOM elements. Start with d3.select() or d3.selectAll() to target elements from the document root, or use selection.select() and selection.selectAll() to target descendants. Chain selection.filter() to narrow results, selection.merge() to combine selections, and selection.selectChild() or selection.selectChildren() to navigate the DOM tree. The result is a D3 selection object ready for chaining further operations.

## Objective

Locate and reference DOM elements for subsequent styling or data binding
## Applicable Signals

- Visualization initialization phase
- Element targeting requirement
- Pre-binding element preparation

## Contraindications

- Working with non-DOM data structures
- Element references are already cached
- Operating outside DOM context

## Workflow Steps

- {'step': 1, 'action': 'Select root or target element', 'detail': 'Use d3.selection() for root, d3.select() for single element, or d3.selectAll() for multiple elements'}
- {'step': 2, 'action': 'Refine selection if needed', 'detail': 'Apply selection.filter(), selection.selectChild(), or selection.selectChildren() to narrow or navigate'}
- {'step': 3, 'action': 'Merge selections if combining multiple queries', 'detail': 'Use selection.merge() to combine two selection objects'}
- {'step': 4, 'action': 'Verify selection object', 'detail': 'Confirm selection contains expected element references before chaining further operations'}

## Constraints

- Requires valid DOM context
- CSS selectors must be valid
- Selection methods must be chained on valid selection objects

## Cautions

- Empty selections are valid but will not execute subsequent chained operations
- Selector specificity affects performance on large DOM trees
- Selection methods are chainable; intermediate results are selection objects

## Output Contract

- Returns a D3 selection object containing one or more DOM element references ready for chaining operations such as styling, data binding, or attribute modification

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a visualization
- Need to target specific elements
- Preparing elements for data binding
