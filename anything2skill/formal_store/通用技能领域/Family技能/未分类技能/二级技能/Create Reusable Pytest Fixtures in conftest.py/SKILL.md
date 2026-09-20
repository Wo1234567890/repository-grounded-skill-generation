---
id: "eaf5aa6c-7f3f-5a0b-99a2-351cf9078d16"
name: "Create Reusable Pytest Fixtures in conftest.py"
description: "Define and manage reusable pytest fixtures in conftest.py to standardize mock objects and test dependencies across test suites. Establishes consistent test infrastructure for unit and integration tests by centralizing fixture definitions and ensuring proper scope alignment."
version: "0.1.0"
tags:
  - "testing"
  - "pytest"
  - "fixtures"
  - "mocking"
  - "test_infrastructure"
  - "reusability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Setting up unit tests that require mock objects"
  - "Setting up integration tests with shared API client mocks"
  - "Establishing test state that multiple test functions will consume"
---

# Create Reusable Pytest Fixtures in conftest.py

Define and manage reusable pytest fixtures in conftest.py to standardize mock objects and test dependencies across test suites. Establishes consistent test infrastructure for unit and integration tests by centralizing fixture definitions and ensuring proper scope alignment.

## Prompt

Define reusable pytest fixtures in conftest.py using the @pytest.fixture decorator. Structure fixtures to return mock objects or test dependencies that can be injected into multiple test functions. Example: mock_llm_client fixture returns a Mock object with pre-configured return values for API calls. Ensure fixtures are scoped appropriately (function, class, module, or session) to match test isolation requirements.

## Objective

Establish consistent, reusable test infrastructure across test suites
## Applicable Signals

- Multiple test functions need the same mock configuration
- Test suite requires standardized mock objects across files
- Need to reduce test setup boilerplate and duplication

## Contraindications

- Tests require unique, non-reusable fixture configurations
- Fixture scope conflicts with test isolation requirements
- One-off mock configurations that apply to a single test only

## Intervention Moves

- Identify common mock objects or test dependencies needed across multiple tests
- Define fixture function in conftest.py with @pytest.fixture decorator
- Configure mock object with expected return values or side effects
- Return configured mock object from fixture
- Inject fixture into test functions by adding fixture name as parameter
- Verify mock is invoked with expected arguments during test execution

## Workflow Steps

- Identify common mock objects or test dependencies needed across multiple tests
- Define fixture function in conftest.py with @pytest.fixture decorator
- Configure mock object with expected return values or side effects
- Return configured mock object from fixture
- Inject fixture into test functions by adding fixture name as parameter
- Verify mock is invoked with expected arguments during test execution

## Constraints

- Fixtures must be defined in conftest.py to be discoverable across test modules
- Fixture scope must align with test isolation boundaries
- Mock return values must be configured before fixture is returned to test

## Cautions

- Avoid over-scoping fixtures; use function scope by default unless module or session scope is explicitly required
- Sanitize sensitive information in mock return values
- Document fixture purpose and expected mock behavior for test maintainers

## Output Contract

- Fixture is defined in conftest.py and successfully injected into test functions; mock object returns expected values on invocation; test functions receive consistent mock configuration across multiple test runs.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Setting up unit tests that require mock objects
- Setting up integration tests with shared API client mocks
- Establishing test state that multiple test functions will consume
