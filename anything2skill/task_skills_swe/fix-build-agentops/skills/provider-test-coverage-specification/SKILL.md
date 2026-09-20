---
id: "2701a65b-9c0c-52ab-aaf8-3522378f0f0e"
name: "Provider Test Coverage Specification"
description: "Reference checklist defining required functionality demonstrations for LLM provider test notebooks. Specifies what capabilities each provider notebook must cover to ensure complete integration testing across basic completion, streaming, async operations, error handling, and tool usage."
version: "0.1.0"
tags:
  - "testing"
  - "provider_integration"
  - "coverage"
  - "reference"
  - "checklist"
triggers:
  - "Creating a new provider notebook"
  - "Reviewing provider test completeness"
  - "Onboarding new LLM integrations"
---

# Provider Test Coverage Specification

Reference checklist defining required functionality demonstrations for LLM provider test notebooks. Specifies what capabilities each provider notebook must cover to ensure complete integration testing across basic completion, streaming, async operations, error handling, and tool usage.

## Prompt

When authoring or reviewing an LLM provider notebook, verify that the notebook includes demonstrations of: (1) basic completion calls, (2) streaming responses, (3) async operations (if supported by provider), (4) error handling, and (5) tool usage (if applicable). Use this checklist during notebook creation and peer review to ensure consistent provider coverage.

## Objective

Define and track completeness criteria for provider test coverage
## Applicable Signals

- New provider integration initiated
- Provider notebook under peer review
- Test coverage audit in progress

## Contraindications

- Do not use during test execution
- Do not use for debugging failing test cases
- Do not use for CI/CD workflow management

## Constraints

- Checklist applies only to provider-specific notebooks in examples/ directory
- Async operations coverage is conditional on provider support
- Tool usage coverage is conditional on provider capability

## Output Contract

- Documented reference checklist of required provider capabilities (basic completion, streaming, async, error handling, tool usage) available for consultation during notebook authoring and review

## Triggers

- Creating a new provider notebook
- Reviewing provider test completeness
- Onboarding new LLM integrations
