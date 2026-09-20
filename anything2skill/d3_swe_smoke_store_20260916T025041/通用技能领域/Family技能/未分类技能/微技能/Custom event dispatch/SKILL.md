---
id: "faa80df1-c1f0-5096-9572-90fee0c805b7"
name: "Custom event dispatch"
description: "Dispatch custom events on DOM selections programmatically using selection.dispatch(). Enables triggering event handlers that propagate through the selection hierarchy without requiring native user interaction."
version: "0.1.0"
tags:
  - "d3"
  - "event_handling"
  - "custom_events"
  - "selection_api"
  - "programmatic_interaction"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need to programmatically invoke event handlers attached to a selection"
  - "Require event propagation through selection hierarchy without user action"
  - "Implementing synthetic or simulated user interactions"
---

# Custom event dispatch

Dispatch custom events on DOM selections programmatically using selection.dispatch(). Enables triggering event handlers that propagate through the selection hierarchy without requiring native user interaction.

## Prompt

Call selection.dispatch(type, parameters) to emit a custom event on the selected DOM elements. The event will propagate to all listeners registered via selection.on() on that selection. Provide the event type as a string and optional parameters object. All attached listeners will receive and can react to the dispatched event.

## Objective

Trigger custom events on DOM selections programmatically
## Applicable Signals

- selection object is available
- event listeners have been registered via selection.on()
- programmatic control flow requires event emission

## Contraindications

- Responding to native user interactions (use native event listeners instead)
- Dispatching browser-native events that should originate from user action
- No listeners are registered on the target selection

## Workflow Steps

- Obtain or create a D3 selection object
- Ensure event listeners are registered on the selection via selection.on()
- Call selection.dispatch(eventType, parameters) with the desired event type and optional data
- Verify that registered listeners receive and process the dispatched event

## Constraints

- selection must be a valid D3 selection object
- event type must be a string
- listeners must have been previously attached via selection.on()

## Cautions

- Custom events do not trigger native browser behavior; they only invoke registered listeners
- Event propagation is limited to the selection hierarchy, not the full DOM tree

## Output Contract

- Custom event is dispatched to the selection; all registered listeners on that selection receive the event and execute their handlers. Returns the selection for method chaining.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to programmatically invoke event handlers attached to a selection
- Require event propagation through selection hierarchy without user action
- Implementing synthetic or simulated user interactions
