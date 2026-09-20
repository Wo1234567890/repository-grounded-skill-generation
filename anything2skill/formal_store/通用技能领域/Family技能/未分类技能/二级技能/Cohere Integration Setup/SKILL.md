---
id: "e348baa7-f030-5c38-acb6-06f039b49a40"
name: "Cohere Integration Setup"
description: "Install and configure AgentOps with Cohere (>=5.4.0) to enable agent monitoring and observability for Cohere-based LLM applications."
version: "0.1.0"
tags:
  - "integration"
  - "cohere"
  - "agentops"
  - "monitoring"
  - "observability"
  - "llm"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new Cohere-based agent project"
  - "Adding AgentOps observability to an existing Cohere application"
---

# Cohere Integration Setup

Install and configure AgentOps with Cohere (>=5.4.0) to enable agent monitoring and observability for Cohere-based LLM applications.

## Prompt

To set up AgentOps with Cohere: (1) Verify Cohere version is 5.4.0 or higher. (2) Install AgentOps library. (3) Initialize AgentOps with Cohere client. (4) Verify agent calls are logged to AgentOps dashboard. Refer to official AgentOps Cohere integration documentation and Cohere API reference for detailed configuration steps.

## Objective

enable_cohere_monitoring
## Applicable Signals

- Project uses Cohere LLM
- Cohere version >= 5.4.0 available
- Monitoring and observability required

## Contraindications

- Cohere version below 5.4.0
- Project does not use Cohere LLM
- Monitoring is not required or not permitted

## Workflow Steps

- Verify Cohere version meets minimum requirement (>= 5.4.0)
- Install or update AgentOps library
- Initialize AgentOps with Cohere client configuration
- Test agent call logging to AgentOps dashboard
- Confirm observability data is visible in dashboard

## Constraints

- Cohere library version must be >= 5.4.0
- AgentOps library must be installed and compatible
- Network access to AgentOps dashboard required for logging

## Cautions

- This is a living integration; check Discord or official documentation for latest updates or required functionality additions.

## Output Contract

- AgentOps successfully initialized with Cohere
- Agent calls are logged and visible in AgentOps dashboard

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new Cohere-based agent project
- Adding AgentOps observability to an existing Cohere application
