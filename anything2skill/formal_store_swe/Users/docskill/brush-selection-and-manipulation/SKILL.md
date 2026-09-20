---
id: "1bd0b637-f755-5a30-aba3-285d6e67c738"
name: "Brush Selection and Manipulation"
description: "Create and control one- or two-dimensional brush selections on DOM elements using mouse or touch input. Supports movement, clearing, extent definition, and event listening for interactive region selection in visualizations."
version: "0.1.0"
tags:
  - "d3"
  - "interaction"
  - "selection"
  - "brush"
  - "mouse"
  - "touch"
triggers:
  - "User initiates mouse or touch input on a visualization element"
  - "Application requires spatial region selection for filtering or zooming"
  - "Interactive selection feedback is needed in real-time"
examples:
  - input: "Create a 2D brush on a 960×500 SVG area"
    output: "Brush instance applied to selection; user can drag to select region; brush.on('brush', ...) fires with coordinates like [[100, 50], [400, 300]]"
    notes: "Typical use case for filtering scatter plot or heatmap data"
  - input: "Create a 1D brush along x-axis only"
    output: "d3.brushX() applied; user drags horizontally; selection returned as [[x0, 0], [x1, height]]"
    notes: "Common for time-series or range selection"
---

# Brush Selection and Manipulation

Create and control one- or two-dimensional brush selections on DOM elements using mouse or touch input. Supports movement, clearing, extent definition, and event listening for interactive region selection in visualizations.

## Prompt

1. Create a brush using d3.brush(), d3.brushX(), or d3.brushY() depending on dimensionality.
2. Apply the brush to a DOM selection via brush(selection).
3. Define the brushable region using brush.extent().
4. Configure input filtering via brush.filter() and touch support via brush.touchable().
5. Listen for brush events using brush.on() to capture selection changes.
6. Retrieve current selection coordinates via d3.brushSelection(node).
7. Move or clear the brush programmatically using brush.move() or brush.clear().
8. Adjust visual appearance via brush.handleSize() and key interaction via brush.keyModifiers().

## Objective

Enable interactive spatial region selection via brush UI component with full lifecycle control
## Applicable Signals

- Mouse down/move/up events on target DOM element
- Touch events on touch-capable devices
- Brush event emissions (start, brush, end)

## Contraindications

- Selection is non-spatial or purely programmatic
- No mouse or touch interaction is available or desired
- Target element is not a valid DOM selection
- Brush extent is undefined or invalid

## Intervention Moves

- Create brush instance with appropriate dimensionality (1D or 2D)
- Bind brush to DOM selection
- Configure extent boundaries and input filters
- Attach event listeners to capture selection state
- Programmatically move or clear brush on demand

## Workflow Steps

- {'step': 1, 'action': 'Instantiate brush', 'detail': 'Call d3.brush(), d3.brushX(), or d3.brushY() to create a new brush generator'}
- {'step': 2, 'action': 'Define extent', 'detail': 'Call brush.extent() to set the rectangular region within which brushing is allowed'}
- {'step': 3, 'action': 'Apply to selection', 'detail': 'Call brush(selection) to bind the brush to a DOM element or group'}
- {'step': 4, 'action': 'Configure input', 'detail': 'Optionally call brush.filter(), brush.touchable(), brush.keyModifiers(), and brush.handleSize() to customize interaction'}
- {'step': 5, 'action': 'Attach listeners', 'detail': "Call brush.on('start', ...), brush.on('brush', ...), and brush.on('end', ...) to handle selection events"}
- {'step': 6, 'action': 'Retrieve or manipulate selection', 'detail': 'Use d3.brushSelection(node) to read current selection, or brush.move(selection, coordinates) to update it programmatically'}

## Constraints

- Brush must be applied to a valid D3 selection
- Brushable extent must be defined before user interaction
- Touch support requires explicit enablement via brush.touchable()
- Event handlers must be attached before brush becomes interactive

## Cautions

- Brush selection coordinates are relative to the brushable extent; caller must map to data space if needed
- Multiple brush instances on overlapping elements may cause input conflicts; use brush.filter() to disambiguate
- Clearing brush does not automatically trigger brush events; use brush.on() to listen for explicit clear actions

## Output Contract

- Returns or emits brush selection as [x0, y0, x1, y1] coordinates (or [x0, x1] for 1D brush) relative to the defined extent. Brush event handlers receive the selection state. d3.brushSelection() returns null if no selection is active, or the coordinate array if active. Visual brush overlay is rendered on the target DOM element.

## Example Executions

### Example 1

- Input: Create a 2D brush on a 960×500 SVG area
- Output: Brush instance applied to selection; user can drag to select region; brush.on('brush', ...) fires with coordinates like [[100, 50], [400, 300]]
- Notes: Typical use case for filtering scatter plot or heatmap data

### Example 2

- Input: Create a 1D brush along x-axis only
- Output: d3.brushX() applied; user drags horizontally; selection returned as [[x0, 0], [x1, height]]
- Notes: Common for time-series or range selection

## Triggers

- User initiates mouse or touch input on a visualization element
- Application requires spatial region selection for filtering or zooming
- Interactive selection feedback is needed in real-time

## Examples

### Example 1

Input:

  Create a 2D brush on a 960×500 SVG area

Output:

  Brush instance applied to selection; user can drag to select region; brush.on('brush', ...) fires with coordinates like [[100, 50], [400, 300]]

Notes:

  Typical use case for filtering scatter plot or heatmap data

### Example 2

Input:

  Create a 1D brush along x-axis only

Output:

  d3.brushX() applied; user drags horizontally; selection returned as [[x0, 0], [x1, height]]

Notes:

  Common for time-series or range selection
