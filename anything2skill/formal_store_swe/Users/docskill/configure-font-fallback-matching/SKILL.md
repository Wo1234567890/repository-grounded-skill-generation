---
id: "fd2eee4d-69a2-5ac8-8bd0-ef56916c556d"
name: "Configure Font Fallback Matching"
description: "Select and configure fallback fonts that closely match the metrics (size, ascent, descent, line-gap) of the primary web font to minimize visual reflow during font swap."
version: "0.1.0"
tags:
  - "font-loading"
  - "CLS-mitigation"
  - "web-performance"
  - "font-metrics"
  - "fallback-font"
  - "visual-stability"
triggers:
  - "Fallback font differs significantly in size or weight from web font"
  - "font-family declaration needs optimization"
  - "CLS is caused by font substitution"
examples:
  - input: "Web font 'Google Sans' with fallback 'sans-serif'; fallback is noticeably smaller"
    output: "font-family: \"Google Sans\", sans-serif; @font-face { font-family: \"Google Sans\"; size-adjust: 95%; ascent-override: 110%; }"
    notes: "Metric overrides reduce visual mismatch during font swap"
  - input: "font-family: \"Google Sans\" (no fallback specified)"
    output: "font-family: \"Google Sans\", sans-serif; (generic fallback added)"
    notes: "Without fallback, browser defaults to serif font, causing larger visual shift"
---

# Configure Font Fallback Matching

Select and configure fallback fonts that closely match the metrics (size, ascent, descent, line-gap) of the primary web font to minimize visual reflow during font swap.

## Prompt

When a web font is loading, the browser initially renders text using a fallback font. If the fallback font differs significantly in size, weight, or line metrics from the target web font, users will see a visible shift (layout instability) when the web font finally loads. To minimize this shift:

1. Always specify a generic fallback family (e.g., sans-serif, serif) in font-family declarations, not just the web font name alone.
2. Use the Font Metrics Override APIs (size-adjust, ascent-override, descent-override, line-gap-override) to align fallback font metrics with the web font metrics.
3. Test the visual appearance during the font-swap phase to ensure the shift is imperceptible to users.

## Objective

Reduce visual mismatch between fallback and web font to minimize Cumulative Layout Shift (CLS) during font loading
## Applicable Signals

- Fallback font differs significantly in size or weight from web font
- font-family declaration lacks a generic fallback family
- Cumulative Layout Shift (CLS) is caused by font substitution
- Font swap phase produces visible text reflow

## Contraindications

- Web font is already loaded synchronously before first paint
- No fallback font is needed (e.g., system font only)
- Font metrics are already identical between fallback and web font

## Intervention Moves

- Add a generic fallback family (sans-serif, serif, monospace) to the font-family declaration
- Apply size-adjust, ascent-override, descent-override, and line-gap-override CSS properties to match fallback metrics to web font metrics
- Verify visual stability during font loading using browser DevTools or performance monitoring

## Workflow Steps

- {'step': 1, 'action': 'Declare font-family with both web font name and generic fallback', 'example': 'font-family: "Google Sans", sans-serif;'}
- {'step': 2, 'action': 'Measure or obtain the metrics (size, ascent, descent, line-gap) of both the web font and fallback font', 'example': 'Use browser DevTools or font analysis tools to extract metrics'}
- {'step': 3, 'action': 'Apply metric override properties in @font-face or CSS to align fallback metrics to web font', 'example': 'size-adjust: 95%; ascent-override: 110%; descent-override: 20%; line-gap-override: 0%;'}
- {'step': 4, 'action': 'Test visual appearance during font-swap phase (use font-display: swap or simulate slow font loading)', 'example': 'Verify that text reflow is imperceptible to the user'}

## Constraints

- Font Metrics Override APIs (size-adjust, ascent-override, descent-override, line-gap-override) require modern browser support
- Fallback font must be available on the user's system or loaded via @font-face
- Metric overrides must be tested across target browsers to ensure compatibility

## Cautions

- Aggressive metric overrides may distort the fallback font appearance; test visually before deployment
- Generic fallback families vary by operating system; test on multiple platforms
- Metric tuning is a trade-off: perfect alignment may not be achievable for all font pairs

## Output Contract

- Fallback font declaration includes appropriate generic family
- Metric override APIs applied if needed
- Visual shift during font swap is imperceptible to users
- CLS contribution from font substitution is minimized

## Example Executions

### Example 1

- Input: Web font 'Google Sans' with fallback 'sans-serif'; fallback is noticeably smaller
- Output: font-family: "Google Sans", sans-serif; @font-face { font-family: "Google Sans"; size-adjust: 95%; ascent-override: 110%; }
- Notes: Metric overrides reduce visual mismatch during font swap

### Example 2

- Input: font-family: "Google Sans" (no fallback specified)
- Output: font-family: "Google Sans", sans-serif; (generic fallback added)
- Notes: Without fallback, browser defaults to serif font, causing larger visual shift

## Triggers

- Fallback font differs significantly in size or weight from web font
- font-family declaration needs optimization
- CLS is caused by font substitution

## Examples

### Example 1

Input:

  Web font 'Google Sans' with fallback 'sans-serif'; fallback is noticeably smaller

Output:

  font-family: "Google Sans", sans-serif; @font-face { font-family: "Google Sans"; size-adjust: 95%; ascent-override: 110%; }

Notes:

  Metric overrides reduce visual mismatch during font swap

### Example 2

Input:

  font-family: "Google Sans" (no fallback specified)

Output:

  font-family: "Google Sans", sans-serif; (generic fallback added)

Notes:

  Without fallback, browser defaults to serif font, causing larger visual shift
