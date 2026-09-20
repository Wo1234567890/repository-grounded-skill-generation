---
id: "65488e1b-1f01-5889-b7f5-dc53cbe11bbd"
name: "Pointer position retrieval"
description: "Extract pointer coordinates from DOM events using d3.pointer() for single pointer or d3.pointers() for multiple pointers. Returns coordinate data relative to a specified container for downstream processing or visualization."
version: "0.1.0"
tags:
  - "d3"
  - "event_handling"
  - "pointer"
  - "coordinates"
  - "interaction"
  - "mouse"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Event handler receives mouse event"
  - "Event handler receives touch event"
  - "Event handler receives pen event"
  - "Coordinates relative to a container are needed"
---

# Pointer position retrieval

Extract pointer coordinates from DOM events using d3.pointer() for single pointer or d3.pointers() for multiple pointers. Returns coordinate data relative to a specified container for downstream processing or visualization.

## Prompt

Call d3.pointer(event) to get [x, y] coordinates of a single pointer relative to the container. Call d3.pointers(event) to get an array of [x, y] coordinate pairs for multiple simultaneous pointers. Pass the event object from a mouse, touch, or pen event handler.

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

- {'step': 1, 'action': 'Receive event object from DOM event handler', 'detail': 'Capture the event from mouse, touch, or pen interaction'}
- {'step': 2, 'action': 'Call d3.pointer(event) or d3.pointers(event)', 'detail': 'Use d3.pointer() for single pointer; use d3.pointers() for multiple pointers'}
- {'step': 3, 'action': 'Extract coordinate pair(s)', 'detail': 'Retrieve [x, y] or array of [x, y] pairs relative to container'}
- {'step': 4, 'action': 'Pass coordinates to downstream processing', 'detail': 'Use extracted coordinates for visualization, interaction, or data binding'}

## Constraints

- Event object must be passed to the function
- Container context must be established for coordinate transformation

## Cautions

- Touch events may have multiple pointers; use d3.pointers() for multi-touch scenarios
- Coordinates are relative to the container; absolute positioning requires additional transformation

## Output Contract

- Returns [x, y] coordinate pair for d3.pointer() or array of [x, y] pairs for d3.pointers(), with coordinates relative to the event's container context. Coordinates are ready for immediate use in visualization or interaction logic.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Event handler receives mouse event
- Event handler receives touch event
- Event handler receives pen event
- Coordinates relative to a container are needed
