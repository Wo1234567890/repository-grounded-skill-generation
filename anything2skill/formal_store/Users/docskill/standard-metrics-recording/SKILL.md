---
id: "6435e985-8972-565a-a361-da1778a0a79c"
name: "Standard Metrics Recording"
description: "Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumentation implementations."
version: "0.1.0"
tags:
  - "instrumentation"
  - "metrics"
  - "observability"
  - "token_counting"
  - "performance_tracking"
triggers:
  - "Instrumentor needs to record token usage and operation duration in a standardized way"
  - "Establishing baseline metrics collection for performance and cost tracking"
---

# Standard Metrics Recording

Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumentation implementations.

## Prompt

Use StandardMetrics to create standard metrics from a meter, then use MetricsRecorder to record token usage (prompt_tokens, completion_tokens) and operation duration. This ensures consistent metrics collection across all instrumentations.

## Objective

Establish consistent metrics recording across instrumentation implementations
## Applicable Signals

- Token usage data available from LLM response
- Operation completion with measurable duration
- Meter instance available for metrics recording

## Contraindications

- Custom metrics schema is required that deviates from standard metrics
- Metrics recording is not needed for the instrumentation

## Workflow Steps

- Import StandardMetrics and MetricsRecorder from agentops.instrumentation.common
- Create standard metrics instance: metrics = StandardMetrics.create_standard_metrics(meter)
- Instantiate MetricsRecorder with the metrics: recorder = MetricsRecorder(metrics)
- Record token usage: recorder.record_token_usage(prompt_tokens=<count>, completion_tokens=<count>)
- Record operation duration: recorder.record_duration(<seconds>)

## Constraints

- Meter must be initialized before creating StandardMetrics
- Token counts (prompt_tokens, completion_tokens) must be available
- Duration must be measurable in seconds

## Output Contract

- MetricsRecorder instance with token_usage and duration metrics recorded to meter; metrics are available for downstream observability and cost tracking

## Triggers

- Instrumentor needs to record token usage and operation duration in a standardized way
- Establishing baseline metrics collection for performance and cost tracking
