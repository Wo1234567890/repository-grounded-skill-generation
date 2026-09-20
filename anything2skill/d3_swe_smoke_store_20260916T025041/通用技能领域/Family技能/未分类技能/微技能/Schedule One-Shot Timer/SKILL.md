---
id: "6cbeed68-9cb6-57b2-ac3d-1dd840b153eb"
name: "Schedule One-Shot Timer"
description: "Schedule a timer that executes once and stops automatically on its first callback. Use this micro skill when you need a delayed, one-time callback without manual stop management."
version: "0.1.0"
tags:
  - "timer"
  - "scheduling"
  - "one-shot"
  - "animation"
  - "deferred"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Need a delayed one-time callback"
  - "Deferred initialization required"
  - "Single animation frame or transition needed"
---

# Schedule One-Shot Timer

Schedule a timer that executes once and stops automatically on its first callback. Use this micro skill when you need a delayed, one-time callback without manual stop management.

## Prompt

Call the timer scheduling function with a callback and optional delay. The callback will execute exactly once after the specified delay, then the timer will automatically stop. No manual stop call is required.

## Objective

Execute a callback once after a delay without manual stop
## Applicable Signals

- One-time execution requirement
- Delay or scheduling needed
- No repetition or periodic behavior

## Contraindications

- Repeating or periodic callbacks required
- Immediate synchronous execution needed
- Continuous animation or interval-based timing

## Workflow Steps

- Prepare callback function
- Invoke timer scheduling with callback and optional delay parameter
- Callback executes once after delay
- Timer automatically stops; no further action needed

## Constraints

- Callback executes exactly once
- Timer automatically stops after first invocation
- No manual stop call required or permitted

## Cautions

- Do not use for repeating tasks; use interval-based timer instead
- Callback must complete within reasonable time to avoid blocking

## Output Contract

- Callback invoked exactly once; timer automatically stopped and cleaned up

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need a delayed one-time callback
- Deferred initialization required
- Single animation frame or transition needed
