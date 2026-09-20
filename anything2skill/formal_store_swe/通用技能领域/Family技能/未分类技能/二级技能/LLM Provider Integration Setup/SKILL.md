---
id: "76e58a88-1c48-588e-81d4-80c15486fe29"
name: "LLM Provider Integration Setup"
description: "Scaffold for implementing a new LLM provider by inheriting from BaseProvider, configuring provider metadata, and wiring required override/undo methods. Use when adding support for a new LLM service to the provider directory."
version: "0.1.0"
tags:
  - "provider_setup"
  - "class_inheritance"
  - "llm_integration"
  - "agentops"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Adding a new LLM provider to agentops/llms/"
  - "Provider client library is available and ready to wrap"
---

# LLM Provider Integration Setup

Scaffold for implementing a new LLM provider by inheriting from BaseProvider, configuring provider metadata, and wiring required override/undo methods. Use when adding support for a new LLM service to the provider directory.

## Prompt

Create a new provider class that inherits from BaseProvider. Decorate with @singleton. In __init__, call super().__init__(client) and set self._provider_name to the provider name. Implement handle_response() to process LLM responses, override() to patch provider methods, and undo_override() to restore original methods. Ensure the class tracks prompts, completions, token usage, timestamps, errors, and tool usage as applicable.

## Objective

Establish a new LLM provider integration following the BaseProvider contract
## Applicable Signals

- New provider support request
- Third-party LLM client library available

## Contraindications

- Modifying existing provider behavior
- Debugging provider runtime errors
- Handling provider-specific response parsing edge cases

## Workflow Steps

- {'step': 1, 'action': 'Create new provider class inheriting from BaseProvider', 'detail': 'Apply @singleton decorator; accept client parameter in __init__'}
- {'step': 2, 'action': 'Call super().__init__(client) and set _provider_name', 'detail': 'Store provider name as instance variable for identification'}
- {'step': 3, 'action': 'Implement handle_response() method', 'detail': 'Process LLM responses and extract prompts, completions, token usage, timestamps, errors'}
- {'step': 4, 'action': 'Implement override() method', 'detail': 'Patch provider client methods to intercept calls and capture events'}
- {'step': 5, 'action': 'Implement undo_override() method', 'detail': 'Restore original provider methods to clean state'}

## Constraints

- Provider client must be instantiable
- BaseProvider base class must be available in agentops/llms/
- Class must be decorated with @singleton

## Cautions

- Ensure @singleton decorator is applied to prevent multiple instances
- Verify all required methods are implemented before deployment
- Test override/undo_override cycle to confirm method restoration works

## Output Contract

- New provider class inheriting BaseProvider with __init__, handle_response, override, and undo_override methods fully implemented and ready for instantiation

## 子技能目录
- [Provider Method Override and Restoration](通用技能领域/Family技能/未分类技能/微技能/Provider Method Override and Restoration/SKILL.md) ｜ 适用：Micro operation to patch provider client methods for interception and restore original methods on cleanup. Enables transparent event capture without modifying provider source code.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Provider Method Override and Restoration` 时，优先调用它。 线索：Provider integration initialization, Enabling provider monitoring, provider_integration, method_interception, event_capture

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Adding a new LLM provider to agentops/llms/
- Provider client library is available and ready to wrap
