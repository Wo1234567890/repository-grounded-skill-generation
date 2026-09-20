---
id: "8612fede-8fc7-5e43-bf65-c945865f7b6f"
name: "Reward Function Contract Definition"
description: "Register a callable tool function with cost annotation using the @tool decorator, enabling cost-aware tool invocation and automatic cost tracking in agent workflows."
version: "0.1.2"
tags:
  - "agent_tools"
  - "cost_tracking"
  - "decorator_pattern"
  - "workflow_setup"
triggers:
  - "Implementing a custom reward function for GRPO training"
  - "Integrating a reward function into a training pipeline"
  - "Need to ensure reward outputs are compatible with advantage and loss computation"
---

# Reward Function Contract Definition

Register a callable tool function with cost annotation using the @tool decorator, enabling cost-aware tool invocation and automatic cost tracking in agent workflows.

## Prompt

Use the @tool decorator to register a callable function as a reusable tool. Provide a name parameter and cost parameter (numeric value representing execution cost). The decorated function becomes callable by agent instances and its cost is tracked automatically.

## Objective

Register a callable tool with cost annotation for agent use
## Applicable Signals

- Function will be called by multiple agent instances
- Tool execution cost needs to be monitored or billed
- Tool is part of a larger agent workflow

## Contraindications

- Tool is one-off or used only once
- Tool is internal-only and not exposed to agents
- Cost tracking is not required

## Workflow Steps

- Define function with appropriate parameters and return type
- Apply @tool decorator with name and cost arguments
- Ensure function body returns expected output type
- Register tool in agent context before workflow execution

## Constraints

- Function must be decorated with @tool before agent invocation
- name parameter must be provided and unique within workflow context
- cost parameter must be a numeric value

## Cautions

- Cost value should reflect actual execution cost to enable accurate billing
- Tool name must be descriptive and unique to avoid conflicts in multi-tool workflows

## Output Contract

- Tool is registered and callable by agent instances with cost metadata attached; cost is tracked on each invocation.

## Triggers

- Implementing a custom reward function for GRPO training
- Integrating a reward function into a training pipeline
- Need to ensure reward outputs are compatible with advantage and loss computation
