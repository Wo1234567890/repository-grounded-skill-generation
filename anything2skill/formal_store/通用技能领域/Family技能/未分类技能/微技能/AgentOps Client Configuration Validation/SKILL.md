---
id: "3f85747b-f87f-5260-883b-250cb09afa01"
name: "AgentOps Client Configuration Validation"
description: "Validates configuration parameters against a whitelist of supported parameters during AgentOps client initialization or reconfiguration. Logs warnings for invalid parameters and applies only valid parameters to the global client instance."
version: "0.1.0"
tags:
  - "configuration"
  - "validation"
  - "client_setup"
  - "parameter_checking"
  - "agentops"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "AgentOps client instantiation with kwargs"
  - "Client reconfiguration request with configuration parameters"
  - "configure() function invoked with keyword arguments"
---

# AgentOps Client Configuration Validation

Validates configuration parameters against a whitelist of supported parameters during AgentOps client initialization or reconfiguration. Logs warnings for invalid parameters and applies only valid parameters to the global client instance.

## Prompt

When the AgentOps client is instantiated or reconfigured with kwargs, validate each parameter against the valid_params whitelist. Log a warning for any invalid parameters detected. Apply only valid parameters to the global client instance.

## Objective

validate_and_apply_config
## Applicable Signals

- User passes configuration parameters to configure function
- Client initialization phase with custom settings

## Contraindications

- Client is already running with an active session
- Configuration is read-only or immutable after initialization

## Workflow Steps

- Receive kwargs dictionary from caller
- Define valid_params set: {api_key, endpoint, app_url, max_wait_time, max_queue_size, default_tags, instrument_llm_calls, auto_start_session, skip_auto_end_session, env_data_opt_out, log_level, fail_safe, exporter, processor, exporter_endpoint}
- Compute invalid_params as set difference: set(kwargs.keys()) - valid_params
- If invalid_params is non-empty, log warning with parameter names
- Apply valid parameters to global _client instance
- Return success status or configuration object

## Constraints

- Validation must occur before applying parameters to global _client
- Only parameters in valid_params set may be applied
- Invalid parameters must be logged as warnings, not errors

## Cautions

- Do not silently ignore invalid parameters; always log warnings
- Do not raise exceptions for invalid parameters unless fail_safe is disabled
- Preserve case sensitivity of parameter names

## Output Contract

- Configuration parameters are validated against valid_params set; invalid parameters are logged as warnings; global _client is updated with valid configuration; caller receives confirmation of applied settings.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- AgentOps client instantiation with kwargs
- Client reconfiguration request with configuration parameters
- configure() function invoked with keyword arguments
