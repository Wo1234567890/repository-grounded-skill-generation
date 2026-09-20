---
id: "e3a07da1-fe8a-5c1d-8d2e-702ddca6ad44"
name: "Run All Tests with Tox"
description: "Execute the complete test suite using tox to validate all test environments and configurations in one command."
version: "0.1.0"
tags:
  - "testing"
  - "validation"
  - "tox"
  - "test-suite"
triggers:
  - "Need to run all tests across all configured environments"
  - "Before committing or merging code"
examples:
  - input: "Developer ready to commit code changes"
    output: "tox completes with all environments passing"
    notes: "Typical pre-commit validation workflow"
---

# Run All Tests with Tox

Execute the complete test suite using tox to validate all test environments and configurations in one command.

## Prompt

Invoke tox to run the full test suite across all configured environments. This ensures all tests pass before committing or merging code.

## Objective

Execute full test suite across all environments
## Applicable Signals

- Before committing or merging code
- Need to validate all test environments
- Require comprehensive test coverage across configurations

## Contraindications

- Debugging a single failing test
- Need rapid feedback on one module
- Running in resource-constrained environment

## Workflow Steps

- {'step': 1, 'action': 'Run tox command', 'command': 'tox', 'description': 'Execute tox to run all configured test environments'}

## Constraints

- Requires tox to be installed and configured
- All test environments must be properly set up
- Execution time may be longer than targeted test runs

## Output Contract

- All test environments pass
- tox reports zero failures and completes successfully

## Example Executions

### Example 1

- Input: Developer ready to commit code changes
- Output: tox completes with all environments passing
- Notes: Typical pre-commit validation workflow

## Triggers

- Need to run all tests across all configured environments
- Before committing or merging code

## Examples

### Example 1

Input:

  Developer ready to commit code changes

Output:

  tox completes with all environments passing

Notes:

  Typical pre-commit validation workflow
