---
id: "ae4e8bc5-4993-5ebb-8b0e-8a67099bc41b"
name: "Session Tagging for Organization and Filtering"
description: "Attach organizational tags to AgentOps sessions at initialization or session start to enable later filtering and categorization of session records by environment, feature, service tier, or other organizational dimensions."
version: "0.1.0"
tags:
  - "session_management"
  - "metadata"
  - "organization"
  - "filtering"
  - "agentops"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new AgentOps session"
  - "Need to categorize or filter session later by environment, feature, or tier"
examples:
  - input: "agentops.init(api_key=\"YOUR_API_KEY\", tags=[\"production\", \"web-app\"])"
    output: "Session initialized with tags attached to metadata; tags queryable for filtering"
    notes: "Tags attached during initialization phase"
  - input: "agentops.start_session(tags=[\"customer-service\", \"tier-1\"])"
    output: "Session started with tags attached to metadata; tags queryable for filtering"
    notes: "Tags attached during manual session start"
---

# Session Tagging for Organization and Filtering

Attach organizational tags to AgentOps sessions at initialization or session start to enable later filtering and categorization of session records by environment, feature, service tier, or other organizational dimensions.

## Prompt

Call agentops.init() or agentops.start_session() with a tags parameter containing a list of string labels. Tags are attached to the session metadata and become queryable for filtering and organization.

## Objective

Attach tags to session for organization and filtering
## Applicable Signals

- Session initialization phase
- Requirement to organize sessions by environment (production, staging, development)
- Requirement to organize sessions by feature or service tier

## Contraindications

- Tags are not needed for session discovery or filtering
- Session is already running and tag attachment is not supported mid-session

## Workflow Steps

- {'step': 1, 'action': 'Prepare tag list', 'detail': 'Create a list of string tags representing the session category (e.g., environment, feature, tier)'}
- {'step': 2, 'action': 'Attach tags at initialization', 'detail': 'Pass tags parameter to agentops.init() or agentops.start_session()'}
- {'step': 3, 'action': 'Verify attachment', 'detail': 'Confirm tags appear in session metadata and are queryable'}

## Constraints

- Tags must be provided as a list of strings
- Tags must be attached at initialization or session start time
- Tag attachment after session start is not supported

## Output Contract

- Tags successfully attached to session object
- Tags appear in session metadata and are queryable for filtering and categorization

## Example Executions

### Example 1

- Input: agentops.init(api_key="YOUR_API_KEY", tags=["production", "web-app"])
- Output: Session initialized with tags attached to metadata; tags queryable for filtering
- Notes: Tags attached during initialization phase

### Example 2

- Input: agentops.start_session(tags=["customer-service", "tier-1"])
- Output: Session started with tags attached to metadata; tags queryable for filtering
- Notes: Tags attached during manual session start

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new AgentOps session
- Need to categorize or filter session later by environment, feature, or tier

## Examples

### Example 1

Input:

  agentops.init(api_key="YOUR_API_KEY", tags=["production", "web-app"])

Output:

  Session initialized with tags attached to metadata; tags queryable for filtering

Notes:

  Tags attached during initialization phase

### Example 2

Input:

  agentops.start_session(tags=["customer-service", "tier-1"])

Output:

  Session started with tags attached to metadata; tags queryable for filtering

Notes:

  Tags attached during manual session start
