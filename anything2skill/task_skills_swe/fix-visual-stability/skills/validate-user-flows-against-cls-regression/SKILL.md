---
id: "41c6a6ea-b987-52fa-80ec-8b0d93030270"
name: "Validate User Flows Against CLS Regression"
description: "Instrument test execution with coverage tracking and generate a coverage report to identify untested code paths and assess test completeness."
version: "0.1.0"
tags:
  - "testing"
  - "coverage"
  - "validation"
  - "quality_assurance"
triggers:
  - "After identifying common CLS causes and before deploying changes"
  - "When validating typical user interaction flows in CI/CD pipelines"
  - "Before releasing updates that may affect page layout stability"
examples:
  - input: "Run coverage on full test suite"
    output: "Coverage report showing overall line coverage (e.g., 85%) and branch coverage (e.g., 72%)"
    notes: "Typical output includes per-file coverage breakdown"
  - input: "Run coverage on specific test file"
    output: "Coverage report focused on modules exercised by that test file"
    notes: "Useful for validating coverage of a single feature or module"
---

# Validate User Flows Against CLS Regression

Instrument test execution with coverage tracking and generate a coverage report to identify untested code paths and assess test completeness.

## Prompt

Execute tests with coverage instrumentation enabled, then generate and display a coverage report showing line and branch coverage percentages. Use this workflow to identify gaps in test coverage before release or when enforcing coverage thresholds.

## Objective

Measure and report code coverage
## Applicable Signals

- Assessing test completeness before release
- Identifying coverage gaps in codebase
- Enforcing coverage thresholds or targets
- Trend analysis of coverage metrics over time

## Contraindications

- Running quick smoke tests or sanity checks
- Debugging a single failing test in isolation
- Time-critical development cycles where overhead is unacceptable

## Workflow Steps

- {'step': 1, 'action': 'Instrument test execution', 'detail': "Run pytest with coverage instrumentation enabled using 'coverage run -m pytest'"}
- {'step': 2, 'action': 'Generate coverage report', 'detail': "Execute 'coverage report' to display line and branch coverage percentages"}
- {'step': 3, 'action': 'Persist coverage data', 'detail': 'Ensure coverage data is saved for trend analysis and historical comparison'}

## Constraints

- Coverage instrumentation adds execution overhead; not suitable for time-critical cycles
- Requires coverage tool to be installed and configured in the test environment

## Cautions

- Coverage percentage alone does not guarantee code quality; high coverage with poor test assertions may mask bugs
- Branch coverage is more stringent than line coverage; set realistic thresholds

## Output Contract

- Coverage report generated and displayed showing line and branch coverage percentages
- Coverage data persisted for trend analysis and downstream reporting

## Example Executions

### Example 1

- Input: Run coverage on full test suite
- Output: Coverage report showing overall line coverage (e.g., 85%) and branch coverage (e.g., 72%)
- Notes: Typical output includes per-file coverage breakdown

### Example 2

- Input: Run coverage on specific test file
- Output: Coverage report focused on modules exercised by that test file
- Notes: Useful for validating coverage of a single feature or module

## Triggers

- After identifying common CLS causes and before deploying changes
- When validating typical user interaction flows in CI/CD pipelines
- Before releasing updates that may affect page layout stability

## Examples

### Example 1

Input:

  Run coverage on full test suite

Output:

  Coverage report showing overall line coverage (e.g., 85%) and branch coverage (e.g., 72%)

Notes:

  Typical output includes per-file coverage breakdown

### Example 2

Input:

  Run coverage on specific test file

Output:

  Coverage report focused on modules exercised by that test file

Notes:

  Useful for validating coverage of a single feature or module
