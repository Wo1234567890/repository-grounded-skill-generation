---
id: "1e4849ca-a605-5714-9f0e-b6174e4ffece"
name: "Local Streaming Program Development and Debugging"
description: "Initialize and automatically record agent program executions as timestamped sessions in a monitoring dashboard with minimal setup overhead. Captures agent behavior data during live execution for post-run analysis and visualization."
version: "0.1.1"
tags:
  - "agent_monitoring"
  - "session_recording"
  - "execution_tracking"
  - "behavioral_visibility"
  - "dashboard_integration"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new Flink streaming program"
  - "Need to debug algorithm logic before cluster deployment"
  - "Want to set breakpoints in IDE for interactive debugging"
examples:
  - input: "Create a local environment and add a simple integer stream"
    output: "DataStream<Integer> myInts = env.fromElements(1, 2, 3, 4, 5); env.execute();"
    notes: "Basic setup for local testing with collection-based data source"
  - input: "Add a custom source and set a breakpoint in a map function"
    output: "Program pauses at breakpoint in IDE, allowing inspection of intermediate values"
    notes: "Interactive debugging workflow for algorithm validation"
---

# Local Streaming Program Development and Debugging

Initialize and automatically record agent program executions as timestamped sessions in a monitoring dashboard with minimal setup overhead. Captures agent behavior data during live execution for post-run analysis and visualization.

## Prompt

Set up agent execution recording by initializing the monitoring system with two lines of code. Each program execution will be automatically recorded as a session with timestamped traces and behavior metrics. Access recorded sessions and execution data through the dashboard.

## Objective

Capture and persist agent behavior data during program execution with minimal code overhead
## Applicable Signals

- Agent program initialization phase
- Live execution context available
- Dashboard access configured

## Contraindications

- Offline analysis or historical log replay without live agent execution
- Scenarios where agent execution is not actively running

## Workflow Steps

- Initialize monitoring system with minimal code setup
- Trigger automatic session creation on program execution start
- Record timestamped execution traces and agent behavior metrics throughout execution
- Persist session data to dashboard on execution completion

## Constraints

- Requires two-line initialization code in agent program
- Requires dashboard backend connectivity
- Session recording occurs only during active program execution

## Output Contract

- Session record created in dashboard containing timestamped execution trace, agent behavior metrics, and full execution history accessible for post-run analysis and visualization

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new Flink streaming program
- Need to debug algorithm logic before cluster deployment
- Want to set breakpoints in IDE for interactive debugging

## Examples

### Example 1

Input:

  Create a local environment and add a simple integer stream

Output:

  DataStream<Integer> myInts = env.fromElements(1, 2, 3, 4, 5); env.execute();

Notes:

  Basic setup for local testing with collection-based data source

### Example 2

Input:

  Add a custom source and set a breakpoint in a map function

Output:

  Program pauses at breakpoint in IDE, allowing inspection of intermediate values

Notes:

  Interactive debugging workflow for algorithm validation
