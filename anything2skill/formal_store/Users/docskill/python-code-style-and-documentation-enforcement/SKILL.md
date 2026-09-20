---
id: "861d8a1a-86b4-5e13-916c-c9ae446beeb9"
name: "Python Code Style and Documentation Enforcement"
description: "Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and structured docstrings during code review and development to maintain codebase quality."
version: "0.1.0"
tags:
  - "code_quality"
  - "python"
  - "formatting"
  - "documentation"
  - "guardrail"
  - "static_analysis"
triggers:
  - "reviewing pull requests"
  - "onboarding new contributors"
  - "setting up linting pipelines"
---

# Python Code Style and Documentation Enforcement

Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and structured docstrings during code review and development to maintain codebase quality.

## Prompt

Verify that submitted code adheres to the following standards:
1. Formatting: Black formatter with 88-character maximum line length
2. Type hints: Present on all public methods
3. Documentation: Docstrings for all public methods, clear inline comments, and updated relevant documentation
4. Error handling: Specific exception types, meaningful error messages with context

Reject or request revision if any standard is not met.

## Objective

enforce_code_quality_standards
## Applicable Signals

- pull request submitted
- new contributor onboarding
- linting pipeline setup
- code review checkpoint

## Contraindications

- Legacy code explicitly exempt from style rules
- Rapid prototyping phases where style enforcement is deferred
- Third-party or vendored code

## Intervention Moves

- Run Black formatter check at 88-character limit
- Scan for type hints on all public methods
- Verify docstrings present and complete
- Check error messages include context
- Request revision if any standard fails

## Workflow Steps

- Check code formatting against Black formatter with 88-character line length
- Verify type hints on all public methods
- Validate docstrings for all public methods
- Review error handling for specific exception types and contextual messages
- Request revision or approve based on compliance

## Constraints

- Black formatter must be applied with 88-character line length
- Type hints required on all public methods
- Docstrings mandatory for all public methods
- Error messages must include meaningful context

## Cautions

- Do not block merges for style-only violations in emergency hotfixes without team agreement
- Ensure linting tools are configured consistently across all environments

## Output Contract

- Code passes Black formatter at 88-character line length, includes type hints on all public methods, and has complete docstrings with inline comments. Error handling uses specific exception types with contextual messages.

## Triggers

- reviewing pull requests
- onboarding new contributors
- setting up linting pipelines
