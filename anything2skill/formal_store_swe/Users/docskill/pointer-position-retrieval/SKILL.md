---
id: "65488e1b-1f01-5889-b7f5-dc53cbe11bbd"
name: "Pointer position retrieval"
description: "Extract pointer coordinates from DOM events using d3.pointer() for single pointer or d3.pointers() for multiple pointers. Returns coordinate data relative to a specified container."
version: "0.1.0"
tags:
  - "d3"
  - "event-handling"
  - "pointer"
  - "coordinates"
  - "mouse"
  - "touch"
triggers:
  - "Event handler receives mouse event"
  - "Event handler receives touch event"
  - "Event handler receives pen event"
  - "Coordinates relative to a container are needed"
---

# Pointer position retrieval

Extract pointer coordinates from DOM events using d3.pointer() for single pointer or d3.pointers() for multiple pointers. Returns coordinate data relative to a specified container.

## Prompt

Call d3.pointer(event, container) to get [x, y] coordinates of a single pointer, or d3.pointers(event, container) to get an array of [x, y] pairs for multiple pointers. Coordinates are relative to the container element passed as the second argument.

## Objective

Extract pointer coordinates from DOM events
## Applicable Signals

- mousemove event
- touchmove event
- pointerdown event
- pointerup event

## Contraindications

- Event has no pointer data
- Coordinate system is not relevant to the task
- Absolute page coordinates are required instead of container-relative coordinates

## Workflow Steps

- Receive event object from event handler
- Determine if single or multiple pointers are needed
- Call d3.pointer(event, container) or d3.pointers(event, container)
- Extract [x, y] coordinate pair(s) from result
- Pass coordinates to downstream processing

## Constraints

- Event object must be passed to the function
- Container element must be specified for coordinate transformation
- Pointer data must be available in the event

## Cautions

- Coordinates are relative to the container; ensure correct container is passed
- Touch events may have multiple pointers; use d3.pointers() for multi-touch scenarios

## Output Contract

- Returns [x, y] coordinate pair for single pointer, or array of [x, y] pairs for multiple pointers, relative to the specified container element.

## Triggers

- Event handler receives mouse event
- Event handler receives touch event
- Event handler receives pen event
- Coordinates relative to a container are needed
