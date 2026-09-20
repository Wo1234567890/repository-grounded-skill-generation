---
id: "b70d5c1b-ab78-543c-b1f1-1ba634d411d5"
name: "Element Matching and Inspection"
description: "Test whether elements match CSS selectors and inspect element properties such as owner window and computed styles. Use when validating element state or filtering selections based on selector criteria."
version: "0.1.0"
tags:
  - "dom_inspection"
  - "element_validation"
  - "selector_matching"
  - "style_inspection"
  - "read_only"
triggers:
  - "Need to filter or validate elements before applying transformations"
  - "Inspect computed styles for conditional branching"
  - "Validate element state against selector criteria"
examples:
  - input: "element = DOM node; selector = '.active'"
    output: "d3.matcher(selector)(element) returns true or false"
    notes: "Use to filter selections by class or other selector criteria"
  - input: "element = DOM node; property = 'display'"
    output: "d3.style(element, property) returns computed style value (e.g., 'block')"
    notes: "Inspect computed styles for visibility or layout decisions"
  - input: "element = DOM node"
    output: "d3.window(element) returns element's owner window object"
    notes: "Retrieve window context for cross-frame or multi-window scenarios"
---

# Element Matching and Inspection

Test whether elements match CSS selectors and inspect element properties such as owner window and computed styles. Use when validating element state or filtering selections based on selector criteria.

## Prompt

Use d3.matcher to test if an element matches a CSS selector. Use d3.style to retrieve computed style values. Use d3.window to get an element's owner window. These operations are read-only and return boolean or property values for conditional logic.

## Objective

Verify element properties and selector matches for conditional logic
## Applicable Signals

- Element selection requires validation
- Conditional DOM logic depends on style or selector state
- Pre-transformation element inspection needed

## Contraindications

- Performing bulk DOM modifications without validation
- Element state is guaranteed and no inspection needed
- Modifying element properties or structure

## Workflow Steps

- {'step': 1, 'action': 'Obtain element reference', 'detail': 'Ensure element is available from prior selection or DOM query'}
- {'step': 2, 'action': 'Test selector match or inspect property', 'detail': 'Call d3.matcher(selector)(element) for boolean match, or d3.style(element, property) for style value, or d3.window(element) for owner window'}
- {'step': 3, 'action': 'Return result for downstream logic', 'detail': 'Pass boolean or property value to conditional or filter operation'}

## Constraints

- Operations are read-only; do not use for DOM mutations
- Style inspection returns computed values only
- Selector matching is synchronous and blocking

## Cautions

- Computed styles may differ from inline styles
- Cross-window element inspection requires owner window context
- Selector matching performance scales with selector complexity

## Output Contract

- Boolean result confirming element matches selector, or string/numeric style value, or window object reference. Caller receives read-only inspection result suitable for conditional branching or filtering.

## Example Executions

### Example 1

- Input: element = DOM node; selector = '.active'
- Output: d3.matcher(selector)(element) returns true or false
- Notes: Use to filter selections by class or other selector criteria

### Example 2

- Input: element = DOM node; property = 'display'
- Output: d3.style(element, property) returns computed style value (e.g., 'block')
- Notes: Inspect computed styles for visibility or layout decisions

### Example 3

- Input: element = DOM node
- Output: d3.window(element) returns element's owner window object
- Notes: Retrieve window context for cross-frame or multi-window scenarios

## Triggers

- Need to filter or validate elements before applying transformations
- Inspect computed styles for conditional branching
- Validate element state against selector criteria

## Examples

### Example 1

Input:

  element = DOM node; selector = '.active'

Output:

  d3.matcher(selector)(element) returns true or false

Notes:

  Use to filter selections by class or other selector criteria

### Example 2

Input:

  element = DOM node; property = 'display'

Output:

  d3.style(element, property) returns computed style value (e.g., 'block')

Notes:

  Inspect computed styles for visibility or layout decisions

### Example 3

Input:

  element = DOM node

Output:

  d3.window(element) returns element's owner window object

Notes:

  Retrieve window context for cross-frame or multi-window scenarios
