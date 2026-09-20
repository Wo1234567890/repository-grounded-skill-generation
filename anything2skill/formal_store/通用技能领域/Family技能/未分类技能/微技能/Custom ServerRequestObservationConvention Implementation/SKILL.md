---
id: "f83a5625-f756-5405-b2a6-f2296b185081"
name: "Custom ServerRequestObservationConvention Implementation"
description: "Extract and log standardized attributes from API requests and responses using semantic conventions. Ensures consistent metadata (model name, token counts, latency, error codes) across all instrumented API calls."
version: "0.1.1"
tags:
  - "instrumentation"
  - "observability"
  - "semantic_conventions"
  - "api_metadata"
  - "distributed_tracing"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Spring Boot 3.0 migration initiated"
  - "WebMvcMetricsFilter or MetricsRestTemplateCustomizer deprecated and removed"
  - "Full control over HTTP observation naming and tagging required"
  - "Custom metric or trace naming strategy needed"
examples:
  - input: "HTTP GET request to /api/users with Spring Boot 3.0 observation support enabled"
    output: "Metric name: 'http.server.requests'; Trace name: 'http get'; KeyValues include method=GET, status=200, exception=none"
    notes: "Custom convention fully replaces deprecated WebMvcMetricsFilter behavior"
  - input: "Extending DefaultServerRequestObservationConvention to add custom KeyValue"
    output: "Default KeyValues preserved plus custom KeyValue (e.g., custom.method=GET) appended"
    notes: "Use extension pattern when only supplementary tags are needed, not full convention replacement"
---

# Custom ServerRequestObservationConvention Implementation

Extract and log standardized attributes from API requests and responses using semantic conventions. Ensures consistent metadata (model name, token counts, latency, error codes) across all instrumented API calls.

## Prompt

When wrapping an API call, extract request and response metadata and format it as a structured attribute dictionary conforming to semantic conventions. Document what attributes are captured. Use common utilities and semantic convention attributes for consistency.

## Objective

Ensure consistent semantic metadata across all instrumented API calls
## Applicable Signals

- API call entry point detected
- Response received from API
- Metadata extraction required for observability

## Contraindications

- Logging free-form debug messages without structure
- Capturing sensitive PII without sanitization
- Non-API operations or internal function calls

## Workflow Steps

- Identify API call context (request type, endpoint, method)
- Extract request metadata (model name, parameters, input tokens)
- Capture response metadata (status code, output tokens, latency)
- Format all attributes according to semantic conventions
- Document captured attributes with inline comments
- Return structured attribute dictionary

## Constraints

- Must conform to agentops.semconv schema
- Attributes must be documented inline
- Sanitize sensitive data before capture

## Cautions

- Do not include raw request/response bodies; extract only metadata
- Validate attribute keys against semantic convention schema before output
- Handle missing optional attributes gracefully with defaults

## Output Contract

- Structured attribute dictionary conforming to agentops.semconv schema, ready for distributed tracing backend consumption

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Spring Boot 3.0 migration initiated
- WebMvcMetricsFilter or MetricsRestTemplateCustomizer deprecated and removed
- Full control over HTTP observation naming and tagging required
- Custom metric or trace naming strategy needed

## Examples

### Example 1

Input:

  HTTP GET request to /api/users with Spring Boot 3.0 observation support enabled

Output:

  Metric name: 'http.server.requests'; Trace name: 'http get'; KeyValues include method=GET, status=200, exception=none

Notes:

  Custom convention fully replaces deprecated WebMvcMetricsFilter behavior

### Example 2

Input:

  Extending DefaultServerRequestObservationConvention to add custom KeyValue

Output:

  Default KeyValues preserved plus custom KeyValue (e.g., custom.method=GET) appended

Notes:

  Use extension pattern when only supplementary tags are needed, not full convention replacement
