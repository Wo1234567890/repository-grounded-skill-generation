---
id: "28490fb0-322f-588f-93fe-359021352c0a"
name: "Detect Jupyter Notebook Execution Context"
description: "Check whether code is running inside a Jupyter Notebook (ZMQInteractiveShell) and conditionally disable auto-start behavior for manual trace control. Returns a flag indicating the execution environment to enable environment-aware session initialization."
version: "0.1.0"
tags:
  - "environment_detection"
  - "jupyter"
  - "session_initialization"
  - "runtime_introspection"
  - "conditional_logic"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Session initialization begins"
  - "Tracing client is being configured"
  - "auto_start_session parameter needs to be determined"
examples:
  - input: "Initialization context in a Jupyter Notebook cell"
    output: "auto_start_session = False; manual start_trace() and end_trace() calls required"
    notes: "Jupyter environment detected; user must explicitly manage trace lifecycle"
  - input: "Initialization context in a standard Python script"
    output: "auto_start_session = True (or default); automatic session management enabled"
    notes: "Non-Jupyter environment; NameError caught and passed; auto-start proceeds"
---

# Detect Jupyter Notebook Execution Context

Check whether code is running inside a Jupyter Notebook (ZMQInteractiveShell) and conditionally disable auto-start behavior for manual trace control. Returns a flag indicating the execution environment to enable environment-aware session initialization.

## Prompt

Attempt to detect if the current runtime is a Jupyter Notebook by checking the IPython shell class. If get_ipython() is available and its class name is 'ZMQInteractiveShell', set auto_start_session to False to require manual trace lifecycle control. If get_ipython() raises NameError (non-Jupyter environment), allow auto_start_session to remain True or use the default value. Do not raise exceptions on NameError; treat it as a normal non-Jupyter case.

## Objective

Adapt session initialization behavior based on execution environment
## Applicable Signals

- Initializing a tracing session
- Needing to determine whether to auto-start or require manual start_trace() calls
- Jupyter notebooks require different session lifecycle handling

## Contraindications

- Execution environment is already known from prior detection
- auto-start behavior is mandatory regardless of environment
- NameError handling is not needed or not desired

## Intervention Moves

- Disable auto-start when Jupyter is detected
- Allow manual trace lifecycle control in interactive notebooks
- Preserve default auto-start behavior in non-Jupyter environments

## Workflow Steps

- {'step': 1, 'action': 'Attempt to call get_ipython()', 'condition': 'No precondition; wrapped in try-except'}
- {'step': 2, 'action': "Check if get_ipython().__class__.__name__ equals 'ZMQInteractiveShell'", 'condition': 'get_ipython() succeeded'}
- {'step': 3, 'action': 'Set auto_start_session = False', 'condition': 'Class name matches ZMQInteractiveShell'}
- {'step': 4, 'action': 'Catch NameError and pass (no action)', 'condition': 'get_ipython() is not defined'}
- {'step': 5, 'action': 'Return or use auto_start_session flag in downstream initialization', 'condition': 'Detection complete'}

## Constraints

- Must catch NameError gracefully without re-raising
- Must not modify global state or side effects beyond setting the auto_start_session flag
- Detection must be non-blocking and fast

## Cautions

- get_ipython() may not be available in all Python environments; NameError is expected and normal
- ZMQInteractiveShell class name is specific to Jupyter; other interactive shells may have different class names
- This check should run early in initialization before other session setup

## Output Contract

- auto_start_session flag is set to False if running in Jupyter Notebook, True (or default) otherwise; no exception is raised on NameError; flag is ready for use in session initialization arguments.

## Example Executions

### Example 1

- Input: Initialization context in a Jupyter Notebook cell
- Output: auto_start_session = False; manual start_trace() and end_trace() calls required
- Notes: Jupyter environment detected; user must explicitly manage trace lifecycle

### Example 2

- Input: Initialization context in a standard Python script
- Output: auto_start_session = True (or default); automatic session management enabled
- Notes: Non-Jupyter environment; NameError caught and passed; auto-start proceeds

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Session initialization begins
- Tracing client is being configured
- auto_start_session parameter needs to be determined

## Examples

### Example 1

Input:

  Initialization context in a Jupyter Notebook cell

Output:

  auto_start_session = False; manual start_trace() and end_trace() calls required

Notes:

  Jupyter environment detected; user must explicitly manage trace lifecycle

### Example 2

Input:

  Initialization context in a standard Python script

Output:

  auto_start_session = True (or default); automatic session management enabled

Notes:

  Non-Jupyter environment; NameError caught and passed; auto-start proceeds
