---
id: "5dcaf70a-1c40-55e6-88e0-927b2eb5e3af"
name: "Feature Branch Setup"
description: "Initialize a local feature branch from upstream main with proper git workflow. Use when starting development on a new feature to ensure clean, isolated work."
version: "0.1.0"
tags:
  - "git"
  - "version_control"
  - "feature_development"
  - "branch_management"
  - "setup"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting work on a new feature"
  - "Need clean branch state from upstream"
  - "Beginning feature development cycle"
---

# Feature Branch Setup

Initialize a local feature branch from upstream main with proper git workflow. Use when starting development on a new feature to ensure clean, isolated work.

## Prompt

Execute the following git sequence to establish an isolated feature branch:
1. Check out main branch
2. Pull latest changes from upstream main
3. Create and check out a new feature branch with naming convention feature/your-feature-name

This ensures your work is isolated on a clean state tracking upstream.

## Objective

Establish isolated feature branch from upstream main
## Applicable Signals

- Feature development initiation
- New task assignment requiring code changes
- Local repository ready for feature work

## Contraindications

- Hotfix or release branch creation
- Already on correct feature branch
- Emergency production fixes requiring direct main branch work

## Workflow Steps

- {'step': 1, 'action': 'git checkout main', 'purpose': 'Switch to main branch'}
- {'step': 2, 'action': 'git pull upstream main', 'purpose': 'Fetch and merge latest upstream changes'}
- {'step': 3, 'action': 'git checkout -b feature/your-feature-name', 'purpose': 'Create and check out new feature branch with standard naming'}

## Constraints

- Upstream remote must be configured
- Local main branch must exist
- No uncommitted changes on current branch before checkout

## Cautions

- Ensure feature name is descriptive and follows team conventions
- Verify upstream pull completes without merge conflicts before proceeding
- Confirm correct branch is active before making code changes

## Output Contract

- Local feature branch checked out, named feature/your-feature-name, tracking upstream main. Caller can proceed with feature development.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting work on a new feature
- Need clean branch state from upstream
- Beginning feature development cycle
