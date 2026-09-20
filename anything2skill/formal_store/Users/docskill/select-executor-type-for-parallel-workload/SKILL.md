---
id: "5a9fd1e3-0c75-5c95-9dce-91ef8a286272"
name: "Select Executor Type for Parallel Workload"
description: "Canonical skill for selecting and understanding the appropriate file-based data source method in Flink DataStream API. Guides caller through readTextFile vs readFile decision based on input data type, format requirements, and execution semantics."
version: "0.1.1"
tags:
  - "flink"
  - "datastream"
  - "source"
  - "file-based"
  - "configuration"
  - "reference"
triggers:
  - "You are designing a parallel application and need to decide between thread-based and process-based concurrency."
---

# Select Executor Type for Parallel Workload

Canonical skill for selecting and understanding the appropriate file-based data source method in Flink DataStream API. Guides caller through readTextFile vs readFile decision based on input data type, format requirements, and execution semantics.

## Prompt

When setting up a Flink streaming job that reads from files, consult this reference to understand available file source methods and their requirements. readTextFile(path) reads text files line-by-line respecting TextInputFormat specification and returns Strings. readFile(fileInputFormat, path) reads files once as dictated by the specified file input format. Use this to determine which method matches your input data type and format requirements.

## Objective

Provide reusable reference for file-based source options and their constraints in Flink DataStream API
## Applicable Signals

- Caller is selecting a data source for a Flink streaming job
- Input data is stored in files (text, structured, or custom format)
- Caller needs to understand file source API options and constraints

## Contraindications

- Source is already fully configured and deployed
- Input data comes from socket, Kafka, or other non-file streaming sources
- Caller requires custom source implementation beyond predefined methods

## Constraints

- readTextFile applies TextInputFormat specification; suitable for line-delimited text only
- readFile reads files once; not suitable for continuous file monitoring
- File path must be accessible from all TaskManager nodes in the cluster

## Output Contract

- Caller understands which file source method (readTextFile or readFile) matches their input data type, format requirements, and execution semantics; can proceed to instantiate the source with correct parameters

## Triggers

- You are designing a parallel application and need to decide between thread-based and process-based concurrency.
