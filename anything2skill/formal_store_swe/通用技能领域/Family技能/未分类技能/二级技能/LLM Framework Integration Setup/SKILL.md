---
id: "5f46e16b-0571-5d46-bf61-c48da74e897a"
name: "LLM Framework Integration Setup"
description: "Establish and configure AgentOps monitoring for a chosen LLM framework (OpenAI, LangChain, LiteLLM, Gemini, Google ADK, CrewAI, OpenAI Agents, SmolAgents, Watsonx, or xAI). Selects the appropriate integration module, initializes the client, and validates connection."
version: "0.1.0"
tags:
  - "framework_integration"
  - "setup"
  - "monitoring"
  - "initialization"
  - "agentops"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new agent project with a specific LLM framework"
  - "Need to enable AgentOps monitoring before agent execution"
  - "Framework selection decision point reached"
---

# LLM Framework Integration Setup

Establish and configure AgentOps monitoring for a chosen LLM framework (OpenAI, LangChain, LiteLLM, Gemini, Google ADK, CrewAI, OpenAI Agents, SmolAgents, Watsonx, or xAI). Selects the appropriate integration module, initializes the client, and validates connection.

## Prompt

Select the target LLM framework from available integrations. Locate the corresponding integration module directory. Initialize the AgentOps client with framework-specific configuration. Validate that the client is connected and monitoring is active before proceeding with agent execution.

## Objective

Initialize framework-specific AgentOps integration and activate monitoring
## Applicable Signals

- Project initialization phase
- Framework choice confirmed
- Monitoring requirements identified

## Contraindications

- Framework already initialized and monitoring active
- Only adding a single micro-operation to existing setup
- Debugging existing agent behavior without re-initialization

## Workflow Steps

- {'step': 1, 'action': 'Select target LLM framework', 'detail': 'Choose from CrewAI, Gemini, Google ADK, LangChain, LiteLLM, OpenAI, OpenAI Agents, SmolAgents, Watsonx, or xAI'}
- {'step': 2, 'action': 'Locate integration module', 'detail': 'Access the corresponding framework directory in the AgentOps repository'}
- {'step': 3, 'action': 'Initialize AgentOps client', 'detail': 'Create and configure the client with framework-specific parameters'}
- {'step': 4, 'action': 'Validate connection', 'detail': 'Verify that monitoring is active and client is ready for agent execution'}

## Constraints

- Target framework must be one of: CrewAI, Gemini, Google ADK, LangChain, LiteLLM, OpenAI, OpenAI Agents, SmolAgents, Watsonx, xAI
- AgentOps client library must be available
- Framework-specific credentials or API keys must be configured

## Cautions

- Ensure framework selection is finalized before initialization
- Validate API credentials before attempting connection
- Monitor initialization logs for connection errors

## Output Contract

- AgentOps client initialized and connected to the chosen framework; monitoring active for subsequent agent calls; ready for agent execution

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new agent project with a specific LLM framework
- Need to enable AgentOps monitoring before agent execution
- Framework selection decision point reached
