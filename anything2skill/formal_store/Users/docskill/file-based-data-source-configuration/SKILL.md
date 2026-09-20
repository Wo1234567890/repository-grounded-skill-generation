---
id: "42bbed97-509d-5d9f-b1db-349f906ba284"
name: "File-based Data Source Configuration"
description: "Configure and instantiate file-based data sources in Flink DataStream API, supporting text files and custom input formats with explicit file processing mode selection to preserve exactly-once semantics."
version: "0.1.0"
tags:
  - "flink"
  - "datastream_api"
  - "data_source"
  - "file_processing"
  - "exactly_once_semantics"
  - "stream_initialization"
triggers:
  - "Initializing a Flink job that reads from local or distributed file systems"
  - "Choosing between one-time or continuous file monitoring"
---

# File-based Data Source Configuration

Configure and instantiate file-based data sources in Flink DataStream API, supporting text files and custom input formats with explicit file processing mode selection to preserve exactly-once semantics.

## Prompt

When initializing a Flink job that reads from local or distributed file systems, use readTextFile(path) for line-by-line text file ingestion or readFile(fileInputFormat, path) for custom format parsing. Always explicitly set the file processing mode: use PROCESS_ONCE for one-time reads (default, preserves exactly-once semantics) or PROCESS_CONTINUOUSLY only when continuous monitoring is required and re-processing of entire files on modification is acceptable. Document the mode choice and its semantic implications.

## Objective

Set up reusable file source connectors with correct processing mode selection and semantic awareness
## Applicable Signals

- Flink job initialization phase
- Data source requirement is local or distributed file system
- Need to choose between one-time or continuous file monitoring

## Contraindications

- Source is socket-based (use socketTextStream instead)
- Source is collection-based (use fromCollection, fromElements, or generateSequence instead)
- Source is custom connector such as Kafka (use addSource with appropriate connector)
- File processing mode is already determined by upstream requirements

## Intervention Moves

- Select readTextFile(path) for text files respecting TextInputFormat specification
- Select readFile(fileInputFormat, path) for custom file input formats
- Explicitly set watchType to FileProcessingMode.PROCESS_ONCE (default) or PROCESS_CONTINUOUSLY
- Document file processing mode choice and its impact on exactly-once semantics

## Workflow Steps

- {'step': 1, 'action': 'Determine file source type', 'detail': 'Identify whether source is text file or requires custom input format'}
- {'step': 2, 'action': 'Select appropriate source method', 'detail': 'Use readTextFile(path) for text files or readFile(fileInputFormat, path) for custom formats'}
- {'step': 3, 'action': 'Determine processing mode requirement', 'detail': 'Decide between PROCESS_ONCE (one-time, preserves exactly-once) or PROCESS_CONTINUOUSLY (continuous monitoring)'}
- {'step': 4, 'action': 'Configure and attach source', 'detail': 'Instantiate source with selected method and explicitly set file processing mode'}
- {'step': 5, 'action': 'Document semantic implications', 'detail': 'Record processing mode choice and its impact on exactly-once semantics for downstream reference'}

## Constraints

- All elements in a collection-based source must be of the same type
- PROCESS_CONTINUOUSLY mode breaks exactly-once semantics when files are appended or modified
- File input format must respect TextInputFormat specification for readTextFile

## Cautions

- PROCESS_CONTINUOUSLY causes entire file contents to be re-processed on any modification, breaking exactly-once guarantees
- Appending data to a file under PROCESS_CONTINUOUSLY will trigger full re-processing of all prior contents

## Output Contract

- Configured StreamExecutionEnvironment with file-based source (readTextFile or readFile) attached; file processing mode explicitly set and documented; exactly-once semantic implications clearly noted for the chosen mode

## Triggers

- Initializing a Flink job that reads from local or distributed file systems
- Choosing between one-time or continuous file monitoring
