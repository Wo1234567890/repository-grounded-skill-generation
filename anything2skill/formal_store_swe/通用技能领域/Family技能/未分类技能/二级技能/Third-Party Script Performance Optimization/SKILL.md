---
id: "803d45fe-dfab-571a-ba81-9ec12337db12"
name: "Third-Party Script Performance Optimization"
description: "Set up AgentOps client in 2 lines of code to automatically capture and replay LLM call analytics and session traces."
version: "0.1.2"
tags:
  - "setup"
  - "observability"
  - "session_replay"
  - "instrumentation"
  - "agent_monitoring"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "application integrates analytics scripts"
  - "application integrates tracking scripts"
  - "application integrates vendor scripts"
  - "page performance metrics show script-related bottlenecks"
---

# Third-Party Script Performance Optimization

Set up AgentOps client in 2 lines of code to automatically capture and replay LLM call analytics and session traces.

## Prompt

Initialize the AgentOps client to enable automatic analytics collection on all LLM calls. This foundational setup enables session replay and observability for agent or LLM applications.

## Objective

Enable session replay and LLM call analytics collection
## Applicable Signals

- Project initialization phase
- Agent framework setup
- LLM application deployment

## Contraindications

- AgentOps client already initialized in the session
- Session replay not required for the application
- Observability infrastructure already in place via alternative means

## Workflow Steps

- Install agentops package via pip
- Import AgentOps client in application code
- Initialize client with minimal configuration (2 lines of code)
- Verify client is ready to capture analytics

## Constraints

- Must be executed before LLM calls are made
- Requires agentops package installation (pip install agentops)
- Single initialization per session

## Output Contract

- AgentOps client initialized and ready to capture LLM calls and session traces; automatic analytics collection enabled.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- application integrates analytics scripts
- application integrates tracking scripts
- application integrates vendor scripts
- page performance metrics show script-related bottlenecks
