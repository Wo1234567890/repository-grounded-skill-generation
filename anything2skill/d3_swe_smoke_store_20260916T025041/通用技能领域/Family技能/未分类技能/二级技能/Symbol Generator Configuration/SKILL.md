---
id: "41aaaa90-4384-567c-9b45-0c36d8ef6a44"
name: "Symbol Generator Configuration"
description: "Create and configure a reusable d3 symbol generator for categorical shape encoding in visualizations. Set symbol type, size, rendering context, and output precision to produce a generator object that renders consistent symbols across multiple data points."
version: "0.1.0"
tags:
  - "d3"
  - "visualization"
  - "symbol"
  - "categorical_encoding"
  - "scatterplot"
  - "shape_encoding"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Building a scatterplot or categorical visualization"
  - "Need consistent symbol rendering across multiple data points"
  - "Encoding categorical variables as distinct shapes"
examples:
  - input: "Create a circle symbol generator with 64 square pixels size for canvas rendering"
    output: "const symbolGen = d3.symbol().type(d3.symbolCircle).size(64).context(canvasContext); symbolGen(dataPoint) renders a circle"
    notes: "Typical scatterplot setup with uniform circle encoding"
  - input: "Configure a multi-type symbol generator for categorical distinction (square for category A, triangle for category B)"
    output: "const symbolGen = d3.symbol().size(100); then call symbolGen.type(d3.symbolSquare) or symbolGen.type(d3.symbolTriangle) based on category before rendering"
    notes: "Symbol type can be changed between calls for different categories"
---

# Symbol Generator Configuration

Create and configure a reusable d3 symbol generator for categorical shape encoding in visualizations. Set symbol type, size, rendering context, and output precision to produce a generator object that renders consistent symbols across multiple data points.

## Prompt

Initialize a symbol generator using d3.symbol(). Configure the generator by chaining methods: set symbol.type() to choose a shape (e.g., circle, square, triangle), set symbol.size() to specify area in square pixels, set symbol.context() to define the rendering target (canvas or SVG path context), and optionally set symbol.digits() for output precision. The configured generator is then ready to render symbols for data points.

## Objective

Configure a reusable symbol generator with type, size, and rendering parameters for categorical shape encoding
## Applicable Signals

- Visualization requires shape-based categorical distinction
- Multiple data points need uniform symbol styling
- Symbol type and size must be configurable per dataset

## Contraindications

- Rendering continuous color scales
- Encoding geographic or spatial features
- Non-categorical or continuous data encoding
- Simple marker rendering without configuration needs

## Workflow Steps

- {'step': 1, 'action': 'Create symbol generator', 'detail': 'Call d3.symbol() to instantiate a new symbol generator object'}
- {'step': 2, 'action': 'Set symbol type', 'detail': 'Call symbol.type(typeValue) where typeValue is one of d3.symbolCircle, d3.symbolSquare, d3.symbolTriangle, d3.symbolStar, d3.symbolDiamond, d3.symbolCross, d3.symbolAsterisk, d3.symbolPlus, d3.symbolWye, or stroke variants (symbolDiamond2, symbolSquare2, symbolTriangle2)'}
- {'step': 3, 'action': 'Set symbol size', 'detail': 'Call symbol.size(pixelArea) where pixelArea is a numeric value representing the area in square pixels'}
- {'step': 4, 'action': 'Set rendering context', 'detail': 'Call symbol.context(ctx) where ctx is a canvas 2D context or SVG path context for output rendering'}
- {'step': 5, 'action': 'Optional: set output precision', 'detail': 'Call symbol.digits(n) to set numeric precision for path output if needed'}
- {'step': 6, 'action': 'Return configured generator', 'detail': 'The symbol generator is now ready to be called with data to render symbols'}

## Constraints

- Symbol type must be selected from d3 built-in types: circle, square, triangle, star, diamond, cross, asterisk, plus, wye, or stroke variants (diamond2, square2, triangle2)
- Size must be specified in square pixels as a numeric value
- Context must be a valid rendering context (canvas 2D context or SVG path context)
- Digits parameter applies only to numeric output precision for path data

## Cautions

- Ensure rendering context is valid before passing to symbol.context()
- Symbol size should be appropriate for the visualization scale to avoid overlapping or invisible symbols
- Different symbol types have different visual weights; test rendering to verify visual consistency
- Use d3.symbolsFill for fill-compatible types and d3.symbolsStroke for stroke-compatible types

## Output Contract

- A configured symbol generator object that accepts a datum and renders the specified symbol type at the configured size to the specified rendering context
- The generator is reusable across multiple data points and can be invoked repeatedly with different data
- Calling the generator with a datum produces a rendered symbol in the specified context

## Example Therapist Responses

### Example 1

- Client/Input: Create a circle symbol generator with 64 square pixels size for canvas rendering
- Therapist/Output: const symbolGen = d3.symbol().type(d3.symbolCircle).size(64).context(canvasContext); symbolGen(dataPoint) renders a circle
- Notes: Typical scatterplot setup with uniform circle encoding

### Example 2

- Client/Input: Configure a multi-type symbol generator for categorical distinction (square for category A, triangle for category B)
- Therapist/Output: const symbolGen = d3.symbol().size(100); then call symbolGen.type(d3.symbolSquare) or symbolGen.type(d3.symbolTriangle) based on category before rendering
- Notes: Symbol type can be changed between calls for different categories

## 子技能目录
- [Symbol Type Selection and Rendering](通用技能领域/Family技能/未分类技能/微技能/Symbol Type Selection and Rendering/SKILL.md) ｜ 适用：Select and render a specific symbol type (circle, square, star, triangle, diamond, cross, asterisk, plus, wye) with appropriate fill or stroke styling for categorical shape encoding in visualizations.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Symbol Type Selection and Rendering` 时，优先调用它。 线索：Assigning a specific categorical symbol to a data point or series, d3, visualization, symbol, shape_encoding

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building a scatterplot or categorical visualization
- Need consistent symbol rendering across multiple data points
- Encoding categorical variables as distinct shapes

## Examples

### Example 1

Input:

  Create a circle symbol generator with 64 square pixels size for canvas rendering

Output:

  const symbolGen = d3.symbol().type(d3.symbolCircle).size(64).context(canvasContext); symbolGen(dataPoint) renders a circle

Notes:

  Typical scatterplot setup with uniform circle encoding

### Example 2

Input:

  Configure a multi-type symbol generator for categorical distinction (square for category A, triangle for category B)

Output:

  const symbolGen = d3.symbol().size(100); then call symbolGen.type(d3.symbolSquare) or symbolGen.type(d3.symbolTriangle) based on category before rendering

Notes:

  Symbol type can be changed between calls for different categories
