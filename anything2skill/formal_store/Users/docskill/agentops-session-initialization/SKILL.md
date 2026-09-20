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

## Triggers

- Starting a new multi-agent workflow or CrewAI task
- Requiring session-level observability and debugging traces
- Need to track cross-agent interactions and task execution
