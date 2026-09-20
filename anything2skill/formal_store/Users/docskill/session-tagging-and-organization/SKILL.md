---
id: "c299061d-6382-5b99-9763-d9808a27ec67"
name: "Session Tagging and Organization"
description: "A micro-skill for adding and managing tags during AgentOps session initialization or startup to organize, filter, and categorize sessions by environment, application type, or service tier."
version: "0.1.0"
tags:
  - "session_management"
  - "metadata"
  - "initialization"
  - "filtering"
  - "organization"
triggers:
  - "Starting a new AgentOps session"
  - "Initializing the AgentOps client"
  - "Need to label sessions for filtering or environment tracking"
---

# Session Tagging and Organization

A micro-skill for adding and managing tags during AgentOps session initialization or startup to organize, filter, and categorize sessions by environment, application type, or service tier.

## Prompt

When initializing or starting an AgentOps session, apply one or more tags to label the session for later filtering and organization. Tags can be added either during client initialization via agentops.init(tags=[...]) or when manually starting a session via agentops.start_session(tags=[...]). Choose tags that reflect the session's environment (e.g., 'production', 'staging'), application context (e.g., 'web-app', 'api'), or service tier (e.g., 'tier-1', 'customer-service').

## Objective

organize_and_filter_sessions
## Applicable Signals

- agentops.init() call is about to be made
- agentops.start_session() call is about to be made
- Session categorization or filtering requirement is identified

## Contraindications

- Session is already running and tags cannot be retroactively applied
- Tag schema is not yet defined by the team
- No filtering or organization requirement exists

## Workflow Steps

- Determine the appropriate tags for the session based on environment, application type, or service tier
- Pass tags as a list to either agentops.init(api_key="YOUR_API_KEY", tags=[...]) or agentops.start_session(tags=[...])
- Verify that tags are applied and visible in session metadata

## Constraints

- Tags must be applied at initialization or session start time
- Tags are passed as a list parameter to init() or start_session()
- Tag values should align with team-defined schema for consistency

## Cautions

- Tags cannot be added or modified after session initialization; plan tag strategy before calling init() or start_session()
- Ensure tag naming is consistent across sessions to enable effective filtering

## Output Contract

- Session is initialized or started with one or more tags applied; tags are visible in session metadata for filtering and organization.

## Triggers

- Starting a new AgentOps session
- Initializing the AgentOps client
- Need to label sessions for filtering or environment tracking
