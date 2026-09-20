---
id: "309cb993-6d25-5c9a-8117-d8eb130d78ff"
name: "Next.js Image Optimization"
description: "Optimize images in Next.js applications using the built-in `next/image` component to reduce file size, improve load performance, and enable responsive sizing with automatic format conversion."
version: "0.1.0"
tags:
  - "image_optimization"
  - "performance"
  - "responsive_design"
  - "lazy_loading"
  - "next.js"
triggers:
  - "Application contains images requiring responsive sizing"
  - "Images need lazy loading to improve initial page load"
  - "Format conversion (WebP, AVIF) is desired for performance"
---

# Next.js Image Optimization

Optimize images in Next.js applications using the built-in `next/image` component to reduce file size, improve load performance, and enable responsive sizing with automatic format conversion.

## Prompt

Use the `next/image` component to wrap image assets. Configure responsive sizing via width/height props or fill layout. Enable lazy loading (default) and automatic format selection (WebP, AVIF). Verify images are served with appropriate srcset and lazy-loading attributes.

## Objective

reduce_image_payload_and_render_time
## Applicable Signals

- Multiple image assets in application
- Performance metrics show image payload as bottleneck
- Need for responsive image delivery across device sizes

## Contraindications

- Images already optimized externally or via third-party CDN with no Next.js integration required
- Static images served directly from public directory without component wrapping

## Intervention Moves

- Import Image component from next/image
- Replace standard <img> tags with <Image> component
- Set src, alt, width, and height props or use fill layout
- Configure priority, sizes, or quality props as needed
- Verify responsive srcset and lazy loading in browser DevTools

## Workflow Steps

- Import Image component from next/image
- Replace standard <img> tags with <Image> component
- Set src, alt, width, and height props (or use fill layout)
- Optionally configure priority, sizes, or quality props
- Verify responsive srcset and lazy loading in browser DevTools

## Constraints

- Images must be imported or have explicit dimensions (width/height) or fill layout
- next/image component requires Next.js 10.0.0 or later

## Cautions

- Lazy loading is enabled by default; use priority prop only for above-the-fold images to avoid performance regression
- Ensure image dimensions are set correctly to prevent layout shift

## Output Contract

- Images are served with automatic format selection, responsive srcset attributes, and lazy loading enabled by default. Caller receives optimized image delivery with reduced payload and improved render performance.

## Triggers

- Application contains images requiring responsive sizing
- Images need lazy loading to improve initial page load
- Format conversion (WebP, AVIF) is desired for performance
