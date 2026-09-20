---
id: "629b66c5-d0e6-5995-a575-f2b286e95f97"
name: "CamelAI Agent Tracking Setup"
description: "Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity monitoring and debugging."
version: "0.1.0"
tags:
  - "agent_integration"
  - "observability"
  - "camelai"
  - "agentops"
  - "sdk_setup"
  - "monitoring"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new CamelAI agent project"
  - "Adding observability to an existing CamelAI system"
  - "Enabling agent activity monitoring for debugging"
---

# CamelAI Agent Tracking Setup

Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity monitoring and debugging.

## Prompt

Follow the CamelAI integration guide to install AgentOps and configure tracking for CamelAI agents. Verify that the SDK version meets the minimum requirement (>=0.32.0) before proceeding. Complete installation steps and confirm that the tracking dashboard is accessible.

## Objective

enable_agent_observability
## Applicable Signals

- CamelAI project initialization
- Need for agent-level visibility
- Debugging multi-agent workflows

## Contraindications

- CamelAI SDK version below 0.32.0
- Agent tracking already configured and operational

## Workflow Steps

- Verify CamelAI SDK version is >=0.32.0
- Install AgentOps package
- Follow official CamelAI integration guide
- Configure AgentOps with CamelAI agents
- Verify tracking dashboard accessibility

## Constraints

- CamelAI Python SDK must be version >=0.32.0
- AgentOps package must be installed in the project environment

## Output Contract

- AgentOps integration active with CamelAI agents; tracking dashboard accessible and operational.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new CamelAI agent project
- Adding observability to an existing CamelAI system
- Enabling agent activity monitoring for debugging
