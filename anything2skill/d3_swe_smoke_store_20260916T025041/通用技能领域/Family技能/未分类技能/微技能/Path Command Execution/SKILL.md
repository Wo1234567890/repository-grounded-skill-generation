---
id: "9a735def-26bd-5987-8dc2-f353083096d9"
name: "Path Command Execution"
description: "Execute individual path drawing operations on a path object by invoking discrete drawing commands such as moveTo, lineTo, quadraticCurveTo, bezierCurveTo, arcTo, arc, rect, or closePath. Use when building up a path incrementally through atomic drawing primitives."
version: "0.1.0"
tags:
  - "graphics"
  - "path_drawing"
  - "d3"
  - "vector_graphics"
  - "primitive_operation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "adding a line segment to an active path"
  - "adding a curve (quadratic or cubic Bézier) to an active path"
  - "adding a circular arc to an active path"
  - "adding a rectangle to an active path"
  - "repositioning the path cursor"
---

# Path Command Execution

Execute individual path drawing operations on a path object by invoking discrete drawing commands such as moveTo, lineTo, quadraticCurveTo, bezierCurveTo, arcTo, arc, rect, or closePath. Use when building up a path incrementally through atomic drawing primitives.

## Prompt

Invoke a single path drawing command on an active path object. Each command updates the path's internal state by adding a new segment or closing the subpath. Commands are: moveTo (reposition), lineTo (straight line), quadraticCurveTo (quadratic Bézier), bezierCurveTo (cubic Bézier), arcTo (circular arc via tangent), arc (circular arc via center), rect (rectangle), closePath (close subpath). Pass the required parameters for the chosen command and verify the path object is updated.

## Objective

execute single path drawing operation
## Applicable Signals

- path object exists and is active
- caller intends to append a single drawing primitive
- path construction is in progress

## Contraindications

- path is already closed and no new subpath has been started
- no active path context exists
- operation is not a drawing primitive (e.g., serialization or format conversion)

## Workflow Steps

- {'step': 1, 'action': 'Verify active path object exists', 'detail': 'Ensure a path object has been created and is ready to receive drawing commands'}
- {'step': 2, 'action': 'Select appropriate drawing command', 'detail': 'Choose one of: moveTo, lineTo, quadraticCurveTo, bezierCurveTo, arcTo, arc, rect, closePath'}
- {'step': 3, 'action': 'Prepare command parameters', 'detail': 'Gather required numeric or coordinate arguments for the chosen command'}
- {'step': 4, 'action': 'Invoke command on path object', 'detail': 'Call the command method with prepared parameters'}
- {'step': 5, 'action': 'Verify path state updated', 'detail': "Confirm the path object's internal state reflects the new segment or closure"}

## Constraints

- path object must be initialized before any drawing command is invoked
- commands must be invoked in a valid sequence (e.g., moveTo typically precedes lineTo or curve commands)
- each command is atomic; partial or interrupted commands may leave the path in an inconsistent state

## Cautions

- closePath terminates the current subpath; subsequent commands will start a new subpath
- arcTo and arc have different parameter signatures; verify correct command is used for the intended arc type
- path state is mutable; commands have side effects on the path object

## Output Contract

- Path object is updated with the new drawing command; internal state reflects the new segment or subpath closure. The path is ready to accept subsequent drawing commands or be serialized.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- adding a line segment to an active path
- adding a curve (quadratic or cubic Bézier) to an active path
- adding a circular arc to an active path
- adding a rectangle to an active path
- repositioning the path cursor
