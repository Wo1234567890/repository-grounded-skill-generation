---
id: "5a63d94f-55c3-5860-b386-acd57dbebc38"
name: "Parallel Task Completion Polling"
description: "Wait for a collection of Futures to reach a completion condition (any, first exception, or all done) with optional timeout. Use this session-level skill to coordinate multi-task workflows and decide when to proceed based on task readiness."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "Future"
  - "polling"
  - "synchronization"
  - "timeout"
  - "multi-task coordination"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to wait for multiple parallel tasks and decide next action based on which tasks complete first"
  - "Require timeout-bounded waiting for task completion"
  - "Must inspect which Futures finished and which are still running after wait returns"
---

# Parallel Task Completion Polling

Wait for a collection of Futures to reach a completion condition (any, first exception, or all done) with optional timeout. Use this session-level skill to coordinate multi-task workflows and decide when to proceed based on task readiness.

## Prompt

Call concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED) to block until a completion condition is met. Specify return_when as one of: FIRST_COMPLETED (return when any Future finishes or is cancelled), FIRST_EXCEPTION (return when any Future raises an exception, or ALL_COMPLETED if none raise), or ALL_COMPLETED (return when all Futures finish or are cancelled). Timeout can be an int or float in seconds; None means no limit. The function returns a tuple (done, pending) where done and pending are sets of Futures.

## Objective

Block and poll a Future collection until a specified completion condition is met, returning a snapshot of done and pending tasks
## Applicable Signals

- Multiple Futures submitted to an Executor
- Caller needs to block until a specific completion condition is met
- Timeout constraint is present or optional

## Contraindications

- Single Future: use Future.result() instead
- No need to wait for completion: use as_completed() for streaming results
- Synchronous blocking is unacceptable in the calling context
- Caller needs results as they arrive rather than a snapshot at a condition

## Workflow Steps

- Collect all Future objects from parallel task submissions
- Choose return_when condition: FIRST_COMPLETED, FIRST_EXCEPTION, or ALL_COMPLETED
- Set timeout value (None for no limit, or int/float seconds)
- Call concurrent.futures.wait(fs, timeout, return_when)
- Inspect returned (done, pending) tuple to determine next action
- Handle any Futures in done set; optionally wait again on pending set if needed

## Constraints

- return_when must be one of: FIRST_COMPLETED, FIRST_EXCEPTION, or ALL_COMPLETED
- timeout must be None, int, or float (seconds)
- fs must be a collection of Future objects
- Function blocks the calling thread until condition is met or timeout expires

## Cautions

- If timeout expires before return_when condition is met, function returns with pending Futures still running
- FIRST_EXCEPTION returns only if a Future raises an exception; if none raise, behaves as ALL_COMPLETED
- Caller must handle both done and pending sets; pending Futures continue running in background

## Output Contract

- Returns a tuple (done, pending) where done is a set of Futures that have completed (finished or cancelled) and pending is a set of Futures still running. Caller can call Future.result() or Future.exception() on done Futures to retrieve outcomes.

## 子技能目录
- [Future Exception Inspection with Timeout](通用技能领域/Family技能/未分类技能/微技能/Future Exception Inspection with Timeout/SKILL.md) ｜ 适用：Decorator-based pattern to define a reusable tool with name and cost attributes, enabling cost tracking and tool discovery in agent workflows.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Future Exception Inspection with Timeout` 时，优先调用它。 线索：A parallel task has completed and the caller needs to examine what exception (if any) was raised, without propagating it immediately., agent_tools, decorator_pattern, cost_tracking, tool_registration

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to wait for multiple parallel tasks and decide next action based on which tasks complete first
- Require timeout-bounded waiting for task completion
- Must inspect which Futures finished and which are still running after wait returns
