---
id: "e90c2a8f-194e-5fb1-99e3-7a99328214fe"
name: "Development Environment Setup"
description: "Initialize a local development environment with API credentials, Python virtual environment, and pre-commit hooks for code quality enforcement."
version: "0.1.0"
tags:
  - "setup"
  - "environment"
  - "configuration"
  - "developer_experience"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Starting a new development session"
  - "Onboarding a new developer"
  - "Initializing a fresh repository clone"
---

# Development Environment Setup

Initialize a local development environment with API credentials, Python virtual environment, and pre-commit hooks for code quality enforcement.

## Prompt

Follow these steps in order to prepare a reproducible development workspace:
1. Create a .env file with required API keys (AGENTOPS_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, and any others).
2. Set up a Python virtual environment using poetry or venv.
3. Install and configure pre-commit hooks to automatically format and lint code on commit.
Verify that the virtual environment is activated, the .env file contains all required credentials, and pre-commit hooks are registered.

## Objective

Prepare a reproducible development workspace
## Applicable Signals

- First-time setup required
- Environment variables not yet configured
- Virtual environment not activated
- Pre-commit hooks not installed

## Contraindications

- Production deployment context
- CI/CD pipeline execution
- Containerized environments where configuration is externalized

## Workflow Steps

- {'step': 1, 'action': 'Create .env file', 'details': 'Create a .env file in the project root with AGENTOPS_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, and any other required keys.'}
- {'step': 2, 'action': 'Set up virtual environment', 'details': "Run 'python -m venv venv' to create a virtual environment, then activate it using 'source venv/bin/activate' (Unix) or '.\\venv\\Scripts\\activate' (Windows)."}
- {'step': 3, 'action': 'Install pre-commit', 'details': "Run 'pip install pre-commit' to install the pre-commit framework."}
- {'step': 4, 'action': 'Register pre-commit hooks', 'details': "Run 'pre-commit install' to register hooks. Verify with 'pre-commit run --all-files' to check all files manually."}

## Constraints

- API keys must be valid and non-empty in .env file
- Python version must be compatible with project requirements
- Pre-commit must be installed before hook registration

## Cautions

- Do not commit .env file to version control; add it to .gitignore.
- Ensure API keys are kept confidential and not logged or exposed.
- Pre-commit hooks will run automatically on commit; allow time for linting and formatting.

## Output Contract

- Activated virtual environment with all dependencies installed, .env file configured with required API keys, and pre-commit hooks registered and functional. Caller can verify by checking: (1) virtual environment is active in shell, (2) .env file exists with all required keys, (3) 'pre-commit run --all-files' completes without errors.

## 子技能目录
- [Configure Pre-commit Hooks](通用技能领域/Family技能/未分类技能/微技能/Configure Pre-commit Hooks/SKILL.md) ｜ 适用：Install and activate pre-commit hooks for automated code quality checks before commits. Enforces code standards at the point of commit in a development environment.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Configure Pre-commit Hooks` 时，优先调用它。 线索：Development environment initialized, After dependency installation (pip install -e .), Before first commit to feature branch, development_setup, code_quality

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new development session
- Onboarding a new developer
- Initializing a fresh repository clone
