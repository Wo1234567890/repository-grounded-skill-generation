---
id: "ce876721-97f3-53be-9f13-b151f476dbe4"
name: "Create OpenAI Instrumentation Metrics"
description: "Initialize a standardized metrics dictionary for OpenAI API instrumentation by invoking StandardMetrics.create_standard_metrics with a provided Meter instance. This skill is invoked during instrumentation setup to establish observability metrics collection."
version: "0.1.0"
tags:
  - "instrumentation"
  - "metrics"
  - "openai"
  - "observability"
  - "initialization"
triggers:
  - "OpenAI instrumentation is being configured"
  - "Metrics collection needs to be initialized"
  - "Meter instance is available and ready"
---

# Create OpenAI Instrumentation Metrics

Initialize a standardized metrics dictionary for OpenAI API instrumentation by invoking StandardMetrics.create_standard_metrics with a provided Meter instance. This skill is invoked during instrumentation setup to establish observability metrics collection.

## Prompt

Call StandardMetrics.create_standard_metrics(meter) to generate a complete metrics dictionary. Pass the Meter instance provided during instrumentation initialization. Return the resulting dictionary without modification.

## Objective

Initialize metrics collection for OpenAI instrumentation
## Applicable Signals

- instrumentation_setup_phase_entered
- meter_instance_provided
- observability_metrics_required

## Contraindications

- Metrics have already been created for this instrumentation session
- Instrumentation is disabled or metrics are not required
- Meter instance is null or invalid

## Workflow Steps

- {'step': 1, 'action': 'Receive Meter instance as parameter', 'validation': 'Verify Meter is not null and is of expected type'}
- {'step': 2, 'action': 'Invoke StandardMetrics.create_standard_metrics(meter)', 'validation': 'Confirm method call succeeds without exception'}
- {'step': 3, 'action': 'Return metrics dictionary', 'validation': 'Verify dictionary is non-empty and contains expected metric keys'}

## Constraints

- Meter parameter must be a valid Meter instance
- StandardMetrics.create_standard_metrics must be available in the runtime environment
- Execution must occur during instrumentation setup phase, before method wrapping

## Cautions

- Do not call this skill multiple times for the same instrumentation session; cache the result
- Ensure the Meter instance is properly initialized before passing it to this skill

## Output Contract

- Returns a Dict[str, Any] containing standardized metrics keyed by metric name, ready for collection and observation during OpenAI API calls.

## Triggers

- OpenAI instrumentation is being configured
- Metrics collection needs to be initialized
- Meter instance is available and ready
