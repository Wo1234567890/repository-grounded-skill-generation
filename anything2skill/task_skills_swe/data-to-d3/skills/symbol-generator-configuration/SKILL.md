---
id: "41aaaa90-4384-567c-9b45-0c36d8ef6a44"
name: "Symbol Generator Configuration"
description: "Create and configure a reusable symbol generator for categorical shape encoding in visualizations. Set symbol type, size, rendering context, and output precision to produce a generator object ready to render symbols for data points."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "symbol"
  - "categorical_encoding"
  - "scatterplot"
  - "shape_encoding"
triggers:
  - "Building a scatterplot or categorical visualization"
  - "Need consistent symbol rendering across multiple data points"
  - "Encoding categorical variables as distinct shapes"
examples:
  - input: "Create a symbol generator for a scatterplot with circle symbols, 64 square pixels each"
    output: "const symbolGen = d3.symbol().type(d3.symbolCircle).size(64); symbolGen is ready to render circles"
    notes: "Circle is suitable for fill rendering; size 64 produces moderate-sized symbols"
  - input: "Configure a symbol generator with square type, 100 square pixels, and canvas context"
    output: "const symbolGen = d3.symbol().type(d3.symbolSquare).size(100).context(canvasContext); symbolGen renders to canvas"
    notes: "Canvas context enables efficient rendering for large datasets"
---

# Symbol Generator Configuration

Create and configure a reusable symbol generator for categorical shape encoding in visualizations. Set symbol type, size, rendering context, and output precision to produce a generator object ready to render symbols for data points.

## Prompt

Initialize a symbol generator using d3.symbol(). Configure the generator by chaining methods: set symbol.type() to choose a shape (e.g., circle, square, triangle), set symbol.size() to specify area in square pixels, set symbol.context() to define the rendering target, and optionally set symbol.digits() for output precision. The configured generator is then ready to render symbols for data points.

## Objective

Configure a reusable symbol generator with type, size, and rendering parameters for categorical shape encoding
## Applicable Signals

- Visualization requires shape-based categorical distinction
- Multiple data points need uniform symbol styling
- Symbol type and size must be configurable

## Contraindications

- Rendering continuous color scales
- Encoding geographic or spatial features
- Non-categorical or continuous data encoding
- Simple marker rendering without configuration needs

## Workflow Steps

- {'step': 1, 'action': 'Create symbol generator', 'detail': 'Call d3.symbol() to instantiate a new symbol generator object'}
- {'step': 2, 'action': 'Set symbol type', 'detail': 'Call symbol.type() with a symbol type constant (e.g., d3.symbolCircle, d3.symbolSquare)'}
- {'step': 3, 'action': 'Set symbol size', 'detail': 'Call symbol.size() with a numeric value representing area in square pixels'}
- {'step': 4, 'action': 'Set rendering context', 'detail': 'Call symbol.context() to specify the target rendering context (canvas or SVG)'}
- {'step': 5, 'action': 'Optional: Set output precision', 'detail': 'Call symbol.digits() to control decimal precision in output if needed'}

## Constraints

- Symbol type must be selected from d3 built-in types (circle, square, triangle, diamond, star, cross, asterisk, plus, wye, or variants)
- Size must be specified in square pixels
- Context must be a valid rendering target (canvas or SVG context)

## Cautions

- Symbol type selection affects rendering quality; fill-oriented types (circle, square, triangle, diamond, star, wye) differ from stroke-oriented types (asterisk, cross, plus, diamond2, square2, triangle2)
- Size in square pixels may require scaling based on data range and visualization dimensions
- Context must be properly initialized before symbol rendering

## Output Contract

- A configured symbol generator object ready to render symbols for given data. The generator accepts datum input and produces symbol path or drawing output to the specified context with the configured type, size, and precision.

## Example Executions

### Example 1

- Input: Create a symbol generator for a scatterplot with circle symbols, 64 square pixels each
- Output: const symbolGen = d3.symbol().type(d3.symbolCircle).size(64); symbolGen is ready to render circles
- Notes: Circle is suitable for fill rendering; size 64 produces moderate-sized symbols

### Example 2

- Input: Configure a symbol generator with square type, 100 square pixels, and canvas context
- Output: const symbolGen = d3.symbol().type(d3.symbolSquare).size(100).context(canvasContext); symbolGen renders to canvas
- Notes: Canvas context enables efficient rendering for large datasets

## Triggers

- Building a scatterplot or categorical visualization
- Need consistent symbol rendering across multiple data points
- Encoding categorical variables as distinct shapes

## Examples

### Example 1

Input:

  Create a symbol generator for a scatterplot with circle symbols, 64 square pixels each

Output:

  const symbolGen = d3.symbol().type(d3.symbolCircle).size(64); symbolGen is ready to render circles

Notes:

  Circle is suitable for fill rendering; size 64 produces moderate-sized symbols

### Example 2

Input:

  Configure a symbol generator with square type, 100 square pixels, and canvas context

Output:

  const symbolGen = d3.symbol().type(d3.symbolSquare).size(100).context(canvasContext); symbolGen renders to canvas

Notes:

  Canvas context enables efficient rendering for large datasets
