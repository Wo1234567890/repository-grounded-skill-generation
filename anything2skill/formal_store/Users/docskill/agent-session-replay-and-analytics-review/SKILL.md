---
id: "4472995e-bfe0-5508-9967-c340abbc67cc"
name: "Agent Session Replay and Analytics Review"
description: "Access and review recorded agent session replays and summary analytics via the AgentOps dashboard to identify and debug agent behavior issues."
version: "0.1.0"
tags:
  - "agent_debugging"
  - "observability"
  - "post_session"
  - "analytics"
  - "session_replay"
triggers:
  - "Session has completed and end_session() has been called"
  - "Need to understand agent behavior or identify execution failures"
  - "Performance optimization or debugging required"
---

# Agent Session Replay and Analytics Review

Access and review recorded agent session replays and summary analytics via the AgentOps dashboard to identify and debug agent behavior issues.

## Prompt

After your agent session completes, navigate to the AgentOps dashboard to load the session replay. Review the execution trace to identify agent behavior patterns, failures, or performance bottlenecks. Examine summary analytics to understand key metrics and outcomes.

## Objective

Inspect agent execution traces and performance metrics
## Applicable Signals

- Session closure confirmation
- Unexpected agent output or behavior
- Performance metrics need review

## Contraindications

- Session has not yet been closed
- No AgentOps dashboard access available
- Session data not yet synced to dashboard

## Workflow Steps

- Confirm session has been closed via end_session() call
- Navigate to AgentOps dashboard (https://app.agentops.ai)
- Locate and load the completed session replay
- Review execution trace and agent decision points
- Examine summary analytics for key metrics
- Document findings or performance issues identified

## Constraints

- AgentOps dashboard must be accessible
- Session must have been properly ended with end_session()
- User must have valid credentials for dashboard access

## Output Contract

- Session replay successfully loaded and displayed
- Summary analytics accessible
- Root cause of agent behavior identified or performance metric reviewed and documented

## Triggers

- Session has completed and end_session() has been called
- Need to understand agent behavior or identify execution failures
- Performance optimization or debugging required
