---
id: "62dc23d5-43a2-5633-9c5a-97701033acac"
name: "Application Performance Monitoring with OpenTelemetry"
description: "Configures and initializes the AgentOps monitoring and debugging SDK with API credentials, session parameters, and instrumentation options. Establishes observability infrastructure for agent applications."
version: "0.1.3"
tags:
  - "initialization"
  - "observability"
  - "sdk_setup"
  - "session_management"
  - "configuration"
triggers:
  - "Application is moving to production"
  - "Distributed tracing is required for debugging"
  - "Performance metrics need to be collected and exported"
  - "Observability platform is available and configured"
---

# Application Performance Monitoring with OpenTelemetry

Configures and initializes the AgentOps monitoring and debugging SDK with API credentials, session parameters, and instrumentation options. Establishes observability infrastructure for agent applications.

## Prompt

Call init() with required and optional parameters: api_key (authentication), endpoint (server address), app_url (dashboard URL), max_wait_time (queue flush timeout), max_queue_size (event buffer limit), tags (session labels), trace_name (session identifier), instrument_llm_calls (enable LLM call tracing), auto_start_session (begin session automatically), auto_init (auto-initialize on first use), skip_auto_end_session (manual session end), env_data_opt_out (disable environment telemetry), log_level (logging verbosity), fail_safe (continue on SDK errors), log_session_replay_url (output replay link), exporter_endpoint (custom telemetry endpoint). Returns initialized SDK instance with active session and configured instrumentation.

## Objective

Initialize SDK with configuration parameters and activate observability session
## Applicable Signals

- Application startup phase
- First-time SDK invocation
- New session creation request

## Contraindications

- SDK is already initialized in the current process
- Agent operates in offline-only mode without telemetry requirements
- Observability is explicitly disabled or not required

## Workflow Steps

- Validate api_key and endpoint parameters
- Configure session parameters (trace_name, tags, default_tags)
- Set instrumentation options (instrument_llm_calls, auto_start_session)
- Configure queue and timeout parameters (max_queue_size, max_wait_time)
- Set logging level and exporter endpoint
- Initialize SDK instance and activate session if auto_start_session=True

## Constraints

- api_key must be valid and authorized
- endpoint must be reachable and properly formatted
- max_queue_size and max_wait_time must be positive integers if specified
- Only one active SDK instance per process

## Cautions

- Initialization failure with fail_safe=False will raise exceptions; set fail_safe=True for graceful degradation
- auto_start_session=True begins session immediately; set False for manual control
- env_data_opt_out=True disables environment metadata collection; may reduce debugging context

## Output Contract

- SDK initialized with active session, endpoint configured, instrumentation enabled per parameters, and ready to log events and traces. Caller receives initialized SDK instance that can immediately accept event logging and session management calls.

## Triggers

- Application is moving to production
- Distributed tracing is required for debugging
- Performance metrics need to be collected and exported
- Observability platform is available and configured
