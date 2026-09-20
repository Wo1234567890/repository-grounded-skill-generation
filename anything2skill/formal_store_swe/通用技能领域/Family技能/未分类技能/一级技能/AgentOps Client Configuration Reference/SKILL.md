---
id: "ef599c86-984c-5cf0-829a-39c20176129c"
name: "AgentOps Client Configuration Reference"
description: "Reference documentation of all supported AgentOps client configuration parameters, their purposes, and valid usage patterns. Provides a mapping of parameter names to their purposes and constraints to support integration planning and troubleshooting."
version: "0.1.0"
tags:
  - "configuration"
  - "client_setup"
  - "reference"
  - "agentops"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Developer needs to understand available configuration options during AgentOps client initialization"
  - "Integration planning phase requires parameter reference"
  - "Troubleshooting client behavior requires understanding configuration contract"
---

# AgentOps Client Configuration Reference

Reference documentation of all supported AgentOps client configuration parameters, their purposes, and valid usage patterns. Provides a mapping of parameter names to their purposes and constraints to support integration planning and troubleshooting.

## Prompt

Use this reference to understand available configuration options when initializing the AgentOps client. Each parameter controls a specific aspect of client behavior: api_key and endpoint for service connectivity, max_wait_time and max_queue_size for event queue management, default_tags for session labeling, instrument_llm_calls for LLM call tracking, auto_start_session and skip_auto_end_session for session lifecycle, env_data_opt_out for privacy control, log_level for logging verbosity, fail_safe for error suppression, and exporter/processor/exporter_endpoint for OpenTelemetry trace customization.

## Objective

Document supported configuration options for AgentOps client initialization
## Applicable Signals

- Client initialization in progress
- Configuration parameter selection needed
- Integration design phase

## Contraindications

- Do not use for runtime parameter validation (use Configuration Validation micro-skill instead)
- Do not use when implementing custom exporter or processor logic (refer to OpenTelemetry documentation)

## Constraints

- This is a reference asset; it documents the configuration contract but does not execute validation or initialization
- Parameter validation logic is separate from this reference

## Output Contract

- Clear mapping of parameter names to their purposes and constraints
- Supported parameters: api_key, endpoint, app_url, max_wait_time, max_queue_size, default_tags, instrument_llm_calls, auto_start_session, skip_auto_end_session, env_data_opt_out, log_level, fail_safe, exporter, processor, exporter_endpoint

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Developer needs to understand available configuration options during AgentOps client initialization
- Integration planning phase requires parameter reference
- Troubleshooting client behavior requires understanding configuration contract
