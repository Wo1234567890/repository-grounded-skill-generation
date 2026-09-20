---
id: "f16628a0-a044-57e2-97cc-a6bee36f5ed8"
name: "Schedule and Control Element Transitions"
description: "Orchestrate animated transitions on DOM selections, including scheduling, interruption, and chaining of sequential transitions with custom timing and easing."
version: "0.1.0"
tags:
  - "animation"
  - "transition"
  - "DOM"
  - "timing"
  - "easing"
  - "selection"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to animate DOM element properties (attributes, styles, text) over time with coordinated timing and easing across multiple elements"
examples:
  - input: "Select elements with class 'box', schedule 1-second transition with 100ms delay, animate opacity from current to 0.5"
    output: "All .box elements fade to opacity 0.5 over 1 second, starting 100ms after transition scheduled"
    notes: "Uses transition.style() with default interpolator"
  - input: "Schedule transition on selection, apply custom easing, chain a second transition to run after first completes"
    output: "First transition runs with specified easing; when complete, second transition begins on same elements"
    notes: "Uses transition.transition() to chain; both transitions share the same selection"
  - input: "Interrupt active transition on a node before it completes"
    output: "Transition stops immediately; element properties freeze at current interpolated state"
    notes: "Uses d3.interrupt() or selection.interrupt()"
---

# Schedule and Control Element Transitions

Orchestrate animated transitions on DOM selections, including scheduling, interruption, and chaining of sequential transitions with custom timing and easing.

## Prompt

Use this skill to animate DOM element properties (attributes, styles, text) over time. Schedule a transition on a selection, configure timing (delay, duration, easing), apply property tweens (attr, style, text), optionally chain or merge transitions, and await completion or interrupt as needed.

## Objective

Execute a complete transition workflow from initiation through completion or cancellation
## Applicable Signals

- Need to animate DOM element properties over time
- Multiple elements require coordinated animated changes
- Custom timing, delay, or easing is required
- Sequential or chained transitions are needed

## Contraindications

- Performing static DOM manipulation without animation
- Handling non-visual state changes
- Working outside a selection context
- No DOM elements selected or selection is empty

## Workflow Steps

- {'step': 1, 'action': 'Schedule transition on selection', 'detail': 'Call selection.transition() to initiate a transition on selected elements'}
- {'step': 2, 'action': 'Configure timing parameters', 'detail': 'Set transition.delay() and transition.duration() for per-element timing in milliseconds'}
- {'step': 3, 'action': 'Specify easing function', 'detail': 'Apply transition.ease() or transition.easeVarying() to control animation curve'}
- {'step': 4, 'action': 'Apply property tweens', 'detail': 'Use transition.attr(), transition.style(), or transition.text() for default interpolation; use attrTween(), styleTween(), or textTween() for custom interpolators'}
- {'step': 5, 'action': 'Optional: chain or merge transitions', 'detail': 'Call transition.transition() to schedule a new transition after this one, or transition.merge() to combine with another transition'}
- {'step': 6, 'action': 'Await or interrupt', 'detail': 'Use transition.end() promise or transition.on() to await completion; call d3.interrupt() or selection.interrupt() to cancel'}

## Constraints

- Selection must contain at least one DOM element
- Delay and duration must be non-negative numbers in milliseconds
- Easing function must be a valid D3 easing function or factory
- Custom interpolators must accept normalized time value (0 to 1) and return interpolated value

## Cautions

- Interrupting a transition cancels all pending tweens on affected elements
- Chained transitions (transition.transition()) execute sequentially; ensure previous transition completes before next begins
- Merging transitions combines their tweens; conflicting tweens on the same property may produce unexpected results
- Text content is set at transition start, not interpolated; use textTween() for animated text changes

## Output Contract

- Transition completes on all selected elements with specified duration, delay, easing, and property tweens applied
- Promise returned by transition.end() resolves when all transitions on all selected elements have finished
- Observable success: DOM properties reflect final tween values; no active transitions remain on selected elements

## Example Therapist Responses

### Example 1

- Client/Input: Select elements with class 'box', schedule 1-second transition with 100ms delay, animate opacity from current to 0.5
- Therapist/Output: All .box elements fade to opacity 0.5 over 1 second, starting 100ms after transition scheduled
- Notes: Uses transition.style() with default interpolator

### Example 2

- Client/Input: Schedule transition on selection, apply custom easing, chain a second transition to run after first completes
- Therapist/Output: First transition runs with specified easing; when complete, second transition begins on same elements
- Notes: Uses transition.transition() to chain; both transitions share the same selection

### Example 3

- Client/Input: Interrupt active transition on a node before it completes
- Therapist/Output: Transition stops immediately; element properties freeze at current interpolated state
- Notes: Uses d3.interrupt() or selection.interrupt()

## 子技能目录
- [Query and Inspect Active Transitions](通用技能领域/Family技能/未分类技能/微技能/Query and Inspect Active Transitions/SKILL.md) ｜ 适用：Retrieve metadata and state information about active or completed transitions, including selection references, element counts, and active transition handles. This is a read-only inspection skill that does not modify transition behavior.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Query and Inspect Active Transitions` 时，优先调用它。 线索：Need to check if a transition is currently active on a node, Need to retrieve the selection associated with a transition, Need to count the number of elements affected by a transition, Need to access the first element in a transition, Need to verify if a transition is empty

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to animate DOM element properties (attributes, styles, text) over time with coordinated timing and easing across multiple elements

## Examples

### Example 1

Input:

  Select elements with class 'box', schedule 1-second transition with 100ms delay, animate opacity from current to 0.5

Output:

  All .box elements fade to opacity 0.5 over 1 second, starting 100ms after transition scheduled

Notes:

  Uses transition.style() with default interpolator

### Example 2

Input:

  Schedule transition on selection, apply custom easing, chain a second transition to run after first completes

Output:

  First transition runs with specified easing; when complete, second transition begins on same elements

Notes:

  Uses transition.transition() to chain; both transitions share the same selection

### Example 3

Input:

  Interrupt active transition on a node before it completes

Output:

  Transition stops immediately; element properties freeze at current interpolated state

Notes:

  Uses d3.interrupt() or selection.interrupt()
