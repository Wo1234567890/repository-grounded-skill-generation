---
id: "34bf73ff-2d7e-5d22-b104-00e18c471e95"
name: "Python Code Style Compliance"
description: "Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and docstring conventions. Apply before code review or merge to standardize code style across the repository."
version: "0.1.0"
tags:
  - "code_style"
  - "formatting"
  - "type_hints"
  - "documentation"
  - "pre_commit"
  - "python"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Developer prepares code for pull request or code review"
  - "Linting/formatting check is required before merge"
---

# Python Code Style Compliance

Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and docstring conventions. Apply before code review or merge to standardize code style across the repository.

## Prompt

1. Run Black formatter on all Python files with 88-character line length limit.
2. Verify all public methods include type hints on parameters and return values.
3. Verify all public methods have docstrings describing purpose and parameters.
4. Add clear inline comments where logic is non-obvious.
5. Update relevant documentation if changes affect public API.
6. Confirm code passes all style checks before proceeding to pull request.

## Objective

Standardize code style across repository
## Applicable Signals

- Developer prepares code for pull request
- Code review or merge is required
- Linting and formatting check is needed before merge

## Contraindications

- Code is already formatted and passes linter
- Third-party or legacy code exempt from style rules
- Code is in experimental or sandbox branch

## Workflow Steps

- {'step': 1, 'action': 'Run Black formatter', 'details': 'Execute Black on all Python files with --line-length=88'}
- {'step': 2, 'action': 'Verify type hints', 'details': 'Check all public methods have type hints on parameters and return values'}
- {'step': 3, 'action': 'Verify docstrings', 'details': 'Confirm all public methods have docstrings describing purpose and parameters'}
- {'step': 4, 'action': 'Add inline comments', 'details': 'Include clear inline comments for non-obvious logic'}
- {'step': 5, 'action': 'Update documentation', 'details': 'Update relevant documentation if changes affect public API'}
- {'step': 6, 'action': 'Validate compliance', 'details': 'Confirm code passes all style checks'}

## Constraints

- Black formatter must be configured with 88-character maximum line length
- Type hints required on all public methods
- Docstrings required on all public methods

## Cautions

- Black formatting may reflow long strings and comments; review changes carefully
- Type hints should use standard library types or project-defined types only
- Docstrings should be clear and concise, not verbose

## Output Contract

- Code passes Black formatter with 88-character line limit
- All public methods include type hints
- All public methods have docstrings
- Inline comments are present for non-obvious logic
- Ready for pull request submission

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Developer prepares code for pull request or code review
- Linting/formatting check is required before merge
