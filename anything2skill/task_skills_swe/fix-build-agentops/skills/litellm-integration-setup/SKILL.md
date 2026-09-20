---
id: "eef033aa-c25c-5fb2-a472-489938d12a32"
name: "LiteLLM Integration Setup"
description: "Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ LLMs through a standardized Input/Output interface."
version: "0.1.0"
tags:
  - "integration"
  - "litellm"
  - "llm_provider"
  - "multi_model"
  - "setup"
triggers:
  - "Starting a new AgentOps project requiring multi-LLM support"
  - "Switching from direct LLM calls to unified LiteLLM interface"
  - "Need to abstract multiple LLM providers behind a single API"
---

# LiteLLM Integration Setup

Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ LLMs through a standardized Input/Output interface.

## Prompt

Install and configure LiteLLM integration with AgentOps. Verify that LiteLLM version meets minimum requirement (>=1.3.1). Initialize AgentOps with LiteLLM as the backend provider to expose 100+ LLM providers through a single standardized interface.

## Objective

Enable LiteLLM provider integration with AgentOps
## Applicable Signals

- Project requires support for 100+ LLM providers
- Standardized Input/Output format needed across LLM calls
- Multi-provider flexibility is a requirement

## Contraindications

- LiteLLM version is below 1.3.1
- Already using a single hardcoded LLM provider without need for provider abstraction
- Project has no requirement for provider switching or multi-LLM support

## Workflow Steps

- Verify LiteLLM version is >=1.3.1
- Install or upgrade LiteLLM package if needed
- Initialize AgentOps with LiteLLM backend
- Verify unified Input/Output format is accessible across providers
- Test access to at least one LLM provider through the unified interface

## Constraints

- LiteLLM version must be >=1.3.1
- AgentOps must be installed and available in the project environment

## Cautions

- Verify LiteLLM version compatibility before initialization
- Ensure all required LLM provider credentials are configured before use

## Output Contract

- AgentOps successfully initialized with LiteLLM backend; 100+ LLM providers accessible via unified Input/Output format; caller can invoke LLM calls through standardized interface

## Triggers

- Starting a new AgentOps project requiring multi-LLM support
- Switching from direct LLM calls to unified LiteLLM interface
- Need to abstract multiple LLM providers behind a single API
