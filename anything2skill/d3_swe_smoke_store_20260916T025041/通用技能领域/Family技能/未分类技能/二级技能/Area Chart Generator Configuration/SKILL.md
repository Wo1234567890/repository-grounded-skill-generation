---
id: "ac0fa8e4-50b8-5f96-83fc-3624fece8bfe"
name: "Area Chart Generator Configuration"
description: "Configure and generate area chart shapes by setting data accessors, curve interpolation, and rendering context for Cartesian or radial coordinate systems."
version: "0.1.0"
tags:
  - "d3"
  - "area-chart"
  - "shape-generation"
  - "data-visualization"
  - "accessor-configuration"
  - "curve-interpolation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "building area or stacked area charts"
  - "need to bind data accessors and set rendering parameters before generating SVG or canvas paths"
  - "preparing Cartesian or radial area visualization"
examples:
  - input: "dataset: [{x: 0, y: 10}, {x: 1, y: 20}]; Cartesian area with linear curve"
    output: "area generator configured with .x(d => d.x), .y0(0), .y1(d => d.y), .curve(d3.curveLinear); calling generator(data) produces SVG path string"
    notes: "basic Cartesian area setup"
  - input: "dataset: [{angle: 0, r: 5}, {angle: Math.PI/2, r: 10}]; radial area with monotone curve"
    output: "areaRadial generator configured with .startAngle(d => d.angle), .endAngle(d => d.angle), .innerRadius(0), .outerRadius(d => d.r), .curve(d3.curveMonotoneRadial); calling generator(data) produces radial area path"
    notes: "radial coordinate system setup"
---

# Area Chart Generator Configuration

Configure and generate area chart shapes by setting data accessors, curve interpolation, and rendering context for Cartesian or radial coordinate systems.

## Prompt

Create and configure an area generator by chaining accessor methods (x0, x1, y0, y1 for Cartesian; startAngle, endAngle, innerRadius, outerRadius for radial) and setting curve interpolation and rendering context. The configured generator accepts a dataset and produces SVG or canvas path output.

## Objective

produce a configured area generator ready to render area chart geometry
## Applicable Signals

- area chart requirement identified
- dataset structure known and accessors can be defined
- rendering target (SVG or canvas) determined

## Contraindications

- rendering line charts only
- working with non-area shape types
- data is already pre-rendered
- no coordinate system defined

## Workflow Steps

- {'step': 1, 'action': 'instantiate area generator', 'detail': 'call d3.area() or d3.areaRadial() to create new generator instance'}
- {'step': 2, 'action': 'set baseline and topline accessors', 'detail': 'for Cartesian: chain .x0(), .x1(), .y0(), .y1(); for radial: chain .startAngle(), .endAngle(), .innerRadius(), .outerRadius()'}
- {'step': 3, 'action': 'set curve interpolation', 'detail': 'chain .curve() with interpolator (e.g., d3.curveLinear, d3.curveMonotoneX)'}
- {'step': 4, 'action': 'set rendering context', 'detail': 'chain .context() if rendering to canvas; omit for SVG default'}
- {'step': 5, 'action': 'optionally set precision and defined accessor', 'detail': 'chain .digits() for output precision; chain .defined() to handle missing data'}
- {'step': 6, 'action': 'invoke generator on dataset', 'detail': 'call configured generator with data array to produce path string or canvas commands'}

## Constraints

- must define x0 and x1 (or startAngle and endAngle for radial) before rendering
- must define y0 and y1 (or innerRadius and outerRadius for radial) before rendering
- curve interpolator must be compatible with area geometry
- rendering context must match output target (SVG or canvas)

## Cautions

- ensure data accessor functions match dataset structure
- verify curve type supports area rendering (not all curves are valid for areas)
- confirm rendering context is initialized before passing to generator

## Output Contract

- configured area generator object with all accessors, curve interpolation, and rendering context applied
- ready to accept dataset and produce SVG path string or canvas rendering commands
- output is a function that accepts data array and returns path geometry

## Example Therapist Responses

### Example 1

- Client/Input: dataset: [{x: 0, y: 10}, {x: 1, y: 20}]; Cartesian area with linear curve
- Therapist/Output: area generator configured with .x(d => d.x), .y0(0), .y1(d => d.y), .curve(d3.curveLinear); calling generator(data) produces SVG path string
- Notes: basic Cartesian area setup

### Example 2

- Client/Input: dataset: [{angle: 0, r: 5}, {angle: Math.PI/2, r: 10}]; radial area with monotone curve
- Therapist/Output: areaRadial generator configured with .startAngle(d => d.angle), .endAngle(d => d.angle), .innerRadius(0), .outerRadius(d => d.r), .curve(d3.curveMonotoneRadial); calling generator(data) produces radial area path
- Notes: radial coordinate system setup

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- building area or stacked area charts
- need to bind data accessors and set rendering parameters before generating SVG or canvas paths
- preparing Cartesian or radial area visualization

## Examples

### Example 1

Input:

  dataset: [{x: 0, y: 10}, {x: 1, y: 20}]; Cartesian area with linear curve

Output:

  area generator configured with .x(d => d.x), .y0(0), .y1(d => d.y), .curve(d3.curveLinear); calling generator(data) produces SVG path string

Notes:

  basic Cartesian area setup

### Example 2

Input:

  dataset: [{angle: 0, r: 5}, {angle: Math.PI/2, r: 10}]; radial area with monotone curve

Output:

  areaRadial generator configured with .startAngle(d => d.angle), .endAngle(d => d.angle), .innerRadius(0), .outerRadius(d => d.r), .curve(d3.curveMonotoneRadial); calling generator(data) produces radial area path

Notes:

  radial coordinate system setup
