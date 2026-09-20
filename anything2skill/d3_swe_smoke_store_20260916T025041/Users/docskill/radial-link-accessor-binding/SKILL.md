---
id: "1c691d52-1981-5add-9d0b-e4a0bf4abbcb"
name: "Radial Link Accessor Binding"
description: "Bind angle and radius accessors to a radial link generator for rendering curved connectors in polar coordinate systems."
version: "0.1.0"
tags:
  - "d3"
  - "link-generator"
  - "radial"
  - "polar-coordinates"
  - "accessor-binding"
  - "visualization"
triggers:
  - "Configuring radial link generators for circular tree or radial force layouts"
---

# Radial Link Accessor Binding

Bind angle and radius accessors to a radial link generator for rendering curved connectors in polar coordinate systems.

## Prompt

Use d3.linkRadial() to create a radial link generator. Call linkRadial.angle() to set the point angle accessor and linkRadial.radius() to set the point radius accessor. These accessors extract angle and radius values from source and target data objects, enabling the generator to produce smooth cubic Bézier curves in polar coordinates.

## Objective

Set angle and radius accessors on a radial link generator
## Applicable Signals

- Configuring radial link generators for circular tree layouts
- Setting up radial force layouts with curved connectors
- Binding polar coordinate accessors to link generators

## Contraindications

- Do not use when working with Cartesian (vertical or horizontal) link generators
- Do not use when accessors are already bound to the generator
- Do not use for non-polar coordinate systems

## Intervention Moves

- Create radial link generator with d3.linkRadial()
- Bind angle accessor via linkRadial.angle(accessor_function)
- Bind radius accessor via linkRadial.radius(accessor_function)

## Workflow Steps

- {'step': 1, 'action': 'Create a radial link generator', 'detail': 'Call d3.linkRadial() to instantiate the generator'}
- {'step': 2, 'action': 'Set the angle accessor', 'detail': 'Call linkRadial.angle(d => d.angle) or equivalent to extract angle from data'}
- {'step': 3, 'action': 'Set the radius accessor', 'detail': 'Call linkRadial.radius(d => d.radius) or equivalent to extract radius from data'}
- {'step': 4, 'action': 'Verify binding', 'detail': 'Test generator with sample source and target objects to confirm accessors extract correct values'}

## Constraints

- Angle accessor must return numeric values in radians or degrees
- Radius accessor must return non-negative numeric values
- Source and target data objects must contain fields accessible by the provided accessor functions

## Cautions

- Ensure accessor functions handle missing or undefined data gracefully
- Verify angle and radius ranges match the intended visualization bounds

## Output Contract

- A radial link generator with angle and radius accessors bound to data field extractors, ready to generate smooth cubic Bézier curves in polar coordinates when invoked with source and target data objects.

## Triggers

- Configuring radial link generators for circular tree or radial force layouts
