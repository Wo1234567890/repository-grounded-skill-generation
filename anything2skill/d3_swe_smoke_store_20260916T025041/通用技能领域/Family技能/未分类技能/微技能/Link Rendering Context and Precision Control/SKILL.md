---
id: "cee1b101-d11e-5a4e-af5c-bb4a7b3493c9"
name: "Link Rendering Context and Precision Control"
description: "Configure the rendering context (canvas or SVG) and output precision for link path generation. This micro-skill optimizes rendering performance and controls numerical precision in generated link paths."
version: "0.1.0"
tags:
  - "d3"
  - "link-generation"
  - "rendering"
  - "canvas"
  - "svg"
  - "precision"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Switching between canvas and SVG rendering backends"
  - "Tuning output file size or numerical precision for large datasets"
  - "Optimizing rendering performance for specific output format"
---

# Link Rendering Context and Precision Control

Configure the rendering context (canvas or SVG) and output precision for link path generation. This micro-skill optimizes rendering performance and controls numerical precision in generated link paths.

## Prompt

Use link.context() to set the rendering backend (canvas or SVG context object) and link.digits() to specify decimal precision for path output. Apply these configurations to a link generator before invoking it to render paths.

## Objective

Configure rendering backend and numerical precision for link path output
## Applicable Signals

- Caller specifies canvas context object
- Caller specifies SVG context object
- Caller requests reduced decimal precision
- Caller requests increased decimal precision

## Contraindications

- Using default rendering context with no precision requirements
- No explicit rendering backend preference

## Workflow Steps

- Obtain or create a link generator (d3.link, d3.linkVertical, d3.linkHorizontal, or d3.linkRadial)
- Call link.context(contextObject) to set the rendering backend
- Call link.digits(precisionInteger) to set decimal precision
- Invoke the configured link generator to render paths

## Constraints

- Context must be a valid canvas or SVG rendering context
- Digits parameter must be a non-negative integer
- Configuration must be applied before link generator invocation

## Cautions

- Reducing precision may introduce visual artifacts in complex paths
- Canvas context and SVG context have different coordinate systems; verify compatibility

## Output Contract

- Link generator configured to output paths to the specified context (canvas or SVG) with the specified decimal precision. Subsequent invocations of the link generator produce paths rendered to the configured backend with the configured precision.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Switching between canvas and SVG rendering backends
- Tuning output file size or numerical precision for large datasets
- Optimizing rendering performance for specific output format
