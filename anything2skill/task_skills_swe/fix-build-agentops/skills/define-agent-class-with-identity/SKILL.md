---
id: "e0717ff9-031e-51b5-83d7-014d5c571d29"
name: "Define Agent Class with Identity"
description: "Decorator-based pattern to define an agent class with a unique agent_id, enabling agent identity tracking and state management in multi-agent systems."
version: "0.1.0"
tags:
  - "agent"
  - "identity"
  - "decorator"
  - "multi-agent"
  - "setup"
triggers:
  - "Need to create an agent with a unique identifier for logging, tracing, or multi-agent coordination"
  - "Multi-agent workflow requires agent identity tracking"
  - "Agent state management and persistence is required"
examples:
  - input: "Create a ResearchSpecialistAgent with identifier 'researcher-alpha-007'"
    output: "ResearchAgent instance with self.agent_id = 'researcher-alpha-007' accessible for tracing and coordination"
    notes: "Agent_id persists across method calls and can be used by AgentOps for session tracking"
---

# Define Agent Class with Identity

Decorator-based pattern to define an agent class with a unique agent_id, enabling agent identity tracking and state management in multi-agent systems.

## Prompt

Use the @agent decorator to define a class that initializes with a unique agent_id. The agent_id is stored as an instance attribute and made available for downstream operations such as logging, tracing, and multi-agent coordination.

## Objective

Create an agent class instance with persistent identity for tracking and orchestration
## Applicable Signals

- Multi-agent system initialization
- Agent orchestration or coordination phase
- Logging or tracing infrastructure in place

## Contraindications

- Agent is stateless or temporary
- No identity tracking required
- Single-agent workflow with no coordination needs

## Workflow Steps

- Apply @agent decorator to the class definition with a descriptive name
- Define __init__ method that accepts agent_id as a parameter
- Store agent_id as an instance attribute (self.agent_id)
- Ensure agent_id is accessible for downstream operations

## Constraints

- agent_id must be unique within the system scope
- agent_id attribute must be set during __init__
- Agent class must be decorated with @agent

## Output Contract

- Agent class instance with agent_id attribute set and accessible for downstream operations such as logging, tracing, and multi-agent coordination

## Example Executions

### Example 1

- Input: Create a ResearchSpecialistAgent with identifier 'researcher-alpha-007'
- Output: ResearchAgent instance with self.agent_id = 'researcher-alpha-007' accessible for tracing and coordination
- Notes: Agent_id persists across method calls and can be used by AgentOps for session tracking

## Triggers

- Need to create an agent with a unique identifier for logging, tracing, or multi-agent coordination
- Multi-agent workflow requires agent identity tracking
- Agent state management and persistence is required

## Examples

### Example 1

Input:

  Create a ResearchSpecialistAgent with identifier 'researcher-alpha-007'

Output:

  ResearchAgent instance with self.agent_id = 'researcher-alpha-007' accessible for tracing and coordination

Notes:

  Agent_id persists across method calls and can be used by AgentOps for session tracking
