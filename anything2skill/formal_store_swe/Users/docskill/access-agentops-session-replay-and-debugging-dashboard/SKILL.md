---
id: "e1db9d1b-0823-5bf4-bffc-b9854a4b0b96"
name: "Access AgentOps Session Replay and Debugging Dashboard"
description: "Retrieve and review recorded agent session execution history, decision logs, and summary analytics through the AgentOps dashboard for post-execution analysis and troubleshooting."
version: "0.1.0"
tags:
  - "debugging"
  - "observability"
  - "session_analysis"
  - "post_execution"
  - "agent_inspection"
triggers:
  - "Investigating agent behavior anomalies, understanding decision paths, or validating agent outputs after session completion"
---

# Access AgentOps Session Replay and Debugging Dashboard

Retrieve and review recorded agent session execution history, decision logs, and summary analytics through the AgentOps dashboard for post-execution analysis and troubleshooting.

## Prompt

After a session has been terminated with agentops.end_session(), navigate to the AgentOps dashboard to view the recorded session replay. Use the dashboard to inspect execution traces, decision logs, and summary analytics to understand agent behavior and troubleshoot issues.

## Objective

Retrieve and review agent session execution history and debug information
## Applicable Signals

- Session has been terminated with end_session() call
- Need to investigate agent behavior anomalies
- Need to understand agent decision paths
- Need to validate agent outputs after execution

## Contraindications

- Session has not yet been terminated
- Dashboard credentials are not configured
- Session data has not been persisted to the dashboard

## Workflow Steps

- Ensure session has been terminated with agentops.end_session()
- Navigate to https://app.agentops.ai
- Authenticate with AgentOps account credentials
- Locate and select the target session from the dashboard
- Review execution traces, decision logs, and summary analytics

## Constraints

- Requires active AgentOps account and dashboard access
- Session must be explicitly ended before replay is available
- Dashboard URL is https://app.agentops.ai

## Output Contract

- Session replay loaded in dashboard; execution trace, decision logs, and summary analytics visible and navigable for inspection and analysis

## Triggers

- Investigating agent behavior anomalies, understanding decision paths, or validating agent outputs after session completion
