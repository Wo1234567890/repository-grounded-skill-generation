---
id: "c31ddfb9-dade-537c-b1a5-7a488905160a"
name: "Notebook-Based Integration Testing for LLM Providers"
description: "Execute Jupyter notebooks as integration tests to verify end-to-end LLM provider functionality, real-world usage patterns, and API compatibility across multiple Python versions. Notebooks are located in examples/ directory, executed via CI workflow on PR merges and manual triggers, with provider API keys configured in GitHub Actions secrets."
version: "0.1.0"
tags:
  - "integration_testing"
  - "llm_providers"
  - "ci_cd"
  - "notebook_execution"
  - "api_verification"
triggers:
  - "Adding or updating LLM provider support"
  - "Running CI/CD on PR merges to main"
  - "Verifying provider API compatibility across Python versions"
---

# Notebook-Based Integration Testing for LLM Providers

Execute Jupyter notebooks as integration tests to verify end-to-end LLM provider functionality, real-world usage patterns, and API compatibility across multiple Python versions. Notebooks are located in examples/ directory, executed via CI workflow on PR merges and manual triggers, with provider API keys configured in GitHub Actions secrets.

## Prompt

Run Jupyter notebooks from the examples/ directory as CI integration tests. Each notebook should demonstrate provider capabilities including basic completion calls, streaming responses, async operations, error handling, and tool usage. Set up environment with provider API keys, install AgentOps from main branch, execute each notebook sequentially, and exclude notebooks requiring manual testing. Verify all notebooks pass across specified Python versions.

## Objective

Validate LLM provider integration through executable notebook tests
## Applicable Signals

- Pull request with changes to agentops/, examples/, or tests/ directories
- Manual workflow trigger
- New provider integration initiated

## Contraindications

- Testing internal unit logic without external API calls
- Debugging provider-specific bugs in isolation
- Manual exploratory testing without CI context

## Workflow Steps

- {'step': 1, 'action': 'Set up CI environment', 'details': 'Configure GitHub Actions workflow with provider API keys and Python version matrix'}
- {'step': 2, 'action': 'Install AgentOps', 'details': 'Install AgentOps package from main branch into test environment'}
- {'step': 3, 'action': 'Locate provider notebooks', 'details': 'Identify all notebooks in examples/ directory for target provider'}
- {'step': 4, 'action': 'Execute notebooks', 'details': 'Run each notebook sequentially, excluding those in manual-testing list'}
- {'step': 5, 'action': 'Verify execution success', 'details': 'Confirm all notebooks complete without errors across all Python versions'}

## Constraints

- Notebooks must be located in examples/ directory
- Each provider must have dedicated notebook subdirectory
- Provider API keys must be configured in GitHub Actions secrets
- Notebooks requiring manual testing must be added to exclude_notebooks list
- Tests run on PR merges and manual triggers only

## Cautions

- Ensure all provider API keys are securely stored in GitHub Actions secrets
- Notebooks requiring manual testing must be explicitly excluded to prevent CI failures
- Monitor API rate limits and costs when running tests against live LLM APIs

## Output Contract

- All provider notebooks execute successfully across specified Python versions; examples remain synchronized with current API behavior; CI workflow completes with pass/fail status for each notebook and Python version combination

## Triggers

- Adding or updating LLM provider support
- Running CI/CD on PR merges to main
- Verifying provider API compatibility across Python versions
