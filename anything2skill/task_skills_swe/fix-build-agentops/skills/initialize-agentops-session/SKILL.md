---
id: "0fc63f00-75b2-5224-9651-74825cf60b50"
name: "Initialize AgentOps Session"
description: "Create and configure a new observability session for agent interaction tracking using the AgentOps init function. Establishes OpenTelemetry context and session ID for telemetry collection."
version: "0.1.0"
tags:
  - "observability"
  - "initialization"
  - "telemetry"
  - "session_management"
  - "agentops"
triggers:
  - "Agent application startup"
  - "New user interaction begins"
  - "Observability instrumentation required"
---

# Initialize AgentOps Session

Create and configure a new observability session for agent interaction tracking using the AgentOps init function. Establishes OpenTelemetry context and session ID for telemetry collection.

## Prompt

Call the AgentOps init function at agent application startup or when a new user interaction begins. This automatically creates a session object and establishes OpenTelemetry instrumentation context for collecting, processing, and exporting telemetry data.

## Objective

Initialize session context for telemetry collection
## Applicable Signals

- Application initialization phase
- User session start event
- Telemetry collection enabled

## Contraindications

- Session already active
- Offline mode required
- Telemetry disabled by policy

## Workflow Steps

- Import agentops module
- Call init function
- Capture returned session object
- Verify session ID and OpenTelemetry context established

## Constraints

- Must be called before agent operations begin
- Requires OpenTelemetry standard compliance

## Output Contract

- Active session object with unique session ID and OpenTelemetry context established; ready for downstream telemetry collection

## Triggers

- Agent application startup
- New user interaction begins
- Observability instrumentation required
