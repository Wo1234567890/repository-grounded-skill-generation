---
id: "ee77b9a1-3922-5f79-86bb-9e4ac606d104"
name: "TF Normalization Stability Assessment and Mitigation"
description: "Eliminate unexpected layout shifts from auto-inserted UI elements (banners, forms, notifications) by deferring DOM insertion or visibility changes until explicit user interaction occurs, or by positioning late-loading content below the initial viewport."
version: "0.1.1"
tags:
  - "layout_shift"
  - "CLS"
  - "content_insertion"
  - "user_interaction"
  - "viewport_stability"
triggers:
  - "deploying maximum tf normalization in production"
  - "planning to update or tune stop word lists"
  - "when ranking consistency across system versions is required"
---

# TF Normalization Stability Assessment and Mitigation

Eliminate unexpected layout shifts from auto-inserted UI elements (banners, forms, notifications) by deferring DOM insertion or visibility changes until explicit user interaction occurs, or by positioning late-loading content below the initial viewport.

## Prompt

When implementing modal dialogs, notification banners, or form overlays, ensure they do not insert into the DOM or become visible without explicit user action (click, scroll, focus). If immediate appearance is unavoidable, position the element below the initial viewport to minimize impact on visible content. Validate that no unplanned cumulative layout shift (CLS) is recorded for the inserted element.

## Objective

Eliminate unexpected layout shifts from auto-inserted UI elements
## Applicable Signals

- Designing modal dialogs, notification banners, or form overlays
- Page load or user navigation events that may trigger UI appearance
- Risk of unplanned content pop-in at viewport top or bottom

## Contraindications

- Content must appear immediately for accessibility or critical user warnings
- Space has already been reserved for the element via min-height or placeholder
- Element is part of critical path that requires synchronous rendering

## Intervention Moves

- Defer DOM insertion or visibility change until user interaction event fires
- Position late-loading content below the fold to avoid shifting visible viewport content
- Show placeholder or maintain min-height to prevent space collapse

## Workflow Steps

- Identify UI elements that may auto-insert during page load or navigation
- Determine if user interaction is required before element visibility
- If deferral is not possible, position element below initial viewport
- Maintain reserved space with min-height or placeholder to prevent collapse
- Validate CLS metric post-insertion to confirm no unplanned shift occurred

## Constraints

- UI insertion must be deferred until after user interaction (click, scroll, focus) or positioned below initial viewport
- Do not collapse reserved space by removing placeholder; maintain allocated height
- Validate CLS metric for the inserted element post-insertion

## Cautions

- Removing space set aside for elements can cause as much CLS as inserting content; preserve reserved space even if content is not loaded
- Banners and forms that shift page content are common sources of unexpected layout shifts

## Output Contract

- UI element inserted only after user interaction or positioned below initial viewport; no unplanned CLS recorded for that element; reserved space maintained or placeholder shown to prevent collapse.

## Triggers

- deploying maximum tf normalization in production
- planning to update or tune stop word lists
- when ranking consistency across system versions is required
