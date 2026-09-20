---
id: "255a3156-f95c-566c-a098-404770013eaf"
name: "Initialize AgentOps for Camel AI Observability"
description: "Set up AgentOps environment variable and initialize the observability client to track and analyze Camel AI agents with full observability."
version: "0.1.0"
tags:
  - "observability"
  - "camel-ai"
  - "agentops"
  - "initialization"
  - "setup"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new Camel AI agent project and need to enable tracking and debugging capabilities"
---

# Initialize AgentOps for Camel AI Observability

Set up AgentOps environment variable and initialize the observability client to track and analyze Camel AI agents with full observability.

## Prompt

1. Set the AGENTOPS_API_KEY environment variable with your AgentOps API key.
2. Initialize AgentOps in your Camel AI agent project.
3. Verify that the observability client is connected to the agent runtime.
4. Confirm API key validation and observability activation.

## Objective

Enable observability for Camel AI agents
## Applicable Signals

- Starting a new Camel AI agent project
- Need to enable tracking and debugging capabilities
- First-time setup of agent observability

## Contraindications

- AgentOps is already initialized in the session
- Observability is not required for the agent workflow
- API key is not available or invalid

## Workflow Steps

- {'step': 1, 'action': 'Set environment variable', 'detail': 'Export or configure AGENTOPS_API_KEY in your environment'}
- {'step': 2, 'action': 'Initialize AgentOps client', 'detail': 'Call AgentOps initialization function in your Camel AI project'}
- {'step': 3, 'action': 'Verify connection', 'detail': 'Confirm observability client is connected to Camel AI agent runtime'}
- {'step': 4, 'action': 'Validate activation', 'detail': 'Check that API key is validated and observability is active'}

## Constraints

- AGENTOPS_API_KEY must be set before initialization
- Camel AI framework must be installed and available
- Network connectivity required for API key validation

## Output Contract

- AgentOps client initialized and connected to Camel AI agent runtime; API key validated and observability active. Agent tracking and analysis capabilities are ready for use.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new Camel AI agent project and need to enable tracking and debugging capabilities
