---
id: "a15dd434-deab-557a-91b4-03289812344f"
name: "Flink DataStream Window Aggregation Setup"
description: "Construct and execute a complete streaming window aggregation pipeline using Flink DataStream API. Chains socket source, flat-map transformation, keying, windowing, and aggregation into one executable job that reads from a socket, transforms data, windows it in fixed time intervals, aggregates within each window, and outputs results."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "windowing"
  - "aggregation"
  - "streaming"
  - "socket_source"
triggers:
  - "Need to aggregate streaming data over fixed time windows (e.g., word count, metric rollup) and execute the job end-to-end."
examples:
  - input: "Socket stream: 'hello world', 'hello flink', 'world flink' (within 5-second window)"
    output: "(hello, 2), (world, 2), (flink, 2)"
    notes: "Tumbling 5-second window counts word occurrences; each word appears twice in the example window."
  - input: "Metric stream: '10', '20', '15' (within 10-second window, keyed by metric type)"
    output: "Sum: 45"
    notes: "Aggregates numeric values within the window using sum operator."
---

# Flink DataStream Window Aggregation Setup

Construct and execute a complete streaming window aggregation pipeline using Flink DataStream API. Chains socket source, flat-map transformation, keying, windowing, and aggregation into one executable job that reads from a socket, transforms data, windows it in fixed time intervals, aggregates within each window, and outputs results.

## Prompt

1. Initialize StreamExecutionEnvironment.
2. Create a socket text stream source (host, port).
3. Apply flatMap to split and filter input (e.g., tokenize words).
4. Key the stream by the grouping field (e.g., word).
5. Apply a tumbling processing-time window (e.g., 5 seconds).
6. Aggregate within the window (e.g., sum, count).
7. Add a sink (e.g., print()).
8. Call env.execute(jobName) to submit and run the job.

## Objective

Build and run a complete windowed stream processing job that reads from a socket, transforms, windows, and aggregates data.
## Applicable Signals

- Need to aggregate streaming data over fixed time windows
- Word count or metric rollup use case
- End-to-end job execution required
- Real-time processing from socket or similar source

## Contraindications

- Batch processing only (use DataSet API instead)
- No windowing requirement (use map/filter directly)
- Using higher-level SQL or Table API
- Event-time semantics required without watermark setup

## Intervention Moves

- Initialize execution environment
- Attach socket text stream source
- Chain flatMap for tokenization or splitting
- Apply keyBy for grouping
- Specify tumbling processing-time window
- Apply aggregation operator (sum, count, etc.)
- Attach sink for output
- Execute job with named identifier

## Workflow Steps

- {'step': 1, 'action': 'Create StreamExecutionEnvironment', 'detail': 'StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();'}
- {'step': 2, 'action': 'Attach socket text stream source', 'detail': 'env.socketTextStream(host, port) returns DataStream<String>'}
- {'step': 3, 'action': 'Apply flatMap transformation', 'detail': 'Split input (e.g., by whitespace), filter empty tokens, emit individual elements'}
- {'step': 4, 'action': 'Key the stream', 'detail': 'keyBy(value -> value.f0) or equivalent; groups elements by key for windowing'}
- {'step': 5, 'action': 'Define tumbling window', 'detail': 'window(TumblingProcessingTimeWindows.of(Time.seconds(N))) creates fixed-size non-overlapping windows'}
- {'step': 6, 'action': 'Apply aggregation', 'detail': 'sum(fieldIndex) or aggregate() to combine values within each window'}
- {'step': 7, 'action': 'Attach sink', 'detail': 'dataStream.print() or other sink (writeAsText, custom sink)'}
- {'step': 8, 'action': 'Execute job', 'detail': 'env.execute(jobName) submits and runs the job; blocks until completion or cancellation'}

## Constraints

- Socket source must be available and listening on specified host:port
- Transformation logic (flatMap, keyBy) must be correctly implemented
- Window size must be appropriate for data arrival rate
- Aggregation field index or key must match stream schema

## Cautions

- Lazy evaluation: transformations are not executed until env.execute() is called
- Socket source is blocking; ensure input stream is active before job starts
- Processing-time windows are not deterministic across runs; use event-time windows for reproducibility if needed
- Ensure flatMap filter removes empty tokens to avoid null key errors

## Output Contract

- Executable Flink job that reads from socket source, applies transformations, windows data in fixed time intervals, aggregates within each window, and outputs results to sink. Job runs until explicitly cancelled or source closes.

## Example Therapist Responses

### Example 1

- Client/Input: Socket stream: 'hello world', 'hello flink', 'world flink' (within 5-second window)
- Therapist/Output: (hello, 2), (world, 2), (flink, 2)
- Notes: Tumbling 5-second window counts word occurrences; each word appears twice in the example window.

### Example 2

- Client/Input: Metric stream: '10', '20', '15' (within 10-second window, keyed by metric type)
- Therapist/Output: Sum: 45
- Notes: Aggregates numeric values within the window using sum operator.

## Triggers

- Need to aggregate streaming data over fixed time windows (e.g., word count, metric rollup) and execute the job end-to-end.

## Examples

### Example 1

Input:

  Socket stream: 'hello world', 'hello flink', 'world flink' (within 5-second window)

Output:

  (hello, 2), (world, 2), (flink, 2)

Notes:

  Tumbling 5-second window counts word occurrences; each word appears twice in the example window.

### Example 2

Input:

  Metric stream: '10', '20', '15' (within 10-second window, keyed by metric type)

Output:

  Sum: 45

Notes:

  Aggregates numeric values within the window using sum operator.
