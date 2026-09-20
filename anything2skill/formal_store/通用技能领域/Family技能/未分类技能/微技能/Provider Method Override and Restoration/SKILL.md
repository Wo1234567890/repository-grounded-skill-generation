---
id: "c4c70be4-b31e-59d7-b98f-d26308951e25"
name: "Provider Method Override and Restoration"
description: "Patch and restore LLM provider methods to enable transparent event capture (prompts, completions, tokens, timestamps, errors, tool usage) without modifying client code. Implements override() to inject wrapper functions and undo_override() to restore original methods."
version: "0.1.0"
tags:
  - "llm_integration"
  - "method_patching"
  - "event_capture"
  - "provider_instrumentation"
  - "transparent_interception"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Provider class instantiation requires method interception"
  - "LLM call event capture is needed without client code modification"
  - "Session setup phase for transparent provider instrumentation"
---

# Provider Method Override and Restoration

Patch and restore LLM provider methods to enable transparent event capture (prompts, completions, tokens, timestamps, errors, tool usage) without modifying client code. Implements override() to inject wrapper functions and undo_override() to restore original methods.

## Prompt

When a provider class needs to intercept LLM calls:
1. In override(): Patch the provider's methods to capture prompts, completions, token usage, timestamps, errors, and tool usage.
2. In undo_override(): Restore original methods to their pre-patch state.
Ensure patching is transparent to the client and restoration leaves no side effects.

## Objective

Patch and restore provider methods for event interception
## Applicable Signals

- Provider inherits from BaseProvider
- Client code uses standard LLM provider methods
- Event tracking (prompts, completions, tokens, errors) is required

## Contraindications

- Provider does not support method patching or uses immutable method bindings
- Client code already wraps or patches LLM calls independently
- Provider methods are protected or cannot be safely overridden

## Intervention Moves

- override(): Patch provider methods to intercept and log events
- undo_override(): Restore original methods after session completion

## Workflow Steps

- {'step': 1, 'action': 'Store references to original provider methods before patching'}
- {'step': 2, 'action': 'Define wrapper functions that capture events (prompts, completions, tokens, timestamps, errors, tool usage)'}
- {'step': 3, 'action': 'Replace provider methods with wrapper functions via override()'}
- {'step': 4, 'action': 'Execute LLM calls; wrappers transparently capture events and delegate to original methods'}
- {'step': 5, 'action': 'Call undo_override() to restore original methods from stored references'}
- {'step': 6, 'action': 'Verify restoration: confirm original methods are active and no patches remain'}

## Constraints

- Patching must not modify client-facing API or behavior
- Original methods must be fully restorable without state leakage
- Event capture must occur transparently during method execution

## Cautions

- Ensure patched methods preserve exception handling and return types
- Test restoration to confirm no lingering patches after undo_override()
- Handle concurrent or nested provider calls during patching window

## Output Contract

- Provider methods are patched to capture events (prompts, completions, token usage, timestamps, errors, tool usage); original methods are restored without side effects or state leakage after session completion.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Provider class instantiation requires method interception
- LLM call event capture is needed without client code modification
- Session setup phase for transparent provider instrumentation
