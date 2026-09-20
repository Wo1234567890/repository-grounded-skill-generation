---
id: "97383e49-571c-52c0-b2d6-94994add9342"
name: "Logarithmic Scale Configuration"
description: "Initialize AgentOps monitoring with automatic or manual session creation, associating all subsequent events and API calls with a tracking session."
version: "0.1.1"
tags:
  - "monitoring"
  - "session_management"
  - "initialization"
  - "event_tracking"
  - "debugging"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Data spans multiple orders of magnitude"
  - "Logarithmic visual encoding is required"
  - "Tick labels and domain bounds need standardization"
examples:
  - input: "Start agent with automatic session creation"
    output: "agentops.init(api_key='YOUR_API_KEY') → Active session created immediately; all subsequent calls logged"
    notes: "Default behavior; simplest setup"
  - input: "Start agent with deferred session creation"
    output: "agentops.init(api_key='YOUR_API_KEY', auto_start_session=False) followed by agentops.start_session(tags=['customer-query']) → Session created on demand with custom tags"
    notes: "Allows fine-grained control over session timing and labeling"
---

# Logarithmic Scale Configuration

Initialize AgentOps monitoring with automatic or manual session creation, associating all subsequent events and API calls with a tracking session.

## Prompt

Call agentops.init() with your API key to set up event tracking. By default, a session starts automatically. For manual control, pass auto_start_session=False and call agentops.start_session() later with optional tags to label the session context.

## Objective

Set up event tracking session for agent execution monitoring
## Applicable Signals

- Agent application startup
- Workflow initialization phase
- Monitoring requirement detected

## Contraindications

- Session is already active
- Monitoring is not required
- Test environments where tracking overhead is unacceptable

## Workflow Steps

- {'step': 1, 'action': 'Call agentops.init(api_key=YOUR_API_KEY) to initialize with automatic session creation', 'condition': 'Default behavior; use when immediate session tracking is needed'}
- {'step': 2, 'action': 'Alternatively, call agentops.init(api_key=YOUR_API_KEY, auto_start_session=False) to defer session creation', 'condition': 'When you need manual control over session timing'}
- {'step': 3, 'action': 'Call agentops.start_session(tags=[...]) at the appropriate time to begin tracking', 'condition': 'Only if auto_start_session=False was set; tags are optional and used for session labeling'}

## Constraints

- API key must be valid and provided
- Only one session should be active per context at a time
- Manual session start requires prior init() call with auto_start_session=False

## Cautions

- Ensure API key is kept secure and not hardcoded in production
- Session initialization must complete before agent operations begin to ensure full event capture

## Output Contract

- Active AgentOps session with API key validated and event association established; all subsequent agent operations are automatically logged to the session.

## Example Executions

### Example 1

- Input: Start agent with automatic session creation
- Output: agentops.init(api_key='YOUR_API_KEY') → Active session created immediately; all subsequent calls logged
- Notes: Default behavior; simplest setup

### Example 2

- Input: Start agent with deferred session creation
- Output: agentops.init(api_key='YOUR_API_KEY', auto_start_session=False) followed by agentops.start_session(tags=['customer-query']) → Session created on demand with custom tags
- Notes: Allows fine-grained control over session timing and labeling

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Data spans multiple orders of magnitude
- Logarithmic visual encoding is required
- Tick labels and domain bounds need standardization

## Examples

### Example 1

Input:

  Start agent with automatic session creation

Output:

  agentops.init(api_key='YOUR_API_KEY') → Active session created immediately; all subsequent calls logged

Notes:

  Default behavior; simplest setup

### Example 2

Input:

  Start agent with deferred session creation

Output:

  agentops.init(api_key='YOUR_API_KEY', auto_start_session=False) followed by agentops.start_session(tags=['customer-query']) → Session created on demand with custom tags

Notes:

  Allows fine-grained control over session timing and labeling
