---
id: "db7d6c09-b85e-5ef5-b1cc-54656bec2509"
name: "Initialize Package Instrumentation"
description: "Start monitoring and instrumenting Python packages using import hooks if not already active. Prevents duplicate instrumentation and respects agentic library precedence by checking _has_agentic_library flag and _active_instrumentors collection."
version: "0.1.0"
tags:
  - "instrumentation"
  - "import_hook"
  - "initialization"
  - "monitoring"
  - "agentops"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "AgentOps monitoring needs to begin"
  - "_active_instrumentors is empty"
  - "No agentic library is already instrumented"
---

# Initialize Package Instrumentation

Start monitoring and instrumenting Python packages using import hooks if not already active. Prevents duplicate instrumentation and respects agentic library precedence by checking _has_agentic_library flag and _active_instrumentors collection.

## Prompt

Call this skill at system startup or when AgentOps monitoring needs to begin. The skill checks if instrumentation is already active by examining _active_instrumentors. If empty, it replaces builtins.__import__ with _import_monitor to intercept all module loads. If an agentic library (OpenAI, Anthropic, CrewAI, AG2/AutoGen, Google GenAI, IBM WatsonX, Google ADK, Agno, Mem0, smolagents) is detected as already instrumented, the skill returns early to avoid conflicts.

## Objective

Set up runtime instrumentation of package imports with safety guards against duplicate and conflicting instrumentation
## Applicable Signals

- System startup or initialization phase
- _active_instrumentors collection is empty
- _has_agentic_library flag is False

## Contraindications

- An agentic library (OpenAI, Anthropic, CrewAI, AG2/AutoGen, Google GenAI, IBM WatsonX, Google ADK, Agno, Mem0, smolagents) is already instrumented
- Instrumentation is already active (_active_instrumentors is non-empty)

## Workflow Steps

- {'step': 1, 'action': 'Check if _active_instrumentors is empty', 'condition': 'If empty, proceed; if non-empty, return (already initialized)'}
- {'step': 2, 'action': 'Replace builtins.__import__ with _import_monitor', 'condition': 'Only if _active_instrumentors was empty'}
- {'step': 3, 'action': 'Check _has_agentic_library flag', 'condition': 'If True, return immediately to avoid conflicts'}
- {'step': 4, 'action': 'Iterate through sys.modules.keys()', 'condition': 'For each module, check if it is a ModuleType instance'}
- {'step': 5, 'action': 'For each valid module, check if package_to_check is in _instrumenting_packages or already instrumented', 'condition': 'If not instrumented, retrieve target_module_obj from sys.modules'}
- {'step': 6, 'action': 'Break loop if _has_agentic_library becomes True during iteration', 'condition': 'Prevents further instrumentation if agentic library is detected'}

## Constraints

- Must check _has_agentic_library before proceeding
- Must iterate through sys.modules.keys() safely; break if agentic library is detected during iteration
- Must verify module type before processing (isinstance check for ModuleType)
- Must not instrument packages already in _instrumenting_packages

## Cautions

- Replacing builtins.__import__ is a global operation; ensure no other import hooks conflict
- Early return if agentic library detected prevents cascading instrumentation

## Output Contract

- builtins.__import__ is replaced with _import_monitor; _active_instrumentors is populated; system is ready to intercept module loads. Returns early without modification if agentic library is already instrumented or if instrumentation is already active.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- AgentOps monitoring needs to begin
- _active_instrumentors is empty
- No agentic library is already instrumented
