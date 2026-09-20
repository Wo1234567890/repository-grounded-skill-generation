---
id: "7800d6b2-de29-59c9-b764-704f0c8df2fe"
name: "Initialize AgentOps Monitoring for Llama Stack"
description: "Set up AgentOps integration with Llama Stack Python Client (>=0.0.53) to enable observability and monitoring of agentic applications."
version: "0.1.0"
tags:
  - "agent_monitoring"
  - "llama_stack"
  - "observability"
  - "initialization"
  - "integration"
triggers:
  - "Starting a new Llama Stack agentic application"
  - "Need to track execution and behavior of Llama Stack agents"
---

# Initialize AgentOps Monitoring for Llama Stack

Set up AgentOps integration with Llama Stack Python Client (>=0.0.53) to enable observability and monitoring of agentic applications.

## Prompt

Initialize AgentOps with Llama Stack Python Client to begin monitoring agent interactions. Ensure the Llama Stack client version meets the minimum requirement (>=0.0.53). Refer to the official integration examples and Llama Stack Python Client documentation for implementation details.

## Objective

Enable monitoring for Llama Stack agents
## Applicable Signals

- Llama Stack client instantiation
- Agent application startup phase

## Contraindications

- Llama Stack client version is below 0.0.53
- Monitoring is not required for the application

## Workflow Steps

- Verify Llama Stack Python Client version is >=0.0.53
- Import and initialize AgentOps in the application
- Configure AgentOps to connect with Llama Stack client
- Verify monitoring is active and logging agent interactions

## Constraints

- Llama Stack Python Client version must be >=0.0.53
- AgentOps must be initialized before agent execution begins

## Output Contract

- AgentOps monitoring is active and logging agent interactions from Llama Stack client
- Observability is enabled for the agentic application

## Triggers

- Starting a new Llama Stack agentic application
- Need to track execution and behavior of Llama Stack agents
