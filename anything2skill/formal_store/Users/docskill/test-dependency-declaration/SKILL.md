---
id: "86134432-1eff-51aa-bef8-04adf0d1de1e"
name: "Test Dependency Declaration"
description: "Declare and enforce test execution order using pytest markers to ensure prerequisite tests run before dependent tests."
version: "0.1.0"
tags:
  - "pytest"
  - "test_ordering"
  - "test_dependencies"
  - "test_orchestration"
  - "marker"
triggers:
  - "Multiple tests have sequential dependencies"
  - "One test requires another to pass first"
  - "Test execution order affects correctness"
---

# Test Dependency Declaration

Declare and enforce test execution order using pytest markers to ensure prerequisite tests run before dependent tests.

## Prompt

Use @pytest.mark.depends(on=['test_prerequisite']) to declare that a test depends on one or more prerequisite tests. The test runner will ensure the prerequisite test(s) pass before executing the dependent test. This enforces sequential test execution when test correctness depends on prior test state or completion.

## Objective

enforce_test_sequence
## Applicable Signals

- test_prerequisite_required
- sequential_test_chain
- order_dependent_tests

## Contraindications

- Tests are independent
- Test order does not affect correctness
- Using test isolation patterns that eliminate ordering requirements

## Workflow Steps

- Identify the prerequisite test name
- Add @pytest.mark.depends(on=['test_prerequisite']) decorator to the dependent test function
- Verify the test runner recognizes the marker
- Run tests and confirm dependent test waits for prerequisite completion

## Constraints

- Prerequisite test must be named and accessible to the test runner
- Dependency chain must be acyclic (no circular dependencies)
- pytest-dependency plugin or equivalent must be installed

## Cautions

- Overuse of test dependencies can create brittle test suites; prefer test isolation where possible
- Circular dependencies will cause test runner errors
- Dependency markers are plugin-specific; ensure compatibility with your test runner

## Output Contract

- Dependent test executes only after prerequisite test passes; test runner respects declared dependency chain and skips dependent test if prerequisite fails.

## Triggers

- Multiple tests have sequential dependencies
- One test requires another to pass first
- Test execution order affects correctness
