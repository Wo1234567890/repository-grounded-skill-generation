---
id: "05a3f641-0650-5109-a0fe-7de1488c7127"
name: "Agent Performance Observability Setup"
description: "Configure and enable comprehensive observability for AI agents, including performance tracking, user interaction logging, and API usage monitoring. Establishes the foundational instrumentation and data collection layer required for downstream analysis, cost control, and failure detection."
version: "0.1.0"
tags:
  - "observability"
  - "monitoring"
  - "instrumentation"
  - "agent_systems"
  - "telemetry"
  - "performance_tracking"
triggers:
  - "Agent is being deployed to production"
  - "Observability gaps are identified in existing agent systems"
  - "New agent system requires visibility into performance and resource usage"
---

# Agent Performance Observability Setup

Configure and enable comprehensive observability for AI agents, including performance tracking, user interaction logging, and API usage monitoring. Establishes the foundational instrumentation and data collection layer required for downstream analysis, cost control, and failure detection.

## Prompt

Set up observability infrastructure for an AI agent system. Enable tracking of agent performance metrics, user interactions, and API usage. Ensure session replays, metrics dashboards, and live monitoring tools are accessible and actively collecting telemetry data.

## Objective

Enable full visibility into agent behavior and resource consumption through active telemetry collection
## Applicable Signals

- Production deployment initiated
- Agent system lacks performance visibility
- API usage tracking requirements identified

## Contraindications

- Agent is in early prototype phase with no external API calls
- Observability infrastructure is already fully configured and operational

## Workflow Steps

- Initialize observability framework for the agent system
- Configure performance metric collection (response times, success rates, resource usage)
- Enable user interaction logging and session tracking
- Set up API usage monitoring and call tracking
- Activate session replay and live monitoring tools
- Verify telemetry pipeline is receiving and processing data

## Constraints

- Observability setup must precede cost control and failure detection workflows
- Telemetry pipeline must be active before metrics dashboards can function
- Session replay capability requires baseline instrumentation

## Cautions

- Ensure telemetry collection does not introduce unacceptable latency to agent operations
- Verify data retention policies comply with privacy and compliance requirements

## Output Contract

- Agent telemetry pipeline active; session replays, metrics dashboards, and live monitoring tools accessible and collecting data. Observability infrastructure ready for downstream cost control and failure detection workflows.

## Triggers

- Agent is being deployed to production
- Observability gaps are identified in existing agent systems
- New agent system requires visibility into performance and resource usage
