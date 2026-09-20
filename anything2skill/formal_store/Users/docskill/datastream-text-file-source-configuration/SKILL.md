---
id: "a568e6ea-9fa3-53ae-8cc8-11776c53f00f"
name: "DataStream Text File Source Configuration"
description: "Configure and instantiate a text file data source for streaming ingestion by reading text files line-by-line into a DataStream using the readTextFile() method."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "source"
  - "file_input"
  - "text_file"
  - "data_ingestion"
triggers:
  - "Need to stream text file content line-by-line; file path is known and accessible"
---

# DataStream Text File Source Configuration

Configure and instantiate a text file data source for streaming ingestion by reading text files line-by-line into a DataStream using the readTextFile() method.

## Prompt

Call StreamExecutionEnvironment.readTextFile(String filePath) to create a DataStream<String> where each element is one line from the input file. The file path must be accessible and in the format 'file:///path/to/file'. The resulting DataStream can be chained with transformations (map, filter, etc.) for downstream processing.

## Objective

Configure and instantiate a text file data source for streaming ingestion
## Applicable Signals

- Need to stream text file content line-by-line
- File path is known and accessible
- Unstructured text data ingestion required

## Contraindications

- Data source is not a text file
- Using structured formats (CSV, Parquet, JSON) that require custom parsing or dedicated readers
- File path is inaccessible or malformed

## Intervention Moves

- Obtain StreamExecutionEnvironment instance via getExecutionEnvironment(), createLocalEnvironment(), or createRemoteEnvironment()
- Call readTextFile(String filePath) with valid file URI
- Assign result to DataStream<String> variable for chaining transformations

## Workflow Steps

- {'step': 1, 'action': 'Obtain execution environment', 'detail': 'Call StreamExecutionEnvironment.getExecutionEnvironment() or equivalent factory method'}
- {'step': 2, 'action': 'Invoke readTextFile with file path', 'detail': 'Call env.readTextFile("file:///path/to/file") with valid URI'}
- {'step': 3, 'action': 'Assign to DataStream variable', 'detail': 'Store result in DataStream<String> for downstream transformation chaining'}

## Constraints

- File must be readable by the Flink runtime
- File path must use proper URI format (file:///path/to/file)
- Output is always DataStream<String> with one element per line

## Cautions

- Large files may cause memory pressure; consider windowing or filtering early in the pipeline
- Line-by-line parsing does not preserve multi-line record structure; use custom parsing for complex formats

## Output Contract

- Returns DataStream<String> where each element is one complete line from the input file, ready for map, filter, or other transformations

## Triggers

- Need to stream text file content line-by-line; file path is known and accessible
