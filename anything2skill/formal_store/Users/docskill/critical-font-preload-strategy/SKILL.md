---
id: "18d3559c-4376-5c2d-b0ce-1f3c590cfad8"
name: "Critical Font Preload Strategy"
description: "Preload critical web fonts early in the document head using <link rel=preload> to increase the likelihood that fonts are available by first paint, eliminating layout shift caused by font swap or late font availability."
version: "0.1.0"
tags:
  - "web_fonts"
  - "cumulative_layout_shift"
  - "performance"
  - "resource_loading"
  - "above_the_fold"
triggers:
  - "web font is required for above-the-fold content"
  - "font file size is moderate and preload overhead is justified"
---

# Critical Font Preload Strategy

Preload critical web fonts early in the document head using <link rel=preload> to increase the likelihood that fonts are available by first paint, eliminating layout shift caused by font swap or late font availability.

## Prompt

Add a <link rel=preload> tag in the document <head> for each critical web font required for above-the-fold content. Specify the font file path, type (font/woff2 or font/woff), and crossorigin attribute if needed. Ensure the preload is placed before other non-critical resources to maximize priority.

## Objective

accelerate_critical_font_availability
## Applicable Signals

- web font is required for above-the-fold content
- font file size is moderate and preload overhead is justified
- CLS is observed due to font swap or late font availability

## Contraindications

- font is non-critical or below-the-fold only
- preload budget is exhausted by other critical resources
- font is already cached or served from a fast CDN with negligible load time

## Intervention Moves

- Identify critical web fonts used in above-the-fold content
- Determine font file path and MIME type (font/woff2 or font/woff)
- Add <link rel=preload> tag in document <head> before non-critical resources
- Verify font loads before first paint using performance tools
- Confirm CLS from font swap is eliminated or negligible

## Workflow Steps

- Identify critical web fonts used in above-the-fold content
- Determine the font file path and MIME type (e.g., font/woff2)
- Add <link rel=preload href="[font-path]" as="font" type="font/woff2" crossorigin> in the document <head>, before other non-critical resources
- Verify the font loads before first paint using performance tools
- Confirm CLS from font swap is eliminated or negligible

## Constraints

- Preload only fonts that are genuinely critical; excessive preloads degrade overall page load performance
- Use appropriate MIME type (font/woff2 for modern browsers, font/woff for broader compatibility)
- Include crossorigin attribute if the font is served from a different origin

## Cautions

- Preloading too many fonts can consume bandwidth and delay other critical resources
- Monitor cumulative preload overhead; prioritize fonts that have the highest impact on CLS

## Output Contract

- <link rel=preload> tag present in document <head> for critical font file
- Font loads before first paint
- CLS from font swap is eliminated or negligible

## Triggers

- web font is required for above-the-fold content
- font file size is moderate and preload overhead is justified
