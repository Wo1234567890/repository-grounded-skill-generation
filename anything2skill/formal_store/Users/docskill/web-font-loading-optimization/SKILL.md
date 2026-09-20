---
id: "77fc95a6-e6a9-5991-a8d3-a5185ebc7a2b"
name: "Web Font Loading Optimization"
description: "Minimize cumulative layout shift (CLS) caused by web font rendering by coordinating font-display strategies, fallback font selection, metric overrides, and preloading techniques to ensure fonts load without triggering text reflow."
version: "0.1.0"
tags:
  - "web_performance"
  - "cumulative_layout_shift"
  - "font_loading"
  - "css"
  - "core_web_vitals"
triggers:
  - "Web page includes custom web fonts and CLS metrics show font-related shifts"
  - "During page load optimization review"
---

# Web Font Loading Optimization

Minimize cumulative layout shift (CLS) caused by web font rendering by coordinating font-display strategies, fallback font selection, metric overrides, and preloading techniques to ensure fonts load without triggering text reflow.

## Prompt

Apply the following coordinated tactics to reduce font-induced layout shift:
1. Set `font-display: optional` to avoid re-layout if the web font is not available by initial layout time.
2. Specify a fallback font in `font-family` (e.g., `font-family: "Google Sans", sans-serif;`) to ensure the browser uses a matching fallback while the web font loads, rather than defaulting to a mismatched serif font.
3. Use `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` CSS APIs to minimize metric differences between fallback and web fonts.
4. Consider the Font Loading API to reduce the time required to obtain necessary fonts.
5. Preload critical web fonts early using `<link rel=preload>` to increase the chance they meet first paint, eliminating layout shifting.

## Objective

reduce_font_induced_layout_shift
## Applicable Signals

- Web page includes custom web fonts
- CLS metrics show font-related shifts or text reflow during load
- Page load optimization review in progress

## Contraindications

- Page uses only system fonts (no custom web fonts)
- Font loading is not a measured contributor to CLS
- Fallback font selection is not feasible due to design constraints

## Intervention Moves

- Set font-display: optional on @font-face rules
- Add fallback font family to font-family declarations
- Apply size-adjust, ascent-override, descent-override, line-gap-override to @font-face
- Preload critical fonts with <link rel=preload>
- Optionally use Font Loading API to manage font load timing

## Workflow Steps

- Identify custom web fonts in use on the page
- Measure current CLS contribution from font loading
- Select appropriate system or generic fallback fonts
- Apply font-display: optional to @font-face rules
- Configure metric overrides (size-adjust, ascent-override, descent-override, line-gap-override) to match fallback and web font metrics
- Preload critical fonts using <link rel=preload>

## Constraints

- Fallback font must be available on the system or specified as a generic family
- Metric overrides (size-adjust, ascent-override, etc.) require careful tuning to avoid visual mismatch
- Preload should be limited to critical fonts only to avoid blocking other resources

## Cautions

- font-display: optional may result in text not rendering if the web font is slow to load; verify acceptable fallback appearance
- Metric overrides can introduce subtle visual inconsistencies if not calibrated correctly
- Preloading too many fonts can increase initial load time; prioritize only essential fonts

## Output Contract

- Web fonts load without triggering text reflow
- Fallback font metrics match web font metrics within acceptable tolerance
- CLS score improves or remains stable after font load
- No layout shift observed during font swap

## Triggers

- Web page includes custom web fonts and CLS metrics show font-related shifts
- During page load optimization review
