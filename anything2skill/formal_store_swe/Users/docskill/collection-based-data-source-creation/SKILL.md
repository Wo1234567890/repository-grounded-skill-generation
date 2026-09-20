---
id: "789fedcd-9fe4-55d3-94e0-837ff175d715"
name: "Collection-based Data Source Creation"
description: "Select and query DOM elements using CSS selectors and D3 selection methods. Use when building interactive visualizations that require targeted element manipulation."
version: "0.1.0"
tags:
  - "d3"
  - "dom"
  - "selection"
  - "query"
  - "css-selector"
  - "initialization"
triggers:
  - "Test data, small reference datasets, or programmatically generated sequences need to be streamed; all elements are homogeneous type"
examples:
  - input: "Java Collection of integers: [1, 2, 3, 4, 5]"
    output: "DataStream<Integer> with 5 elements, ready for map/filter operations"
    notes: "Use fromCollection(Collection) for standard Java collections"
  - input: "Iterator over strings with type class String.class"
    output: "DataStream<String> populated from iterator elements"
    notes: "Use fromCollection(Iterator, Class) when data is iterator-based"
  - input: "Numeric range: generateSequence(1, 100)"
    output: "DataStream<Long> with sequence 1 to 100 generated in parallel"
    notes: "Use generateSequence for numeric sequences; parallel execution by default"
---

# Collection-based Data Source Creation

Select and query DOM elements using CSS selectors and D3 selection methods. Use when building interactive visualizations that require targeted element manipulation.

## Prompt

Use D3 selection methods to locate and reference DOM elements. Start with d3.select() or d3.selectAll() to target elements from the document, then chain selection.select(), selection.selectAll(), or selection.filter() to refine or traverse descendants. Merge selections when combining multiple element sets. Return a D3 selection object ready for chaining downstream operations.

## Objective

Locate and reference DOM elements for subsequent styling or data binding
## Applicable Signals

- Visualization initialization phase
- Element reference required for downstream chaining
- CSS selector pattern available

## Contraindications

- Working with non-DOM data structures
- Element references already cached or pre-computed
- Operating outside browser DOM context

## Intervention Moves

- d3.select(selector) — select single element
- d3.selectAll(selector) — select multiple elements
- selection.select(selector) — select descendant for each element
- selection.selectAll(selector) — select multiple descendants for each element
- selection.filter(predicate) — filter elements based on data or condition
- selection.merge(other) — merge two selections
- selection.selectChild(selector) — select a child element for each selected element
- selection.selectChildren(selector) — select the children elements for each selected element

## Workflow Steps

- {'step': 1, 'action': 'Invoke root selection', 'detail': 'Call d3.selection() to select the root document element, or d3.select(selector) to target a single element'}
- {'step': 2, 'action': 'Refine or traverse', 'detail': 'Chain selection.select(), selection.selectAll(), or selection.filter() to narrow or expand the selection'}
- {'step': 3, 'action': 'Merge if needed', 'detail': 'Use selection.merge() to combine multiple selections into one'}
- {'step': 4, 'action': 'Return selection object', 'detail': 'Pass the final selection to downstream operations (styling, data binding, etc.)'}

## Constraints

- Selector must be valid CSS or D3 selector syntax
- Target elements must exist in the DOM at invocation time
- Selection operations are chainable but do not mutate the original DOM

## Cautions

- Empty selections return valid objects; check selection.empty() if needed
- Chaining operations on empty selections will not error but will have no effect

## Output Contract

- A D3 selection object containing one or more DOM element references, ready for chaining operations such as .attr(), .style(), .data(), or further selection refinement

## Triggers

- Test data, small reference datasets, or programmatically generated sequences need to be streamed; all elements are homogeneous type

## Examples

### Example 1

Input:

  Java Collection of integers: [1, 2, 3, 4, 5]

Output:

  DataStream<Integer> with 5 elements, ready for map/filter operations

Notes:

  Use fromCollection(Collection) for standard Java collections

### Example 2

Input:

  Iterator over strings with type class String.class

Output:

  DataStream<String> populated from iterator elements

Notes:

  Use fromCollection(Iterator, Class) when data is iterator-based

### Example 3

Input:

  Numeric range: generateSequence(1, 100)

Output:

  DataStream<Long> with sequence 1 to 100 generated in parallel

Notes:

  Use generateSequence for numeric sequences; parallel execution by default
