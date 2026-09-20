---
id: "c6f8f040-bf36-59a6-bcee-6d80b6f1a546"
name: "Collect Field CLS Attribution Data"
description: "Configure and generate area chart shapes (Cartesian or radial) by setting baseline/topline accessors (or angle/radius for radial), curve interpolation, and rendering context. Use when building area, radial area, or rose diagrams from tabular data."
version: "0.1.1"
tags:
  - "d3"
  - "visualization"
  - "radial"
  - "polar"
  - "area-chart"
  - "generator"
triggers:
  - "Need to understand CLS patterns in production environments"
  - "Correlating layout shifts with real user behavior and interactions"
  - "Debugging field performance issues reported by end users"
  - "Establishing baseline CLS metrics across user segments"
examples:
  - input: "Dataset: [{angle: 0, radius: 10}, {angle: Math.PI/2, radius: 15}]; Accessors: startAngle=d=>d.angle, endAngle=d=>d.angle+0.1, innerRadius=d=>5, outerRadius=d=>d.radius"
    output: "SVG path string or canvas drawing of a radial area segment in polar space"
    notes: "Demonstrates basic angle and radius mapping for a two-point radial area"
  - input: "Rose diagram data with 12 petals; each petal has angle range and variable radius"
    output: "Configured generator produces closed radial area paths for each petal when called with dataset"
    notes: "Common use case for rose/polar area charts"
---

# Collect Field CLS Attribution Data

Configure and generate area chart shapes (Cartesian or radial) by setting baseline/topline accessors (or angle/radius for radial), curve interpolation, and rendering context. Use when building area, radial area, or rose diagrams from tabular data.

## Prompt

Create a radial area generator by chaining accessor methods: set startAngle and endAngle to map angular position, set innerRadius and outerRadius to map radial extent, optionally configure curve interpolation and rendering context. Pass a dataset to the configured generator to produce SVG path data or canvas rendering in polar coordinates.

## Objective

Generate radial area geometry for charting
## Applicable Signals

- Dataset with angular and radial dimensions
- Requirement for polar coordinate visualization
- Need for configurable curve interpolation in radial space

## Contraindications

- Rendering Cartesian area charts
- Line charts or non-radial geometries
- When polar coordinates are not required
- Non-tabular or unstructured data sources

## Workflow Steps

- Create a new area generator using d3.area() for Cartesian or d3.areaRadial() for polar coordinates
- For Cartesian areas: chain accessor methods .x0(), .x1() to define baseline and .y0(), .y1() to define topline
- For radial areas: chain accessor methods .startAngle() and .endAngle() for angular position, .innerRadius() and .outerRadius() for radial extent
- Set curve interpolator using .curve() method; defaults to curveLinear
- Set rendering context using .context() if canvas rendering is needed; omit for SVG path output
- Call the configured generator with dataset to produce path data or render to canvas

## Constraints

- Data must be array-like with consistent field structure
- Accessor functions must return numeric values for coordinates (Cartesian) or angles in radians and radii (radial)
- Curve type must be a valid d3 curve factory
- For radial areas: innerRadius must be less than or equal to outerRadius

## Cautions

- Ensure accessor functions handle undefined or missing data gracefully via defined() method
- Verify curve type is compatible with area geometry (not all curves suit areas)
- Context setting is required for canvas rendering; omit for SVG path output
- For radial areas: angle values should be in radians; convert from degrees if needed

## Output Contract

- Configured radial area generator object that accepts a dataset and produces SVG path data (string) or canvas rendering in polar coordinates; output is a closed path enclosing the area between startAngle/endAngle and innerRadius/outerRadius for each data point

## Example Executions

### Example 1

- Input: Dataset: [{angle: 0, radius: 10}, {angle: Math.PI/2, radius: 15}]; Accessors: startAngle=d=>d.angle, endAngle=d=>d.angle+0.1, innerRadius=d=>5, outerRadius=d=>d.radius
- Output: SVG path string or canvas drawing of a radial area segment in polar space
- Notes: Demonstrates basic angle and radius mapping for a two-point radial area

### Example 2

- Input: Rose diagram data with 12 petals; each petal has angle range and variable radius
- Output: Configured generator produces closed radial area paths for each petal when called with dataset
- Notes: Common use case for rose/polar area charts

## Triggers

- Need to understand CLS patterns in production environments
- Correlating layout shifts with real user behavior and interactions
- Debugging field performance issues reported by end users
- Establishing baseline CLS metrics across user segments

## Examples

### Example 1

Input:

  Dataset: [{angle: 0, radius: 10}, {angle: Math.PI/2, radius: 15}]; Accessors: startAngle=d=>d.angle, endAngle=d=>d.angle+0.1, innerRadius=d=>5, outerRadius=d=>d.radius

Output:

  SVG path string or canvas drawing of a radial area segment in polar space

Notes:

  Demonstrates basic angle and radius mapping for a two-point radial area

### Example 2

Input:

  Rose diagram data with 12 petals; each petal has angle range and variable radius

Output:

  Configured generator produces closed radial area paths for each petal when called with dataset

Notes:

  Common use case for rose/polar area charts
