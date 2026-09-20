---
id: "4cf1f416-b910-53e6-9cd4-08ea9a9bf8f0"
name: "Monitor Live CLS During User Interaction"
description: "Install project dependencies in editable mode for local development. Use after cloning or when setting up a fresh development environment."
version: "0.1.0"
tags:
  - "development"
  - "setup"
  - "pip"
  - "environment"
  - "editable_mode"
triggers:
  - "CrUX field CLS score is significantly higher than Lighthouse lab CLS score"
  - "Post-load CLS is suspected but not yet identified"
  - "Need to correlate user interactions with layout shift events"
---

# Monitor Live CLS During User Interaction

Install project dependencies in editable mode for local development. Use after cloning or when setting up a fresh development environment.

## Prompt

Run `pip install -e .` in the project root directory to install the project in editable mode. This allows local source changes to be immediately reflected without reinstalling.

## Objective

Install project in editable mode for development
## Applicable Signals

- Development environment setup phase
- Local source modification workflow
- Pre-development environment validation

## Contraindications

- Production deployment context
- Virtual environment not activated or unavailable

## Workflow Steps

- Verify virtual environment is activated
- Navigate to project root directory
- Execute: pip install -e .
- Verify installation success by checking import paths

## Constraints

- Python virtual environment must be active
- Project root directory must contain setup.py or pyproject.toml
- pip must be available in the active environment

## Cautions

- Editable mode links to local source; changes to source files take effect immediately
- Do not use in production environments

## Output Contract

- Project installed in editable mode; import paths resolve to local source; no errors reported by pip

## Triggers

- CrUX field CLS score is significantly higher than Lighthouse lab CLS score
- Post-load CLS is suspected but not yet identified
- Need to correlate user interactions with layout shift events
