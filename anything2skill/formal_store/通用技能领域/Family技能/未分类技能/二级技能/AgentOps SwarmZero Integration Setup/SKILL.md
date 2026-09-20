---
id: "1d94a0e3-5f38-5710-bfc2-ef9462e26487"
name: "AgentOps SwarmZero Integration Setup"
description: "Initialize AgentOps observability for SwarmZero multi-agent systems by setting environment credentials and configuring the integration. Enables full tracking of agent actions, decisions, and performance metrics."
version: "0.1.0"
tags:
  - "agent_monitoring"
  - "swarmzero"
  - "observability"
  - "integration"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Deploying SwarmZero agents to production or staging"
  - "Need to track agent actions, decisions, and performance metrics"
  - "Require centralized observability dashboard for multi-agent systems"
---

# AgentOps SwarmZero Integration Setup

Initialize AgentOps observability for SwarmZero multi-agent systems by setting environment credentials and configuring the integration. Enables full tracking of agent actions, decisions, and performance metrics.

## Prompt

Set AGENTOPS_API_KEY in your environment and initialize AgentOps to begin observability for SwarmZero agents. Refer to the official SwarmZero Python SDK and AgentOps integration documentation for framework-specific initialization patterns.

## Objective

Enable full observability and tracking of SwarmZero agent behavior
## Applicable Signals

- SwarmZero framework selected for agent orchestration
- Monitoring and tracing requirements identified
- Environment setup phase before agent deployment

## Contraindications

- Local development without monitoring requirements
- Agents do not use SwarmZero framework
- No observability or telemetry needs

## Workflow Steps

- Set AGENTOPS_API_KEY environment variable with valid credentials
- Install SwarmZero Python SDK and AgentOps integration package
- Initialize AgentOps in SwarmZero agent configuration
- Verify telemetry connection to AgentOps dashboard
- Confirm agent actions and decisions are being tracked

## Constraints

- AGENTOPS_API_KEY must be set in environment before initialization
- SwarmZero Python SDK must be installed
- Valid AgentOps account and API credentials required

## Output Contract

- AgentOps initialized with valid API key; SwarmZero agent telemetry flowing to observability dashboard; agent actions and metrics visible in monitoring interface

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Deploying SwarmZero agents to production or staging
- Need to track agent actions, decisions, and performance metrics
- Require centralized observability dashboard for multi-agent systems
