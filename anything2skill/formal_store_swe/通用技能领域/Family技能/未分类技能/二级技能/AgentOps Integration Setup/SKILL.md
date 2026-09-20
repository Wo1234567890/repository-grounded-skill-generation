---
id: "1d4c22ad-24cd-57e6-ad62-07fdfdc66fb6"
name: "AgentOps Integration Setup"
description: "Scaffold for integrating AgentOps monitoring and debugging into AI/ML projects. Use when starting a new agent project or adding observability to an existing framework."
version: "0.1.0"
tags:
  - "observability"
  - "agent_monitoring"
  - "debugging"
  - "integration"
  - "setup"
  - "onboarding"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting new AI/ML agent project"
  - "Adding debugging or monitoring to existing codebase"
  - "Evaluating AgentOps capabilities for observability"
---

# AgentOps Integration Setup

Scaffold for integrating AgentOps monitoring and debugging into AI/ML projects. Use when starting a new agent project or adding observability to an existing framework.

## Prompt

Follow the provided example notebooks and Python scripts to initialize AgentOps client, configure logging, and verify that agent actions are being captured to the dashboard. Start with the example matching your framework (e.g., LangChain, AutoGen, custom agent), then adapt configuration to your codebase.

## Objective

Establish AgentOps integration with minimal configuration
## Applicable Signals

- Project requires agent action logging
- Need for centralized debugging dashboard
- Framework integration not yet attempted

## Contraindications

- AgentOps already integrated and operational
- Troubleshooting runtime errors in existing integration
- Modifying core agent logic unrelated to observability

## Workflow Steps

- Select example notebook or script matching your AI/ML framework
- Review example code and explanations
- Initialize AgentOps client with project credentials
- Configure logging for agent actions
- Run example or adapt to your codebase
- Verify agent actions appear in AgentOps dashboard

## Constraints

- Requires AgentOps library installed
- Requires valid API credentials or local setup
- Example framework must match project stack

## Cautions

- Ensure API credentials are securely stored, not hardcoded
- Test in development environment before production deployment
- Verify framework compatibility with AgentOps version

## Output Contract

- AgentOps client initialized and logging agent actions to dashboard; example notebook or script runs without integration errors; dashboard displays captured agent activity.

## 子技能目录
- [Fork and Clone Repository](通用技能领域/Family技能/未分类技能/微技能/Fork and Clone Repository/SKILL.md) ｜ 适用：Micro-skill for forking a GitHub repository and cloning it locally to establish a development workspace. Use when starting contribution or local development on a shared codebase.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Fork and Clone Repository` 时，优先调用它。 线索：beginning contribution workflow, need local editable copy, starting fresh development environment, git, repository

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting new AI/ML agent project
- Adding debugging or monitoring to existing codebase
- Evaluating AgentOps capabilities for observability
