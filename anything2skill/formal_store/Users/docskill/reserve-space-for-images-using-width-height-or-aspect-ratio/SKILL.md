---
id: "1bfee323-162c-54a1-aa26-bee590f1710f"
name: "Reserve space for images using width, height, or aspect-ratio"
description: "Prevent layout shifts caused by images by explicitly declaring dimensions via `width` and `height` attributes or CSS `aspect-ratio` property before the image loads. This ensures the browser allocates correct layout space in the document while the image is fetching."
version: "0.1.0"
tags:
  - "layout_shift"
  - "CLS"
  - "image_optimization"
  - "web_performance"
  - "reflow_prevention"
triggers:
  - "Images are present on the page and dimensions are known; developer wants to eliminate image-related CLS."
---

# Reserve space for images using width, height, or aspect-ratio

Prevent layout shifts caused by images by explicitly declaring dimensions via `width` and `height` attributes or CSS `aspect-ratio` property before the image loads. This ensures the browser allocates correct layout space in the document while the image is fetching.

## Prompt

When implementing this skill:
1. Add `width` and `height` attributes to all `<img>` and `<video>` elements with known dimensions.
2. Alternatively, use CSS `aspect-ratio` property to reserve space.
3. Ensure space is allocated before the browser fetches the image resource.
4. Verify that the reserved space matches the actual image dimensions to avoid distortion.

## Objective

prevent_image_reflow
## Applicable Signals

- Images present on page with known dimensions
- Developer goal is to eliminate image-related Cumulative Layout Shift (CLS)
- Page performance audit identifies image-caused layout shifts

## Contraindications

- Image dimensions are truly unknown or highly variable across breakpoints
- Images are decorative-only and can be lazy-loaded without space reservation
- Responsive images require fluid sizing without fixed aspect ratio

## Intervention Moves

- Add `width` and `height` attributes to `<img>` tags
- Apply CSS `aspect-ratio` property as alternative
- Reserve layout space before image fetch begins

## Constraints

- Dimensions must be known at implementation time
- Reserved space should match actual image dimensions to avoid distortion
- Method must be applied before image resource is fetched

## Cautions

- Mismatched reserved space and actual image dimensions can cause visual distortion
- Decorative images may not justify space reservation overhead

## Output Contract

- All images on the page have explicit width/height attributes or CSS aspect-ratio set
- Browser allocates correct layout space before image fetch completes
- No image-related layout shifts occur

## Triggers

- Images are present on the page and dimensions are known; developer wants to eliminate image-related CLS.
