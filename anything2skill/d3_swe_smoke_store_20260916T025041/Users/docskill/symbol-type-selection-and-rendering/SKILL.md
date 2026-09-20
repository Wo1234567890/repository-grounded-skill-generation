---
id: "93959f5e-32ea-5c9e-939d-09c9f06a6157"
name: "Symbol Type Selection and Rendering"
description: "Select and render a specific symbol type (circle, square, star, triangle, diamond, cross, asterisk, plus, wye) with appropriate fill or stroke styling for categorical shape encoding in visualizations."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "symbol"
  - "shape_encoding"
  - "categorical"
  - "rendering"
triggers:
  - "Assigning a specific categorical symbol to a data point or series"
examples:
  - input: "symbol_type = d3.symbolCircle, context = canvas_2d_context"
    output: "A filled circle rendered to the canvas context"
    notes: "Circle supports both fill and stroke; fill is default"
  - input: "symbol_type = d3.symbolStar, context = svg_path_context"
    output: "A pentagonal star (pentagram) rendered to the SVG context"
    notes: "Star is fill-only"
  - input: "symbol_type = d3.symbolAsterisk, context = canvas_2d_context"
    output: "An asterisk mark rendered to the canvas context"
    notes: "Asterisk is stroke-only"
---

# Symbol Type Selection and Rendering

Select and render a specific symbol type (circle, square, star, triangle, diamond, cross, asterisk, plus, wye) with appropriate fill or stroke styling for categorical shape encoding in visualizations.

## Prompt

Choose one symbol type from the built-in catalog (circle, square, star, triangle, diamond, cross, asterisk, plus, wye, or rotated variants). Determine whether the symbol should use fill or stroke rendering based on the symbol type constraints. Call symbolType.draw() to render the symbol to the target context.

## Objective

Choose and render one symbol type from built-in catalog to a rendering context
## Applicable Signals

- Assigning a specific categorical symbol to a single data point
- Rendering a symbol for a series with uniform type
- Need to encode categorical data as a visual mark

## Contraindications

- Do not use when rendering multiple different symbol types in a single operation; use the symbol generator workflow instead
- Do not use when symbol type must be dynamically selected per datum; delegate to generator configuration

## Intervention Moves

- Identify the symbol type required (e.g., d3.symbolCircle, d3.symbolSquare, d3.symbolStar, d3.symbolTriangle)
- Verify the symbol supports the intended rendering mode (fill or stroke)
- Call symbolType.draw(context) to render the symbol to the target canvas or SVG context

## Constraints

- Fill-only symbols: circle, diamond, square, star, triangle, cross, wye
- Stroke-only symbols: asterisk, diamond2, plus, square2, triangle2
- Fill or stroke: circle

## Cautions

- Verify the rendering context is valid before calling draw()
- Ensure the symbol type matches the intended visual encoding (fill vs. stroke)

## Output Contract

- A rendered symbol of the selected type drawn to the specified rendering context; the symbol is immediately visible or queued for rendering in the target canvas or SVG element.

## Example Therapist Responses

### Example 1

- Client/Input: symbol_type = d3.symbolCircle, context = canvas_2d_context
- Therapist/Output: A filled circle rendered to the canvas context
- Notes: Circle supports both fill and stroke; fill is default

### Example 2

- Client/Input: symbol_type = d3.symbolStar, context = svg_path_context
- Therapist/Output: A pentagonal star (pentagram) rendered to the SVG context
- Notes: Star is fill-only

### Example 3

- Client/Input: symbol_type = d3.symbolAsterisk, context = canvas_2d_context
- Therapist/Output: An asterisk mark rendered to the canvas context
- Notes: Asterisk is stroke-only

## Triggers

- Assigning a specific categorical symbol to a data point or series

## Examples

### Example 1

Input:

  symbol_type = d3.symbolCircle, context = canvas_2d_context

Output:

  A filled circle rendered to the canvas context

Notes:

  Circle supports both fill and stroke; fill is default

### Example 2

Input:

  symbol_type = d3.symbolStar, context = svg_path_context

Output:

  A pentagonal star (pentagram) rendered to the SVG context

Notes:

  Star is fill-only

### Example 3

Input:

  symbol_type = d3.symbolAsterisk, context = canvas_2d_context

Output:

  An asterisk mark rendered to the canvas context

Notes:

  Asterisk is stroke-only
