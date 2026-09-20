---
id: "16faeab5-7a96-5c7c-b37b-4a9f8030cdb2"
name: "Project Dependency Installation"
description: "Installs project dependencies in editable mode to enable local development and testing. Execute after branch setup and before running development tasks."
version: "0.1.0"
tags:
  - "setup"
  - "dependencies"
  - "pip"
  - "development"
  - "environment"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "fresh development environment setup"
  - "after pulling new dependency changes from upstream"
  - "before running development or test tasks"
---

# Project Dependency Installation

Installs project dependencies in editable mode to enable local development and testing. Execute after branch setup and before running development tasks.

## Prompt

Run `pip install -e .` in the project root directory to install all dependencies in editable mode. This allows local code changes to be immediately reflected without reinstalling.

## Objective

install_development_dependencies
## Applicable Signals

- developer has just checked out a feature branch
- requirements or setup.py has been modified
- import errors indicate missing dependencies

## Contraindications

- dependencies are already installed and no changes to requirements have been made
- running in a production environment

## Workflow Steps

- {'step': 1, 'action': 'navigate to project root directory'}
- {'step': 2, 'action': 'execute command: pip install -e .'}
- {'step': 3, 'action': 'verify installation completed without errors'}

## Constraints

- must be executed in the project root directory
- requires pip and Python to be available in PATH
- project must have a setup.py or pyproject.toml file

## Cautions

- editable mode (-e flag) allows live code changes but may cause issues if dependencies are modified during development
- ensure virtual environment is activated before running pip install

## Output Contract

- All project dependencies installed in editable mode; developer can import project modules and run development tasks without additional setup.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- fresh development environment setup
- after pulling new dependency changes from upstream
- before running development or test tasks
