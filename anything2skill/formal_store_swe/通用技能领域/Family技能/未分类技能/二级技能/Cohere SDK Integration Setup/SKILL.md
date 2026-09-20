---
id: "bb292af1-9249-5d0a-b61e-8d183ccd9280"
name: "Cohere SDK Integration Setup"
description: "Install and configure AgentOps with Cohere SDK (version >=5.4.0) to enable agent monitoring and observability for Cohere-based applications."
version: "0.1.0"
tags:
  - "integration"
  - "cohere"
  - "agentops"
  - "observability"
  - "monitoring"
  - "sdk_setup"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new Cohere-based agent project"
  - "Adding AgentOps monitoring to an existing Cohere application"
---

# Cohere SDK Integration Setup

Install and configure AgentOps with Cohere SDK (version >=5.4.0) to enable agent monitoring and observability for Cohere-based applications.

## Prompt

Set up AgentOps integration with Cohere SDK to enable agent session logging and observability. Ensure Cohere SDK version is >=5.4.0 before proceeding. Follow official AgentOps and Cohere documentation for configuration steps.

## Objective

Enable Cohere agent observability via AgentOps
## Applicable Signals

- Cohere SDK dependency declared in project
- Agent session initialization required
- Observability and monitoring needed for Cohere agents

## Contraindications

- Cohere SDK version below 5.4.0
- Integration not yet available for specific use case

## Workflow Steps

- Verify Cohere SDK version is >=5.4.0
- Install AgentOps library
- Configure AgentOps with Cohere SDK credentials and settings
- Initialize AgentOps in Cohere agent code
- Verify agent sessions are logged and visible in AgentOps dashboard

## Constraints

- Cohere SDK version must be >=5.4.0
- AgentOps library must be installed and compatible

## Cautions

- This is a living integration; functionality may evolve; check Discord or official channels for updates

## Output Contract

- AgentOps successfully initialized and connected to Cohere SDK; agent sessions are logged and visible in AgentOps dashboard

## 子技能目录
- [Declare and Manage Local Variables](通用技能领域/Family技能/未分类技能/微技能/Declare and Manage Local Variables/SKILL.md) ｜ 适用：Enable automatic monitoring and observability for CrewAI agents by setting the AGENTOPS_API_KEY environment variable. Minimal-overhead configuration that routes CrewAI crew execution data to the AgentOps dashboard without code modification.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Declare and Manage Local Variables` 时，优先调用它。 线索：Need to store data bound to a specific D3 selection or DOM node, Require isolated state without global side effects, Managing per-element or per-context metadata, crewai, observability

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new Cohere-based agent project
- Adding AgentOps monitoring to an existing Cohere application
