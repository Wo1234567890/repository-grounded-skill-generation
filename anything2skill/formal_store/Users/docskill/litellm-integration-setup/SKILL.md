---
id: "77e6d001-80b3-518d-a129-4377a6e3fa82"
name: "LiteLLM Integration Setup"
description: "Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ language models through a standardized Input/Output interface."
version: "0.1.0"
tags:
  - "llm"
  - "integration"
  - "litellm"
  - "multi-provider"
  - "setup"
triggers:
  - "User needs to integrate multiple LLM providers into an agent system and wants unified API handling"
---

# LiteLLM Integration Setup

Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ language models through a standardized Input/Output interface.

## Prompt

Install and configure AgentOps with LiteLLM to route requests across multiple LLM providers using a single standardized API. Verify that the LiteLLM version meets the minimum requirement (>=1.3.1) and that AgentOps can successfully abstract provider-specific calls.

## Objective

Enable multi-LLM routing via LiteLLM provider abstraction
## Applicable Signals

- User needs to integrate multiple LLM providers into an agent system
- Unified API handling across 100+ LLMs is required
- Agent system requires provider-agnostic LLM routing

## Contraindications

- Single LLM provider is already directly integrated without need for abstraction
- LiteLLM version is below 1.3.1
- Agent system does not require multi-provider support

## Workflow Steps

- Verify LiteLLM version is >=1.3.1
- Install AgentOps with LiteLLM support
- Configure AgentOps integration with LiteLLM
- Test unified Input/Output format across selected providers
- Verify request routing to target LLM provider

## Constraints

- LiteLLM version must be >=1.3.1
- AgentOps must be compatible with the installed LiteLLM version

## Output Contract

- AgentOps successfully routes requests to selected LLM provider via LiteLLM abstraction layer
- Unified Input/Output format is operational across configured providers

## Triggers

- User needs to integrate multiple LLM providers into an agent system and wants unified API handling
