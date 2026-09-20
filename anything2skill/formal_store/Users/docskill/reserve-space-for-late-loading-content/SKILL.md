---
id: "8624e3c7-025a-53d3-bbad-168bc7106343"
name: "Reserve Space for Late-Loading Content"
description: "Prevent layout shifts caused by ads, embeds, iframes, and dynamically injected content by pre-allocating space in the initial layout before content loads."
version: "0.1.0"
tags:
  - "layout_shift"
  - "cls"
  - "performance"
  - "ads"
  - "embeds"
  - "iframes"
triggers:
  - "Placing third-party ads, embeds, or iframes in the content flow"
  - "CLS is measured and attributed to dynamic content insertion"
  - "Late-loaded content will appear after initial page render"
---

# Reserve Space for Late-Loading Content

Prevent layout shifts caused by ads, embeds, iframes, and dynamically injected content by pre-allocating space in the initial layout before content loads.

## Prompt

When placing late-loading content (ads, embeds, iframes, or other dynamically injected elements) in the content flow, reserve the space for them in the initial layout. This prevents surrounding elements from shifting when the content arrives.

## Objective

avoid_layout_shift
## Applicable Signals

- Third-party content insertion planned
- Dynamic embed or ad placement identified
- CLS contribution from content insertion detected

## Contraindications

- Content dimensions are truly unknown and cannot be estimated
- Content insertion is user-initiated (use alternative techniques)
- Content loads synchronously with page render

## Intervention Moves

- Identify the expected dimensions of late-loading content
- Reserve space in the initial layout using CSS or container sizing
- Ensure surrounding elements do not shift when content loads

## Workflow Steps

- {'step': 1, 'action': 'Identify late-loading content type and expected dimensions', 'detail': 'Determine the size or aspect ratio of ads, embeds, or iframes that will be inserted'}
- {'step': 2, 'action': 'Create a container with reserved dimensions in initial layout', 'detail': 'Use CSS width/height, aspect-ratio, or min-height to allocate space before content loads'}
- {'step': 3, 'action': 'Insert late-loading content into the reserved container', 'detail': 'Ensure content loads into the pre-allocated space without triggering layout recalculation'}
- {'step': 4, 'action': 'Verify no layout shift occurs on content load', 'detail': 'Measure CLS or visually confirm surrounding elements remain stable'}

## Constraints

- Must have reasonable estimate of content dimensions or aspect ratio
- Space reservation must occur before content insertion
- Applicable only to late-loaded or asynchronously injected content

## Cautions

- If dimensions are significantly underestimated, layout shift may still occur
- Third-party content may have variable dimensions; use conservative estimates or aspect ratio containers

## Output Contract

- Layout space is reserved in initial render; subsequent content load does not cause visible shift of surrounding elements; CLS contribution from that content insertion is zero or near-zero

## Triggers

- Placing third-party ads, embeds, or iframes in the content flow
- CLS is measured and attributed to dynamic content insertion
- Late-loaded content will appear after initial page render
