---
id: "596ec7cd-13ce-5fa5-9ae0-d8e547a3bbe7"
name: "Next.js Font Loading Optimization"
description: "Optimize web fonts using the built-in `next/font` loaders to reduce font file size, improve text rendering performance, and eliminate layout shift during font load."
version: "0.1.0"
tags:
  - "font_optimization"
  - "next_js"
  - "performance"
  - "web_fonts"
  - "layout_shift"
  - "asset_optimization"
triggers:
  - "Application uses custom or third-party web fonts"
  - "Page load time is impacted by font delivery"
  - "Font rendering causes visible layout shift"
---

# Next.js Font Loading Optimization

Optimize web fonts using the built-in `next/font` loaders to reduce font file size, improve text rendering performance, and eliminate layout shift during font load.

## Prompt

Use the built-in `next/font` loaders to configure and optimize web fonts in your Next.js application. Configure font subsetting, preloading, and fallback strategies to ensure fonts load efficiently without causing cumulative layout shift (CLS).

## Objective

reduce_font_payload_and_improve_text_rendering
## Applicable Signals

- Custom font files referenced in layout or page components
- Multiple font weights or variants required
- Performance audit flags font-related CLS or LCP issues

## Contraindications

- System fonts only (no custom fonts needed)
- Fonts already optimized via external CDN with proper caching
- Font files served from third-party provider with built-in optimization

## Workflow Steps

- {'step': 1, 'action': 'Identify custom or third-party fonts in use', 'detail': 'Audit application for font files and external font sources'}
- {'step': 2, 'action': 'Configure next/font loader', 'detail': 'Import and configure font loader with appropriate subsetting and weight options'}
- {'step': 3, 'action': 'Apply font to layout or page component', 'detail': 'Assign loaded font to CSS class or style variable for use in components'}
- {'step': 4, 'action': 'Define fallback font stack', 'detail': 'Ensure fallback fonts match loaded font metrics to minimize layout shift'}
- {'step': 5, 'action': 'Verify preloading and subset behavior', 'detail': 'Test font loading in browser DevTools; confirm no CLS during font load'}

## Constraints

- Font loader configuration must be applied at layout or page level
- Subsetting strategy should match actual character usage in application
- Fallback font stack must be defined to prevent layout shift

## Cautions

- Ensure font preloading does not conflict with other resource priorities
- Test font loading behavior across network conditions (slow 3G, 4G)
- Verify no duplicate font requests after optimization

## Output Contract

- Fonts are preloaded and subset automatically
- No cumulative layout shift (CLS) occurs during font load
- Font file size is reduced through subsetting
- Text renders with optimized font without blocking page interaction

## Triggers

- Application uses custom or third-party web fonts
- Page load time is impacted by font delivery
- Font rendering causes visible layout shift
