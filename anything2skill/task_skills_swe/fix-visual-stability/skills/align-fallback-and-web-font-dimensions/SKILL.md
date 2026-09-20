---
id: "df45dad5-394d-5cd3-b1fc-09f10079e108"
name: "Align fallback and web font dimensions"
description: "Ensure fallback font and web font have matching dimensions (width, height, line-height) to prevent text reflow and layout shifts when the web font loads asynchronously. Applies to both FOUT (Flash of Unstyled Text) and FOIT (Flash of Invisible Text) scenarios."
version: "0.1.0"
tags:
  - "web_performance"
  - "layout_shift"
  - "font_loading"
  - "CLS_mitigation"
  - "font_metrics"
  - "FOUT"
triggers:
  - "Web font is loaded asynchronously"
  - "Fallback font is displayed before web font arrives"
  - "Text block dimensions differ between fallback and web font"
  - "FOUT or FOIT behavior is observed in production"
---

# Align fallback and web font dimensions

Ensure fallback font and web font have matching dimensions (width, height, line-height) to prevent text reflow and layout shifts when the web font loads asynchronously. Applies to both FOUT (Flash of Unstyled Text) and FOIT (Flash of Invisible Text) scenarios.

## Prompt

When a web font loads asynchronously, the fallback font is displayed first. If the fallback and web font have different metrics, the text block will reflow when the swap occurs, causing layout shift. Align the dimensions by setting explicit width, height, and line-height values that match both fonts, or use font-display and font-metric-override techniques to minimize the visual difference.

## Objective

Eliminate dimension mismatch between fallback and web font to prevent text reflow and cumulative layout shift (CLS)
## Applicable Signals

- Cumulative Layout Shift (CLS) detected during font swap
- Text reflow observed when web font loads
- Fallback and web font have different metrics
- Flash of Unstyled Text (FOUT) causing visible layout shift
- Flash of Invisible Text (FOIT) causing layout shift when text becomes visible

## Contraindications

- Fonts are loaded synchronously (no swap occurs)
- No fallback font is used
- Responsive font sizing is incompatible with fixed dimension constraints

## Intervention Moves

- Measure and document fallback font dimensions across target platforms
- Measure web font dimensions when loaded
- Apply explicit CSS constraints (width, height, line-height) to text containers
- Verify font-metric-override browser support and apply if available
- Test font swap behavior in target browsers and viewports

## Workflow Steps

- {'step': 1, 'action': 'Measure fallback font dimensions', 'detail': 'Determine the width, height, and line-height of the fallback font as rendered in the target viewport and across target operating systems.'}
- {'step': 2, 'action': 'Measure web font dimensions', 'detail': 'Determine the width, height, and line-height of the web font when loaded.'}
- {'step': 3, 'action': 'Set explicit CSS dimensions', 'detail': 'Apply width, height, and line-height values to the text container that accommodate both fonts without reflow.'}
- {'step': 4, 'action': 'Verify no reflow occurs', 'detail': 'Test the font swap in the browser and confirm that text block position and size remain stable during FOUT or FOIT.'}

## Constraints

- Dimension alignment must account for both fallback and web font metrics
- Fixed dimensions may conflict with responsive design requirements
- Line-height and letter-spacing must be consistent across font swap
- Fallback font metrics may vary across operating systems; test on target platforms

## Cautions

- Over-constraining dimensions may degrade responsive behavior
- Fallback font metrics may vary across operating systems; test on target platforms
- Font-metric-override is not universally supported; verify browser compatibility before relying on it
- Both FOUT and FOIT scenarios can cause layout shifts even if text is invisible during FOIT

## Output Contract

- Fallback and web font occupy identical layout space
- No text reflow or layout shift occurs when font swap happens
- CLS contribution from font swap is eliminated or minimized
- Text remains readable during both FOUT and FOIT phases

## Triggers

- Web font is loaded asynchronously
- Fallback font is displayed before web font arrives
- Text block dimensions differ between fallback and web font
- FOUT or FOIT behavior is observed in production
