---
id: "2207c09a-ca7c-54bc-9033-d9731247c4d0"
name: "AgentOps Session Initialization"
description: "Initialize and configure AgentOps client for multi-agent workflow monitoring and tracing. Sets up session tracking with custom tags and trace naming for debugging and observability."
version: "0.1.0"
tags:
  - "monitoring"
  - "observability"
  - "session_setup"
  - "multi_agent"
  - "crewai"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new multi-agent workflow or CrewAI task"
  - "Requiring session-level observability and debugging traces"
  - "Need to track cross-agent interactions and task execution"
---

# AgentOps Session Initialization

Initialize and configure AgentOps client for multi-agent workflow monitoring and tracing. Sets up session tracking with custom tags and trace naming for debugging and observability.

## Prompt

Call agentops.init() with auto_start_session=False to defer session start, provide a descriptive trace_name for the workflow, and supply relevant tags for filtering and categorization. Ensure the client is initialized before agents and tasks are instantiated.

## Objective

establish_monitoring_session
## Applicable Signals

- Workflow entry point before agent instantiation
- Requirement for centralized monitoring and tracing
- Multi-agent orchestration context

## Contraindications

- Running standalone single-agent scripts without cross-agent tracing needs
- Offline or local-only debugging without external monitoring requirements
- Environments where AgentOps client is unavailable or disabled

## Workflow Steps

- Import agentops module
- Call agentops.init() with auto_start_session=False
- Provide trace_name parameter with descriptive workflow identifier
- Supply tags list for workflow categorization and filtering
- Verify client is ready before proceeding to agent/task setup

## Constraints

- AgentOps package must be installed and importable
- Initialization must occur before agents and tasks are created
- auto_start_session should be set to False to allow manual session control

## Output Contract

- AgentOps client initialized with auto_start_session=False, trace_name set, and tags applied; ready to accept agent and task events for session tracking.

## 子技能目录
- [AgentOps Client Configuration Validation](通用技能领域/Family技能/未分类技能/微技能/AgentOps Client Configuration Validation/SKILL.md) ｜ 适用：Validates configuration parameters against a whitelist of supported parameters during AgentOps client initialization or reconfiguration. Logs warnings for invalid parameters and applies only valid parameters to the global client instance.
- [Update Ehcache to Jakarta EE 9 Classifier](通用技能领域/Family技能/未分类技能/微技能/Update Ehcache to Jakarta EE 9 Classifier/SKILL.md) ｜ 适用：Initialize the AgentOps client in 2 lines of code to automatically capture and replay LLM session analytics and call traces.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `AgentOps Client Configuration Validation` 时，优先调用它。 线索：AgentOps client instantiation with kwargs, Client reconfiguration request with configuration parameters, configure() function invoked with keyword arguments, configuration, validation
- 当目标、阶段或方法更接近 `Update Ehcache to Jakarta EE 9 Classifier` 时，优先调用它。 线索：Migrating Spring Boot application to version 3.0, Ehcache is declared as a project dependency, Target environment requires Jakarta EE 9 or later support, llm_monitoring, observability

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new multi-agent workflow or CrewAI task
- Requiring session-level observability and debugging traces
- Need to track cross-agent interactions and task execution
