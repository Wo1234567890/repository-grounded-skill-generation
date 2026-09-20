---
id: "13a5326f-0977-5ab3-ac1f-79ddc42717b1"
name: "CamelAI Agent Tracking Setup"
description: "Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity tracking and monitoring."
version: "0.1.0"
tags:
  - "agent_integration"
  - "camelai"
  - "observability"
  - "sdk_setup"
  - "monitoring"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new CamelAI agent project"
  - "Adding observability to an existing CamelAI system"
  - "Enabling agent activity monitoring for CamelAI-based agents"
---

# CamelAI Agent Tracking Setup

Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity tracking and monitoring.

## Prompt

To set up AgentOps tracking for CamelAI agents:
1. Verify CamelAI SDK version is >=0.32.0
2. Install AgentOps integration package
3. Configure AgentOps client in your CamelAI agent initialization
4. Verify tracking is active by checking dashboard logs for agent actions
Refer to the CamelAI integration guide for framework-specific configuration details.

## Objective

Enable agent tracking for CamelAI-built systems
## Applicable Signals

- CamelAI SDK version >=0.32.0 available
- Agent initialization phase
- Need for agent action logging and dashboard visibility

## Contraindications

- Using non-CamelAI agent frameworks
- CamelAI version < 0.32.0

## Workflow Steps

- Verify CamelAI SDK version meets minimum requirement (>=0.32.0)
- Install AgentOps integration for CamelAI
- Initialize AgentOps client in agent setup code
- Configure tracking parameters for CamelAI agent actions
- Validate tracking is active by observing dashboard logs

## Constraints

- CamelAI Python SDK must be version >=0.32.0 or later
- AgentOps package must be compatible with target CamelAI version

## Cautions

- Verify SDK version compatibility before installation
- Ensure AgentOps credentials are configured before agent initialization

## Output Contract

- AgentOps tracking active and logging CamelAI agent actions to dashboard; agent activity visible in monitoring interface

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new CamelAI agent project
- Adding observability to an existing CamelAI system
- Enabling agent activity monitoring for CamelAI-based agents
