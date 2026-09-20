---
id: "b70d5c1b-ab78-543c-b1f1-1ba634d411d5"
name: "Element Matching and Inspection"
description: "Test whether elements match CSS selectors and inspect element properties such as owner window and computed styles. Use when validating element state or filtering selections based on selector criteria."
version: "0.1.0"
tags:
  - "dom"
  - "validation"
  - "selector"
  - "inspection"
  - "read-only"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to filter or validate elements before applying transformations, or inspect computed styles"
examples:
  - input: "element = document.querySelector('div.active'); matcher = d3.matcher('.active')"
    output: "matcher(element) returns true"
    notes: "Validates that element matches the selector."
  - input: "element = document.querySelector('p'); d3.style(element, 'color')"
    output: "Returns computed color value, e.g., 'rgb(0, 0, 0)'"
    notes: "Inspects computed style without modifying the element."
  - input: "element = document.querySelector('svg'); d3.window(element)"
    output: "Returns the Window object owning the element"
    notes: "Retrieves owner window for cross-frame or context checks."
---

# Element Matching and Inspection

Test whether elements match CSS selectors and inspect element properties such as owner window and computed styles. Use when validating element state or filtering selections based on selector criteria.

## Prompt

Use d3.matcher to test if an element matches a CSS selector. Use d3.style to retrieve computed style values from an element. Use d3.window to get an element's owner window. These operations are read-only and return boolean or property values for conditional logic.

## Objective

Verify element properties and selector matches for conditional logic
## Applicable Signals

- Need to filter or validate elements before applying transformations
- Inspect computed styles for conditional branching
- Verify element selector match before proceeding with modifications

## Contraindications

- Performing bulk DOM modifications without validation
- When element state is guaranteed and no inspection is needed
- For write operations; this skill is read-only

## Workflow Steps

- {'step': 1, 'action': 'Test selector match', 'detail': 'Call d3.matcher(selector) to create a test function, then apply it to an element to return a boolean.'}
- {'step': 2, 'action': 'Retrieve computed style', 'detail': 'Call d3.style(element, property) to get the current computed style value of the element.'}
- {'step': 3, 'action': 'Get owner window', 'detail': "Call d3.window(element) to retrieve the element's owner window object."}
- {'step': 4, 'action': 'Use result for conditional logic', 'detail': 'Branch or filter based on the boolean or property value returned.'}

## Constraints

- All operations are read-only; no DOM mutations occur.
- Selector syntax must be valid CSS.
- Element must be a valid DOM node.

## Cautions

- Computed styles may vary across browsers; test in target environments.
- d3.window may return null for detached elements.

## Output Contract

- Returns a boolean (for matcher), a string or null (for style), or a Window object (for d3.window). Caller receives a definitive property state or match result suitable for conditional branching or filtering.

## Example Therapist Responses

### Example 1

- Client/Input: element = document.querySelector('div.active'); matcher = d3.matcher('.active')
- Therapist/Output: matcher(element) returns true
- Notes: Validates that element matches the selector.

### Example 2

- Client/Input: element = document.querySelector('p'); d3.style(element, 'color')
- Therapist/Output: Returns computed color value, e.g., 'rgb(0, 0, 0)'
- Notes: Inspects computed style without modifying the element.

### Example 3

- Client/Input: element = document.querySelector('svg'); d3.window(element)
- Therapist/Output: Returns the Window object owning the element
- Notes: Retrieves owner window for cross-frame or context checks.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to filter or validate elements before applying transformations, or inspect computed styles

## Examples

### Example 1

Input:

  element = document.querySelector('div.active'); matcher = d3.matcher('.active')

Output:

  matcher(element) returns true

Notes:

  Validates that element matches the selector.

### Example 2

Input:

  element = document.querySelector('p'); d3.style(element, 'color')

Output:

  Returns computed color value, e.g., 'rgb(0, 0, 0)'

Notes:

  Inspects computed style without modifying the element.

### Example 3

Input:

  element = document.querySelector('svg'); d3.window(element)

Output:

  Returns the Window object owning the element

Notes:

  Retrieves owner window for cross-frame or context checks.
