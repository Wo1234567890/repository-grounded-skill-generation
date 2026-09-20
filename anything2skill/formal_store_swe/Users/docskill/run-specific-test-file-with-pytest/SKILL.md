---
id: "607f6958-ca2b-5d5b-b3cc-8477b66d19a4"
name: "Run Specific Test File with Pytest"
description: "Execute a single test file with verbose output to isolate and debug specific test cases or modules."
version: "0.1.0"
tags:
  - "testing"
  - "pytest"
  - "debugging"
  - "validation"
  - "single-file"
triggers:
  - "Debugging a specific test failure"
  - "Developing a new test case"
  - "Need fast feedback on one module"
examples:
  - input: "Test file path: tests/llms/test_anthropic.py"
    output: "pytest tests/llms/test_anthropic.py -v\n[test results with individual test case status]"
    notes: "Verbose output shows each test name and result"
---

# Run Specific Test File with Pytest

Execute a single test file with verbose output to isolate and debug specific test cases or modules.

## Prompt

Use pytest to run a single test file with verbose flag enabled. Provide the relative path to the test file (e.g., tests/llms/test_anthropic.py). Output will show pass/fail status for each test case in the file.

## Objective

Execute targeted test file with verbose output for isolated debugging
## Applicable Signals

- Single test file identified as problematic
- Iterative test development in progress
- Quick validation needed before full suite run

## Contraindications

- Running full regression suite
- Need coverage metrics across entire codebase
- Testing across multiple environments or configurations

## Workflow Steps

- Identify the target test file path relative to project root
- Invoke pytest with file path and -v flag
- Capture and display test execution output
- Report pass/fail status for each test case

## Constraints

- Test file must exist at specified path
- pytest must be installed and available in environment
- Verbose flag (-v) should be included for clear output

## Output Contract

- Test file executes with verbose output; pass/fail status displayed for each test case; execution completes with exit code indicating overall result.

## Example Executions

### Example 1

- Input: Test file path: tests/llms/test_anthropic.py
- Output: pytest tests/llms/test_anthropic.py -v
[test results with individual test case status]
- Notes: Verbose output shows each test name and result

## Triggers

- Debugging a specific test failure
- Developing a new test case
- Need fast feedback on one module

## Examples

### Example 1

Input:

  Test file path: tests/llms/test_anthropic.py

Output:

  pytest tests/llms/test_anthropic.py -v
  [test results with individual test case status]

Notes:

  Verbose output shows each test name and result
