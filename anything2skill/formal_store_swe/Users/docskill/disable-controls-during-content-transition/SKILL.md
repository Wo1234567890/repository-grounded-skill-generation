---
id: "4a1471a0-fedc-5bf8-baab-a358ee4b3a55"
name: "Disable Controls During Content Transition"
description: "Prevent accidental user interaction by disabling links and controls while new content is being inserted or transitioned. Re-enable after transition completes."
version: "0.1.0"
tags:
  - "interaction_safety"
  - "content_loading"
  - "carousel"
  - "transition"
  - "user_experience"
  - "cls_mitigation"
triggers:
  - "Content replacement begins in a fixed-size container"
  - "Carousel animation starts"
  - "New content is loading into the viewport"
examples:
  - input: "User clicks 'Load More' button; carousel begins sliding to show new products"
    output: "All product links and buttons in carousel are disabled during slide animation; re-enabled when slide completes"
    notes: "Prevents user from clicking a product link while the carousel is still moving"
  - input: "Live feed updates with new posts; old posts fade out and new posts fade in"
    output: "All post interaction elements (like, reply, share buttons) are disabled during fade transition; re-enabled when fade completes"
    notes: "Prevents accidental interaction with partially-visible or transitioning content"
---

# Disable Controls During Content Transition

Prevent accidental user interaction by disabling links and controls while new content is being inserted or transitioned. Re-enable after transition completes.

## Prompt

When replacing old content with new content in a fixed-size container or carousel, disable all interactive elements (links, buttons, controls) before the transition begins. Keep them disabled until the transition animation or content insertion is complete, then re-enable them. This prevents accidental clicks or taps while new content is arriving.

## Objective

Block unintended user input during content replacement or carousel transitions
## Applicable Signals

- transition_start_event
- carousel_animation_initiated
- dynamic_content_load_triggered

## Contraindications

- Transition is instantaneous with no animation duration
- User input is required during the content change
- Content is not being replaced or updated

## Intervention Moves

- Identify all interactive elements in transition zone before disabling
- Apply disabled state atomically to all identified elements
- Confirm transition completion before re-enabling
- Restore full functionality and visual state after transition

## Workflow Steps

- {'step': 1, 'action': 'Identify all interactive elements (links, buttons, form controls) in the transition zone', 'detail': 'Query or maintain a list of elements that could receive user input'}
- {'step': 2, 'action': 'Set disabled state on all identified elements before transition starts', 'detail': 'Apply disabled attribute, aria-disabled, or pointer-events: none; optionally add visual feedback (reduced opacity, disabled cursor)'}
- {'step': 3, 'action': 'Trigger content replacement or carousel animation', 'detail': 'Begin the transition (swap content, animate carousel, load new items)'}
- {'step': 4, 'action': 'Wait for transition completion', 'detail': 'Listen for transitionend, animationend, or explicit completion callback'}
- {'step': 5, 'action': 'Re-enable all interactive elements', 'detail': 'Remove disabled attribute, aria-disabled, or pointer-events restriction; restore visual state'}

## Constraints

- All interactive elements must be identified and tracked before disabling
- Disable state must be applied atomically to prevent partial interaction
- Re-enable must occur only after transition completion is confirmed

## Cautions

- Ensure disabled state is visually communicated to users (e.g., opacity, cursor change)
- Do not disable elements longer than necessary; re-enable promptly after transition
- Test on touch devices to confirm tap events are blocked

## Output Contract

- All interactive elements are disabled during transition
- No accidental clicks or taps are registered
- Controls are re-enabled after transition completes and are fully functional

## Example Executions

### Example 1

- Input: User clicks 'Load More' button; carousel begins sliding to show new products
- Output: All product links and buttons in carousel are disabled during slide animation; re-enabled when slide completes
- Notes: Prevents user from clicking a product link while the carousel is still moving

### Example 2

- Input: Live feed updates with new posts; old posts fade out and new posts fade in
- Output: All post interaction elements (like, reply, share buttons) are disabled during fade transition; re-enabled when fade completes
- Notes: Prevents accidental interaction with partially-visible or transitioning content

## Triggers

- Content replacement begins in a fixed-size container
- Carousel animation starts
- New content is loading into the viewport

## Examples

### Example 1

Input:

  User clicks 'Load More' button; carousel begins sliding to show new products

Output:

  All product links and buttons in carousel are disabled during slide animation; re-enabled when slide completes

Notes:

  Prevents user from clicking a product link while the carousel is still moving

### Example 2

Input:

  Live feed updates with new posts; old posts fade out and new posts fade in

Output:

  All post interaction elements (like, reply, share buttons) are disabled during fade transition; re-enabled when fade completes

Notes:

  Prevents accidental interaction with partially-visible or transitioning content
