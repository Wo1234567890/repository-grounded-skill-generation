---
id: "b4f0b265-62ea-5406-8b19-8336dca59031"
name: "Socket-based Data Source Connection"
description: "Establish and configure socket-based data sources in Flink to read text streams from network sockets with configurable element delimiters."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "source"
  - "socket"
  - "network"
  - "text_stream"
triggers:
  - "Streaming data from a network socket"
  - "Elements are text-based and separated by a known delimiter"
  - "Testing or low-throughput scenarios"
---

# Socket-based Data Source Connection

Establish and configure socket-based data sources in Flink to read text streams from network sockets with configurable element delimiters.

## Prompt

Use socketTextStream to connect to a network socket endpoint and parse incoming text data. Configure the delimiter to separate elements in the stream. The resulting DataStream<String> is ready for downstream processing.

## Objective

Connect to a socket endpoint and parse incoming text data with delimiter-based element separation
## Applicable Signals

- Network socket availability
- Text-based data stream
- Known delimiter specification

## Contraindications

- Source is file-based
- Source is collection-based
- Using managed connector (e.g., Kafka)
- High-throughput production workload
- Binary or non-text data

## Workflow Steps

- Obtain StreamExecutionEnvironment instance
- Call socketTextStream(hostname, port, delimiter) method
- Verify DataStream<String> is created and connected
- Proceed to apply transformations or sinks

## Constraints

- All elements must be text-based
- Delimiter must be specified and consistent
- Socket endpoint must be reachable and stable

## Cautions

- Socket connections may be interrupted; implement reconnection logic if needed
- Delimiter parsing assumes well-formed delimited text; malformed data may cause parsing errors

## Output Contract

- DataStream<String> connected to socket with delimiter parsing configured; ready to receive and process incoming text elements

## Triggers

- Streaming data from a network socket
- Elements are text-based and separated by a known delimiter
- Testing or low-throughput scenarios
