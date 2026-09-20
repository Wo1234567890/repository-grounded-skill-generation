---
id: "2285ec99-0e94-5dab-b9d7-af473547a03a"
name: "Schedule Periodic Timer"
description: "Schedule a timer that executes a callback repeatedly at a configurable interval. Use when you need repeating callbacks at fixed intervals, such as polling or periodic updates."
version: "0.1.0"
tags:
  - "timer"
  - "scheduling"
  - "periodic"
  - "interval"
  - "animation"
  - "callback"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need repeating callbacks at fixed intervals"
  - "Polling or periodic update requirement"
  - "Configurable interval-based execution needed"
---

# Schedule Periodic Timer

Schedule a timer that executes a callback repeatedly at a configurable interval. Use when you need repeating callbacks at fixed intervals, such as polling or periodic updates.

## Prompt

Call the timer scheduling function with a callback and interval duration. The callback will be invoked repeatedly at the specified interval. Stop the timer by calling the stop method when periodic execution is no longer needed.

## Objective

Execute a callback at regular intervals
## Applicable Signals

- Interval duration specified
- Callback function provided
- Repeating execution required

## Contraindications

- One-time callbacks only
- Event-driven execution required
- Variable-rate callbacks needed

## Workflow Steps

- Provide callback function and interval duration to timer scheduler
- Timer begins executing callback at specified interval
- Callback invoked repeatedly until timer.stop() is called

## Constraints

- Callback must be provided
- Interval must be a valid duration
- Timer must be explicitly stopped to halt execution

## Cautions

- Ensure callback completes within interval to avoid overlapping executions
- Stop timer when no longer needed to prevent resource leaks

## Output Contract

- Callback is invoked repeatedly at the specified interval. Execution continues until the timer is explicitly stopped. No return value; side effects occur via callback invocation.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need repeating callbacks at fixed intervals
- Polling or periodic update requirement
- Configurable interval-based execution needed
