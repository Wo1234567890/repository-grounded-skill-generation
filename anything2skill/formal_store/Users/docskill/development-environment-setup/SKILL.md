---
id: "c8fa3e03-1270-53ed-b939-cea44fb4db42"
name: "Development Environment Setup"
description: "Configure local development environment with API keys, virtual environment, and pre-commit hooks for code quality enforcement. Bundles environment variable configuration, Python virtual environment activation, and pre-commit hook installation into one reproducible session-level workflow."
version: "0.1.0"
tags:
  - "setup"
  - "initialization"
  - "environment"
  - "configuration"
  - "developer_experience"
  - "onboarding"
triggers:
  - "Developer begins new project or onboards to codebase"
  - "Local development environment needs to be initialized"
  - "Reproducible setup required before development work"
---

# Development Environment Setup

Configure local development environment with API keys, virtual environment, and pre-commit hooks for code quality enforcement. Bundles environment variable configuration, Python virtual environment activation, and pre-commit hook installation into one reproducible session-level workflow.

## Prompt

Execute the following steps in order:
1. Create a .env file with required API keys (AGENTOPS_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, and any other keys needed).
2. Set up a Python virtual environment using poetry or venv:
   - Run: python -m venv venv
   - Activate: source venv/bin/activate (Unix) or .\venv\Scripts\activate (Windows)
3. Install and configure pre-commit hooks:
   - Run: pip install pre-commit
   - Run: pre-commit install
4. Verify setup by running: pre-commit run --all-files
All steps must complete successfully before development work begins.

## Objective

prepare_development_workspace
## Applicable Signals

- First-time project setup
- New team member onboarding
- Fresh clone of repository

## Contraindications

- Production deployment environment
- CI/CD pipeline configuration
- Containerized or managed environments
- Shared or restricted development machines

## Workflow Steps

- {'step': 1, 'name': 'Create environment variables file', 'action': 'Create .env file in project root with required API keys', 'inputs': ['AGENTOPS_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY'], 'validation': '.env file exists and contains all required keys'}
- {'step': 2, 'name': 'Set up virtual environment', 'action': 'Create and activate Python virtual environment', 'inputs': ['Python installation path'], 'validation': 'Virtual environment activated (shell prompt shows venv indicator)'}
- {'step': 3, 'name': 'Install and configure pre-commit', 'action': 'Install pre-commit package and register hooks', 'inputs': ['Active virtual environment'], 'validation': 'pre-commit install completes without errors'}
- {'step': 4, 'name': 'Verify setup', 'action': 'Run pre-commit on all files to confirm hooks are functional', 'inputs': ['Installed pre-commit hooks'], 'validation': 'pre-commit run --all-files completes successfully'}

## Constraints

- API keys must be valid and have appropriate permissions
- Python 3.6+ must be installed
- Git must be initialized in the project directory
- Write permissions required for .env file and venv directory creation

## Cautions

- Do not commit .env file to version control; add to .gitignore
- API keys are sensitive; rotate periodically
- Virtual environment must be activated before installing dependencies or running code
- Pre-commit hooks will block commits if code quality checks fail; fix issues before retrying commit

## Output Contract

- Upon successful completion: (1) .env file created with all required API keys, (2) Python virtual environment activated and ready for use, (3) pre-commit hooks installed and verified with successful test run on all files, (4) developer can proceed with dependency installation and development work.

## Triggers

- Developer begins new project or onboards to codebase
- Local development environment needs to be initialized
- Reproducible setup required before development work
