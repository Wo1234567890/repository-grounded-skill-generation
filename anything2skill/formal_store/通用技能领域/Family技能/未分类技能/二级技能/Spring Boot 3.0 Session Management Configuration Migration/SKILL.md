---
id: "1072ee5f-187b-592e-af1b-3cab89353e55"
name: "Spring Boot 3.0 Session Management Configuration Migration"
description: "Initialize and manage an AgentOps session for a single user interaction with an agent. Automatically creates a session context when the init function is called, enabling telemetry collection and tracking throughout the interaction."
version: "0.1.1"
tags:
  - "agent_observability"
  - "session_management"
  - "telemetry"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Application uses Spring Session requiring Spring Boot 3.0 updates"
---

# Spring Boot 3.0 Session Management Configuration Migration

Initialize and manage an AgentOps session for a single user interaction with an agent. Automatically creates a session context when the init function is called, enabling telemetry collection and tracking throughout the interaction.

## Prompt

Call the AgentOps init function to create a session. A session represents a single user interaction with your agent and automatically establishes telemetry collection boundaries. The session object is created and ready to receive observability events.

## Objective

Set up and maintain a bounded session context for agent observability
## Applicable Signals

- User initiates interaction with agent
- New agent deployment or restart
- Telemetry collection required for interaction tracking

## Contraindications

- Session already active for current interaction
- No agent interaction required
- Telemetry disabled by organizational policy

## Intervention Moves

- Invoke init function to create session
- Capture returned session object
- Ensure session remains active throughout interaction lifecycle

## Workflow Steps

- {'step': 1, 'action': 'Import agentops module', 'detail': 'Ensure agentops library is available in execution environment'}
- {'step': 2, 'action': 'Call init function', 'detail': 'Invoke agentops.init() to create and activate session'}
- {'step': 3, 'action': 'Capture session object', 'detail': 'Store returned session reference for lifecycle management'}
- {'step': 4, 'action': 'Proceed with agent interaction', 'detail': 'Execute agent logic with active session context'}

## Constraints

- Session must be initialized before telemetry events are collected
- One session per discrete user interaction
- Session context must remain in scope during agent operation

## Cautions

- Ensure session is properly closed or cleaned up after interaction completes
- Do not reinitialize session for same interaction

## Output Contract

- Active session object with unique session ID; telemetry collection enabled and ready to receive events; session context available for downstream observability operations

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Application uses Spring Session requiring Spring Boot 3.0 updates
