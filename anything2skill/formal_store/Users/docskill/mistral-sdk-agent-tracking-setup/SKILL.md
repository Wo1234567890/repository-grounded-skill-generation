---
id: "e5a881b8-b0a6-5796-ba6a-0ca467046cb2"
name: "Mistral SDK Agent Tracking Setup"
description: "Configure and initialize AgentOps integration with Mistral Python SDK (>=0.32.0) to enable agent activity tracking and monitoring."
version: "0.1.0"
tags:
  - "agent_integration"
  - "mistral"
  - "agentops"
  - "monitoring"
  - "observability"
  - "sdk_setup"
triggers:
  - "Starting a new agent project using Mistral SDK"
  - "Requiring observability or debugging capabilities for Mistral agents"
---

# Mistral SDK Agent Tracking Setup

Configure and initialize AgentOps integration with Mistral Python SDK (>=0.32.0) to enable agent activity tracking and monitoring.

## Prompt

Initialize AgentOps client with Mistral SDK to track agent execution. Verify SDK version meets minimum requirement (>=0.32.0). Connect AgentOps to your Mistral agent instance and confirm tracking is active in the AgentOps dashboard.

## Objective

enable_agent_monitoring
## Applicable Signals

- Mistral SDK project initialized
- Need for agent activity tracking
- Debugging or monitoring requirement identified

## Contraindications

- Using Mistral without AgentOps integration requirement
- Mistral SDK version below 0.32.0

## Workflow Steps

- Verify Mistral SDK version is >=0.32.0
- Install AgentOps integration package
- Initialize AgentOps client
- Connect AgentOps client to Mistral agent instance
- Verify tracking is active in AgentOps dashboard

## Constraints

- Mistral Python SDK version must be >=0.32.0
- AgentOps client library must be installed

## Output Contract

- AgentOps client initialized and connected to Mistral agent
- Tracking logs confirmed in AgentOps dashboard

## Triggers

- Starting a new agent project using Mistral SDK
- Requiring observability or debugging capabilities for Mistral agents
