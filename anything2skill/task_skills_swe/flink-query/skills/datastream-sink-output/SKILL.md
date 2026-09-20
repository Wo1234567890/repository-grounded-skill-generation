---
id: "53c2d99e-669f-543e-951a-f62195b88c0f"
name: "DataStream Sink Output"
description: "Restart or stop an active timer, resetting its start time and callback or terminating execution."
version: "0.1.1"
tags:
  - "animation"
  - "timer"
  - "scheduling"
  - "lifecycle"
  - "control"
triggers:
  - "Pipeline transformation is complete"
  - "Results must be persisted or forwarded to external destination"
  - "Output format and destination are defined"
examples:
  - input: "Extend DefaultServerRequestObservationConvention to add a custom 'custom.method' tag"
    output: "Class ExtendedServerRequestObservationConvention extends DefaultServerRequestObservationConvention with overridden getLowCardinalityKeyValues() that calls super and appends KeyValue.of('custom.method', context.getCarrier().getMethod())"
    notes: "Preserves all default tags while adding one custom tag"
  - input: "Implement ServerRequestObservationConvention directly with full control over metric name, trace name, and tags"
    output: "Class CustomServerRequestObservationConvention implements ServerRequestObservationConvention with getName() returning 'http.server.requests', getContextualName() returning 'http ' + method, and getLowCardinalityKeyValues() returning KeyValues.of(method, status, exception)"
    notes: "Full control; no default tags inherited"
---

# DataStream Sink Output

Restart or stop an active timer, resetting its start time and callback or terminating execution.

## Prompt

Use this skill to modify or terminate an active timer during execution. Call timer.restart() to reset the timer's start time and update its callback function mid-execution. Call timer.stop() to halt the timer and remove it from the animation queue. Ensure the timer is already scheduled before invoking these operations.

## Objective

Modify or terminate timer state during execution
## Applicable Signals

- Active timer exists in queue
- Callback needs modification
- Execution should be terminated

## Contraindications

- Timer not yet scheduled
- Timer already completed or stopped

## Workflow Steps

- {'step': 1, 'action': 'Verify timer is active and scheduled', 'condition': 'Timer exists in queue'}
- {'step': 2, 'action': 'Choose operation: restart or stop', 'condition': 'Based on execution requirement'}
- {'step': 3, 'action': 'If restart: call timer.restart(callback) with new callback', 'condition': 'Need to reset start time and update callback'}
- {'step': 4, 'action': 'If stop: call timer.stop()', 'condition': 'Need to terminate timer execution'}

## Constraints

- Timer must be active in the animation queue
- Restart operation requires valid callback function

## Cautions

- Restarting a timer resets its internal clock; elapsed time is lost
- Stopping a timer removes it permanently from the animation queue
- Callback function must be valid when restarting

## Output Contract

- Timer restarted with new start time and callback, or timer stopped and removed from queue. Caller receives confirmation of state change.

## Triggers

- Pipeline transformation is complete
- Results must be persisted or forwarded to external destination
- Output format and destination are defined

## Examples

### Example 1

Input:

  Extend DefaultServerRequestObservationConvention to add a custom 'custom.method' tag

Output:

  Class ExtendedServerRequestObservationConvention extends DefaultServerRequestObservationConvention with overridden getLowCardinalityKeyValues() that calls super and appends KeyValue.of('custom.method', context.getCarrier().getMethod())

Notes:

  Preserves all default tags while adding one custom tag

### Example 2

Input:

  Implement ServerRequestObservationConvention directly with full control over metric name, trace name, and tags

Output:

  Class CustomServerRequestObservationConvention implements ServerRequestObservationConvention with getName() returning 'http.server.requests', getContextualName() returning 'http ' + method, and getLowCardinalityKeyValues() returning KeyValues.of(method, status, exception)

Notes:

  Full control; no default tags inherited
