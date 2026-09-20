---
id: "c20f49cc-1854-560a-9f83-89494b3d0cc1"
name: "AgentOps SDK Initialization"
description: "Configures and initializes the AgentOps monitoring SDK with API credentials, session parameters, and instrumentation options to establish agent observability and session tracking."
version: "0.1.0"
tags:
  - "sdk"
  - "initialization"
  - "observability"
  - "monitoring"
  - "session_setup"
  - "agentops"
triggers:
  - "Application startup before agent execution"
  - "When observability instrumentation is required"
  - "Before any agent operations or LLM calls"
---

# AgentOps SDK Initialization

Configures and initializes the AgentOps monitoring SDK with API credentials, session parameters, and instrumentation options to establish agent observability and session tracking.

## Prompt

Call this function at application startup before agent execution begins. Provide api_key and endpoint for authentication. Set instrument_llm_calls to true to capture LLM interactions. Use auto_start_session to automatically begin a monitoring session. Configure max_queue_size and max_wait_time to tune event batching behavior. Set tags and default_tags to label the session. Enable log_session_replay_url to retrieve session replay links. Use fail_safe=true to prevent SDK errors from crashing the application.

## Objective

Initialize SDK with configuration parameters and establish monitoring session
## Applicable Signals

- Application initialization phase
- Need for session-level monitoring
- Requirement to track agent behavior and LLM interactions

## Contraindications

- SDK already initialized in current process
- No monitoring or observability needed
- Resource-constrained environments where session overhead is unacceptable

## Workflow Steps

- {'step': 1, 'action': 'Provide authentication credentials', 'detail': 'Supply api_key and endpoint parameters for SDK authentication'}
- {'step': 2, 'action': 'Configure session parameters', 'detail': 'Set trace_name, tags, default_tags, and app_url to identify and label the session'}
- {'step': 3, 'action': 'Enable instrumentation', 'detail': 'Set instrument_llm_calls=true to capture LLM call events; configure auto_start_session and auto_init for automatic lifecycle management'}
- {'step': 4, 'action': 'Tune queue and timing behavior', 'detail': 'Set max_queue_size and max_wait_time to control event batching and flush frequency'}
- {'step': 5, 'action': 'Configure output and safety', 'detail': 'Set log_session_replay_url=true to enable session replay retrieval; set fail_safe=true to prevent SDK errors from crashing the application'}

## Constraints

- Must be called once per application lifecycle
- Requires valid api_key and endpoint for remote monitoring
- auto_start_session and auto_init parameters control automatic session lifecycle

## Cautions

- If fail_safe is false, SDK initialization errors will propagate to caller
- env_data_opt_out controls whether environment metadata is collected
- log_level affects verbosity of SDK logging output

## Output Contract

- SDK initialized with active session, monitoring endpoints configured, instrumentation active, and ready to capture agent events and LLM interactions

## Triggers

- Application startup before agent execution
- When observability instrumentation is required
- Before any agent operations or LLM calls
