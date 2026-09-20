---
id: "95f51236-966f-55cc-af09-a06f85484a4d"
name: "D3 Zoom Behavior Configuration"
description: "Configure and apply zoom behavior to SVG/canvas elements, including transform constraints, event filtering, and transition settings. Use when building interactive zoomable visualizations."
version: "0.1.0"
tags:
  - "d3"
  - "zoom"
  - "interaction"
  - "visualization"
  - "transform"
  - "event-handling"
triggers:
  - "User needs to add zoom interactivity to a chart or map"
  - "Building an interactive visualization with pan and zoom controls"
  - "Implementing constrained zoom behavior on SVG or canvas elements"
examples:
  - input: "SVG element with width=800, height=600; requirement: zoom range 1x to 10x, pan constrained to data bounds"
    output: "Zoom behavior configured with scaleExtent([1, 10]) and translateExtent set to data bounds; applied to SVG via .call(zoom); user can zoom and pan within constraints"
    notes: "Typical interactive chart scenario"
  - input: "Canvas element; requirement: disable zoom on right-click, enable only on wheel and left-drag"
    output: "zoom.filter() returns true only for wheel events and left-button drag; right-click events ignored"
    notes: "Custom event filtering use case"
---

# D3 Zoom Behavior Configuration

Configure and apply zoom behavior to SVG/canvas elements, including transform constraints, event filtering, and transition settings. Use when building interactive zoomable visualizations.

## Prompt

1. Create a zoom behavior instance using d3.zoom().
2. Set viewport extent using zoom.extent() to define the interactive area.
3. Configure scale range using zoom.scaleExtent() to limit zoom levels.
4. Set world extent using zoom.translateExtent() to constrain pan boundaries.
5. Apply event filtering with zoom.filter() to control which input events trigger zoom.
6. Configure touch support with zoom.touchable() if needed.
7. Set wheel scaling behavior with zoom.wheelDelta() for mouse wheel events.
8. Attach zoom event listeners using zoom.on() to respond to zoom, start, and end events.
9. Apply the configured zoom behavior to selected elements using selection.call(zoom).
10. Optionally set transition duration and interpolation for smooth zoom animations.

## Objective

Set up and manage zoom interactions on selected DOM elements with full configuration of constraints, event filtering, and transitions
## Applicable Signals

- Interactive visualization requirement identified
- User interaction (mouse wheel, touch, drag) expected on visual elements
- Zoom extent or scale constraints specified in requirements

## Contraindications

- Static visualizations with no user interaction requirement
- Non-interactive displays or read-only charts
- When zoom functionality is explicitly not needed
- Performance-critical scenarios with very large datasets where zoom overhead is prohibitive

## Workflow Steps

- {'step': 1, 'action': 'Instantiate zoom behavior', 'detail': 'const zoom = d3.zoom();'}
- {'step': 2, 'action': 'Configure viewport extent', 'detail': 'zoom.extent([[0, 0], [width, height]]);'}
- {'step': 3, 'action': 'Set scale range limits', 'detail': 'zoom.scaleExtent([minScale, maxScale]);'}
- {'step': 4, 'action': 'Set pan boundary constraints', 'detail': 'zoom.translateExtent([[x0, y0], [x1, y1]]);'}
- {'step': 5, 'action': 'Filter input events', 'detail': "zoom.filter(event => !event.button || event.type === 'wheel');"}
- {'step': 6, 'action': 'Attach event listeners', 'detail': "zoom.on('zoom', handleZoom).on('start', handleStart).on('end', handleEnd);"}
- {'step': 7, 'action': 'Apply zoom to selected elements', 'detail': "d3.select('svg').call(zoom);"}

## Constraints

- Selected elements must be SVG or canvas-compatible DOM nodes
- Zoom extent must be defined before applying behavior to elements
- Scale extent values must be positive numbers with min < max
- Translate extent must be a valid rectangular boundary
- Event filter function must return boolean to allow or block events

## Cautions

- Zoom behavior modifies element transforms; ensure underlying data bindings are preserved
- Touch support detection may vary across browsers; test on target platforms
- Wheel delta scaling can be sensitive; test with actual user input
- Transition duration should be balanced against responsiveness expectations

## Output Contract

- Zoom behavior is successfully applied to selected elements
- User can interact with the element via mouse wheel, touch gestures, or drag operations
- Zoom transforms are constrained by configured extent and scale limits
- Zoom events fire with correct event type and transform data
- Transitions execute smoothly if duration is configured

## Example Therapist Responses

### Example 1

- Client/Input: SVG element with width=800, height=600; requirement: zoom range 1x to 10x, pan constrained to data bounds
- Therapist/Output: Zoom behavior configured with scaleExtent([1, 10]) and translateExtent set to data bounds; applied to SVG via .call(zoom); user can zoom and pan within constraints
- Notes: Typical interactive chart scenario

### Example 2

- Client/Input: Canvas element; requirement: disable zoom on right-click, enable only on wheel and left-drag
- Therapist/Output: zoom.filter() returns true only for wheel events and left-button drag; right-click events ignored
- Notes: Custom event filtering use case

## Triggers

- User needs to add zoom interactivity to a chart or map
- Building an interactive visualization with pan and zoom controls
- Implementing constrained zoom behavior on SVG or canvas elements

## Examples

### Example 1

Input:

  SVG element with width=800, height=600; requirement: zoom range 1x to 10x, pan constrained to data bounds

Output:

  Zoom behavior configured with scaleExtent([1, 10]) and translateExtent set to data bounds; applied to SVG via .call(zoom); user can zoom and pan within constraints

Notes:

  Typical interactive chart scenario

### Example 2

Input:

  Canvas element; requirement: disable zoom on right-click, enable only on wheel and left-drag

Output:

  zoom.filter() returns true only for wheel events and left-button drag; right-click events ignored

Notes:

  Custom event filtering use case
