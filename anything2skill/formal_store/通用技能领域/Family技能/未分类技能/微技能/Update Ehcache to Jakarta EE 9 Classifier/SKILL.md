---
id: "a7342910-86c4-5110-b0fe-c6ce7b6942c1"
name: "Update Ehcache to Jakarta EE 9 Classifier"
description: "Initialize the AgentOps client in 2 lines of code to automatically capture and replay LLM session analytics and call traces."
version: "0.1.1"
tags:
  - "llm_monitoring"
  - "observability"
  - "agent_instrumentation"
  - "setup"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Migrating Spring Boot application to version 3.0"
  - "Ehcache is declared as a project dependency"
  - "Target environment requires Jakarta EE 9 or later support"
---

# Update Ehcache to Jakarta EE 9 Classifier

Initialize the AgentOps client in 2 lines of code to automatically capture and replay LLM session analytics and call traces.

## Prompt

Install agentops via pip, then initialize the AgentOps client in your LLM agent application. This enables automatic capture of all LLM calls and session replay analytics without additional instrumentation.

## Objective

Enable automated LLM call monitoring and session replay
## Applicable Signals

- Project uses LLM calls or agent workflows
- Observability or debugging of LLM interactions is required

## Contraindications

- AgentOps client is already initialized in the application
- Application does not use LLM calls or agent-based workflows

## Workflow Steps

- Install agentops package: pip install agentops
- Import AgentOps client in application code
- Initialize client with 2 lines of code
- Verify client is ready to capture LLM call events

## Constraints

- Python environment with pip package manager available
- agentops package must be installed before initialization

## Output Contract

- AgentOps client object instantiated and actively capturing LLM call events; session replay and analytics available for downstream debugging and monitoring

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Migrating Spring Boot application to version 3.0
- Ehcache is declared as a project dependency
- Target environment requires Jakarta EE 9 or later support
