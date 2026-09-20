---
id: "8b49b13d-85a0-5a33-8a6a-2dce35abe350"
name: "Dynamic Content Loading with Layout Stability"
description: "Orchestrate animated transitions on DOM selections, including scheduling, interruption, and chaining of sequential transitions with custom timing and easing."
version: "0.1.1"
tags:
  - "animation"
  - "transition"
  - "DOM"
  - "timing"
  - "easing"
  - "d3"
triggers:
  - "Adding products to a list dynamically"
  - "Updating live feed content"
  - "Inserting new content after user interaction"
  - "Prefetching content for immediate display"
examples:
  - input: "User clicks 'Load more' button on product list"
    output: "New products load within fixed-size container; old products removed after transition; CLS does not increase"
    notes: "User-initiated load with prefetch ensures immediate display and no surprise shift"
  - input: "Live feed updates with new posts"
    output: "New posts load offscreen; 'Scroll to top' notice appears; user can choose to view new content"
    notes: "Offscreen loading prevents unexpected layout shift; user controls when to view new content"
---

# Dynamic Content Loading with Layout Stability

Orchestrate animated transitions on DOM selections, including scheduling, interruption, and chaining of sequential transitions with custom timing and easing.

## Prompt

Use this skill to animate DOM element properties (attributes, styles, text) over time. Schedule a transition on a selection, configure timing (delay, duration, easing), apply property tweens (attr, style, text), optionally chain or merge transitions, and await completion or interrupt as needed.

## Objective

Execute a complete transition workflow from initiation through completion or cancellation
## Applicable Signals

- selection.transition invoked
- transition lifecycle event (start, progress, end)
- user interaction or state change requiring animation

## Contraindications

- Performing static DOM manipulation without animation
- Handling non-visual state changes
- Working outside a selection context
- No DOM elements selected

## Workflow Steps

- {'step': 1, 'action': 'Schedule transition', 'detail': 'Call selection.transition() or d3.transition() to initiate a transition on selected elements or root document'}
- {'step': 2, 'action': 'Configure timing', 'detail': 'Set transition.delay() and transition.duration() for per-element or uniform timing; apply transition.ease() or transition.easeVarying() for interpolation curve'}
- {'step': 3, 'action': 'Apply property tweens', 'detail': 'Use transition.attr(), transition.style(), or transition.text() for default interpolation; use transition.attrTween(), transition.styleTween(), or transition.textTween() for custom interpolators'}
- {'step': 4, 'action': 'Optional: chain or merge', 'detail': 'Call transition.transition() to schedule a new transition after this one completes; call transition.merge() to combine with another transition'}
- {'step': 5, 'action': 'Optional: interrupt or monitor', 'detail': 'Call selection.interrupt() or d3.interrupt() to cancel; call transition.end() to await completion as a promise; call transition.on() to listen for end event'}
- {'step': 6, 'action': 'Cleanup', 'detail': 'Optionally call transition.remove() to remove elements when transition ends; verify all tweens have completed via promise resolution or event listener'}

## Constraints

- Transition must operate on a valid D3 selection
- Duration and delay must be non-negative milliseconds
- Easing function must be a valid D3 easing function or factory
- Custom tweens must return interpolator functions

## Cautions

- Interrupting a transition cancels all pending tweens on affected elements
- Chaining transitions (transition.transition) creates sequential execution; ensure prior transition completes before next begins
- Merging transitions combines their timelines; verify timing compatibility
- Promise from transition.end resolves only when all tweens on all selected elements complete

## Output Contract

- Transition completes on all selected elements with specified duration, delay, easing, and property tweens applied. Promise from transition.end() resolves when all transitions end. If interrupted, transition cancels and promise may reject or resolve early depending on implementation.

## Triggers

- Adding products to a list dynamically
- Updating live feed content
- Inserting new content after user interaction
- Prefetching content for immediate display

## Examples

### Example 1

Input:

  User clicks 'Load more' button on product list

Output:

  New products load within fixed-size container; old products removed after transition; CLS does not increase

Notes:

  User-initiated load with prefetch ensures immediate display and no surprise shift

### Example 2

Input:

  Live feed updates with new posts

Output:

  New posts load offscreen; 'Scroll to top' notice appears; user can choose to view new content

Notes:

  Offscreen loading prevents unexpected layout shift; user controls when to view new content
