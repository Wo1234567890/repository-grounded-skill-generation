---
id: "4491cbb1-ed9a-5442-bd19-3ef552539f4f"
name: "Timer Queue Management"
description: "Manage and execute thousands of concurrent animations using an efficient queue system with precise timing control. Coordinates scheduling, lifecycle control, and immediate execution of pending timers."
version: "0.1.0"
tags:
  - "animation"
  - "timing"
  - "concurrency"
  - "queue"
  - "d3-timer"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to coordinate multiple concurrent animations, manage timer lifecycle, or flush pending animations immediately"
---

# Timer Queue Management

Manage and execute thousands of concurrent animations using an efficient queue system with precise timing control. Coordinates scheduling, lifecycle control, and immediate execution of pending timers.

## Prompt

Use this skill to schedule multiple timers, control their lifecycle (restart/stop), and flush pending timers. Call d3.timer to schedule a new timer with a callback. Use timer.restart to reset start time and callback. Use timer.stop to halt execution. Use d3.timerFlush to immediately execute all eligible pending timers. Use d3.now for high-resolution current time queries.

## Objective

Schedule, control, and flush animation timers with high-resolution timing
## Applicable Signals

- Need to coordinate multiple concurrent animations
- Require timer lifecycle management (start, restart, stop)
- Must flush pending animations immediately
- High-resolution timing required for animation synchronization

## Contraindications

- Single synchronous animation without concurrency requirements
- Real-time systems with hard latency constraints
- Non-animation use cases without timing coordination needs

## Workflow Steps

- Query current high-resolution time using d3.now if needed for reference
- Schedule new timers using d3.timer with callback function
- Restart timers as needed using timer.restart to reset start time and callback
- Stop timers using timer.stop when animation completes or is cancelled
- Flush all eligible pending timers using d3.timerFlush for immediate execution

## Constraints

- Timer queue is designed for thousands of concurrent animations; use for appropriate scale
- Callbacks execute in queue order; ordering guarantees depend on scheduling sequence
- timerFlush executes only eligible timers; ineligible timers remain queued

## Cautions

- High-resolution timing is relative; absolute time values are not guaranteed across systems
- Stopping a timer does not remove it from queue immediately; use timerFlush to ensure execution state
- Restarting a timer changes its callback and start time; previous state is lost

## Output Contract

- All scheduled timers execute according to queue order and timing. Restarted timers execute with new callback and reset start time. Stopped timers do not execute. timerFlush completes all eligible pending timers synchronously.

## 子技能目录
- [Schedule One-Shot Timer](通用技能领域/Family技能/未分类技能/微技能/Schedule One-Shot Timer/SKILL.md) ｜ 适用：Schedule a timer that executes once and stops automatically on its first callback. Use this micro skill when you need a delayed, one-time callback without manual stop management.
- [Schedule Periodic Timer](通用技能领域/Family技能/未分类技能/微技能/Schedule Periodic Timer/SKILL.md) ｜ 适用：Schedule a timer that executes a callback repeatedly at a configurable interval. Use when you need repeating callbacks at fixed intervals, such as polling or periodic updates.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Schedule One-Shot Timer` 时，优先调用它。 线索：Need a delayed one-time callback, Deferred initialization required, Single animation frame or transition needed, timer, scheduling
- 当目标、阶段或方法更接近 `Schedule Periodic Timer` 时，优先调用它。 线索：Need repeating callbacks at fixed intervals, Polling or periodic update requirement, Configurable interval-based execution needed, timer, scheduling

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to coordinate multiple concurrent animations, manage timer lifecycle, or flush pending animations immediately
