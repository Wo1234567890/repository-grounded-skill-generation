---
id: "20d5f145-6862-53e0-b6ca-186486afc92e"
name: "DataStream Map Transformation"
description: "Apply element-wise transformation to each record in a DataStream using MapFunction to convert or enrich data types. Each input record produces exactly one output record with a potentially different type."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "transformation"
  - "stateless"
  - "map"
triggers:
  - "Need to convert, parse, or enrich individual stream records; one input record produces one output record"
examples:
  - input: "DataStream<String> text = env.readTextFile(\"file:///path/to/file\");"
    output: "DataStream<Integer> parsed = text.map(new MapFunction<String, Integer>() { @Override public Integer map(String value) { return Integer.parseInt(value); } });"
    notes: "Converts each line (String) to an Integer; one-to-one transformation."
---

# DataStream Map Transformation

Apply element-wise transformation to each record in a DataStream using MapFunction to convert or enrich data types. Each input record produces exactly one output record with a potentially different type.

## Prompt

1. Obtain or create a DataStream source (e.g., via env.readTextFile() or other source method).
2. Call .map() on the DataStream, passing a MapFunction implementation.
3. Implement the map() method to define the transformation logic for each element.
4. The resulting DataStream contains transformed elements; chain further operations or write to a sink.

## Objective

Transform stream elements one-to-one
## Applicable Signals

- Need to convert individual stream records to a different type
- Need to parse or enrich each element independently
- One input record must produce exactly one output record

## Contraindications

- Do not use for aggregation or windowing operations
- Do not use when output cardinality differs from input (e.g., filtering or flattening)
- Do not use for stateful transformations requiring state backends

## Intervention Moves

- Define a MapFunction with the input and output type parameters
- Implement the map(T value) method with transformation logic
- Chain the result to downstream operations or sinks

## Workflow Steps

- {'step': 1, 'action': 'Obtain StreamExecutionEnvironment', 'detail': 'Use StreamExecutionEnvironment.getExecutionEnvironment() or createLocalEnvironment()'}
- {'step': 2, 'action': 'Create or obtain a DataStream source', 'detail': 'Use env.readTextFile(), env.socketTextStream(), or other source method'}
- {'step': 3, 'action': 'Invoke .map() with MapFunction', 'detail': 'Pass a MapFunction<InputType, OutputType> implementation to the map() method'}
- {'step': 4, 'action': 'Implement transformation logic', 'detail': 'Override map(InputType value) to return OutputType for each element'}
- {'step': 5, 'action': 'Chain or sink the result', 'detail': 'Apply further transformations or write to sink (e.g., print(), writeAsText())'}

## Constraints

- MapFunction must be serializable
- Transformation logic must be deterministic and side-effect free for fault tolerance
- Input and output types must be compatible with Flink's type system

## Output Contract

- A new DataStream<OutputType> containing one transformed element for each input element, preserving order and parallelism properties of the source.

## Example Therapist Responses

### Example 1

- Client/Input: DataStream<String> text = env.readTextFile("file:///path/to/file");
- Therapist/Output: DataStream<Integer> parsed = text.map(new MapFunction<String, Integer>() { @Override public Integer map(String value) { return Integer.parseInt(value); } });
- Notes: Converts each line (String) to an Integer; one-to-one transformation.

## Triggers

- Need to convert, parse, or enrich individual stream records; one input record produces one output record

## Examples

### Example 1

Input:

  DataStream<String> text = env.readTextFile("file:///path/to/file");

Output:

  DataStream<Integer> parsed = text.map(new MapFunction<String, Integer>() { @Override public Integer map(String value) { return Integer.parseInt(value); } });

Notes:

  Converts each line (String) to an Integer; one-to-one transformation.
