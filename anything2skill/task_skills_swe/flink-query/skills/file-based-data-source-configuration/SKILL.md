---
id: "411cca2d-87da-5a7b-bfb9-bee7173f3d23"
name: "File-based Data Source Configuration"
description: "Configure and instantiate file-based data sources in Flink DataStream API, supporting text files and custom input formats. Handles continuous file monitoring with explicit awareness of exactly-once semantics constraints."
version: "0.1.0"
tags:
  - "data_source"
  - "file_input"
  - "streaming"
  - "initialization"
  - "flink_datastream_api"
triggers:
  - "Streaming application requires reading from local or distributed file systems"
  - "Data source is text-based or uses custom InputFormat"
  - "File-based ingestion is the primary data entry point"
---

# File-based Data Source Configuration

Configure and instantiate file-based data sources in Flink DataStream API, supporting text files and custom input formats. Handles continuous file monitoring with explicit awareness of exactly-once semantics constraints.

## Prompt

To set up a file-based data source:
1. Choose the appropriate method: readTextFile(path) for text files, or readFile(fileInputFormat, path) for custom formats.
2. If continuous monitoring is required, set watchType to FileProcessingMode.PROCESS_CONTINUOUSLY, but understand this breaks exactly-once semantics when files are appended.
3. Attach the configured source to the StreamExecutionEnvironment.
4. Verify the resulting DataStream is ready for downstream transformations.

## Objective

Set up file-based streaming data ingestion
## Applicable Signals

- StreamExecutionEnvironment initialization phase
- Data source configuration requirement identified
- File path and format parameters available

## Contraindications

- Source is socket-based (use socketTextStream instead)
- Source is collection-based (use fromCollection, fromElements, or generateSequence)
- Source requires custom connector such as Kafka (use addSource with appropriate consumer)
- Exactly-once semantics is critical and file modification is expected during execution

## Workflow Steps

- {'step': 1, 'action': 'Determine file source type', 'detail': 'Identify whether source is text file or requires custom InputFormat'}
- {'step': 2, 'action': 'Select configuration method', 'detail': 'Use readTextFile(path) for text files or readFile(fileInputFormat, path) for custom formats'}
- {'step': 3, 'action': 'Configure watchType if continuous monitoring needed', 'detail': 'Set watchType parameter; if FileProcessingMode.PROCESS_CONTINUOUSLY, acknowledge exactly-once breakage risk'}
- {'step': 4, 'action': 'Attach source to StreamExecutionEnvironment', 'detail': 'Invoke configured method on environment instance to create DataStream'}
- {'step': 5, 'action': 'Verify DataStream readiness', 'detail': 'Confirm DataStream object is created and ready for downstream operations'}

## Constraints

- All elements in a collection-based source must be of the same type
- FileProcessingMode.PROCESS_CONTINUOUSLY re-processes entire file contents on modification, breaking exactly-once guarantees
- File must respect TextInputFormat specification for readTextFile method

## Cautions

- Appending data to a file with PROCESS_CONTINUOUSLY mode causes all prior contents to be re-processed
- Exactly-once semantics cannot be guaranteed when using continuous file monitoring with file modifications

## Output Contract

- Configured DataStream object with file source attached, watchType parameter set appropriately, and ready for downstream transformations or actions

## Triggers

- Streaming application requires reading from local or distributed file systems
- Data source is text-based or uses custom InputFormat
- File-based ingestion is the primary data entry point
