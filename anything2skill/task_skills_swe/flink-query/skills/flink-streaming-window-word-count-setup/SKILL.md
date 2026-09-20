---
id: "cbd56c68-880c-5cd7-ab60-b410e16feb78"
name: "Flink Streaming Window Word Count Setup"
description: "Initialize a Flink StreamExecutionEnvironment, ingest text from a socket source, apply flatMap tokenization, key by word, apply tumbling processing-time windows, and aggregate word counts. Use this to build basic streaming aggregation pipelines with fixed time windows."
version: "0.1.0"
tags:
  - "flink"
  - "streaming"
  - "windowing"
  - "aggregation"
  - "word-count"
  - "socket-source"
triggers:
  - "Need to count or aggregate streaming events over fixed time intervals; have text or tokenizable input from a socket or file source; want to group results by a key field."
examples:
  - input: "Socket stream: 'hello world\\nhello flink\\nworld'"
    output: "(hello, 1)\n(world, 1)\n(hello, 2)\n(world, 2)"
    notes: "Within a 5-second window, repeated words accumulate; new window resets counts"
  - input: "Continuous socket input over 10 seconds with window size 5s"
    output: "Two separate aggregation outputs, one per window period"
    notes: "Each tumbling window is independent; no overlap"
---

# Flink Streaming Window Word Count Setup

Initialize a Flink StreamExecutionEnvironment, ingest text from a socket source, apply flatMap tokenization, key by word, apply tumbling processing-time windows, and aggregate word counts. Use this to build basic streaming aggregation pipelines with fixed time windows.

## Prompt

Set up a complete Flink streaming job that reads text from a socket, tokenizes it, groups by word, applies a tumbling processing-time window, and outputs aggregated counts. Follow the pattern: create StreamExecutionEnvironment → socketTextStream → flatMap (tokenize) → keyBy (word) → window(TumblingProcessingTimeWindows) → sum(1) → print/sink → env.execute().

## Objective

Build and execute a complete streaming word-count application with windowed aggregation
## Applicable Signals

- Need to count or aggregate streaming events over fixed time intervals
- Have text or tokenizable input from a socket or file source
- Want to group results by a key field
- Require processing-time semantics (not event-time)

## Contraindications

- Require event-time semantics or watermarks
- Need session windows or sliding windows
- Input is not naturally tokenizable or keyed
- Require custom aggregation logic beyond sum

## Workflow Steps

- Create StreamExecutionEnvironment via getExecutionEnvironment()
- Attach socketTextStream source with host and port
- Apply flatMap to tokenize input (split on non-word characters, filter empty)
- Map each token to (word, 1) tuple
- Key the stream by word (f0 field)
- Apply TumblingProcessingTimeWindows with configured duration (e.g., 5 seconds)
- Aggregate using sum(1) on the count field
- Attach print() sink or custom sink
- Execute job with env.execute(jobName)

## Constraints

- Socket source must be available and listening on specified host:port
- Window duration must be positive
- Input must be line-delimited text
- Processing-time windows do not require watermarks

## Cautions

- Ensure netcat or equivalent is running on the socket before starting the job
- Window size affects latency; smaller windows produce more frequent output
- Tokenization logic (split pattern) must match input format
- Job runs indefinitely until manually stopped

## Output Contract

- Executable Flink job that prints aggregated word counts every configured window duration (e.g., 5 seconds) to stdout or sink, with format (word, count).

## Example Executions

### Example 1

- Input: Socket stream: 'hello world\nhello flink\nworld'
- Output: (hello, 1)
(world, 1)
(hello, 2)
(world, 2)
- Notes: Within a 5-second window, repeated words accumulate; new window resets counts

### Example 2

- Input: Continuous socket input over 10 seconds with window size 5s
- Output: Two separate aggregation outputs, one per window period
- Notes: Each tumbling window is independent; no overlap

## Triggers

- Need to count or aggregate streaming events over fixed time intervals; have text or tokenizable input from a socket or file source; want to group results by a key field.

## Examples

### Example 1

Input:

  Socket stream: 'hello world\nhello flink\nworld'

Output:

  (hello, 1)
  (world, 1)
  (hello, 2)
  (world, 2)

Notes:

  Within a 5-second window, repeated words accumulate; new window resets counts

### Example 2

Input:

  Continuous socket input over 10 seconds with window size 5s

Output:

  Two separate aggregation outputs, one per window period

Notes:

  Each tumbling window is independent; no overlap
