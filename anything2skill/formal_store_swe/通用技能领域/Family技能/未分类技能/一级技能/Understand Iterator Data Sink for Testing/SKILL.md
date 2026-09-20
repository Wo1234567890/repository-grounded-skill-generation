---
id: "deb40d3c-decc-5a9e-baca-1eb2d0b34ee1"
name: "Understand Iterator Data Sink for Testing"
description: "Reference schema for organizing agent execution activities into a six-level hierarchical span structure (SESSION → AGENT → WORKFLOW → OPERATION/TASK → LLM → TOOL). Use when designing tracing, logging, or debugging infrastructure for multi-level agent workflows."
version: "0.1.0"
tags:
  - "observability"
  - "tracing"
  - "agent_debugging"
  - "hierarchical_logging"
  - "execution_trace"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "collecting and inspecting DataStream results for validation"
  - "designing test assertions"
  - "debugging DataStream output"
examples:
  - input: "Need to collect and inspect DataStream results for validation"
    output: "Use myResult.collectAsync() to retrieve Iterator of results"
    notes: "Intended for test assertions and debugging inspection only"
---

# Understand Iterator Data Sink for Testing

Reference schema for organizing agent execution activities into a six-level hierarchical span structure (SESSION → AGENT → WORKFLOW → OPERATION/TASK → LLM → TOOL). Use when designing tracing, logging, or debugging infrastructure for multi-level agent workflows.

## Prompt

When building or extending agent observability systems, organize activities into the following hierarchical span levels:

1. SESSION: Root container for all activities in a single execution of your workflow
2. AGENT: Represents an autonomous entity with specialized capabilities
3. WORKFLOW: A logical grouping of related operations
4. OPERATION/TASK: A specific task or function performed by an agent
5. LLM: An interaction with a language model
6. TOOL: The use of a tool or API by an agent

Each level creates a complete trace of your agent's execution, enabling hierarchical debugging and observability.

## Objective

Define reusable span hierarchy for agent execution tracing
## Applicable Signals

- Need for hierarchical activity organization
- Multi-agent or multi-workflow execution context
- Requirement for complete execution tracing

## Contraindications

- Implementing flat-structure logging systems
- Working with non-hierarchical execution models
- Debugging single-function calls without agent context
- Systems without multi-level activity nesting

## Constraints

- Span hierarchy must maintain strict parent-child relationships
- Each span level must have clear invocation rules
- SESSION must be the root container for all activities

## Output Contract

- Documented span hierarchy schema with clear parent-child relationships, invocation rules for each level, and guidance for mapping agent execution activities to appropriate span types.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- collecting and inspecting DataStream results for validation
- designing test assertions
- debugging DataStream output

## Examples

### Example 1

Input:

  Need to collect and inspect DataStream results for validation

Output:

  Use myResult.collectAsync() to retrieve Iterator of results

Notes:

  Intended for test assertions and debugging inspection only
