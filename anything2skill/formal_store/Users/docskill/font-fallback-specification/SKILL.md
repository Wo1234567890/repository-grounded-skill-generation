---
id: "82214843-03fd-5748-881c-77620f32df05"
name: "Font Fallback Specification"
description: "Select and declare fallback fonts that closely match the metrics (size, ascent, descent, line-gap) of the intended web font to minimize layout shift during font swap."
version: "0.1.0"
tags:
  - "font-fallback"
  - "layout-shift"
  - "CLS"
  - "CSS"
  - "performance"
  - "font-metrics"
triggers:
  - "Declaring font-family CSS rule with uncertain or variable web font load time"
---

# Font Fallback Specification

Select and declare fallback fonts that closely match the metrics (size, ascent, descent, line-gap) of the intended web font to minimize layout shift during font swap.

## Prompt

When declaring a font-family CSS rule with a web font whose load time is uncertain, specify a generic fallback font (e.g., sans-serif) and use @font-face metric override APIs (size-adjust, ascent-override, descent-override, line-gap-override) to align the fallback font metrics with the target web font. This reduces visual reflow when the web font becomes available.

## Objective

match_fallback_font_metrics
## Applicable Signals

- Declaring font-family CSS rule with web font
- Web font load time is uncertain or variable
- Cumulative Layout Shift (CLS) is being measured or optimized

## Contraindications

- Using only system fonts with no web font fallback
- Fallback font metrics are already verified to match web font exactly
- Font swap is not a concern (e.g., font-display: optional is sufficient)

## Intervention Moves

- Specify font-family with both web font name and generic fallback: font-family: "Web Font Name", sans-serif;
- Apply @font-face metric overrides: size-adjust, ascent-override, descent-override, line-gap-override to align fallback metrics with web font
- Verify fallback font choice matches the intended web font category (serif vs. sans-serif)

## Workflow Steps

- Identify the target web font and measure its key metrics (size, ascent, descent, line-gap)
- Select a generic fallback font (sans-serif, serif, monospace) that is closest in category
- Declare font-family rule with both names: font-family: "Target Font", generic-fallback;
- Apply @font-face overrides to minimize size and metric differences between fallback and web font
- Test rendering in browser to confirm minimal visual shift when web font loads

## Constraints

- Fallback font must be a system font available on the target platform
- Metric overrides require browser support for @font-face descriptor APIs
- This skill addresses font swap only; does not control font preload timing or Font Loading API usage

## Cautions

- Metric overrides are approximate; perfect alignment may not be achievable
- Over-aggressive metric adjustment may make fallback font appear distorted
- Test across multiple browsers and devices to ensure fallback rendering is acceptable

## Output Contract

- CSS font-family rule that includes a generic fallback font; optionally, @font-face rule with size-adjust, ascent-override, descent-override, and/or line-gap-override properties set to values that minimize metric mismatch with the target web font.

## Triggers

- Declaring font-family CSS rule with uncertain or variable web font load time
