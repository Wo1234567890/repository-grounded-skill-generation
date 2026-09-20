---
id: "ee49c5d9-8843-5c74-8be6-3666b7ca86c1"
name: "Track Mistral Agent Execution"
description: "Integrate AgentOps monitoring with Mistral Python SDK (>=0.32.0) to track agent behavior, decisions, and outcomes in real time."
version: "0.1.0"
tags:
  - "mistral"
  - "agentops"
  - "monitoring"
  - "agent_tracking"
  - "observability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Building or deploying agents using Mistral Python SDK and requiring execution tracking, debugging, or performance monitoring"
---

# Track Mistral Agent Execution

Integrate AgentOps monitoring with Mistral Python SDK (>=0.32.0) to track agent behavior, decisions, and outcomes in real time.

## Prompt

Initialize AgentOps session with Mistral Python SDK to enable observability of agent actions, tool calls, and state transitions. Ensure AgentOps SDK is installed and configured before agent instantiation.

## Objective

Enable observability and debugging of Mistral-based agents
## Applicable Signals

- Mistral Python SDK (>=0.32.0) available in environment
- Agent initialization phase
- Requirement for execution tracking or debugging
- Performance monitoring needed

## Contraindications

- Using Mistral via non-Python interfaces
- AgentOps SDK not available or not installed
- Environment does not support SDK instrumentation

## Workflow Steps

- Verify Mistral Python SDK (>=0.32.0) is installed
- Verify AgentOps SDK is installed
- Initialize AgentOps session before creating Mistral agent
- Instantiate Mistral agent with AgentOps instrumentation active
- Confirm AgentOps is logging agent actions and tool calls

## Constraints

- Mistral Python SDK version must be >=0.32.0
- AgentOps SDK must be installed in the same environment
- Session initialization must occur before agent instantiation

## Cautions

- Ensure AgentOps initialization occurs before agent creation to capture all events
- Monitor session lifecycle to avoid premature termination

## Output Contract

- AgentOps session initialized and actively logging Mistral agent actions, tool calls, and state transitions. Session remains active for the duration of agent execution.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building or deploying agents using Mistral Python SDK and requiring execution tracking, debugging, or performance monitoring
