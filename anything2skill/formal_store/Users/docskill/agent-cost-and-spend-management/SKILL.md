---
id: "aff6e491-a33a-54b2-85f3-d6032a265023"
name: "Agent Cost and Spend Management"
description: "Monitor and control spending on LLM and API calls to optimize agent operational costs and prevent budget overruns."
version: "0.1.0"
tags:
  - "cost_control"
  - "budget_management"
  - "spend_tracking"
  - "agent_monitoring"
  - "production_operations"
triggers:
  - "agent deployed to production"
  - "agent scaling to handle increased load"
  - "budget constraints or cost control requirements identified"
  - "need to track spend per session or per API call"
---

# Agent Cost and Spend Management

Monitor and control spending on LLM and API calls to optimize agent operational costs and prevent budget overruns.

## Prompt

Set up cost tracking for your agent's LLM and API calls. Configure spend limits and thresholds. Monitor actual spend against budget in real time. Generate alerts when spending approaches or exceeds defined thresholds. Use cost dashboards to identify expensive operations and optimize call patterns.

## Objective

manage_agent_costs
## Applicable Signals

- production deployment status
- budget allocation or spending limits defined
- cost visibility requirement stated
- multi-agent or high-volume API usage pattern

## Contraindications

- cost is not a constraint or concern
- agent is in early prototype phase with no budget limits
- no spending thresholds or budget caps defined

## Workflow Steps

- Configure cost tracking for all LLM and API calls
- Define budget limits and spending thresholds
- Enable real-time spend monitoring and aggregation
- Set up alerts for threshold breaches
- Generate cost dashboards showing spend per session and per call
- Review and optimize high-cost operations

## Constraints

- requires integration with LLM and API call tracking systems
- thresholds and budget limits must be configured before monitoring begins
- cost data must be collected and aggregated per session and per call

## Cautions

- alerts should trigger before budget is fully exhausted to allow corrective action
- cost tracking overhead should not significantly impact agent performance

## Output Contract

- Cost dashboard displaying spend per session, spend per API call, budget utilization percentage, and alerts triggered when spending approaches or exceeds defined thresholds. Actionable insights on which operations or calls are most expensive.

## Triggers

- agent deployed to production
- agent scaling to handle increased load
- budget constraints or cost control requirements identified
- need to track spend per session or per API call
