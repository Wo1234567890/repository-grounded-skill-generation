---
id: "8232fe9a-857e-55f8-a124-87b1f3545372"
name: "Critical Section Bottleneck Scaling Assessment"
description: "Prevent cumulative layout shift (CLS) caused by ads, embeds, iframes, and dynamically injected content by pre-allocating space in the initial layout using CSS min-height or aspect-ratio properties, with responsive adjustments via media queries."
version: "0.1.1"
tags:
  - "layout_shift"
  - "cls_mitigation"
  - "css_optimization"
  - "responsive_design"
  - "third_party_content"
  - "performance"
triggers:
  - "Throughput plateaus or degrades beyond 16–32 active threads"
  - "Shared global state is suspected as the cause of performance degradation"
  - "Multi-threaded scalability evaluation is required"
examples:
  - input: "Ad container with unknown height, responsive across mobile and desktop"
    output: "CSS rule: min-height: 250px on mobile, min-height: 600px on desktop using media queries; space reserved before ad loads"
    notes: "Prevents shift when ad renders at different heights"
  - input: "Embed with known aspect ratio (e.g., 16:9 video)"
    output: "CSS rule: aspect-ratio: 16 / 9; width: 100%; reserves proportional space automatically"
    notes: "Responsive approach scales with container width"
---

# Critical Section Bottleneck Scaling Assessment

Prevent cumulative layout shift (CLS) caused by ads, embeds, iframes, and dynamically injected content by pre-allocating space in the initial layout using CSS min-height or aspect-ratio properties, with responsive adjustments via media queries.

## Prompt

When placing late-loading content (ads, embeds, iframes, dynamically injected elements) into the content flow, reserve space for them in the initial layout to avoid layout shifts. Use CSS min-height to reserve a fixed space, or use the aspect-ratio CSS property for responsive content such as ads. Account for subtle differences in ad or placeholder sizes across form factors using media queries.

## Objective

Eliminate cumulative layout shift from late-loaded third-party content by pre-allocating space before insertion
## Applicable Signals

- Late-loading content detected in content flow
- Third-party content insertion planned
- Variable or unknown content dimensions
- Responsive design with multiple form factors

## Contraindications

- Content is already sized and positioned in the layout
- User interaction triggers content insertion (use avoid-insertion rule instead)
- Content is absolutely positioned outside the normal flow
- Content size is fixed and known at page load time

## Workflow Steps

- {'step': 1, 'action': 'Identify the container element that will hold the late-loading content'}
- {'step': 2, 'action': 'Determine the expected dimensions or aspect ratio of the content across form factors'}
- {'step': 3, 'action': 'Apply CSS min-height rule to reserve vertical space, or use aspect-ratio property for responsive sizing'}
- {'step': 4, 'action': 'Use media queries to adjust reserved space for different viewport sizes if content dimensions vary'}
- {'step': 5, 'action': 'Verify that layout remains stable when content loads and renders'}

## Constraints

- Must account for form factor differences using media queries
- Space reservation must occur before content insertion
- Placeholder or reserved space must accommodate actual content dimensions

## Cautions

- Over-reserving space may create excessive whitespace on some form factors
- Under-reserving space will still cause layout shifts when content exceeds reserved area
- Media query breakpoints must align with actual content size variations

## Output Contract

- Layout remains stable when late-loaded content renders
- No downward shift of subsequent content occurs
- Cumulative layout shift (CLS) metric unchanged or reduced

## Example Executions

### Example 1

- Input: Ad container with unknown height, responsive across mobile and desktop
- Output: CSS rule: min-height: 250px on mobile, min-height: 600px on desktop using media queries; space reserved before ad loads
- Notes: Prevents shift when ad renders at different heights

### Example 2

- Input: Embed with known aspect ratio (e.g., 16:9 video)
- Output: CSS rule: aspect-ratio: 16 / 9; width: 100%; reserves proportional space automatically
- Notes: Responsive approach scales with container width

## Triggers

- Throughput plateaus or degrades beyond 16–32 active threads
- Shared global state is suspected as the cause of performance degradation
- Multi-threaded scalability evaluation is required

## Examples

### Example 1

Input:

  Ad container with unknown height, responsive across mobile and desktop

Output:

  CSS rule: min-height: 250px on mobile, min-height: 600px on desktop using media queries; space reserved before ad loads

Notes:

  Prevents shift when ad renders at different heights

### Example 2

Input:

  Embed with known aspect ratio (e.g., 16:9 video)

Output:

  CSS rule: aspect-ratio: 16 / 9; width: 100%; reserves proportional space automatically

Notes:

  Responsive approach scales with container width
