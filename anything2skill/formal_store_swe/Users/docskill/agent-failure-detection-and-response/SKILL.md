---
id: "89e1298d-2695-5e57-bf61-5348b993f97a"
name: "Agent Failure Detection and Response"
description: "Identify, classify, and respond to agent failures and multi-agent interaction issues in real time. Monitors live agent sessions for anomalies, errors, and unexpected behavior, then triggers appropriate escalation or remediation actions."
version: "0.1.0"
tags:
  - "agent_monitoring"
  - "failure_detection"
  - "real_time_response"
  - "multi_agent"
  - "observability"
triggers:
  - "Agent is running in production"
  - "Anomalies or errors detected in session telemetry"
  - "Unexpected agent behavior observed in live monitoring"
---

# Agent Failure Detection and Response

Identify, classify, and respond to agent failures and multi-agent interaction issues in real time. Monitors live agent sessions for anomalies, errors, and unexpected behavior, then triggers appropriate escalation or remediation actions.

## Prompt

When agent telemetry shows errors or anomalies during a live session: (1) Capture failure signals from session data; (2) Classify the failure type (e.g., API error, timeout, logic failure, multi-agent coordination issue); (3) Log the failure with context; (4) Trigger escalation or remediation based on severity and failure class.

## Objective

Detect and escalate agent failures before they impact end users
## Applicable Signals

- Session error logs
- API call failures
- Agent response timeouts
- Multi-agent interaction failures
- Metric threshold breaches

## Contraindications

- Agent is offline or not actively running
- Observability data is unavailable or disconnected
- Failure is already known and being manually handled by operator

## Workflow Steps

- {'step': 1, 'action': 'Monitor session telemetry for error signals', 'input': 'Live session data stream', 'output': 'Detected anomaly or error event'}
- {'step': 2, 'action': 'Classify failure type and severity', 'input': 'Error event with context (API call, timeout, logic failure, multi-agent issue)', 'output': 'Failure classification with severity level'}
- {'step': 3, 'action': 'Log failure with full context', 'input': 'Classified failure, session ID, timestamp, agent state', 'output': 'Failure record in observability system'}
- {'step': 4, 'action': 'Trigger escalation or remediation', 'input': 'Failure severity and type', 'output': 'Escalation action queued or remediation initiated'}

## Constraints

- Requires active session telemetry stream
- Failure classification must be deterministic and logged
- Escalation action must be triggered synchronously or queued reliably

## Cautions

- Do not escalate duplicate failures within a short time window without deduplication
- Ensure escalation routing is configured before enabling this skill

## Output Contract

- Failure is classified and logged with full context; appropriate escalation or remediation action is triggered and confirmed. Downstream caller receives failure record and escalation status.

## Triggers

- Agent is running in production
- Anomalies or errors detected in session telemetry
- Unexpected agent behavior observed in live monitoring
