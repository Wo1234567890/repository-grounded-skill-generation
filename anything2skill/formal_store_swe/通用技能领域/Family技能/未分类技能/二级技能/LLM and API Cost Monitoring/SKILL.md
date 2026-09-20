---
id: "fd8ec31f-9dc9-5b5e-997b-2b59db376255"
name: "LLM and API Cost Monitoring"
description: "Track and manage spending on LLM and API calls to prevent budget overruns and optimize resource allocation. Provides real-time cost metrics, spending alerts, and budget guardrails for agent sessions."
version: "0.1.0"
tags:
  - "cost_control"
  - "budget_management"
  - "observability"
  - "financial_metrics"
  - "agent_monitoring"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Agent makes frequent LLM or API calls; budget constraints exist; cost optimization is required"
---

# LLM and API Cost Monitoring

Track and manage spending on LLM and API calls to prevent budget overruns and optimize resource allocation. Provides real-time cost metrics, spending alerts, and budget guardrails for agent sessions.

## Prompt

Monitor cumulative spend across all LLM and external API calls within an agent session. Collect cost data per call, aggregate by service/model, and trigger alerts when spending approaches or exceeds configured thresholds. Maintain a cost metrics dashboard and provide spending pattern analysis for optimization.

## Objective

Monitor and control cumulative spend across LLM and external API calls
## Applicable Signals

- Agent makes frequent LLM or API calls
- Budget constraints are defined
- Cost optimization is a stated priority
- Session begins with cost tracking enabled

## Contraindications

- Agent has no external API dependencies
- Cost is not a constraint or concern
- Budget tracking is disabled or not configured

## Workflow Steps

- Initialize cost tracking context with budget limits and alert thresholds
- Capture cost metadata for each LLM call (model, tokens, latency, price per unit)
- Capture cost metadata for each external API call (endpoint, request size, response size, pricing tier)
- Aggregate costs by service, model, and time window
- Compare cumulative spend against configured budget limits
- Trigger spending alerts when thresholds are approached or exceeded
- Populate cost metrics dashboard with real-time and historical data
- Provide spending pattern analysis and optimization recommendations at session end

## Constraints

- Cost data must be collected at call time; retroactive cost assignment is not supported
- Budget limits and alert thresholds must be configured before session start
- Cost tracking requires access to pricing metadata for all integrated services

## Cautions

- Ensure pricing data is current; outdated rates may lead to inaccurate cost projections
- Alert thresholds should be set conservatively to allow time for corrective action
- Cost metrics are session-scoped; cross-session budget analysis requires external aggregation

## Output Contract

- Cost metrics dashboard populated with per-call, per-service, and cumulative spend data; spending alerts configured and active; session cost summary with breakdown by service and model provided at completion

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent makes frequent LLM or API calls; budget constraints exist; cost optimization is required
