---
id: "ed255c75-c359-5a78-b92a-51cd0adcbe51"
name: "Provider Test Coverage Checklist"
description: "Structured checklist defining required test scenarios for each LLM provider integration: basic completion calls, streaming responses, async operations, error handling, and tool usage. Use when onboarding a new provider or reviewing test completeness."
version: "0.1.0"
tags:
  - "integration_testing"
  - "provider_onboarding"
  - "test_specification"
  - "ci_workflow"
  - "llm_provider"
triggers:
  - "Onboarding a new LLM provider"
  - "Reviewing provider test completeness before PR merge"
  - "Creating or updating example notebooks for a provider"
---

# Provider Test Coverage Checklist

Structured checklist defining required test scenarios for each LLM provider integration: basic completion calls, streaming responses, async operations, error handling, and tool usage. Use when onboarding a new provider or reviewing test completeness.

## Prompt

For the target LLM provider, verify that example notebooks in `examples/provider_name/` demonstrate all applicable functionality:
1. Basic completion calls
2. Streaming responses
3. Async operations (if supported)
4. Error handling
5. Tool usage (if applicable)

If a provider does not support a capability, document the exclusion and update the CI workflow `exclude_notebooks` list if manual testing is required.

## Objective

Ensure comprehensive test coverage for new LLM provider integrations
## Applicable Signals

- New provider integration initiated
- Provider documentation or API changes
- Test coverage gaps identified in CI

## Contraindications

- Provider does not support certain operations (e.g., streaming, async)
- Manual testing is preferred over automated notebook execution
- Provider requires interactive or real-time user input

## Workflow Steps

- {'step': 1, 'action': 'Create notebook directory', 'detail': 'Create `examples/provider_name/` directory structure'}
- {'step': 2, 'action': 'Implement basic completion test', 'detail': 'Add notebook demonstrating basic completion calls with the provider'}
- {'step': 3, 'action': 'Implement streaming test', 'detail': 'Add notebook demonstrating streaming responses (if supported)'}
- {'step': 4, 'action': 'Implement async operations test', 'detail': 'Add notebook demonstrating async operations (if supported)'}
- {'step': 5, 'action': 'Implement error handling test', 'detail': 'Add notebook demonstrating error handling and edge cases'}
- {'step': 6, 'action': 'Implement tool usage test', 'detail': 'Add notebook demonstrating tool usage (if applicable)'}
- {'step': 7, 'action': 'Configure CI workflow', 'detail': 'Add provider API keys to GitHub Actions secrets; update `test-notebooks.yml` if manual testing exclusion needed'}
- {'step': 8, 'action': 'Verify CI execution', 'detail': 'Ensure notebooks execute successfully on PR merge across multiple Python versions'}

## Constraints

- All required secrets and API keys must be added to GitHub Actions before CI execution
- Notebooks must be executable end-to-end against actual provider APIs
- Each provider should have a dedicated directory under `examples/`

## Cautions

- Notebooks must use actual provider APIs; mock responses are insufficient for integration testing
- Ensure API keys and secrets are never committed to repository; use GitHub Actions secrets only
- If a provider capability is not supported, explicitly document the exclusion in the notebook or workflow

## Output Contract

- Notebook(s) created in `examples/provider_name/` with all applicable provider functionality demonstrated
- Test scenarios documented
- CI workflow updated with provider secrets and exclusions if needed
- All notebooks pass execution on PR merge

## Triggers

- Onboarding a new LLM provider
- Reviewing provider test completeness before PR merge
- Creating or updating example notebooks for a provider
