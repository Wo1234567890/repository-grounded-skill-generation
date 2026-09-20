---
id: "97d75468-35c4-5f42-8dde-9130eca9cf72"
name: "Automatic Watermark Interval Configuration"
description: "Configure the interval for automatic watermark emission in Flink DataStream applications via setAutoWatermarkInterval() on ExecutionConfig. Controls the cadence at which watermarks are emitted to advance event-time progress."
version: "0.1.0"
tags:
  - "event_time"
  - "watermark"
  - "configuration"
  - "execution_config"
  - "datastream_api"
triggers:
  - "event-time semantics are required and automatic watermark emission interval needs tuning; default interval is insufficient for application requirements"
examples:
  - input: "StreamExecutionEnvironment with default watermark interval; application requires watermarks every 100 ms"
    output: "env.getConfig().setAutoWatermarkInterval(100); watermarks emitted at 100 ms cadence"
    notes: "Typical configuration for event-time windows with moderate latency tolerance"
  - input: "Low-latency application requiring frequent watermark updates"
    output: "env.getConfig().setAutoWatermarkInterval(10); watermarks emitted every 10 ms"
    notes: "Smaller interval increases watermark frequency; monitor overhead"
---

# Automatic Watermark Interval Configuration

Configure the interval for automatic watermark emission in Flink DataStream applications via setAutoWatermarkInterval() on ExecutionConfig. Controls the cadence at which watermarks are emitted to advance event-time progress.

## Prompt

Use setAutoWatermarkInterval(long milliseconds) on the StreamExecutionEnvironment's ExecutionConfig to set the watermark emission interval. Retrieve the current value with getAutoWatermarkInterval(). The interval determines how frequently watermarks are automatically generated and sent downstream.

## Objective

configure_watermark_emission_cadence
## Applicable Signals

- event-time semantics are required for the application
- default watermark emission interval is insufficient
- watermark latency or granularity needs tuning
- application uses event-time windows or joins

## Contraindications

- custom watermark generators are already assigned to sources
- processing-time semantics are sufficient for the application
- watermark emission is managed externally or via SourceFunction

## Intervention Moves

- Call setAutoWatermarkInterval(milliseconds) on ExecutionConfig before job submission
- Query current interval with getAutoWatermarkInterval() to verify configuration
- Adjust interval based on event-time progress requirements and latency constraints

## Workflow Steps

- {'step': 1, 'action': 'Obtain StreamExecutionEnvironment instance', 'detail': 'Create or retrieve the execution environment for the DataStream job'}
- {'step': 2, 'action': 'Access ExecutionConfig', 'detail': 'Call getConfig() on the StreamExecutionEnvironment'}
- {'step': 3, 'action': 'Set watermark interval', 'detail': 'Call setAutoWatermarkInterval(milliseconds) with desired interval value'}
- {'step': 4, 'action': 'Verify configuration (optional)', 'detail': 'Call getAutoWatermarkInterval() to confirm the interval is set'}

## Constraints

- interval must be a positive long value in milliseconds
- configuration must be set on ExecutionConfig before job execution
- applies only to automatic watermark emission; does not override custom generators

## Cautions

- very small intervals may increase overhead; balance latency and throughput
- interval affects all sources using automatic watermark generation
- does not apply if sources implement custom watermark generation logic

## Output Contract

- Watermark emission interval is configured on ExecutionConfig
- watermarks are emitted at the specified cadence during job execution
- getAutoWatermarkInterval() returns the configured value

## Example Therapist Responses

### Example 1

- Client/Input: StreamExecutionEnvironment with default watermark interval; application requires watermarks every 100 ms
- Therapist/Output: env.getConfig().setAutoWatermarkInterval(100); watermarks emitted at 100 ms cadence
- Notes: Typical configuration for event-time windows with moderate latency tolerance

### Example 2

- Client/Input: Low-latency application requiring frequent watermark updates
- Therapist/Output: env.getConfig().setAutoWatermarkInterval(10); watermarks emitted every 10 ms
- Notes: Smaller interval increases watermark frequency; monitor overhead

## Triggers

- event-time semantics are required and automatic watermark emission interval needs tuning; default interval is insufficient for application requirements

## Examples

### Example 1

Input:

  StreamExecutionEnvironment with default watermark interval; application requires watermarks every 100 ms

Output:

  env.getConfig().setAutoWatermarkInterval(100); watermarks emitted at 100 ms cadence

Notes:

  Typical configuration for event-time windows with moderate latency tolerance

### Example 2

Input:

  Low-latency application requiring frequent watermark updates

Output:

  env.getConfig().setAutoWatermarkInterval(10); watermarks emitted every 10 ms

Notes:

  Smaller interval increases watermark frequency; monitor overhead
