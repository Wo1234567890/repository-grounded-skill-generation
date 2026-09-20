---
id: "080b9d08-e952-56df-8d89-d09f39ae4f19"
name: "Initialize AgentOps Session with Manual Control"
description: "Initialize the AgentOps SDK with auto_start_session=False to enable manual session lifecycle management. Use when you need explicit control over when tracing begins and ends."
version: "0.1.0"
tags:
  - "agentops"
  - "sdk_initialization"
  - "session_management"
  - "manual_control"
  - "tracing"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Application requires manual control over session lifecycle"
  - "Setup operations must complete before tracing begins"
  - "Conditional session start based on runtime state"
examples:
  - input: "Application needs to initialize AgentOps but defer tracing until database connection is established"
    output: "agentops.init(auto_start_session=False) called; @trace decorated functions defined; session.start() called after db connection succeeds"
    notes: "Ensures tracing only begins when all dependencies are ready"
---

# Initialize AgentOps Session with Manual Control

Initialize the AgentOps SDK with auto_start_session=False to enable manual session lifecycle management. Use when you need explicit control over when tracing begins and ends.

## Prompt

Call agentops.init() with auto_start_session=False before defining traced functions. This defers session start until you explicitly call session.start(). Useful when other setup must complete before tracing begins.

## Objective

Set up AgentOps SDK initialization with deferred session start
## Applicable Signals

- Need to defer tracing until after initialization
- Multi-stage setup with dependencies
- Explicit session lifecycle management required

## Contraindications

- Automatic session management is acceptable
- No manual session.start() call will be made
- Simple fire-and-forget tracing is sufficient

## Workflow Steps

- {'step': 1, 'action': 'Import agentops and decorators', 'detail': 'from agentops import init; from agentops.sdk.decorators import trace'}
- {'step': 2, 'action': 'Call agentops.init() with auto_start_session=False', 'detail': 'agentops.init(auto_start_session=False)'}
- {'step': 3, 'action': 'Define traced functions using @trace decorator', 'detail': '@trace(name="workflow-name", tags=[...]) def my_function(): ...'}
- {'step': 4, 'action': 'Manually start session when ready', 'detail': 'Call session.start() after all setup is complete'}

## Constraints

- Must call agentops.init() before defining @trace decorated functions
- Must explicitly call session.start() after initialization completes
- Session remains in stopped state until manual start

## Cautions

- If session.start() is never called, tracing will not occur
- Ensure initialization order: init() → setup → session.start()

## Output Contract

- AgentOps SDK initialized with session in stopped state, ready for manual start() call. Traced functions are registered but not actively tracing until session.start() is invoked.

## Example Executions

### Example 1

- Input: Application needs to initialize AgentOps but defer tracing until database connection is established
- Output: agentops.init(auto_start_session=False) called; @trace decorated functions defined; session.start() called after db connection succeeds
- Notes: Ensures tracing only begins when all dependencies are ready

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Application requires manual control over session lifecycle
- Setup operations must complete before tracing begins
- Conditional session start based on runtime state

## Examples

### Example 1

Input:

  Application needs to initialize AgentOps but defer tracing until database connection is established

Output:

  agentops.init(auto_start_session=False) called; @trace decorated functions defined; session.start() called after db connection succeeds

Notes:

  Ensures tracing only begins when all dependencies are ready
