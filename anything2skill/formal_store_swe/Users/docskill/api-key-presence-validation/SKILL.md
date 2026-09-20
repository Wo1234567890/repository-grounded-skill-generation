---
id: "0dac1628-ec7a-5e9f-808d-1a0a8b514899"
name: "API Key Presence Validation"
description: "Validates that an API key is present and non-empty in the Client configuration during initialization. Raises NoApiKeyException if the API key is missing, preventing Client initialization from completing without valid credentials."
version: "0.1.0"
tags:
  - "credential_validation"
  - "precondition_check"
  - "initialization_guard"
  - "api_security"
triggers:
  - "After Client configuration is loaded"
  - "Before any API operations are attempted"
  - "During Client initialization flow"
---

# API Key Presence Validation

Validates that an API key is present and non-empty in the Client configuration during initialization. Raises NoApiKeyException if the API key is missing, preventing Client initialization from completing without valid credentials.

## Prompt

Check if self.config.api_key is set and non-empty. If the API key is missing, None, or an empty string, raise NoApiKeyException immediately with a clear, actionable error message. Do not expose the actual API key value in any error logs or messages. This validation must execute after Client configuration is loaded but before any API operations proceed.

## Objective

Enforce API key presence before Client initialization completes
## Applicable Signals

- Client.__init__() execution reaches configuration validation phase
- config object is instantiated and ready for inspection

## Contraindications

- Do not apply if API key is already confirmed present in prior validation step
- Do not apply in offline or mock testing modes where credentials are not required
- Do not apply if caller explicitly opts out of credential validation

## Workflow Steps

- {'step': 1, 'action': 'Inspect self.config.api_key', 'condition': 'Configuration object exists'}
- {'step': 2, 'action': 'Check if api_key is None or empty string', 'condition': 'No precondition'}
- {'step': 3, 'action': 'Raise NoApiKeyException if check fails', 'condition': 'api_key is falsy'}
- {'step': 4, 'action': 'Allow execution to proceed', 'condition': 'api_key is present and non-empty'}

## Constraints

- Must execute synchronously before returning from initialization
- Must not suppress or log-only the exception; must raise it to caller
- API key check must validate non-empty string, not just non-None
- Must execute after Client configuration object is instantiated

## Cautions

- Ensure exception message is clear and actionable for developers
- Do not expose actual API key values in error logs or messages
- This is a hard blocker; no fallback or retry logic should bypass it

## Output Contract

- If api_key is present and non-empty: execution proceeds to next initialization step. If api_key is missing or empty: NoApiKeyException is raised with clear error message; Client initialization halts.

## Triggers

- After Client configuration is loaded
- Before any API operations are attempted
- During Client initialization flow
