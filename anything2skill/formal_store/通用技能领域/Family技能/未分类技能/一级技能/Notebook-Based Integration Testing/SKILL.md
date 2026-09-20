---
id: "ba2be65f-c4e9-52c2-8061-6bed1954ca14"
name: "Notebook-Based Integration Testing"
description: "Automated workflow to test LLM provider integrations using Jupyter notebooks as executable integration tests. Verifies real-world usage patterns and end-to-end functionality across multiple Python versions and actual LLM APIs."
version: "0.1.0"
tags:
  - "integration_testing"
  - "continuous_integration"
  - "llm_providers"
  - "jupyter_notebooks"
  - "ci_cd"
  - "automated_testing"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Adding or modifying LLM provider integrations"
  - "Running PR validation before merge to main"
  - "Ensuring example notebooks remain functional"
---

# Notebook-Based Integration Testing

Automated workflow to test LLM provider integrations using Jupyter notebooks as executable integration tests. Verifies real-world usage patterns and end-to-end functionality across multiple Python versions and actual LLM APIs.

## Prompt

Execute Jupyter notebooks from the examples/ directory as integration tests for LLM providers. Each notebook should demonstrate basic completion calls, streaming responses, async operations, error handling, and tool usage. Run notebooks via CI workflow on PR merges and manual triggers. Exclude notebooks requiring manual testing. Verify all notebooks execute without errors and validate examples against actual provider APIs.

## Objective

Validate LLM provider integrations through automated notebook execution across multiple Python versions
## Applicable Signals

- Adding or modifying LLM provider integrations
- Running PR validation before merge to main
- Ensuring example notebooks remain functional
- Verifying end-to-end provider functionality

## Contraindications

- Testing requires manual interaction or user input
- Provider API keys unavailable in CI environment
- Notebook contains non-deterministic outputs
- Provider does not support automated testing

## Workflow Steps

- {'step': 1, 'action': 'Organize notebooks', 'detail': 'Create notebook in examples/provider_name/ directory with all provider functionality demonstrated'}
- {'step': 2, 'action': 'Configure CI workflow', 'detail': 'Use test-notebooks.yml workflow; trigger on PR merges and manual events; set paths filter for agentops/**, examples/**, tests/**'}
- {'step': 3, 'action': 'Set up environment', 'detail': 'Add necessary provider API keys as GitHub Actions secrets; install AgentOps from main branch'}
- {'step': 4, 'action': 'Execute notebooks', 'detail': 'Run each notebook in sequence; test against multiple Python versions; exclude notebooks requiring manual testing'}
- {'step': 5, 'action': 'Validate coverage', 'detail': 'Ensure each provider notebook covers: basic completion calls, streaming responses, async operations (if supported), error handling, tool usage (if applicable)'}
- {'step': 6, 'action': 'Log and report results', 'detail': 'Capture execution logs; report pass/fail status; verify examples match actual LLM API behavior'}

## Constraints

- Notebooks must be located in examples/ directory
- CI workflow must run on PR merges to main and manual triggers
- All provider API keys must be configured in GitHub Actions secrets
- Non-deterministic notebooks must be explicitly excluded from automated runs
- AgentOps must be installed from main branch for testing

## Cautions

- API rate limits may affect test execution; consider batching or scheduling
- Notebook outputs must be deterministic or excluded to prevent flaky tests
- Manual testing notebooks must be explicitly marked in exclude_notebooks configuration
- Multiple Python version testing increases execution time; monitor CI performance

## Output Contract

- All notebooks execute without errors
- Test results are logged and reported
- Examples are verified to work against actual LLM APIs
- CI workflow completes with pass/fail status indicating integration health

## 子技能目录
- [LiteLLM Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LiteLLM Integration Setup/SKILL.md) ｜ 适用：Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ language models through a standardized Input/Output interface.
- [LLM Provider Integration Pattern](通用技能领域/Family技能/未分类技能/二级技能/LLM Provider Integration Pattern/SKILL.md) ｜ 适用：Establish a reusable provider class that inherits from BaseProvider, implements required LLM response handling methods, and manages event tracking for prompts, tokens, and errors.
- [Provider Test Coverage Checklist](通用技能领域/Family技能/未分类技能/二级技能/Provider Test Coverage Checklist/SKILL.md) ｜ 适用：Structured checklist defining required test scenarios for each LLM provider integration: basic completion calls, streaming responses, async operations, error handling, and tool usage. Use when onboarding a new provider or reviewing test completeness.

## 选用规则（二级技能目录）
- 当目标、阶段或方法更接近 `LiteLLM Integration Setup` 时，优先调用它。 线索：User needs to integrate multiple LLM providers into an agent system and wants unified API handling, llm, integration, litellm, multi-provider
- 当目标、阶段或方法更接近 `LLM Provider Integration Pattern` 时，优先调用它。 线索：Adding support for a new LLM provider, Extending existing provider functionality, Implementing provider-level integration with AgentOps, llm_integration, provider_pattern
- 当目标、阶段或方法更接近 `Provider Test Coverage Checklist` 时，优先调用它。 线索：Onboarding a new LLM provider, Reviewing provider test completeness before PR merge, Creating or updating example notebooks for a provider, integration_testing, provider_onboarding

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Adding or modifying LLM provider integrations
- Running PR validation before merge to main
- Ensuring example notebooks remain functional
