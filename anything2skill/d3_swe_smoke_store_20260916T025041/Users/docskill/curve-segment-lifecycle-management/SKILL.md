---
id: "9374a068-0fbf-50f1-b860-65362f46ce8a"
name: "Curve Segment Lifecycle Management"
description: "Manage the lifecycle of line and area segments by starting, adding points, and ending segments in the correct sequence. This micro-skill ensures proper state transitions when rendering continuous shapes with explicit segment boundaries."
version: "0.1.0"
tags:
  - "curve"
  - "segment"
  - "lifecycle"
  - "rendering"
  - "state_management"
triggers:
  - "Rendering a line or area shape; need to add multiple points in sequence with explicit segment boundaries"
examples:
  - input: "Curve object and array of points: [(10, 20), (30, 40), (50, 60)]"
    output: "curve.lineStart(); curve.point(10, 20); curve.point(30, 40); curve.point(50, 60); curve.lineEnd();"
    notes: "Line segment with three points rendered in sequence"
  - input: "Curve object and array of points for filled area: [(0, 0), (100, 50), (200, 0)]"
    output: "curve.areaStart(); curve.point(0, 0); curve.point(100, 50); curve.point(200, 0); curve.areaEnd();"
    notes: "Area segment with three points for filled shape rendering"
---

# Curve Segment Lifecycle Management

Manage the lifecycle of line and area segments by starting, adding points, and ending segments in the correct sequence. This micro-skill ensures proper state transitions when rendering continuous shapes with explicit segment boundaries.

## Prompt

Execute the segment lifecycle in order: call lineStart() or areaStart() to initialize, add one or more points via point(x, y), then call lineEnd() or areaEnd() to close the segment. Do not interleave segment starts/ends or omit boundary markers.

## Objective

Execute point-addition sequence with proper segment boundary markers
## Applicable Signals

- Rendering a line or area shape
- Need to add multiple points in sequence
- Explicit segment boundaries required
- Using d3 curve API for shape interpolation

## Contraindications

- Single isolated point rendering without segment structure
- No segment boundaries required
- Rendering complete pre-computed paths
- Using alternative rendering methods that do not require explicit lifecycle calls

## Intervention Moves

- Call lineStart() to begin a new line segment
- Call areaStart() to begin a new area segment
- Call point(x, y) to add a coordinate to the current segment
- Call lineEnd() to finalize the current line segment
- Call areaEnd() to finalize the current area segment

## Workflow Steps

- {'step': 1, 'action': 'Initialize segment', 'detail': 'Call curve.lineStart() for line segments or curve.areaStart() for filled area segments'}
- {'step': 2, 'action': 'Add points', 'detail': 'Call curve.point(x, y) for each coordinate in sequence'}
- {'step': 3, 'action': 'Finalize segment', 'detail': 'Call curve.lineEnd() or curve.areaEnd() to close the segment'}

## Constraints

- lineStart/areaStart must be called before any point() calls
- lineEnd/areaEnd must be called after all point() calls for that segment
- Do not call lineStart and areaStart in the same segment
- Do not call lineEnd and areaEnd in the same segment
- At least one point() must be added between start and end

## Cautions

- Omitting start or end calls will result in incomplete or malformed shapes
- Interleaving multiple segments without proper end markers may cause rendering errors
- Ensure coordinate values are valid numbers before passing to point()

## Output Contract

- Sequence of lineStart → point(x,y) → point(x,y) → ... → lineEnd (or areaStart/areaEnd for filled regions) executed without error; segment is ready for rendering or handoff to downstream shape consumer

## Example Therapist Responses

### Example 1

- Client/Input: Curve object and array of points: [(10, 20), (30, 40), (50, 60)]
- Therapist/Output: curve.lineStart(); curve.point(10, 20); curve.point(30, 40); curve.point(50, 60); curve.lineEnd();
- Notes: Line segment with three points rendered in sequence

### Example 2

- Client/Input: Curve object and array of points for filled area: [(0, 0), (100, 50), (200, 0)]
- Therapist/Output: curve.areaStart(); curve.point(0, 0); curve.point(100, 50); curve.point(200, 0); curve.areaEnd();
- Notes: Area segment with three points for filled shape rendering

## Triggers

- Rendering a line or area shape; need to add multiple points in sequence with explicit segment boundaries

## Examples

### Example 1

Input:

  Curve object and array of points: [(10, 20), (30, 40), (50, 60)]

Output:

  curve.lineStart(); curve.point(10, 20); curve.point(30, 40); curve.point(50, 60); curve.lineEnd();

Notes:

  Line segment with three points rendered in sequence

### Example 2

Input:

  Curve object and array of points for filled area: [(0, 0), (100, 50), (200, 0)]

Output:

  curve.areaStart(); curve.point(0, 0); curve.point(100, 50); curve.point(200, 0); curve.areaEnd();

Notes:

  Area segment with three points for filled shape rendering
