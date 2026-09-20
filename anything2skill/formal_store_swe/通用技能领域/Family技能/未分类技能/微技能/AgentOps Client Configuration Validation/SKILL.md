---
id: "4d929a45-8acb-52fc-a9ff-d895f5661c60"
name: "AgentOps Client Configuration Validation"
description: "Validates incoming configuration parameters against a whitelist of supported AgentOps client settings, logging warnings for invalid parameters before client initialization."
version: "0.1.0"
tags:
  - "configuration"
  - "validation"
  - "parameter_check"
  - "client_initialization"
  - "guardrail"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "AgentOps client is being configured with keyword arguments"
  - "Before instantiating or updating the global client instance"
---

# AgentOps Client Configuration Validation

Validates incoming configuration parameters against a whitelist of supported AgentOps client settings, logging warnings for invalid parameters before client initialization.

## Prompt

Check all keyword arguments passed to the client configuration against the valid_params whitelist. Identify any parameters not in the whitelist and log them as warnings. Allow valid parameters to proceed to client initialization without interruption.

## Objective

Validate configuration parameters against supported whitelist
## Applicable Signals

- kwargs dict passed to configure() function
- Presence of user-supplied configuration parameters

## Contraindications

- Configuration is hardcoded or sourced from a trusted internal factory
- No user-supplied kwargs present
- Configuration bypass mode is explicitly enabled

## Intervention Moves

- Log warning for each invalid parameter detected
- Pass valid parameters through to client initialization

## Workflow Steps

- {'step': 1, 'action': 'Define valid_params whitelist', 'detail': 'Maintain set of supported parameters: api_key, endpoint, app_url, max_wait_time, max_queue_size, default_tags, instrument_llm_calls, auto_start_session, skip_auto_end_session, env_data_opt_out, log_level, fail_safe, exporter, processor, exporter_endpoint'}
- {'step': 2, 'action': 'Extract invalid parameters', 'detail': 'Compute set difference: invalid_params = set(kwargs.keys()) - valid_params'}
- {'step': 3, 'action': 'Log warnings for invalid parameters', 'detail': 'If invalid_params is non-empty, log warning message identifying the invalid parameters'}
- {'step': 4, 'action': 'Pass valid parameters forward', 'detail': 'Return or allow only valid parameters to proceed to client initialization'}

## Constraints

- Must check all kwargs keys against the valid_params whitelist
- Must not block valid parameters from proceeding
- Must log warnings for invalid parameters, not raise exceptions

## Cautions

- Warnings are logged but do not block execution; caller must monitor logs to detect misconfiguration
- Whitelist must be kept in sync with actual supported parameters across client versions

## Output Contract

- All invalid parameters identified and logged; valid parameters passed through to client initialization without interruption. Caller receives confirmation that validation completed and any warnings issued.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- AgentOps client is being configured with keyword arguments
- Before instantiating or updating the global client instance
