---
id: "a62645f1-49ab-577d-a59d-a78d5d2e51cf"
name: "Schedule Single-Fire Timer"
description: "Schedule a timer that executes once and stops automatically on its first callback. Use this micro-skill when you need a one-time delayed callback or timeout behavior without manual stop management."
version: "0.1.0"
tags:
  - "timer"
  - "scheduling"
  - "animation"
  - "single-fire"
  - "timeout"
  - "micro-operation"
triggers:
  - "Need a one-time delayed callback"
  - "Timeout behavior required"
  - "Single execution with automatic cleanup"
---

# Schedule Single-Fire Timer

Schedule a timer that executes once and stops automatically on its first callback. Use this micro-skill when you need a one-time delayed callback or timeout behavior without manual stop management.

## Prompt

Call the timer scheduling function with your callback and optional delay. The timer will execute the callback exactly once, then automatically stop. No manual stop() call is required.

## Objective

Execute a callback function exactly once after a delay
## Applicable Signals

- Caller requests non-repeating timer
- Delay-then-execute pattern detected
- Resource cleanup on first fire is acceptable

## Contraindications

- Repeating or interval-based animation required
- Caller needs manual control over timer lifecycle
- Multiple callbacks needed from same timer instance

## Workflow Steps

- Accept callback function and optional delay parameter
- Schedule timer with provided callback
- Execute callback exactly once
- Automatically stop timer after first execution
- Return completion signal to caller

## Constraints

- Timer stops automatically after first callback execution
- No restart() or manual stop() needed by caller
- Callback receives elapsed time as parameter

## Cautions

- Do not use for recurring animations; use interval-based timer instead
- Callback must complete within reasonable time to avoid blocking

## Output Contract

- Callback executed exactly once; timer automatically stopped and cleaned up; no further invocations occur

## Triggers

- Need a one-time delayed callback
- Timeout behavior required
- Single execution with automatic cleanup
