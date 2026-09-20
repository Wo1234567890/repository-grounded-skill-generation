---
id: "bd9a1ba1-b78f-5a70-aa79-22fae910b2d2"
name: "Configure GitHub Actions Notebook Test Workflow"
description: "Set up and maintain the test-notebooks.yml CI workflow to automatically execute Jupyter notebooks on pull requests, manage provider API secrets in the GitHub Actions environment, and exclude notebooks requiring manual testing."
version: "0.1.0"
tags:
  - "ci_cd"
  - "github_actions"
  - "notebook_testing"
  - "integration_testing"
  - "workflow_configuration"
  - "automation"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Pull request opened or updated with changes to agentops/, examples/, or tests/ directories"
  - "Manual workflow dispatch trigger"
  - "Merge to main branch"
examples:
  - input: "Pull request modifies examples/openai/basic_completion.ipynb"
    output: "Workflow triggers, installs AgentOps, sets OPENAI_API_KEY from GitHub secret, executes all notebooks in examples/ except those in exclude_notebooks, reports success or failure"
    notes: "Demonstrates standard PR-triggered execution path"
  - input: "New provider notebook added to examples/anthropic/; exclude_notebooks list not updated"
    output: "Workflow executes new notebook; if it requires manual setup, workflow may fail; developer must add notebook name to exclude_notebooks and re-run"
    notes: "Illustrates importance of maintaining exclude_notebooks configuration"
---

# Configure GitHub Actions Notebook Test Workflow

Set up and maintain the test-notebooks.yml CI workflow to automatically execute Jupyter notebooks on pull requests, manage provider API secrets in the GitHub Actions environment, and exclude notebooks requiring manual testing.

## Prompt

Configure the test-notebooks.yml GitHub Actions workflow file to trigger on PR events affecting agentops/, examples/, or tests/ directories. Install AgentOps from the main branch, set up provider API keys as environment variables from GitHub secrets, execute each notebook sequentially, skip notebooks listed in exclude_notebooks, and report pass/fail status. Verify the workflow runs on PR merges and supports manual trigger invocation.

## Objective

Automate notebook-based integration testing in CI/CD pipeline via GitHub Actions configuration
## Applicable Signals

- PR event with modified notebook or provider code
- New LLM provider added requiring test coverage
- Provider API credentials need to be registered in CI environment
- Notebook exclusion rules need updating

## Contraindications

- Do not use for local notebook debugging or development iteration
- Do not use for managing provider API keys outside the CI/CD context
- Do not use for testing notebook logic itself; use local execution instead
- Do not apply to workflows that do not use GitHub Actions

## Workflow Steps

- {'step': 1, 'action': 'Define workflow trigger', 'detail': 'Set on: pull_request with paths filter for agentops/**, examples/**, tests/**; add manual workflow_dispatch for on-demand runs'}
- {'step': 2, 'action': 'Set up environment', 'detail': 'Configure job to run on ubuntu-latest; set up Python matrix for multiple versions'}
- {'step': 3, 'action': 'Install dependencies', 'detail': 'Install AgentOps from main branch; install notebook execution dependencies (jupyter, nbconvert, or equivalent)'}
- {'step': 4, 'action': 'Configure provider secrets', 'detail': 'Export provider API keys from GitHub Actions secrets as environment variables for each LLM provider'}
- {'step': 5, 'action': 'Execute notebooks', 'detail': 'Iterate over notebooks in examples/ directory; skip notebooks in exclude_notebooks list; execute each notebook and capture output'}
- {'step': 6, 'action': 'Report results', 'detail': 'Fail workflow if any notebook execution returns non-zero exit code; upload logs or artifacts for debugging'}

## Constraints

- Workflow file must be located in .github/workflows/test-notebooks.yml
- Trigger paths must include agentops/**, examples/**, and tests/**
- Provider API keys must be configured as GitHub Actions secrets before workflow execution
- Notebooks requiring manual testing must be explicitly listed in exclude_notebooks
- Workflow must support multiple Python versions

## Cautions

- Ensure all provider API secrets are registered in GitHub repository settings before enabling the workflow
- Verify exclude_notebooks list is updated when adding notebooks that require manual intervention
- Monitor workflow execution time; long-running notebooks may cause CI timeouts
- Test workflow changes on a feature branch before merging to main

## Output Contract

- Workflow file is valid YAML, triggers correctly on PR events, installs all dependencies, executes all non-excluded notebooks against actual LLM APIs, and reports pass/fail status. Excluded notebooks are skipped without error. Environment variables for provider API keys are set and accessible to notebook execution.

## Example Executions

### Example 1

- Input: Pull request modifies examples/openai/basic_completion.ipynb
- Output: Workflow triggers, installs AgentOps, sets OPENAI_API_KEY from GitHub secret, executes all notebooks in examples/ except those in exclude_notebooks, reports success or failure
- Notes: Demonstrates standard PR-triggered execution path

### Example 2

- Input: New provider notebook added to examples/anthropic/; exclude_notebooks list not updated
- Output: Workflow executes new notebook; if it requires manual setup, workflow may fail; developer must add notebook name to exclude_notebooks and re-run
- Notes: Illustrates importance of maintaining exclude_notebooks configuration

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Pull request opened or updated with changes to agentops/, examples/, or tests/ directories
- Manual workflow dispatch trigger
- Merge to main branch

## Examples

### Example 1

Input:

  Pull request modifies examples/openai/basic_completion.ipynb

Output:

  Workflow triggers, installs AgentOps, sets OPENAI_API_KEY from GitHub secret, executes all notebooks in examples/ except those in exclude_notebooks, reports success or failure

Notes:

  Demonstrates standard PR-triggered execution path

### Example 2

Input:

  New provider notebook added to examples/anthropic/; exclude_notebooks list not updated

Output:

  Workflow executes new notebook; if it requires manual setup, workflow may fail; developer must add notebook name to exclude_notebooks and re-run

Notes:

  Illustrates importance of maintaining exclude_notebooks configuration
