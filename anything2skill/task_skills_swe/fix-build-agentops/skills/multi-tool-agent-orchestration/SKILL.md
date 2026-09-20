---
id: "61cc67c4-b893-5bb7-add2-1faa08914a31"
name: "Multi-Tool Agent Orchestration"
description: "Coordinate multiple tools or agents in a single execution flow, managing tool selection, parameter passing, and result aggregation. Handles complex tool chains and multi-agent system coordination across frameworks like CrewAI, LangChain, OpenAI, and SmolAgents."
version: "0.1.0"
tags:
  - "multi-tool"
  - "agent-coordination"
  - "orchestration"
  - "workflow"
  - "tool-chaining"
  - "crewai"
triggers:
  - "Agent requires multiple tools in sequence or parallel"
  - "Multi-agent system needs coordination"
  - "Complex tool chains with interdependencies detected"
---

# Multi-Tool Agent Orchestration

Coordinate multiple tools or agents in a single execution flow, managing tool selection, parameter passing, and result aggregation. Handles complex tool chains and multi-agent system coordination across frameworks like CrewAI, LangChain, OpenAI, and SmolAgents.

## Prompt

Execute a coordinated workflow across multiple tools or agents. Determine tool execution order based on dependencies, pass outputs from one tool as inputs to the next, aggregate final results, and handle tool selection logic. Ensure all interdependencies are resolved before returning aggregated results to the caller.

## Objective

Execute coordinated multi-tool or multi-agent workflows
## Applicable Signals

- Multiple tool invocations in workflow
- Tool output dependency chain identified
- Multi-agent system initialization

## Contraindications

- Single-tool agent execution
- Simple linear tool call without selection logic
- No tool interdependencies or coordination required

## Workflow Steps

- Identify all tools or agents required for the workflow
- Determine execution order and dependencies
- Validate tool parameters and input compatibility
- Execute tools in correct sequence or parallel batches
- Pass outputs from upstream tools as inputs to downstream tools
- Aggregate results from all tools
- Return aggregated results to caller

## Constraints

- All tool dependencies must be resolved before execution
- Tool parameters must be validated before passing to next stage
- Result aggregation must preserve execution order and metadata

## Cautions

- Verify tool compatibility before chaining
- Monitor for circular dependencies in tool chains
- Ensure timeout handling for long-running tool sequences

## Output Contract

- All tools executed in correct order; results aggregated and returned to caller; tool dependencies resolved; execution metadata preserved

## Triggers

- Agent requires multiple tools in sequence or parallel
- Multi-agent system needs coordination
- Complex tool chains with interdependencies detected
