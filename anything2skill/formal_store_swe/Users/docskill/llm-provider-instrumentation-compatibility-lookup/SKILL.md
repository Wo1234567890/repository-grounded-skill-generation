---
id: "b563919d-c70f-5b34-a5f8-aff7efb13aa9"
name: "LLM Provider Instrumentation Compatibility Lookup"
description: "Reference skill for verifying LLM provider support and minimum version requirements before planning OpenTelemetry instrumentation integration. Provides static compatibility matrix to confirm whether a target provider can be instrumented and what minimum library version is required."
version: "0.1.0"
tags:
  - "instrumentation"
  - "compatibility"
  - "reference"
  - "provider_support"
  - "version_matrix"
  - "opentelemetry"
triggers:
  - "Caller needs to verify if a specific LLM provider can be instrumented"
  - "Caller must check minimum version requirements before integration"
  - "Caller is planning instrumentation scope and needs provider support confirmation"
examples:
  - input: "Provider: OpenAI, Current version: v1.3.0"
    output: "Supported. Minimum version: v0.27.0+ or v1.0.0+. Current version v1.3.0 meets requirement."
    notes: "OpenAI has two supported version tracks."
  - input: "Provider: Anthropic, Current version: v0.6.0"
    output: "Not supported. Minimum version required: v0.7.0+. Current version v0.6.0 is below threshold."
    notes: "Caller should upgrade Anthropic library before instrumentation."
  - input: "Provider: CrewAI, Current version: v0.56.0"
    output: "Supported. Minimum version: v0.56.0+. Current version meets requirement."
    notes: "CrewAI is at minimum threshold."
---

# LLM Provider Instrumentation Compatibility Lookup

Reference skill for verifying LLM provider support and minimum version requirements before planning OpenTelemetry instrumentation integration. Provides static compatibility matrix to confirm whether a target provider can be instrumented and what minimum library version is required.

## Prompt

Consult this registry to determine if a target LLM provider is supported for OpenTelemetry instrumentation and what minimum version is required. Use the provider name and current version to confirm compatibility before proceeding with instrumentation planning.

## Objective

Provide version compatibility and provider support matrix for instrumentation planning
## Applicable Signals

- Provider name provided by caller
- Current or target version of LLM library available
- Planning phase: before instrumentation implementation begins

## Contraindications

- Do not use for runtime instrumentation decisions
- Do not use for dynamic provider detection during execution
- Do not use for version negotiation or fallback logic

## Workflow Steps

- Receive provider name and current version from caller
- Look up provider in supported instrumentors registry
- Compare current version against minimum version threshold
- Return compatibility status and version requirement

## Constraints

- Registry is static; reflects supported providers at documentation time
- Minimum versions are hard requirements; older versions are not supported
- Only listed providers are instrumented; unlisted providers require custom implementation

## Output Contract

- Confirmed provider support status (supported/unsupported) and minimum version threshold for target LLM library. If provider is supported, return minimum version string (e.g., 'v0.27.0+'); if unsupported, return null or 'not_listed'. Include note if current version meets or fails to meet requirement.

## Example Executions

### Example 1

- Input: Provider: OpenAI, Current version: v1.3.0
- Output: Supported. Minimum version: v0.27.0+ or v1.0.0+. Current version v1.3.0 meets requirement.
- Notes: OpenAI has two supported version tracks.

### Example 2

- Input: Provider: Anthropic, Current version: v0.6.0
- Output: Not supported. Minimum version required: v0.7.0+. Current version v0.6.0 is below threshold.
- Notes: Caller should upgrade Anthropic library before instrumentation.

### Example 3

- Input: Provider: CrewAI, Current version: v0.56.0
- Output: Supported. Minimum version: v0.56.0+. Current version meets requirement.
- Notes: CrewAI is at minimum threshold.

## Triggers

- Caller needs to verify if a specific LLM provider can be instrumented
- Caller must check minimum version requirements before integration
- Caller is planning instrumentation scope and needs provider support confirmation

## Examples

### Example 1

Input:

  Provider: OpenAI, Current version: v1.3.0

Output:

  Supported. Minimum version: v0.27.0+ or v1.0.0+. Current version v1.3.0 meets requirement.

Notes:

  OpenAI has two supported version tracks.

### Example 2

Input:

  Provider: Anthropic, Current version: v0.6.0

Output:

  Not supported. Minimum version required: v0.7.0+. Current version v0.6.0 is below threshold.

Notes:

  Caller should upgrade Anthropic library before instrumentation.

### Example 3

Input:

  Provider: CrewAI, Current version: v0.56.0

Output:

  Supported. Minimum version: v0.56.0+. Current version meets requirement.

Notes:

  CrewAI is at minimum threshold.
