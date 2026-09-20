---
id: "89c79e01-e6e8-5d05-acf6-f6fec8b4f794"
name: "Trace and Tag Workflow Execution"
description: "Decorator-based pattern to wrap a workflow function with execution tracing, naming, and semantic tags for observability and workflow discovery."
version: "0.1.0"
tags:
  - "workflow"
  - "tracing"
  - "observability"
  - "instrumentation"
  - "decorator"
  - "metadata"
triggers:
  - "Defining a reusable workflow that spans multiple agent operations"
  - "Need for observability, replay, or semantic categorization of workflow execution"
  - "Workflow involves coordinated multi-step operations requiring traceability"
examples:
  - input: "Workflow function `run_full_research_workflow(topic: str)` with multiple agent research steps"
    output: "Function decorated with @trace(name=\"FullResearchWorkflow\", tags=[\"research\", \"analysis\", \"example\"]) emits execution trace with workflow name and semantic tags"
    notes: "Tags enable discovery and filtering of research-related workflows in observability systems"
---

# Trace and Tag Workflow Execution

Decorator-based pattern to wrap a workflow function with execution tracing, naming, and semantic tags for observability and workflow discovery.

## Prompt

Use the @trace decorator to instrument a multi-step workflow function. Provide a descriptive name and a list of semantic tags that categorize the workflow. The decorator will automatically capture execution events, timing, and context for later analysis or replay.

## Objective

Instrument a multi-step workflow with tracing and metadata for observability and replay
## Applicable Signals

- Workflow function definition with multiple sequential or parallel operations
- Requirement to track execution flow and timing across workflow stages
- Need to categorize or discover workflows by semantic tags

## Contraindications

- Single atomic operation without multi-step composition
- No observability or replay requirement
- Workflow is one-off or internal with no reuse intent

## Workflow Steps

- Define the workflow function with clear input and output signatures
- Apply @trace decorator with a descriptive name parameter
- Provide a list of semantic tags that categorize the workflow domain and purpose
- Ensure the decorated function calls agent operations or other instrumented components
- Verify that execution events are captured and logged by the tracing system

## Constraints

- Workflow function must be well-defined and callable
- Tags should be semantically meaningful and consistent across similar workflows
- Trace decorator must be applied at the function definition level

## Cautions

- Tag names should be consistent across workflows to enable effective filtering and discovery
- Trace overhead may impact performance for very high-frequency workflows; monitor accordingly
- Ensure downstream systems can consume and process the emitted trace events

## Output Contract

- Workflow function wrapped with trace context; execution events logged with name and tags for later analysis or replay. Caller receives a callable workflow that automatically emits observability data.

## Example Executions

### Example 1

- Input: Workflow function `run_full_research_workflow(topic: str)` with multiple agent research steps
- Output: Function decorated with @trace(name="FullResearchWorkflow", tags=["research", "analysis", "example"]) emits execution trace with workflow name and semantic tags
- Notes: Tags enable discovery and filtering of research-related workflows in observability systems

## Triggers

- Defining a reusable workflow that spans multiple agent operations
- Need for observability, replay, or semantic categorization of workflow execution
- Workflow involves coordinated multi-step operations requiring traceability

## Examples

### Example 1

Input:

  Workflow function `run_full_research_workflow(topic: str)` with multiple agent research steps

Output:

  Function decorated with @trace(name="FullResearchWorkflow", tags=["research", "analysis", "example"]) emits execution trace with workflow name and semantic tags

Notes:

  Tags enable discovery and filtering of research-related workflows in observability systems
