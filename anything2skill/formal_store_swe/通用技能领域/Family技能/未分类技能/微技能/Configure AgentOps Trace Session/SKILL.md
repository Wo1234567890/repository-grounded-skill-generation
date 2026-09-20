---
id: "240df21b-51fb-5f43-b991-0845a46f49cb"
name: "Configure AgentOps Trace Session"
description: "Set up an AgentOps trace session with custom trace name and metadata tags to enable monitoring and debugging of agent execution."
version: "0.1.0"
tags:
  - "agentops"
  - "tracing"
  - "debugging"
  - "instrumentation"
  - "metadata"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Initializing AgentOps for an agent workflow"
  - "Need to label and categorize execution traces for debugging or analytics"
  - "Starting a new instrumented agent session"
examples:
  - input: "{'trace_name': 'OpenAI Sync Example', 'tags': ['openai-sync-example', 'openai', 'agentops-example']}"
    output: "tracer object ready to log agent operations"
    notes: "Typical setup for OpenAI-based agent workflow"
---

# Configure AgentOps Trace Session

Set up an AgentOps trace session with custom trace name and metadata tags to enable monitoring and debugging of agent execution.

## Prompt

Call agentops.start_trace() with a descriptive trace_name and relevant tags array. The trace_name should identify the workflow or agent type; tags should categorize execution context (e.g., model type, execution mode, example identifier). Return the tracer object for downstream operation capture.

## Objective

Create and configure a named trace session with contextual metadata
## Applicable Signals

- agentops client initialized
- agent workflow entry point reached
- trace metadata requirements defined

## Contraindications

- Tracing is disabled or not required
- Trace session already active
- Running in a non-instrumented environment

## Workflow Steps

- Prepare trace_name string identifying the workflow or agent type
- Prepare tags list with relevant context labels (e.g., model, mode, example)
- Call agentops.start_trace(trace_name=<name>, tags=<tags>)
- Capture and return the tracer object

## Constraints

- agentops client must be initialized before calling start_trace()
- trace_name must be a non-empty string
- tags must be a list of strings

## Output Contract

- Tracer object created with specified trace_name and tags; ready to capture agent operations downstream

## Example Executions

### Example 1

- Input: {'trace_name': 'OpenAI Sync Example', 'tags': ['openai-sync-example', 'openai', 'agentops-example']}
- Output: tracer object ready to log agent operations
- Notes: Typical setup for OpenAI-based agent workflow

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Initializing AgentOps for an agent workflow
- Need to label and categorize execution traces for debugging or analytics
- Starting a new instrumented agent session

## Examples

### Example 1

Input:

  {'trace_name': 'OpenAI Sync Example', 'tags': ['openai-sync-example', 'openai', 'agentops-example']}

Output:

  tracer object ready to log agent operations

Notes:

  Typical setup for OpenAI-based agent workflow
