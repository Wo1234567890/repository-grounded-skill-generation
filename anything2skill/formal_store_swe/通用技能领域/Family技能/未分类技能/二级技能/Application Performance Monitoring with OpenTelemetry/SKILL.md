---
id: "07935192-6a9c-5de5-a763-07352cabd2fb"
name: "Application Performance Monitoring with OpenTelemetry"
description: "Choose and apply the appropriate test category (unit, integration, end-to-end, or performance) based on the scope and objective of the component or workflow being validated. This skill routes test design decisions to the correct category before fixture setup and data organization."
version: "0.1.0"
tags:
  - "testing"
  - "test_planning"
  - "test_strategy"
  - "routing"
  - "classification"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "application requires production monitoring and observability"
  - "distributed tracing across services is needed"
  - "compliance or audit requirements mandate telemetry collection"
  - "performance degradation or error patterns need investigation"
examples:
  - input: "Testing a single authentication function for correct token validation"
    output: "Unit test category selected; rationale: individual component validation with no external dependencies"
    notes: "Scope is narrow; objective is correctness of a single unit"
  - input: "Testing interaction between API client and database layer when fetching user records"
    output: "Integration test category selected; rationale: validates correct interaction between two components"
    notes: "Scope spans multiple components; objective is correctness of their interaction"
  - input: "Testing complete user registration workflow from form submission to confirmation email"
    output: "End-to-end test category selected; rationale: validates complete workflow across multiple systems"
    notes: "Scope is entire workflow; objective is correctness of full user journey"
---

# Application Performance Monitoring with OpenTelemetry

Choose and apply the appropriate test category (unit, integration, end-to-end, or performance) based on the scope and objective of the component or workflow being validated. This skill routes test design decisions to the correct category before fixture setup and data organization.

## Prompt

Evaluate the scope and objective of the component or workflow to be tested. Determine whether the test should focus on individual components (unit), component interactions (integration), complete workflows (end-to-end), or system performance (performance). Document the rationale for the category selection.

## Objective

Route test design to the correct test category
## Applicable Signals

- Test scope is undefined
- Resource allocation for testing is pending
- Component or workflow validation is required

## Contraindications

- Test execution is already underway
- Fixtures and test data are already configured
- Test category has already been assigned and approved

## Workflow Steps

- {'step': 1, 'action': 'Assess the scope of the component or workflow', 'detail': 'Determine whether the target is a single component, multiple interacting components, a complete workflow, or system-wide performance'}
- {'step': 2, 'action': 'Evaluate the testing objective', 'detail': 'Clarify whether the goal is correctness of individual units, correctness of interactions, end-to-end behavior, or performance characteristics'}
- {'step': 3, 'action': 'Map scope and objective to test category', 'detail': 'Unit tests for individual components; integration tests for component interactions; end-to-end tests for complete workflows; performance tests for response times and resource usage'}
- {'step': 4, 'action': 'Document category assignment with rationale', 'detail': 'Record the selected category and explain why it is appropriate for the given scope and objective'}

## Constraints

- Decision must precede fixture setup
- Decision must precede test data organization
- Rationale must be documented for downstream teams

## Cautions

- A single component or workflow may require multiple test categories; this skill selects the primary category for the current test phase
- Category selection is a planning decision and does not execute tests

## Output Contract

- Clear test category assignment (unit, integration, end-to-end, or performance) with documented rationale explaining why the selected category is appropriate for the component or workflow scope and testing objective

## Example Executions

### Example 1

- Input: Testing a single authentication function for correct token validation
- Output: Unit test category selected; rationale: individual component validation with no external dependencies
- Notes: Scope is narrow; objective is correctness of a single unit

### Example 2

- Input: Testing interaction between API client and database layer when fetching user records
- Output: Integration test category selected; rationale: validates correct interaction between two components
- Notes: Scope spans multiple components; objective is correctness of their interaction

### Example 3

- Input: Testing complete user registration workflow from form submission to confirmation email
- Output: End-to-end test category selected; rationale: validates complete workflow across multiple systems
- Notes: Scope is entire workflow; objective is correctness of full user journey

## 子技能目录
- [Implement Contextual Error Logging](通用技能领域/Family技能/未分类技能/微技能/Implement Contextual Error Logging/SKILL.md) ｜ 适用：Implement specific exception types with meaningful error messages and contextual logging to ensure errors are logged with sufficient context for debugging and production issue resolution.
- [Record and Replay HTTP Interactions with pytest-vcr](通用技能领域/Family技能/未分类技能/微技能/Record and Replay HTTP Interactions with pytest-vcr/SKILL.md) ｜ 适用：Use pytest-vcr to record HTTP requests and responses during test execution, then replay them in subsequent runs to avoid external API calls. Enables deterministic, fast test runs by isolating tests from external HTTP dependencies.
- [Test Fixture Setup](通用技能领域/Family技能/未分类技能/微技能/Test Fixture Setup/SKILL.md) ｜ 适用：Create and manage reusable pytest fixtures in conftest.py for consistent test initialization. Fixtures provide mock objects, stubs, and test dependencies that can be injected across unit, integration, and end-to-end test cases.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Implement Contextual Error Logging` 时，优先调用它。 线索：Writing exception handlers or error paths, Debugging production issues or test failures, Implementing error recovery logic, error_handling, logging
- 当目标、阶段或方法更接近 `Record and Replay HTTP Interactions with pytest-vcr` 时，优先调用它。 线索：Test function makes HTTP requests to external APIs, Need deterministic test runs independent of external service availability, Require fast test execution without network latency, testing, http_mocking
- 当目标、阶段或方法更接近 `Test Fixture Setup` 时，优先调用它。 线索：Multiple test cases require the same mock client or external service stub, Test suite initialization needs consistent, reusable test dependencies, Fixture-based dependency injection is preferred over inline mock creation, pytest, testing

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- application requires production monitoring and observability
- distributed tracing across services is needed
- compliance or audit requirements mandate telemetry collection
- performance degradation or error patterns need investigation

## Examples

### Example 1

Input:

  Testing a single authentication function for correct token validation

Output:

  Unit test category selected; rationale: individual component validation with no external dependencies

Notes:

  Scope is narrow; objective is correctness of a single unit

### Example 2

Input:

  Testing interaction between API client and database layer when fetching user records

Output:

  Integration test category selected; rationale: validates correct interaction between two components

Notes:

  Scope spans multiple components; objective is correctness of their interaction

### Example 3

Input:

  Testing complete user registration workflow from form submission to confirmation email

Output:

  End-to-end test category selected; rationale: validates complete workflow across multiple systems

Notes:

  Scope is entire workflow; objective is correctness of full user journey
