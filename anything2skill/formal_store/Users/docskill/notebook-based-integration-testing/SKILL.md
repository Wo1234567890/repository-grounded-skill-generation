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

## Triggers

- Adding or modifying LLM provider integrations
- Running PR validation before merge to main
- Ensuring example notebooks remain functional
