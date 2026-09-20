---
id: "fab77e2b-d66a-5af0-af54-fd6e8653f985"
name: "Executor Shutdown and Resource Cleanup"
description: "Configure and bind a DataStream sink to write final results to external systems or console output. This is a terminal operation that completes the processing pipeline by specifying the output destination and method."
version: "0.1.1"
tags:
  - "flink"
  - "datastream"
  - "sink"
  - "output"
  - "terminal_operation"
triggers:
  - "All tasks have been submitted to the executor"
  - "No further task submission is planned"
  - "Resource cleanup is required"
---

# Executor Shutdown and Resource Cleanup

Configure and bind a DataStream sink to write final results to external systems or console output. This is a terminal operation that completes the processing pipeline by specifying the output destination and method.

## Prompt

After all transformations are complete and you have a DataStream containing final results, create a sink to persist or display the output. Use writeAsText(String path) to write to a file, or print() to output to console. The sink is a terminal operation and must be the last step in your pipeline.

## Objective

Configure stream output destination and bind sink operator
## Applicable Signals

- Final DataStream results are ready
- Need to persist output to external system
- Need to display output to console
- Pipeline transformations are complete

## Contraindications

- Do not apply sink during intermediate transformation stages
- Do not apply sink before all required transformations are complete
- Do not apply multiple sinks to the same DataStream unless intentionally branching output

## Intervention Moves

- Call writeAsText(String path) on the DataStream to write results to a file
- Call print() on the DataStream to output results to console
- Verify sink configuration matches the output schema of the upstream DataStream

## Constraints

- Sink must be applied to a fully-transformed DataStream
- Sink is a terminal operation; no further transformations can follow
- Output path must be valid and writable for writeAsText()

## Cautions

- Ensure the DataStream schema is compatible with the sink format
- File paths in writeAsText() should use proper URI format (e.g., file:///path/to/file)
- print() outputs to stdout and may impact performance in production environments

## Output Contract

- Sink operator is configured and registered with the execution environment, ready to receive and output stream records during job execution.

## Triggers

- All tasks have been submitted to the executor
- No further task submission is planned
- Resource cleanup is required
