---
id: "9494ffe2-c1cc-5ca4-977e-3dd37018fc5c"
name: "Manual Session Control Pattern"
description: "Defer automatic session creation and manually start sessions with custom tags when finer control over session lifecycle is needed. Use this when multiple independent agent tasks run in sequence and session boundaries must align with business events."
version: "0.1.0"
tags:
  - "session_management"
  - "agent_monitoring"
  - "lifecycle_control"
  - "event_driven"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Multiple independent agent tasks run in sequence"
  - "Session boundaries must align with business events (e.g., customer queries)"
  - "Need to tag sessions for filtering or analysis"
examples:
  - input: "Initialize without auto-start, then trigger session for customer query"
    output: "Session created with tags=['customer-query']; events logged under this session until session ends"
    notes: "Enables per-customer or per-request session isolation"
---

# Manual Session Control Pattern

Defer automatic session creation and manually start sessions with custom tags when finer control over session lifecycle is needed. Use this when multiple independent agent tasks run in sequence and session boundaries must align with business events.

## Prompt

Initialize AgentOps without auto-starting a session using agentops.init(api_key=YOUR_API_KEY, auto_start_session=False). Later, when a specific task or business event occurs, manually invoke agentops.start_session(tags=[...]) with contextual tags to begin event logging for that session scope.

## Objective

Enable explicit session lifecycle management with contextual tagging
## Applicable Signals

- Event-driven session requirement detected
- Task context change or business event boundary
- Custom session metadata needed for downstream filtering

## Contraindications

- Simple single-session monitoring is sufficient
- Auto-start session behavior is acceptable
- Session tags are not needed for filtering or analysis

## Workflow Steps

- {'step': 1, 'action': 'Initialize AgentOps with auto_start_session=False', 'detail': 'agentops.init(api_key=YOUR_API_KEY, auto_start_session=False)'}
- {'step': 2, 'action': 'Wait for task or business event trigger', 'detail': 'Do not start logging until the appropriate session boundary is reached'}
- {'step': 3, 'action': 'Manually start session with contextual tags', 'detail': 'agentops.start_session(tags=[tag1, tag2, ...])'}
- {'step': 4, 'action': 'Event logging begins for this session scope', 'detail': 'All subsequent API calls and events are associated with the tagged session'}

## Constraints

- Must call agentops.init() with auto_start_session=False before any manual session start
- Event logging does not begin until agentops.start_session() is explicitly called
- Tags must be provided as a list to start_session()

## Output Contract

- Session created with specified tags; event logging begins only after manual start_session() call; session is scoped to the specific task context and can be filtered by tags downstream.

## Example Executions

### Example 1

- Input: Initialize without auto-start, then trigger session for customer query
- Output: Session created with tags=['customer-query']; events logged under this session until session ends
- Notes: Enables per-customer or per-request session isolation

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Multiple independent agent tasks run in sequence
- Session boundaries must align with business events (e.g., customer queries)
- Need to tag sessions for filtering or analysis

## Examples

### Example 1

Input:

  Initialize without auto-start, then trigger session for customer query

Output:

  Session created with tags=['customer-query']; events logged under this session until session ends

Notes:

  Enables per-customer or per-request session isolation
