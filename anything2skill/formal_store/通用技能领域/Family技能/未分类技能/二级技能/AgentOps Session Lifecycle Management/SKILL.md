---
id: "5c3d9b07-1dd7-525a-8a57-f941ca7647ba"
name: "AgentOps Session Lifecycle Management"
description: "Initialize, stream events, and terminate an AgentOps monitoring session for agent applications. Captures text-generation events and logs session completion status."
version: "0.1.0"
tags:
  - "agent_monitoring"
  - "session_lifecycle"
  - "observability"
  - "event_streaming"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Agent application startup requiring observability"
  - "Need to track and stream agent execution events"
  - "Agent framework supports AgentOps SDK integration"
---

# AgentOps Session Lifecycle Management

Initialize, stream events, and terminate an AgentOps monitoring session for agent applications. Captures text-generation events and logs session completion status.

## Prompt

1. Initialize AgentOps session at agent startup.
2. Enter event streaming loop; check event.event_type for 'text-generation' and process accordingly.
3. Call agentops.end_session() with completion status ('Success' or appropriate status) to close the session and log results.

## Objective

Establish and close a monitored agent execution session with event streaming
## Applicable Signals

- Agent initialization phase
- Event stream available from agent framework
- Session monitoring required for debugging or audit

## Contraindications

- Agent framework does not support AgentOps SDK
- No event streaming capability available
- Session lifecycle already managed by external wrapper or framework

## Workflow Steps

- {'step': 1, 'action': 'Initialize AgentOps session', 'detail': 'Call agentops.init() or equivalent at agent startup'}
- {'step': 2, 'action': 'Stream and filter events', 'detail': "Iterate over event stream; check event.event_type == 'text-generation' and process output"}
- {'step': 3, 'action': 'Terminate session', 'detail': "Call agentops.end_session(status) with completion status (e.g., 'Success')"}

## Constraints

- AgentOps SDK must be installed and initialized before use
- Event loop must be accessible from agent execution context
- Session termination must occur before application exit

## Cautions

- Ensure agentops.end_session() is called even on error paths to avoid orphaned sessions
- Verify event.event_type filtering matches framework's event schema

## Output Contract

- Session initialized and active
- Events streamed to output with text-generation events processed
- Session terminated with status logged and session closed

## 子技能目录
- [Agent Session Replay and Analytics Review](通用技能领域/Family技能/未分类技能/微技能/Agent Session Replay and Analytics Review/SKILL.md) ｜ 适用：Access and review recorded agent session replays and summary analytics via the AgentOps dashboard to identify and debug agent behavior issues.
- [Anthropic Claude API Message Creation with AgentOps Tracking](通用技能领域/Family技能/未分类技能/微技能/Anthropic Claude API Message Creation with AgentOps Tracking/SKILL.md) ｜ 适用：Execute a single non-streaming message creation call to Anthropic's Claude model with AgentOps session tracking enabled. Captures API interactions for debugging and monitoring multi-agent workflows.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Agent Session Replay and Analytics Review` 时，优先调用它。 线索：Session has completed and end_session() has been called, Need to understand agent behavior or identify execution failures, Performance optimization or debugging required, agent_debugging, observability
- 当目标、阶段或方法更接近 `Anthropic Claude API Message Creation with AgentOps Tracking` 时，优先调用它。 线索：Integrating Anthropic Claude into an agentic system that requires session-level observability; when you need to log and debug LLM interactions, anthropic, claude, llm_integration, agentops

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent application startup requiring observability
- Need to track and stream agent execution events
- Agent framework supports AgentOps SDK integration
