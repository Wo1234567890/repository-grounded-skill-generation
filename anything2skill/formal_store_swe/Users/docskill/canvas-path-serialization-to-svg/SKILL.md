---
id: "31be7577-341e-557f-b36e-6c4ba2959768"
name: "Canvas Path Serialization to SVG"
description: "Convert Canvas path drawing commands (moveTo, lineTo, curves, arcs, rectangles) into SVG path data strings. Use when you need to translate procedural canvas graphics into portable SVG format for web delivery or vector editing."
version: "0.1.0"
tags:
  - "graphics"
  - "serialization"
  - "SVG"
  - "canvas"
  - "path"
  - "vector"
triggers:
  - "need to convert canvas drawing operations to SVG"
  - "exporting graphics for web or vector editing"
  - "require portable path representation"
---

# Canvas Path Serialization to SVG

Convert Canvas path drawing commands (moveTo, lineTo, curves, arcs, rectangles) into SVG path data strings. Use when you need to translate procedural canvas graphics into portable SVG format for web delivery or vector editing.

## Prompt

Create a path serializer using d3.path(), collect canvas drawing operations (move, line, curve, arc, rectangle commands) by calling the appropriate path methods in sequence, then invoke toString() to produce the final SVG d attribute value.

## Objective

serialize canvas path commands to SVG path data string
## Applicable Signals

- canvas context path operations collected
- SVG output format required
- vector graphics portability needed

## Contraindications

- working with raster graphics
- no SVG output required
- canvas rendering is final output

## Workflow Steps

- {'step': 1, 'action': 'instantiate path serializer', 'detail': 'call d3.path() to create a new path serializer instance, or d3.pathRound() for fixed-point precision'}
- {'step': 2, 'action': 'issue path commands', 'detail': 'call path methods in sequence: moveTo, lineTo, quadraticCurveTo, bezierCurveTo, arcTo, arc, rect, closePath as needed'}
- {'step': 3, 'action': 'serialize to SVG', 'detail': 'call path.toString() to produce SVG path data string'}

## Constraints

- path commands must be issued in valid sequence (moveTo before drawing)
- output precision can be controlled via d3.pathRound() for fixed-point serialization

## Cautions

- ensure all path operations are completed before calling toString()
- closePath() must be called explicitly if subpath closure is required

## Output Contract

- SVG path data string (d attribute value) that reproduces the canvas path visually and is compatible with SVG <path> elements

## Triggers

- need to convert canvas drawing operations to SVG
- exporting graphics for web or vector editing
- require portable path representation
