---
id: "57751b4b-e694-5e62-99a0-0629ff271c2a"
name: "Minimize Web Font Layout Shift"
description: "Apply CSS and font-loading techniques to prevent Cumulative Layout Shift (CLS) caused by web font rendering delays. Coordinates font-display strategy, fallback font matching, metric overrides, and preloading to ensure text stability during page load."
version: "0.1.0"
tags:
  - "web_performance"
  - "CLS"
  - "font_loading"
  - "layout_stability"
  - "page_load_optimization"
triggers:
  - "Web fonts are loaded asynchronously and cause visible text reflow"
  - "Font-family fallback mismatches are detected during page load"
  - "CLS metrics show font-related shifts or font-swap events"
examples:
  - input: "Page uses Google Sans web font loaded asynchronously; fallback is Times (serif); CLS detected during font swap."
    output: "Apply `font-family: \"Google Sans\", sans-serif;` with `font-display: optional;` and metric overrides to match sans-serif fallback; preload font with `<link rel=preload>`. Result: CLS eliminated, text stable during load."
    notes: "Serif fallback (Times) was worse match than sans-serif; explicit fallback selection resolved the issue."
  - input: "Critical heading font not preloaded; visible text reflow occurs 200ms after page load."
    output: "Add `<link rel=preload as=font href=heading-font.woff2 type=font/woff2 crossorigin>` to head. Font loads before first paint, no layout shift."
    notes: "Preload increases font priority; ensures font is available by initial layout time."
---

# Minimize Web Font Layout Shift

Apply CSS and font-loading techniques to prevent Cumulative Layout Shift (CLS) caused by web font rendering delays. Coordinates font-display strategy, fallback font matching, metric overrides, and preloading to ensure text stability during page load.

## Prompt

To minimize layout shift from web fonts:
1. Set `font-display: optional` to avoid re-layout if the web font is not available by initial layout time.
2. Specify a fallback font in `font-family` (e.g., `font-family: "Google Sans", sans-serif;`) to ensure the browser uses a matching fallback while the web font loads. Do not use `font-family: "Google Sans"` alone, as it defaults to a serif font (e.g., Times) which may cause larger shifts.
3. Minimize metric differences between fallback and web font using `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` CSS APIs.
4. Use the Font Loading API to reduce font acquisition time.
5. Preload critical web fonts early with `<link rel=preload>` to increase the chance they load before first paint, eliminating layout shift.

## Objective

Reduce CLS impact from web font substitution and loading delays
## Applicable Signals

- Observed layout shift during web font load
- Fallback font differs significantly in metrics from web font
- CLS score increases during font-swap phase

## Contraindications

- All fonts are system fonts with no async loading
- Font loading is synchronous and blocking
- CLS is caused by layout changes unrelated to typography

## Intervention Moves

- Apply font-display: optional to prevent re-layout if web font unavailable by initial layout time
- Specify explicit fallback font in font-family declaration matching font category
- Apply metric overrides (size-adjust, ascent-override, descent-override, line-gap-override) to align fallback and web font dimensions
- Preload critical fonts with <link rel=preload> in document head
- Invoke Font Loading API to reduce font acquisition time

## Workflow Steps

- {'step': 1, 'action': 'Define font-family with explicit fallback', 'detail': 'Use `font-family: "Web Font Name", fallback-category;` (e.g., sans-serif, serif) to ensure browser selects a matching fallback while web font loads.'}
- {'step': 2, 'action': 'Apply font-display strategy', 'detail': 'Set `font-display: optional` in @font-face to prevent re-layout if web font is not available by initial layout time.'}
- {'step': 3, 'action': 'Measure and apply metric overrides', 'detail': 'Use `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` in @font-face to align fallback font metrics with web font metrics.'}
- {'step': 4, 'action': 'Preload critical fonts', 'detail': 'Add `<link rel=preload as=font href=font-file.woff2 type=font/woff2 crossorigin>` in document head for fonts needed before first paint.'}
- {'step': 5, 'action': 'Optionally use Font Loading API', 'detail': 'Call Font Loading API to reduce time to font availability and coordinate font swap timing.'}

## Constraints

- Fallback font must be specified in font-family declaration
- Metric override APIs must be applied to @font-face rule
- Preload link must reference the correct font file format and weight

## Cautions

- font-display: optional may cause text to not render if font is unavailable; use only for non-critical fonts
- Metric overrides require precise measurement of fallback and web font dimensions to be effective
- Preloading too many fonts can delay other critical resources

## Output Contract

- Web font loads without triggering layout shift
- Fallback font metrics match web font closely
- CLS score remains stable during font-swap phase
- Text remains readable throughout load sequence

## Example Executions

### Example 1

- Input: Page uses Google Sans web font loaded asynchronously; fallback is Times (serif); CLS detected during font swap.
- Output: Apply `font-family: "Google Sans", sans-serif;` with `font-display: optional;` and metric overrides to match sans-serif fallback; preload font with `<link rel=preload>`. Result: CLS eliminated, text stable during load.
- Notes: Serif fallback (Times) was worse match than sans-serif; explicit fallback selection resolved the issue.

### Example 2

- Input: Critical heading font not preloaded; visible text reflow occurs 200ms after page load.
- Output: Add `<link rel=preload as=font href=heading-font.woff2 type=font/woff2 crossorigin>` to head. Font loads before first paint, no layout shift.
- Notes: Preload increases font priority; ensures font is available by initial layout time.

## Triggers

- Web fonts are loaded asynchronously and cause visible text reflow
- Font-family fallback mismatches are detected during page load
- CLS metrics show font-related shifts or font-swap events

## Examples

### Example 1

Input:

  Page uses Google Sans web font loaded asynchronously; fallback is Times (serif); CLS detected during font swap.

Output:

  Apply `font-family: "Google Sans", sans-serif;` with `font-display: optional;` and metric overrides to match sans-serif fallback; preload font with `<link rel=preload>`. Result: CLS eliminated, text stable during load.

Notes:

  Serif fallback (Times) was worse match than sans-serif; explicit fallback selection resolved the issue.

### Example 2

Input:

  Critical heading font not preloaded; visible text reflow occurs 200ms after page load.

Output:

  Add `<link rel=preload as=font href=heading-font.woff2 type=font/woff2 crossorigin>` to head. Font loads before first paint, no layout shift.

Notes:

  Preload increases font priority; ensures font is available by initial layout time.
