---
id: "5476118e-1932-5ef1-bbdb-60d6f02fb84b"
name: "Set Automatic Watermark Emission Interval"
description: "Configure the interval for automatic watermark emission in StreamExecutionEnvironment. Controls how frequently watermarks are generated to advance event time during runtime setup."
version: "0.1.0"
tags:
  - "event_time"
  - "watermark"
  - "execution_config"
  - "latency_control"
  - "streaming"
triggers:
  - "need to tune watermark emission frequency"
  - "during ExecutionConfig setup before job execution"
  - "when default watermark interval is insufficient for latency or throughput requirements"
---

# Set Automatic Watermark Emission Interval

Configure the interval for automatic watermark emission in StreamExecutionEnvironment. Controls how frequently watermarks are generated to advance event time during runtime setup.

## Prompt

Use setAutoWatermarkInterval(long milliseconds) on the StreamExecutionEnvironment to set the watermark emission frequency. The interval determines how often watermarks are automatically emitted to mark progress in event time. Retrieve the current value with getAutoWatermarkInterval().

## Objective

configure_watermark_timing
## Applicable Signals

- ExecutionConfig initialization phase
- StreamExecutionEnvironment creation
- pre-job-submission configuration window

## Contraindications

- using custom watermark generators (use custom generator configuration instead)
- watermark interval already tuned and stable
- using event time assignment without automatic watermark emission

## Workflow Steps

- Obtain or create a StreamExecutionEnvironment instance
- Call setAutoWatermarkInterval(milliseconds) with desired interval in milliseconds
- Optionally verify the setting by calling getAutoWatermarkInterval()
- Proceed with job configuration and submission

## Constraints

- must be called on StreamExecutionEnvironment before job execution
- interval value must be in milliseconds
- applies globally to all sources using automatic watermark emission

## Cautions

- very small intervals may increase overhead; balance latency vs. throughput
- interval affects all watermark-dependent operations (windows, joins, side outputs)

## Output Contract

- Watermark emission interval is set in the ExecutionConfig and can be retrieved via getAutoWatermarkInterval(). Watermarks will be emitted at the configured interval during job execution.

## Triggers

- need to tune watermark emission frequency
- during ExecutionConfig setup before job execution
- when default watermark interval is insufficient for latency or throughput requirements
