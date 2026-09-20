---
id: "7c32f9a3-248f-5476-b184-3b15af1891d9"
name: "Workflow Tracing and Tagging"
description: "Wrap a multi-step workflow function with the @trace decorator to enable end-to-end logging, tagging, and observability across agent and tool calls."
version: "0.1.0"
tags:
  - "workflow"
  - "instrumentation"
  - "observability"
  - "tracing"
  - "debugging"
  - "decorator_pattern"
triggers:
  - "Defining a multi-phase workflow that involves multiple agents or tools"
  - "Requirement for end-to-end tracing and categorization across workflow steps"
  - "Need to capture and log nested agent and tool calls"
---

# Workflow Tracing and Tagging

Wrap a multi-step workflow function with the @trace decorator to enable end-to-end logging, tagging, and observability across agent and tool calls.

## Prompt

Apply the @trace decorator to a workflow function, specifying a descriptive name and relevant tags. The decorator will automatically capture all nested agent and tool calls within the workflow, enabling end-to-end observability and debugging.

## Objective

Instrument a complete workflow for observability and debugging
## Applicable Signals

- Workflow function with multiple sequential or parallel steps
- Multiple agent or tool invocations within a single workflow
- Debugging or observability requirements

## Contraindications

- Workflow is simple or single-step
- Observability is not required
- Minimal or no nested agent/tool calls

## Workflow Steps

- Define or identify the multi-step workflow function
- Apply @trace decorator with name parameter (descriptive workflow identifier)
- Add tags parameter as a list of relevant category strings (e.g., ["research", "analysis"])
- Ensure all nested agent and tool calls are properly decorated
- Execute the workflow and verify trace metadata is captured in logs

## Constraints

- Workflow function must be defined before decoration
- All nested agents and tools must be properly instrumented with @agent and @tool decorators
- Tags should be semantically meaningful for filtering and categorization

## Cautions

- Tag names should be consistent across workflows for effective filtering
- Trace decorator overhead is minimal but should be considered for performance-critical workflows
- Ensure downstream observability system is configured to receive and store trace data

## Output Contract

- Workflow execution is logged with trace metadata (name, tags) and all nested agent/tool calls are captured in observability system

## Triggers

- Defining a multi-phase workflow that involves multiple agents or tools
- Requirement for end-to-end tracing and categorization across workflow steps
- Need to capture and log nested agent and tool calls
