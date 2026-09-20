---
id: "d68ed7cc-0e6f-59e0-be4b-23d284fc1279"
name: "Spring Boot 2.x to 3.0 Instrumentation Migration Reference"
description: "Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system."
version: "0.1.1"
tags:
  - "integration"
  - "observability"
  - "agent_framework"
  - "instrumentation"
  - "reference"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "assessing Spring Boot 2.x instrumentation code for 3.0 compatibility; identifying which classes and patterns must be refactored"
---

# Spring Boot 2.x to 3.0 Instrumentation Migration Reference

Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system.

## Prompt

Identify the target agent framework. Consult the AgentOps integration reference to find the framework-specific integration approach, code examples, and official client library. Apply the framework-native instrumentation pattern to enable monitoring.

## Objective

Provide framework-specific integration guidance and code examples for AgentOps observability
## Applicable Signals

- Selecting AgentOps support for a particular agent framework
- Implementing observability in a framework-based agent system
- Framework is in the supported integration list (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, OpenAI Agents SDK, Cohere, CamelAI, LiteLLM, LlamaIndex)

## Contraindications

- Framework is not in the supported AgentOps integration list
- Custom agent implementation without framework dependency
- Monitoring is not a requirement

## Workflow Steps

- Identify the target agent framework
- Consult the AgentOps integration reference for framework-specific approach
- Locate code examples and official client library documentation
- Apply framework-native instrumentation pattern

## Constraints

- Integration approach must be framework-native
- Code examples and official client library must be available for the target framework

## Output Contract

- Reference documentation and code examples identified for the target framework
- Integration approach clarified and ready for implementation

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- assessing Spring Boot 2.x instrumentation code for 3.0 compatibility; identifying which classes and patterns must be refactored
