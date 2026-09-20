---
id: "b819db81-00de-5681-a388-8b25b47a43b2"
name: "Preload Critical Web Fonts"
description: "Use `<link rel=preload>` to load critical web fonts early in the page lifecycle, increasing the likelihood they are available before first paint and eliminating layout shift caused by font loading."
version: "0.1.0"
tags:
  - "web_performance"
  - "CLS_mitigation"
  - "font_loading"
  - "resource_optimization"
  - "page_speed"
triggers:
  - "Web fonts are critical for above-the-fold content"
  - "Font loading time is identified as a performance bottleneck"
  - "CLS is caused by late font availability or font swap"
---

# Preload Critical Web Fonts

Use `<link rel=preload>` to load critical web fonts early in the page lifecycle, increasing the likelihood they are available before first paint and eliminating layout shift caused by font loading.

## Prompt

Add a preload link in the document head for each critical web font. Use `<link rel="preload" as="font" href="path/to/font.woff2" type="font/woff2" crossorigin>`. Ensure the font file path is correct and the font is truly critical for above-the-fold content. A preloaded font has a higher chance to meet the first paint, eliminating layout shifting.

## Objective

Ensure web font availability before first paint to prevent Cumulative Layout Shift (CLS)
## Applicable Signals

- Font-related layout shift detected in performance metrics
- Web font load time exceeds first paint timing
- Critical text content depends on custom font rendering

## Contraindications

- Font is non-critical or positioned below the fold
- Preload budget is exhausted or resource hints are already at capacity
- Font is already inlined or served from a warm cache

## Intervention Moves

- Insert preload link in document head before other resource hints
- Pair preload with appropriate font-display strategy (optional or swap)
- Specify correct font file format and crossorigin attribute

## Workflow Steps

- {'step': 1, 'action': 'Identify critical web fonts', 'detail': 'Determine which fonts are essential for above-the-fold content rendering'}
- {'step': 2, 'action': 'Add preload link to document head', 'detail': 'Insert `<link rel="preload" as="font" href="font-url" type="font/woff2" crossorigin>` before other resource hints'}
- {'step': 3, 'action': 'Verify font availability at first paint', 'detail': 'Use performance monitoring tools to confirm font is loaded before first paint'}
- {'step': 4, 'action': 'Measure CLS reduction', 'detail': 'Compare CLS metrics before and after preload implementation'}

## Constraints

- Only preload fonts that are genuinely critical; excessive preloading degrades performance
- Ensure crossorigin attribute is set when loading from a different origin
- Verify font file format is supported by target browsers

## Cautions

- Preloading too many fonts can block other critical resources
- Font file paths must be accurate; broken preload links waste bandwidth
- Combine with appropriate font-display strategy (e.g., font-display: optional or font-display: swap) for best results

## Output Contract

- Preload link is added to document head
- Font is fetched early in the page lifecycle
- Font is available by first paint, eliminating layout shift caused by font loading

## Triggers

- Web fonts are critical for above-the-fold content
- Font loading time is identified as a performance bottleneck
- CLS is caused by late font availability or font swap
