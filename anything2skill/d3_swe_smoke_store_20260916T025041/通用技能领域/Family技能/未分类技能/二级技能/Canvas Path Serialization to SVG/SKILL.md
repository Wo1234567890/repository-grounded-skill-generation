---
id: "ccc341fc-5c8e-5858-8aa6-80724ce42411"
name: "Canvas Path Serialization to SVG"
description: "Convert Canvas path drawing commands (moveTo, lineTo, curves, arcs, rectangles) into SVG path data strings. Use when you need to translate procedural canvas graphics into portable SVG format for web delivery or vector editing."
version: "0.1.0"
tags:
  - "graphics"
  - "serialization"
  - "SVG"
  - "canvas"
  - "path"
  - "d3"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "need to convert canvas drawing operations to SVG"
  - "exporting graphics for web or vector editing"
  - "require portable path representation"
---

# Canvas Path Serialization to SVG

Convert Canvas path drawing commands (moveTo, lineTo, curves, arcs, rectangles) into SVG path data strings. Use when you need to translate procedural canvas graphics into portable SVG format for web delivery or vector editing.

## Prompt

Create a path serializer using d3.path() or d3.pathRound(digits) for fixed precision. Collect canvas drawing operations by invoking path methods in sequence: moveTo(x, y), lineTo(x, y), quadraticCurveTo(cpx, cpy, x, y), bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y), arcTo(x1, y1, x2, y2, radius), arc(x, y, radius, startAngle, endAngle, counterclockwise), rect(x, y, width, height), closePath(). Finally, call path.toString() to produce the SVG path data string suitable for the d attribute of an SVG <path> element.

## Objective

serialize canvas path commands to SVG
## Applicable Signals

- canvas context path methods have been called
- SVG output format is required
- path must be reusable across rendering contexts

## Contraindications

- working with raster graphics only
- no SVG output required
- canvas rendering is the final output
- performance-critical real-time rendering

## Workflow Steps

- {'step': 1, 'action': 'instantiate path serializer', 'detail': 'call d3.path() to create a new path serializer, or d3.pathRound(digits) for fixed precision output'}
- {'step': 2, 'action': 'collect path commands', 'detail': 'invoke path methods in sequence: moveTo(x, y), lineTo(x, y), quadraticCurveTo(cpx, cpy, x, y), bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y), arcTo(x1, y1, x2, y2, radius), arc(x, y, radius, startAngle, endAngle, counterclockwise), rect(x, y, width, height), closePath()'}
- {'step': 3, 'action': 'serialize to SVG', 'detail': 'call path.toString() to produce SVG path data string suitable for the d attribute of an SVG <path> element'}

## Constraints

- input must be valid canvas path operations
- output precision can be controlled via d3.pathRound() for fixed decimal places
- path serialization is deterministic given the same command sequence

## Cautions

- ensure coordinate system matches between canvas and SVG (canvas origin top-left, SVG origin typically top-left in web context)
- precision loss may occur with floating-point coordinates; use d3.pathRound() if fixed precision is required
- complex paths with many commands may produce long strings; consider compression or optimization for large graphics

## Output Contract

- SVG path data string (d attribute value) that reproduces the canvas path visually when applied to an SVG <path> element

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- need to convert canvas drawing operations to SVG
- exporting graphics for web or vector editing
- require portable path representation
