---
id: "6189c9e9-1481-5b41-b604-589a4a974263"
name: "Agent Session Observation via Dashboard"
description: "Execute an agent program and navigate to the AgentOps dashboard to observe real-time or post-run session activity. Use this to inspect agent behavior, logs, and outcomes after execution."
version: "0.1.0"
tags:
  - "agent_debugging"
  - "dashboard"
  - "session_inspection"
  - "post_execution_analysis"
  - "observability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Agent program execution has completed"
  - "Session logs and trace data are available in AgentOps backend"
  - "User needs to review agent behavior or validate execution outcomes"
---

# Agent Session Observation via Dashboard

Execute an agent program and navigate to the AgentOps dashboard to observe real-time or post-run session activity. Use this to inspect agent behavior, logs, and outcomes after execution.

## Prompt

After your agent program completes execution, AgentOps will print a clickable URL to the console. Visit that URL or navigate to the dashboard drilldown view to inspect the session trace, logs, and execution outcomes.

## Objective

Observe and inspect agent session execution results
## Applicable Signals

- Completion of agent run
- Console output contains clickable session URL
- Need for post-execution analysis or behavior inspection

## Contraindications

- Agent is still running; use real-time monitoring instead
- Debugging requires code-level inspection or local breakpoints
- Session data has not yet been persisted to backend

## Workflow Steps

- {'step': 1, 'action': 'Execute your agent program', 'detail': 'Run the agent code to completion'}
- {'step': 2, 'action': 'Retrieve session URL from console output', 'detail': 'AgentOps prints a clickable URL linking directly to your session'}
- {'step': 3, 'action': 'Navigate to dashboard', 'detail': 'Click the URL or visit app.agentops.ai/drilldown to access the session view'}
- {'step': 4, 'action': 'Inspect session trace and logs', 'detail': 'Review agent decisions, execution flow, and outcome summary in the dashboard'}

## Constraints

- Dashboard must be accessible at app.agentops.ai/drilldown
- Agent execution must have completed and logged to AgentOps
- User must have valid session URL or dashboard access credentials

## Cautions

- Ensure agent execution has fully completed before attempting to view session
- Session data may take a few moments to appear in the dashboard after execution

## Output Contract

- Dashboard session view loaded with agent execution trace, logs, and outcome summary visible and accessible for inspection

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent program execution has completed
- Session logs and trace data are available in AgentOps backend
- User needs to review agent behavior or validate execution outcomes
