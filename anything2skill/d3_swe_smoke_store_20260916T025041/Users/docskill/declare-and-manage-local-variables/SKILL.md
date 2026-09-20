---
id: "82d405b7-2d06-5f3a-9591-ba6f11452199"
name: "Declare and Manage Local Variables"
description: "Create, set, retrieve, and remove scoped local variables in D3 contexts. Use when you need isolated state that does not pollute global scope or require explicit lifecycle management."
version: "0.1.0"
tags:
  - "d3"
  - "state_management"
  - "scoping"
  - "variable_lifecycle"
  - "dom_binding"
triggers:
  - "Need to store data bound to a specific D3 selection or DOM node"
  - "Require isolated state without global side effects"
  - "Managing per-element or per-context metadata"
---

# Declare and Manage Local Variables

Create, set, retrieve, and remove scoped local variables in D3 contexts. Use when you need isolated state that does not pollute global scope or require explicit lifecycle management.

## Prompt

Use d3.local() to declare a new local variable. Call local.set(node, value) to assign a value to a specific DOM node or selection context. Call local.get(node) to retrieve the value. Call local.remove(node) to delete the variable from that context. Call local.toString() to inspect the property identifier. This pattern ensures state remains bound to its execution context without affecting global scope.

## Objective

Manage scoped local variable lifecycle
## Applicable Signals

- Selection-scoped data storage requirement
- Execution context isolation needed
- Lifecycle-bound variable management

## Contraindications

- Persistent cross-session state required
- Global configuration or shared data across unrelated components
- Data that must survive component unmounting

## Workflow Steps

- {'step': 1, 'action': 'Declare a new local variable', 'detail': 'Call d3.local() to create a new local variable instance'}
- {'step': 2, 'action': 'Set value in context', 'detail': 'Call local.set(node, value) to bind a value to a specific DOM node or selection'}
- {'step': 3, 'action': 'Retrieve value', 'detail': 'Call local.get(node) to access the stored value from the same context'}
- {'step': 4, 'action': 'Inspect identifier (optional)', 'detail': 'Call local.toString() to get the property identifier for debugging'}
- {'step': 5, 'action': 'Clean up', 'detail': 'Call local.remove(node) to delete the variable when context is no longer needed'}

## Constraints

- Local variables are bound to specific DOM nodes or execution contexts
- Values are not automatically serialized or persisted
- Removal must be explicit; garbage collection depends on node lifecycle

## Cautions

- Do not use for application-wide state; use a state management library instead
- Ensure local.remove() is called when context is destroyed to prevent memory leaks
- Local variables are not visible in browser DevTools; use local.toString() for debugging

## Output Contract

- Local variable is created, assigned a value, retrieved on demand, and removed when no longer needed. No global namespace pollution occurs. Caller receives isolated, context-bound state that persists only for the lifetime of the associated DOM node or execution context.

## Triggers

- Need to store data bound to a specific D3 selection or DOM node
- Require isolated state without global side effects
- Managing per-element or per-context metadata
