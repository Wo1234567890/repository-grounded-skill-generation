---
id: "22ac7a8c-8b93-5cdb-997a-acdd78054ed8"
name: "Agent Class Definition with ID Binding"
description: "Define an agent class using the @agent decorator, binding a unique agent_id that persists across method calls and enables agent-level logging and tracing."
version: "0.1.0"
tags:
  - "agent_setup"
  - "identity_binding"
  - "logging"
  - "tracing"
  - "class_decorator"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Building a specialized agent that will be instantiated with a unique ID"
  - "Agent will be used across multiple workflow invocations"
  - "Agent-level logging and tracing is required"
---

# Agent Class Definition with ID Binding

Define an agent class using the @agent decorator, binding a unique agent_id that persists across method calls and enables agent-level logging and tracing.

## Prompt

Use the @agent decorator to define a class. In __init__, accept and store an agent_id parameter. This ID will be used by the logging and tracing system to track all operations performed by this agent instance across multiple workflow invocations.

## Objective

Create a reusable agent class with stable identity for multi-step workflows
## Applicable Signals

- Multi-step workflow requires agent identity tracking
- Agent performs multiple operations that need to be correlated
- Logging system expects stable agent_id

## Contraindications

- Agent is stateless or single-use
- No persistent identity tracking required
- Agent does not participate in multi-step workflows

## Workflow Steps

- Apply @agent decorator with name parameter to class definition
- Define __init__ method accepting agent_id as parameter
- Store agent_id as self.agent_id instance attribute
- Ensure agent_id is accessible to all instance methods

## Constraints

- agent_id must be unique and stable across instantiation
- agent_id must be stored as instance attribute in __init__
- @agent decorator must be applied to the class

## Cautions

- Ensure agent_id is unique across concurrent agent instances
- Do not modify agent_id after instantiation
- Verify that logging system can access self.agent_id

## Output Contract

- Agent instance created with agent_id stored and available for logging and tracing. The agent_id persists for the lifetime of the instance and is accessible to downstream logging/tracing systems.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Building a specialized agent that will be instantiated with a unique ID
- Agent will be used across multiple workflow invocations
- Agent-level logging and tracing is required
