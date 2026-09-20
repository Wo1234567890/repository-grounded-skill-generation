---
id: "c03cab17-cce0-5065-a181-06aa165cf87d"
name: "Next.js Image Optimization"
description: "Optimize images in Next.js applications using the built-in next/image component to reduce file size, improve load performance, and enable responsive sizing and lazy loading."
version: "0.1.0"
tags:
  - "next.js"
  - "image-optimization"
  - "performance"
  - "responsive-design"
  - "lazy-loading"
  - "asset-optimization"
triggers:
  - "application contains raster images (PNG, JPG, GIF) requiring responsive sizing"
  - "page load performance metrics show image payload as bottleneck"
  - "need for automatic format conversion and lazy loading"
examples:
  - input: "Static image asset in public/images/hero.jpg, 1200x600px, above-the-fold"
    output: "Image component with priority=true, width=1200, height=600, automatic WebP conversion, eager load"
    notes: "Use priority=true only for hero/critical images"
  - input: "Responsive image gallery with unknown dimensions, external source"
    output: "Image component with layout='fill', parent container with position:relative, lazy loading enabled by default"
    notes: "External domain must be whitelisted in next.config.js"
---

# Next.js Image Optimization

Optimize images in Next.js applications using the built-in next/image component to reduce file size, improve load performance, and enable responsive sizing and lazy loading.

## Prompt

Use the next/image component to wrap image assets. Configure width, height, and priority props. The component automatically handles responsive sizing, format conversion (WebP), and lazy loading. Set priority=true only for above-the-fold images to avoid layout shift.

## Objective

reduce image payload and rendering latency through component-based optimization
## Applicable Signals

- images present in layout or page components
- responsive design requirements across device sizes
- performance audit flags unoptimized image delivery

## Contraindications

- images already served from external CDN with pre-optimization applied
- SVG-only assets (use native img or inline SVG instead)
- images requiring custom loading behavior incompatible with next/image constraints

## Intervention Moves

- Replace img tags with next/image Image component
- Configure width and height props to prevent layout shift
- Set priority=true for critical above-the-fold images only
- Whitelist external image domains in next.config.js

## Workflow Steps

- {'step': 1, 'action': 'Import Image component', 'detail': "import Image from 'next/image'"}
- {'step': 2, 'action': 'Replace img tags with Image component', 'detail': 'Wrap image source and set width, height, alt, and optional priority props'}
- {'step': 3, 'action': 'Configure external domains if needed', 'detail': 'Add image domain to next.config.js images.domains array'}
- {'step': 4, 'action': 'Verify responsive behavior', 'detail': 'Test image rendering across breakpoints; confirm lazy loading in DevTools Network tab'}

## Constraints

- width and height props must be specified or layout='fill' used with parent position:relative
- priority prop should be set to true only for critical above-the-fold images
- external image domains must be configured in next.config.js

## Cautions

- Cumulative Layout Shift (CLS) can occur if dimensions are not locked; always provide explicit width/height or use layout='fill'
- priority=true on multiple images negates performance benefit; reserve for single hero image per page

## Output Contract

- Images served with appropriate resolution and format (WebP when supported)
- lazy-load attributes applied to off-screen images
- priority images loaded eagerly
- initial page load time reduced
- no layout shift on image load

## Example Executions

### Example 1

- Input: Static image asset in public/images/hero.jpg, 1200x600px, above-the-fold
- Output: Image component with priority=true, width=1200, height=600, automatic WebP conversion, eager load
- Notes: Use priority=true only for hero/critical images

### Example 2

- Input: Responsive image gallery with unknown dimensions, external source
- Output: Image component with layout='fill', parent container with position:relative, lazy loading enabled by default
- Notes: External domain must be whitelisted in next.config.js

## Triggers

- application contains raster images (PNG, JPG, GIF) requiring responsive sizing
- page load performance metrics show image payload as bottleneck
- need for automatic format conversion and lazy loading

## Examples

### Example 1

Input:

  Static image asset in public/images/hero.jpg, 1200x600px, above-the-fold

Output:

  Image component with priority=true, width=1200, height=600, automatic WebP conversion, eager load

Notes:

  Use priority=true only for hero/critical images

### Example 2

Input:

  Responsive image gallery with unknown dimensions, external source

Output:

  Image component with layout='fill', parent container with position:relative, lazy loading enabled by default

Notes:

  External domain must be whitelisted in next.config.js
