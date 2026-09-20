---
id: "c30581b0-7eb6-5161-b5d3-b7238458f952"
name: "Fork and Clone Repository"
description: "Micro-skill for forking a GitHub repository and cloning it locally to establish a development workspace. Use when starting contribution or local development on a shared codebase."
version: "0.1.0"
tags:
  - "git"
  - "repository"
  - "setup"
  - "initialization"
  - "development"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "beginning contribution workflow"
  - "need local editable copy"
  - "starting fresh development environment"
examples:
  - input: "User wants to contribute to a shared GitHub project"
    output: "Local clone of forked repository in ~/repository-name/ with git remote pointing to user's fork"
    notes: "Assumes GitHub account exists and git is installed"
---

# Fork and Clone Repository

Micro-skill for forking a GitHub repository and cloning it locally to establish a development workspace. Use when starting contribution or local development on a shared codebase.

## Prompt

1. Fork the repository by clicking the 'Fork' button in the top right of the target GitHub repository. This creates your own copy.
2. Clone your fork locally using: git clone https://github.com/YOUR_USERNAME/repository-name.git
3. Navigate into the cloned directory: cd repository-name
4. Verify the clone is complete and ready for edits.

## Objective

establish local development copy
## Applicable Signals

- contributor ready to start work
- local development environment needed
- fresh repository access required

## Contraindications

- already have local clone
- read-only access sufficient
- git not installed on system

## Intervention Moves

- fork repository on GitHub
- clone fork to local machine
- navigate to repository directory

## Workflow Steps

- Click 'Fork' button on GitHub repository page
- Execute git clone command with forked repository URL
- Change directory to cloned repository
- Verify clone completion and working directory readiness

## Constraints

- GitHub account required
- git command-line tool must be installed
- network connectivity required for clone operation
- sufficient disk space for repository

## Cautions

- Ensure you fork before cloning to avoid permission issues on push
- Replace YOUR_USERNAME with actual GitHub username
- Verify clone completes without errors before proceeding

## Output Contract

- local repository directory with upstream remote configured and working directory ready for edits

## Example Executions

### Example 1

- Input: User wants to contribute to a shared GitHub project
- Output: Local clone of forked repository in ~/repository-name/ with git remote pointing to user's fork
- Notes: Assumes GitHub account exists and git is installed

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- beginning contribution workflow
- need local editable copy
- starting fresh development environment

## Examples

### Example 1

Input:

  User wants to contribute to a shared GitHub project

Output:

  Local clone of forked repository in ~/repository-name/ with git remote pointing to user's fork

Notes:

  Assumes GitHub account exists and git is installed
