---
id: "f79dec56-8f91-5eaa-80bc-6d8f686412df"
name: "Third-Party Script Performance Optimization"
description: "Structured workflow for running unit tests at different scopes (all tests, specific files, with coverage reporting). Use when validating code changes or preparing for deployment."
version: "0.1.1"
tags:
  - "testing"
  - "validation"
  - "ci-cd"
  - "quality-assurance"
  - "test-automation"
triggers:
  - "Application integrates external scripts for analytics, ads, or tracking"
  - "Performance audit identifies third-party scripts blocking main thread"
  - "Need to defer non-critical script execution"
examples:
  - input: "List of integers [1, 2, 3, 4, 5]"
    output: "DataStream<Integer> ready for map, filter, or aggregation operators"
    notes: "Typical unit test setup for validating a simple transformation"
  - input: "List of Tuple2<String, Integer> records"
    output: "DataStream<Tuple2<String, Integer>> ready for keyed operations or joins"
    notes: "Common for testing stateful operators or windowed aggregations"
---

# Third-Party Script Performance Optimization

Structured workflow for running unit tests at different scopes (all tests, specific files, with coverage reporting). Use when validating code changes or preparing for deployment.

## Prompt

Execute tests using the appropriate command based on scope: (1) Run all tests with tox for full validation, (2) Run specific test file with pytest and verbose output for targeted verification, (3) Run with coverage instrumentation to measure line and branch coverage. Report results including pass/fail summary and coverage percentages.

## Objective

Execute and report test results
## Applicable Signals

- Code changes staged for commit
- Pre-deployment validation gate
- Module-specific regression check needed

## Contraindications

- No test suite exists in repository
- Integration tests require live external services
- Manual exploratory testing is the primary goal

## Workflow Steps

- {'step': 1, 'action': 'Run all tests', 'command': 'tox', 'purpose': 'Full validation across all test files and configurations'}
- {'step': 2, 'action': 'Run specific test file', 'command': 'pytest <test_file_path> -v', 'purpose': 'Targeted verification of single module or component'}
- {'step': 3, 'action': 'Run with coverage instrumentation', 'command': 'coverage run -m pytest && coverage report', 'purpose': 'Measure line and branch coverage percentages'}

## Constraints

- Test suite must be present and discoverable
- pytest and tox must be installed in environment
- Coverage tool must be available for coverage mode

## Cautions

- Coverage mode adds execution overhead; use selectively
- Specific test file paths must be valid relative to test root
- Verbose output (-v flag) increases log volume; filter as needed

## Output Contract

- Test execution completes with pass/fail summary and optional coverage report showing line/branch coverage percentages. Caller receives structured result indicating test status and coverage metrics.

## Triggers

- Application integrates external scripts for analytics, ads, or tracking
- Performance audit identifies third-party scripts blocking main thread
- Need to defer non-critical script execution

## Examples

### Example 1

Input:

  List of integers [1, 2, 3, 4, 5]

Output:

  DataStream<Integer> ready for map, filter, or aggregation operators

Notes:

  Typical unit test setup for validating a simple transformation

### Example 2

Input:

  List of Tuple2<String, Integer> records

Output:

  DataStream<Tuple2<String, Integer>> ready for keyed operations or joins

Notes:

  Common for testing stateful operators or windowed aggregations
