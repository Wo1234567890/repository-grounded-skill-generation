---
id: "cb55fb3e-7b22-513e-b682-5f6a4cb952b8"
name: "StreamExecutionEnvironment Setup"
description: "Establishes a clean feature branch from upstream main before starting development work. Ensures local repository is synchronized and isolated for new feature implementation."
version: "0.1.0"
tags:
  - "git"
  - "version_control"
  - "branch_management"
  - "development_setup"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new Flink streaming application"
  - "Switching between local development and cluster deployment"
  - "Initializing a streaming pipeline before defining sources"
---

# StreamExecutionEnvironment Setup

Establishes a clean feature branch from upstream main before starting development work. Ensures local repository is synchronized and isolated for new feature implementation.

## Prompt

Execute the following steps in order to prepare a feature branch:
1. Check out the main branch locally.
2. Pull the latest changes from upstream main to synchronize.
3. Create and check out a new feature branch with a descriptive name (e.g., feature/your-feature-name).
This workflow ensures your feature work is isolated and based on the latest upstream state.

## Objective

prepare_development_environment
## Applicable Signals

- feature development initiation
- new task assignment requiring code changes

## Contraindications

- working on hotfixes or emergency patches that require direct main branch work
- already on an active feature branch with uncommitted changes

## Workflow Steps

- {'step': 1, 'action': 'git checkout main', 'purpose': 'switch to main branch'}
- {'step': 2, 'action': 'git pull upstream main', 'purpose': 'synchronize local main with upstream latest state'}
- {'step': 3, 'action': 'git checkout -b feature/your-feature-name', 'purpose': 'create and check out new isolated feature branch'}

## Constraints

- upstream remote must be configured and accessible
- local main branch must exist
- no uncommitted changes on current branch before checkout

## Cautions

- ensure feature branch name is descriptive and follows team naming conventions
- verify upstream remote is the correct source before pulling

## Output Contract

- new feature branch created and checked out, synchronized with upstream main
- developer is ready to begin feature implementation

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new Flink streaming application
- Switching between local development and cluster deployment
- Initializing a streaming pipeline before defining sources
