---
id: "eb9e3ad6-d72e-5d9c-a6c2-7645bc532b35"
name: "Test Fixture Setup"
description: "Create and manage reusable pytest fixtures in conftest.py for consistent test initialization. Fixtures provide mock objects, stubs, and test dependencies that can be injected across unit, integration, and end-to-end test cases."
version: "0.1.0"
tags:
  - "pytest"
  - "testing"
  - "mock"
  - "fixture"
  - "test_setup"
  - "conftest"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Multiple test cases require the same mock client or external service stub"
  - "Test suite initialization needs consistent, reusable test dependencies"
  - "Fixture-based dependency injection is preferred over inline mock creation"
examples:
  - input: "Test suite requires a mock LLM client with a chat.completions.create method"
    output: "@pytest.fixture\ndef mock_llm_client():\n    client = Mock()\n    client.chat.completions.create.return_value = Mock()\n    return client"
    notes: "Fixture is injected into test functions as a parameter; pytest handles initialization and cleanup"
---

# Test Fixture Setup

Create and manage reusable pytest fixtures in conftest.py for consistent test initialization. Fixtures provide mock objects, stubs, and test dependencies that can be injected across unit, integration, and end-to-end test cases.

## Prompt

Define a pytest fixture function in conftest.py using the @pytest.fixture decorator. Configure the fixture to return a properly initialized mock object or test dependency. Ensure the fixture is scoped appropriately (function, class, module, or session) and returns a consistent, reusable object ready for test injection.

## Objective

Initialize mock objects and test dependencies for reuse across test cases
## Applicable Signals

- Test file imports conftest.py
- Test function signature includes fixture parameter
- Mock object configuration is repeated across test cases

## Contraindications

- Testing real API integrations or live service calls; use VCR cassettes instead
- Fixture requires stateful persistence across test runs
- Mock configuration is test-case-specific and cannot be generalized

## Workflow Steps

- {'step': 1, 'action': 'Define fixture function in conftest.py', 'detail': 'Create a function with @pytest.fixture decorator; name should reflect the mock object or dependency it provides'}
- {'step': 2, 'action': 'Configure mock object or dependency', 'detail': 'Initialize the mock (e.g., Mock(), MagicMock()) and set return values, side effects, or attributes as needed'}
- {'step': 3, 'action': 'Return the configured object', 'detail': 'Fixture function returns the mock or dependency ready for injection into test functions'}
- {'step': 4, 'action': 'Inject fixture into test functions', 'detail': 'Test functions receive fixture as a parameter; pytest automatically calls the fixture and passes the returned object'}

## Constraints

- Fixture must be defined in conftest.py or imported from it
- Fixture function must use @pytest.fixture decorator
- Fixture must return a consistent, deterministic object
- Sensitive information must not be hardcoded in fixture definitions

## Cautions

- Ensure fixture scope matches test isolation requirements (function-scoped fixtures reset between tests)
- Avoid side effects in fixture setup that could affect test independence
- Document fixture purpose and expected return type for clarity

## Output Contract

- Reusable fixture function in conftest.py that returns a properly configured mock object or test dependency. The fixture is callable by any test function that includes it as a parameter, and returns a consistent, initialized object ready for test assertions.

## Example Executions

### Example 1

- Input: Test suite requires a mock LLM client with a chat.completions.create method
- Output: @pytest.fixture
def mock_llm_client():
    client = Mock()
    client.chat.completions.create.return_value = Mock()
    return client
- Notes: Fixture is injected into test functions as a parameter; pytest handles initialization and cleanup

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Multiple test cases require the same mock client or external service stub
- Test suite initialization needs consistent, reusable test dependencies
- Fixture-based dependency injection is preferred over inline mock creation

## Examples

### Example 1

Input:

  Test suite requires a mock LLM client with a chat.completions.create method

Output:

  @pytest.fixture
  def mock_llm_client():
      client = Mock()
      client.chat.completions.create.return_value = Mock()
      return client

Notes:

  Fixture is injected into test functions as a parameter; pytest handles initialization and cleanup
