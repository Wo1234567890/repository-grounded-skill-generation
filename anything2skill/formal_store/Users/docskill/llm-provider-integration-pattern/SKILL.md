---
id: "9c94fdb4-079e-5b48-9d89-aa66d04b09e6"
name: "LLM Provider Integration Pattern"
description: "Establish a reusable provider class that inherits from BaseProvider, implements required LLM response handling methods, and manages event tracking for prompts, tokens, and errors."
version: "0.1.0"
tags:
  - "llm_integration"
  - "provider_pattern"
  - "event_tracking"
  - "class_inheritance"
  - "method_override"
triggers:
  - "Adding support for a new LLM provider"
  - "Extending existing provider functionality"
  - "Implementing provider-level integration with AgentOps"
---

# LLM Provider Integration Pattern

Establish a reusable provider class that inherits from BaseProvider, implements required LLM response handling methods, and manages event tracking for prompts, tokens, and errors.

## Prompt

To integrate a new LLM provider into the AgentOps framework:

1. Create a new provider class in the agentops/llms/ directory that inherits from BaseProvider using the @singleton decorator.
2. In __init__, call super().__init__(client) and set self._provider_name to the provider's name.
3. Implement handle_response() to process LLM responses.
4. Implement override() to patch the provider's methods for event tracking.
5. Implement undo_override() to restore original methods.
6. Ensure event tracking captures prompts, completions, token usage, timestamps, errors, and tool usage (if applicable).

## Objective

Integrate a new LLM provider into the AgentOps framework
## Applicable Signals

- New LLM provider needs to be supported
- Provider methods require instrumentation for event tracking
- Integration with BaseProvider framework is required

## Contraindications

- Do not use when modifying the core BaseProvider class itself
- Do not use for debugging individual LLM calls without provider-level changes
- Do not use for provider-agnostic response handling

## Workflow Steps

- {'step': 1, 'action': 'Create provider class', 'detail': 'Define new class in agentops/llms/ that inherits from BaseProvider with @singleton decorator'}
- {'step': 2, 'action': 'Initialize provider', 'detail': 'Call super().__init__(client) and set _provider_name attribute'}
- {'step': 3, 'action': 'Implement handle_response()', 'detail': 'Process LLM responses and extract relevant data'}
- {'step': 4, 'action': 'Implement override()', 'detail': 'Patch provider methods to enable event tracking'}
- {'step': 5, 'action': 'Implement undo_override()', 'detail': 'Restore original provider methods'}
- {'step': 6, 'action': 'Configure event tracking', 'detail': 'Ensure prompts, completions, tokens, timestamps, errors, and tool usage are tracked'}

## Constraints

- Provider class must inherit from BaseProvider
- Must use @singleton decorator
- Must implement all three required methods: handle_response(), override(), undo_override()
- Event tracking must capture prompts, completions, token usage, timestamps, and errors

## Output Contract

- A new provider class that successfully inherits from BaseProvider, implements handle_response(), override(), and undo_override() methods, and passes event tracking tests. The provider is ready for integration into the AgentOps framework.

## Triggers

- Adding support for a new LLM provider
- Extending existing provider functionality
- Implementing provider-level integration with AgentOps
