---
id: "aa70b4ce-2bbe-5641-9ec3-765f02288449"
name: "AgentOps Session Initialization with Tracing"
description: "Initialize AgentOps SDK with deferred session startup and decorate workflow functions with trace metadata to enable session tracking, debugging, and observability. Establishes manual control over session lifecycle and instruments functions with name and tag annotations."
version: "0.1.0"
tags:
  - "observability"
  - "debugging"
  - "session_management"
  - "instrumentation"
  - "agent_workflow"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new agent workflow or session that requires debugging, monitoring, or audit trails"
---

# AgentOps Session Initialization with Tracing

Initialize AgentOps SDK with deferred session startup and decorate workflow functions with trace metadata to enable session tracking, debugging, and observability. Establishes manual control over session lifecycle and instruments functions with name and tag annotations.

## Prompt

1. Call agentops.init() with auto_start_session=False to defer session startup.
2. Apply @trace decorator to target workflow function with name parameter (e.g., 'my-workflow') and tags list (e.g., ['production']).
3. Ensure decorated function executes within the initialized session context.
4. Verify trace metadata is captured before function returns.

## Objective

Enable structured session initialization and workflow-level tracing for agent observability
## Applicable Signals

- Starting a new agent workflow or session
- Requirement for debugging, monitoring, or audit trails
- Need to instrument function-level execution with metadata

## Contraindications

- Environments where tracing overhead is unacceptable
- Session state managed externally or by third-party framework
- Real-time latency-critical workflows where instrumentation adds unacceptable delay

## Intervention Moves

- Import agentops and trace decorator
- Initialize SDK with auto_start_session=False
- Decorate workflow function with @trace(name=..., tags=[...])
- Execute decorated function within session context

## Workflow Steps

- Import agentops module and trace decorator
- Call agentops.init(auto_start_session=False)
- Define or identify target workflow function
- Apply @trace(name=..., tags=[...]) decorator
- Execute decorated function within session context
- Verify trace metadata capture

## Constraints

- auto_start_session must be set to False to allow manual session control
- Decorated function must execute after agentops.init() call
- Trace name and tags must be provided as decorator arguments

## Cautions

- Ensure session is properly closed or managed to avoid resource leaks
- Trace metadata overhead may impact performance in high-frequency call scenarios

## Output Contract

- AgentOps session initialized with deferred startup; decorated function instrumented with trace metadata (name, tags) and ready for execution; trace data captured and available for debugging and monitoring downstream.

## 子技能目录
- [Async and Generator Function Instrumentation](通用技能领域/Family技能/未分类技能/微技能/Async and Generator Function Instrumentation/SKILL.md) ｜ 适用：Enable observability decorators to correctly instrument async/await and generator functions, capturing execution state at each await or yield boundary without introducing performance overhead or altering function semantics.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Async and Generator Function Instrumentation` 时，优先调用它。 线索：Agent operation uses async/await syntax, Function contains yield or yield from statements, Observability must capture intermediate states or streaming outputs, observability, instrumentation

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new agent workflow or session that requires debugging, monitoring, or audit trails
