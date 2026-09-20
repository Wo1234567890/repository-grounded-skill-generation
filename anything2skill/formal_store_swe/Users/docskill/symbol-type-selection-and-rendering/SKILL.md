---
id: "854f25f5-6cdb-529f-ac94-b2c9a1b99cf4"
name: "Symbol Type Selection and Rendering"
description: "Select and render a specific symbol type (circle, square, star, triangle, etc.) with appropriate fill or stroke styling for categorical shape encoding in visualizations."
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
  - "Encoding categorical data with a single shape glyph"
examples:
  - input: "symbolType = d3.symbolCircle, context = canvas2d"
    output: "Circle glyph rendered to canvas context"
    notes: "Fill symbol suitable for scatterplot marks"
  - input: "symbolType = d3.symbolStar, context = canvas2d"
    output: "Pentagonal star glyph rendered to canvas context"
    notes: "Fill symbol for categorical distinction"
  - input: "symbolType = d3.symbolCross, context = canvas2d"
    output: "Greek cross glyph rendered to canvas context"
    notes: "Stroke symbol for outline rendering"
---

# Symbol Type Selection and Rendering

Select and render a specific symbol type (circle, square, star, triangle, etc.) with appropriate fill or stroke styling for categorical shape encoding in visualizations.

## Prompt

Choose one symbol type from the built-in catalog (d3.symbolCircle, d3.symbolSquare, d3.symbolStar, d3.symbolTriangle, d3.symbolDiamond, d3.symbolAsterisk, d3.symbolCross, d3.symbolPlus, d3.symbolWye, or stroke variants). Call symbolType.draw(context) to render the selected symbol to the given rendering context.

## Objective

Choose and render one symbol type from built-in catalog
## Applicable Signals

- Need to render a single symbol type for a scatterplot or mark
- Symbol type already determined; ready for rendering

## Contraindications

- Rendering multiple symbol types in a single call; use the generator workflow instead
- Dynamically switching symbol types per datum; use d3.symbol generator with type accessor

## Workflow Steps

- {'step': 1, 'action': 'Select symbol type', 'detail': 'Choose one constant from d3.symbolsFill (circle, square, star, triangle, diamond, wye) or d3.symbolsStroke (asterisk, cross, plus, diamond2, square2, triangle2)'}
- {'step': 2, 'action': 'Obtain or create rendering context', 'detail': 'Prepare a canvas or SVG context for drawing'}
- {'step': 3, 'action': 'Call symbolType.draw(context)', 'detail': 'Invoke the draw method on the selected symbol type to render it to the context'}

## Constraints

- Symbol type must be one of the built-in d3.symbol* constants
- Rendering context must be provided and valid
- Fill symbols (circle, square, star, triangle, diamond, wye) and stroke symbols (asterisk, cross, plus, diamond2, square2, triangle2) have different visual purposes

## Cautions

- Verify symbol type matches rendering intent (fill vs. stroke)
- Ensure context is initialized before calling draw()

## Output Contract

- A rendered symbol of the selected type drawn to the specified context; the symbol is visually complete and ready for display or further composition.

## Example Executions

### Example 1

- Input: symbolType = d3.symbolCircle, context = canvas2d
- Output: Circle glyph rendered to canvas context
- Notes: Fill symbol suitable for scatterplot marks

### Example 2

- Input: symbolType = d3.symbolStar, context = canvas2d
- Output: Pentagonal star glyph rendered to canvas context
- Notes: Fill symbol for categorical distinction

### Example 3

- Input: symbolType = d3.symbolCross, context = canvas2d
- Output: Greek cross glyph rendered to canvas context
- Notes: Stroke symbol for outline rendering

## Triggers

- Assigning a specific categorical symbol to a data point or series
- Encoding categorical data with a single shape glyph

## Examples

### Example 1

Input:

  symbolType = d3.symbolCircle, context = canvas2d

Output:

  Circle glyph rendered to canvas context

Notes:

  Fill symbol suitable for scatterplot marks

### Example 2

Input:

  symbolType = d3.symbolStar, context = canvas2d

Output:

  Pentagonal star glyph rendered to canvas context

Notes:

  Fill symbol for categorical distinction

### Example 3

Input:

  symbolType = d3.symbolCross, context = canvas2d

Output:

  Greek cross glyph rendered to canvas context

Notes:

  Stroke symbol for outline rendering
