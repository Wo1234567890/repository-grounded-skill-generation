---
id: "0a2a2531-de87-56a6-b24c-ab18b66de26d"
name: "Singleton Client Initialization"
description: "Initialize and manage a singleton Client instance for AgentOps service, ensuring only one active client exists throughout the application lifecycle."
version: "0.1.0"
tags:
  - "singleton"
  - "initialization"
  - "client_lifecycle"
  - "agentops"
triggers:
  - "Application startup requires AgentOps client connection"
  - "First invocation of Client() constructor"
---

# Singleton Client Initialization

Initialize and manage a singleton Client instance for AgentOps service, ensuring only one active client exists throughout the application lifecycle.

## Prompt

Implement singleton pattern for Client class: check __instance class variable; if None, create new instance with config, _initialized flag, _init_trace_context, and _legacy_session_for_init_trace; return the single instance on all subsequent calls.

## Objective

Establish single Client instance with trace context and session state
## Applicable Signals

- Client class instantiation request
- No active __instance exists

## Contraindications

- Multiple independent Client instances are required
- Testing scenarios requiring isolated clients

## Workflow Steps

- Check if __instance class variable is None
- If None: instantiate new Client with config, _initialized=False, _init_trace_context=None, _legacy_session_for_init_trace=None
- Set _initialized to True
- Store _init_trace_context if auto-trace enabled
- Store _legacy_session_for_init_trace if legacy session wrapper required
- Return __instance

## Constraints

- Only one __instance may be active per application lifecycle
- _initialized flag must be set to True after successful initialization
- Trace context and session state must be stored if auto-trace is enabled

## Cautions

- Thread safety: singleton pattern may require locking in multi-threaded environments
- Ensure config is valid before Client instantiation

## Output Contract

- Single __instance variable populated; _initialized flag set to True; _init_trace_context and _legacy_session_for_init_trace stored if auto-trace enabled; subsequent calls return same instance without re-initialization

## Triggers

- Application startup requires AgentOps client connection
- First invocation of Client() constructor
