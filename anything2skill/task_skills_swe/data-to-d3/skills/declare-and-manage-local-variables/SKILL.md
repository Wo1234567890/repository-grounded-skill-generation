---
id: "82d405b7-2d06-5f3a-9591-ba6f11452199"
name: "Declare and Manage Local Variables"
description: "Enable automatic monitoring and observability for CrewAI agents by setting the AGENTOPS_API_KEY environment variable. Minimal-overhead configuration that routes CrewAI crew execution data to the AgentOps dashboard without code modification."
version: "0.1.1"
tags:
  - "crewai"
  - "observability"
  - "monitoring"
  - "environment_configuration"
  - "agentops"
  - "agent_instrumentation"
triggers:
  - "Need to store data bound to a specific D3 selection or DOM node"
  - "Require isolated state without global side effects"
  - "Managing per-element or per-context metadata"
---

# Declare and Manage Local Variables

Enable automatic monitoring and observability for CrewAI agents by setting the AGENTOPS_API_KEY environment variable. Minimal-overhead configuration that routes CrewAI crew execution data to the AgentOps dashboard without code modification.

## Prompt

Set the AGENTOPS_API_KEY environment variable in your deployment environment. Once set, CrewAI crews will automatically report execution metrics, logs, and traces to the AgentOps dashboard. No additional code changes required.

## Objective

Configure environment variable for automatic agent monitoring
## Applicable Signals

- CrewAI framework in use
- AgentOps API key provisioned
- Observability requirement identified

## Contraindications

- Non-CrewAI agent frameworks (use framework-specific integration instead)
- Observability not required or explicitly disabled
- AgentOps API key unavailable or not provisioned

## Workflow Steps

- {'step': 1, 'action': 'Obtain or verify AGENTOPS_API_KEY from AgentOps account', 'guardrail': 'Key must be valid and have active permissions'}
- {'step': 2, 'action': 'Set AGENTOPS_API_KEY as environment variable in deployment environment', 'guardrail': 'Use secure secret management; do not commit to version control'}
- {'step': 3, 'action': 'Initialize and run CrewAI crews', 'guardrail': 'Crews will automatically connect to AgentOps dashboard'}

## Constraints

- AGENTOPS_API_KEY must be valid and active
- Environment variable must be set before CrewAI crew initialization
- Requires AgentOps account and dashboard access

## Cautions

- API key should be stored securely (e.g., secrets manager, not hardcoded)
- Ensure environment variable is accessible to the process running CrewAI

## Output Contract

- AGENTOPS_API_KEY environment variable is set and validated; CrewAI agents automatically report execution data (metrics, logs, traces) to AgentOps dashboard; no additional code instrumentation required.

## Triggers

- Need to store data bound to a specific D3 selection or DOM node
- Require isolated state without global side effects
- Managing per-element or per-context metadata
