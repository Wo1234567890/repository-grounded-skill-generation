---
id: "96abbecd-3805-599a-ac25-86c3ea66ac10"
name: "Tick Customization and Formatting"
description: "Customize tick generation, values, and formatting for axes. Allows explicit tick value specification, format templates, and tick size/padding control to fine-tune tick appearance and labeling on an axis."
version: "0.1.0"
tags:
  - "d3"
  - "axis"
  - "tick"
  - "formatting"
  - "visualization"
  - "rendering"
triggers:
  - "Axis ticks need custom formatting for readability"
  - "Explicit tick values must be specified instead of auto-generated"
  - "Tick size or padding adjustments are required for design requirements"
  - "Tick labels need format templates applied"
examples:
  - input: "axis object with scale, requirement to show every 10th value with currency format"
    output: "axis.tickValues([0, 10, 20, 30, ...]).tickFormat(d3.format('$,.0f')).tickPadding(8)"
    notes: "Explicit values and format applied; padding increased for readability"
  - input: "axis object, requirement to reduce tick size for compact layout"
    output: "axis.tickSize(3).tickSizeInner(2).tickSizeOuter(0).tickPadding(4)"
    notes: "Inner ticks reduced, outer ticks hidden, padding minimized"
---

# Tick Customization and Formatting

Customize tick generation, values, and formatting for axes. Allows explicit tick value specification, format templates, and tick size/padding control to fine-tune tick appearance and labeling on an axis.

## Prompt

Use this skill to customize how ticks appear on an axis. You can set explicit tick values, apply format templates, control tick sizes (inner, outer, and padding), and adjust spacing. Apply these configurations to an axis object before rendering.

## Objective

Fine-tune tick appearance and labeling on an axis
## Applicable Signals

- axis object is available and configured with a scale
- tick appearance does not meet design or readability requirements
- specific tick values or intervals are known in advance

## Contraindications

- Default tick generation is acceptable for the use case
- Axis is not being rendered or used
- Tick customization is not required

## Workflow Steps

- {'step': 1, 'action': 'Obtain or create an axis object (e.g., d3.axisBottom, d3.axisLeft)', 'note': 'Axis must already have a scale configured'}
- {'step': 2, 'action': 'Set explicit tick values using axis.tickValues() or configure tick generation using axis.ticks() or axis.tickArguments()', 'note': 'Choose one approach: explicit values or generation parameters'}
- {'step': 3, 'action': 'Apply a tick format using axis.tickFormat() with a format template or function', 'note': 'Format must match the data type (e.g., number, date, currency)'}
- {'step': 4, 'action': 'Adjust tick sizes using axis.tickSize(), axis.tickSizeInner(), or axis.tickSizeOuter()', 'note': 'Sizes control visual prominence of ticks'}
- {'step': 5, 'action': 'Set padding between ticks and labels using axis.tickPadding()', 'note': 'Padding improves label readability'}
- {'step': 6, 'action': 'Return the configured axis object for rendering', 'note': 'Axis is now ready to be applied to a selection'}

## Constraints

- Axis must have a scale set before tick customization
- Tick values must be compatible with the axis scale domain
- Format templates must be valid for the data type

## Cautions

- Excessive tick customization may reduce readability if too many ticks are specified
- Tick padding and size adjustments should maintain visual hierarchy

## Output Contract

- Axis object with applied tick configuration (format, values, size, padding) ready for rendering to a DOM selection

## Example Therapist Responses

### Example 1

- Client/Input: axis object with scale, requirement to show every 10th value with currency format
- Therapist/Output: axis.tickValues([0, 10, 20, 30, ...]).tickFormat(d3.format('$,.0f')).tickPadding(8)
- Notes: Explicit values and format applied; padding increased for readability

### Example 2

- Client/Input: axis object, requirement to reduce tick size for compact layout
- Therapist/Output: axis.tickSize(3).tickSizeInner(2).tickSizeOuter(0).tickPadding(4)
- Notes: Inner ticks reduced, outer ticks hidden, padding minimized

## Triggers

- Axis ticks need custom formatting for readability
- Explicit tick values must be specified instead of auto-generated
- Tick size or padding adjustments are required for design requirements
- Tick labels need format templates applied

## Examples

### Example 1

Input:

  axis object with scale, requirement to show every 10th value with currency format

Output:

  axis.tickValues([0, 10, 20, 30, ...]).tickFormat(d3.format('$,.0f')).tickPadding(8)

Notes:

  Explicit values and format applied; padding increased for readability

### Example 2

Input:

  axis object, requirement to reduce tick size for compact layout

Output:

  axis.tickSize(3).tickSizeInner(2).tickSizeOuter(0).tickPadding(4)

Notes:

  Inner ticks reduced, outer ticks hidden, padding minimized
