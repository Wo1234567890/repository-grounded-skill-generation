---
id: "c8a58023-0cb3-5780-bf50-bf2990b5bb78"
name: "Next.js Font Loading Optimization"
description: "Detect and mitigate Cumulative Layout Shift (CLS) caused by web font loading by selecting between FOUT (Flash of Unstyled Text) and FOIT (Flash of Invisible Text) strategies and aligning fallback and web font dimensions to minimize text reflow."
version: "0.1.1"
tags:
  - "web_performance"
  - "cumulative_layout_shift"
  - "font_loading"
  - "rendering_optimization"
  - "fout"
  - "foit"
triggers:
  - "application uses custom or third-party web fonts"
  - "page rendering is delayed by font loading"
  - "Cumulative Layout Shift (CLS) metric needs improvement"
examples:
  - input: "Page loads with font-display: swap; fallback font (Arial) is 14px, web font (custom serif) is 16px."
    output: "Adjust fallback font CSS to 16px or use size-adjust: 114% to scale Arial. Monitor CLS during font swap; expect minimal shift if dimensions match."
    notes: "FOUT strategy chosen for readability; dimension alignment prevents reflow."
  - input: "Page uses font-display: block; text is invisible until web font loads; CLS spike observed when text becomes visible."
    output: "Pre-reserve space for text block using min-height or aspect-ratio. Ensure web font dimensions are declared or measured. Re-test CLS."
    notes: "FOIT strategy chosen for visual consistency; space reservation prevents layout shift on visibility change."
---

# Next.js Font Loading Optimization

Detect and mitigate Cumulative Layout Shift (CLS) caused by web font loading by selecting between FOUT (Flash of Unstyled Text) and FOIT (Flash of Invisible Text) strategies and aligning fallback and web font dimensions to minimize text reflow.

## Prompt

When web fonts load asynchronously, text rendering can shift layout in two ways: (1) FOUT—fallback font swaps to web font, causing visible reflow; (2) FOIT—text stays invisible until web font loads, then becomes visible and shifts. Both cause CLS because the fallback font dimensions differ from the web font. To mitigate: choose a font-display strategy (swap for FOUT, block for FOIT), measure fallback and web font metrics (width, height, line-height), and ensure dimensions match or pre-reserve space. Monitor CLS metrics during font load to confirm shift reduction.

## Objective

Reduce CLS impact from web font rendering transitions
## Applicable Signals

- font-display property is set to swap or block
- Fallback font and web font have different metrics
- Layout Shift Inspector or CLS monitoring detects shifts during font load phase

## Contraindications

- Fonts are preloaded synchronously (font already available before render)
- No layout shift is observed in CLS metrics
- font-display is set to auto without fallback consideration

## Intervention Moves

- Switch font-display strategy if current choice causes unacceptable UX impact
- Adjust fallback font CSS (size, weight, letter-spacing) to match web font metrics
- Pre-reserve layout space using min-height or aspect-ratio on text container

## Workflow Steps

- {'step': 1, 'action': 'Identify font-display strategy', 'detail': 'Choose FOUT (font-display: swap) for immediate text visibility or FOIT (font-display: block) for visual consistency. Document the choice and rationale.'}
- {'step': 2, 'action': 'Measure fallback and web font dimensions', 'detail': 'Obtain or calculate width, height, and line-height metrics for both fallback and web font. Use font metrics APIs or manual measurement.'}
- {'step': 3, 'action': 'Align dimensions or pre-reserve space', 'detail': 'If dimensions differ, either adjust CSS to match or use size-adjust descriptor to scale fallback font. Alternatively, pre-reserve layout space for text block to prevent shift.'}
- {'step': 4, 'action': 'Test and monitor CLS', 'detail': 'Load page with font strategy in place. Use CLS monitoring tools (Web Vitals, DevTools) to confirm shift reduction during font load phase.'}

## Constraints

- Fallback font must be available before web font loads
- Web font metrics must be measurable or declared
- Strategy choice (FOUT vs. FOIT) depends on user experience priority (readability vs. visual consistency)

## Cautions

- FOUT may cause visible text flash; FOIT may cause invisible text delay—choose based on UX requirements
- Dimension mismatch between fallback and web font is the root cause; metric alignment is critical
- Monitor actual CLS values post-deployment; strategy effectiveness varies by font pair and network conditions

## Output Contract

- Web font loads with minimal or zero CLS; fallback and web font dimensions are matched or space is pre-reserved; text remains visible (FOUT) or invisible (FOIT) consistently without unexpected reflow; CLS metric for font-load phase is below threshold (typically <0.1).

## Example Executions

### Example 1

- Input: Page loads with font-display: swap; fallback font (Arial) is 14px, web font (custom serif) is 16px.
- Output: Adjust fallback font CSS to 16px or use size-adjust: 114% to scale Arial. Monitor CLS during font swap; expect minimal shift if dimensions match.
- Notes: FOUT strategy chosen for readability; dimension alignment prevents reflow.

### Example 2

- Input: Page uses font-display: block; text is invisible until web font loads; CLS spike observed when text becomes visible.
- Output: Pre-reserve space for text block using min-height or aspect-ratio. Ensure web font dimensions are declared or measured. Re-test CLS.
- Notes: FOIT strategy chosen for visual consistency; space reservation prevents layout shift on visibility change.

## Triggers

- application uses custom or third-party web fonts
- page rendering is delayed by font loading
- Cumulative Layout Shift (CLS) metric needs improvement

## Examples

### Example 1

Input:

  Page loads with font-display: swap; fallback font (Arial) is 14px, web font (custom serif) is 16px.

Output:

  Adjust fallback font CSS to 16px or use size-adjust: 114% to scale Arial. Monitor CLS during font swap; expect minimal shift if dimensions match.

Notes:

  FOUT strategy chosen for readability; dimension alignment prevents reflow.

### Example 2

Input:

  Page uses font-display: block; text is invisible until web font loads; CLS spike observed when text becomes visible.

Output:

  Pre-reserve space for text block using min-height or aspect-ratio. Ensure web font dimensions are declared or measured. Re-test CLS.

Notes:

  FOIT strategy chosen for visual consistency; space reservation prevents layout shift on visibility change.
