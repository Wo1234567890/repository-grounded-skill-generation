---
id: "87f86160-f44f-511c-82f8-58083943120b"
name: "Custom Source Function Integration"
description: "Attach and configure custom or third-party source functions (e.g., Kafka consumer) to a Flink DataStream using the addSource() API. Use this skill when connecting to managed message brokers, databases, or proprietary systems where a source function implementation is already available or provided by the Flink connectors library."
version: "0.1.0"
tags:
  - "data_source"
  - "connector"
  - "kafka"
  - "external_integration"
  - "flink_api"
triggers:
  - "Connecting to managed message brokers (Kafka, Pulsar), databases, or proprietary systems; source function is already implemented or available from Flink connectors library"
examples:
  - input: "StreamExecutionEnvironment env; need to read from Kafka topic 'events'"
    output: "DataStream<String> stream = env.addSource(new FlinkKafkaConsumer<>(\"events\", new SimpleStringSchema(), kafkaProps))"
    notes: "FlinkKafkaConsumer is instantiated with topic name, deserialization schema, and properties before passing to addSource()"
---

# Custom Source Function Integration

Attach and configure custom or third-party source functions (e.g., Kafka consumer) to a Flink DataStream using the addSource() API. Use this skill when connecting to managed message brokers, databases, or proprietary systems where a source function implementation is already available or provided by the Flink connectors library.

## Prompt

Call addSource(sourceFunction) on the StreamExecutionEnvironment or DataStream to attach a custom source function. Ensure the source function is instantiated with required configuration (e.g., FlinkKafkaConsumer with broker addresses, topic, and deserialization schema). The source function must implement the SourceFunction interface and be ready to emit elements of type T.

## Objective

Integrate external data sources via pluggable source functions for enterprise connectors
## Applicable Signals

- Need to connect to managed message brokers (Kafka, Pulsar)
- Integrating with external databases or proprietary systems
- Source function implementation is already available or provided by Flink connectors library

## Contraindications

- Source is a built-in type (file, socket, collection)
- Custom source function is not yet implemented or tested
- Source function lacks required SourceFunction interface implementation

## Workflow Steps

- Instantiate the custom source function with required configuration parameters
- Call addSource(sourceFunction) on StreamExecutionEnvironment or intermediate DataStream
- Verify the returned DataStream<T> is properly typed and ready for downstream operations

## Constraints

- Source function must implement SourceFunction<T> interface
- Source function must be instantiated with all required configuration before passing to addSource()
- Type parameter T must be consistent across the DataStream pipeline

## Cautions

- Ensure external connector library (e.g., flink-connector-kafka) is included in project dependencies
- Verify source function configuration (broker addresses, credentials, topic/queue names) before deployment
- Test source function behavior in isolation before integrating into full pipeline

## Output Contract

- Returns a DataStream<T> with the custom source function attached and initialized. The source is ready to emit elements of type T into the pipeline.

## Example Therapist Responses

### Example 1

- Client/Input: StreamExecutionEnvironment env; need to read from Kafka topic 'events'
- Therapist/Output: DataStream<String> stream = env.addSource(new FlinkKafkaConsumer<>("events", new SimpleStringSchema(), kafkaProps))
- Notes: FlinkKafkaConsumer is instantiated with topic name, deserialization schema, and properties before passing to addSource()

## Triggers

- Connecting to managed message brokers (Kafka, Pulsar), databases, or proprietary systems; source function is already implemented or available from Flink connectors library

## Examples

### Example 1

Input:

  StreamExecutionEnvironment env; need to read from Kafka topic 'events'

Output:

  DataStream<String> stream = env.addSource(new FlinkKafkaConsumer<>("events", new SimpleStringSchema(), kafkaProps))

Notes:

  FlinkKafkaConsumer is instantiated with topic name, deserialization schema, and properties before passing to addSource()
