---
id: "812e7026-499e-5857-812c-08f5685e456e"
name: "Standard Metrics Recording"
description: "Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumented operations."
version: "0.1.0"
tags:
  - "observability"
  - "metrics"
  - "opentelemetry"
  - "instrumentation"
  - "token-counting"
  - "performance-monitoring"
triggers:
  - "Need to record token usage and duration metrics across multiple operations"
  - "Using OpenTelemetry meter for observability"
  - "Want standardized metric names and types across instrumentations"
examples:
  - input: "meter=MeterProvider().get_meter('my-service'), prompt_tokens=100, completion_tokens=50, duration=1.5"
    output: "MetricsRecorder with token_usage metric set to 150 total tokens and duration metric set to 1.5 seconds"
    notes: "Typical LLM operation metrics aggregation"
---

# Standard Metrics Recording

Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumented operations.

## Prompt

Initialize StandardMetrics from an OpenTelemetry meter, then use MetricsRecorder to populate token usage and duration metrics. Call record_token_usage with prompt_tokens and completion_tokens counts, and record_duration with elapsed time in seconds. Export metrics to the configured meter for downstream collection.

## Objective

Initialize and populate standard metrics for an instrumentation session
## Applicable Signals

- Multiple instrumented operations completing
- Token counts available from LLM responses
- Operation duration measurable

## Contraindications

- Metrics are custom or non-standard
- Using a different metrics framework (not OpenTelemetry)
- Metrics are recorded directly on spans without aggregation

## Workflow Steps

- Import StandardMetrics and MetricsRecorder from agentops.instrumentation.common
- Create standard metrics by calling StandardMetrics.create_standard_metrics(meter)
- Instantiate MetricsRecorder with the created metrics
- Call recorder.record_token_usage(prompt_tokens=<count>, completion_tokens=<count>)
- Call recorder.record_duration(<elapsed_seconds>)
- Metrics are automatically exported to the configured meter

## Constraints

- Meter must be initialized and passed to StandardMetrics.create_standard_metrics
- Token counts (prompt_tokens, completion_tokens) must be available
- Duration must be measured in seconds

## Output Contract

- MetricsRecorder instance with token_usage and duration metrics populated and exported to the configured OpenTelemetry meter; metrics available for downstream collection and analysis

## Example Executions

### Example 1

- Input: meter=MeterProvider().get_meter('my-service'), prompt_tokens=100, completion_tokens=50, duration=1.5
- Output: MetricsRecorder with token_usage metric set to 150 total tokens and duration metric set to 1.5 seconds
- Notes: Typical LLM operation metrics aggregation

## Triggers

- Need to record token usage and duration metrics across multiple operations
- Using OpenTelemetry meter for observability
- Want standardized metric names and types across instrumentations

## Examples

### Example 1

Input:

  meter=MeterProvider().get_meter('my-service'), prompt_tokens=100, completion_tokens=50, duration=1.5

Output:

  MetricsRecorder with token_usage metric set to 150 total tokens and duration metric set to 1.5 seconds

Notes:

  Typical LLM operation metrics aggregation
