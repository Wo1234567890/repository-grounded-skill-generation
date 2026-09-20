---
id: "d6cbc3d5-6285-56b6-8bb1-6b94034567d1"
name: "Flink DataStream Program Construction"
description: "Scaffold for building a complete Flink DataStream application by sequencing execution environment setup, data source creation, stream transformations, sink specification, and execution trigger. Use when starting a new streaming application or integrating a new data pipeline."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "program_construction"
  - "stream_processing"
  - "workflow_scaffold"
triggers:
  - "Starting a new Flink streaming application or integrating a new data pipeline"
---

# Flink DataStream Program Construction

Scaffold for building a complete Flink DataStream application by sequencing execution environment setup, data source creation, stream transformations, sink specification, and execution trigger. Use when starting a new streaming application or integrating a new data pipeline.

## Prompt

Follow the standard Flink program anatomy: (1) Obtain an execution environment, (2) Load or create initial data via a source, (3) Specify transformations on the DataStream, (4) Specify where results go via a sink, (5) Trigger execution. Each step builds on the previous one to form a complete, runnable program.

## Objective

Construct and execute a runnable Flink DataStream program
## Applicable Signals

- Starting a new Flink streaming application
- Integrating a new data pipeline
- Building a complete end-to-end stream processing workflow

## Contraindications

- Debugging existing runtime issues
- Tuning performance of an already-running program
- Modifying only transformation logic within an existing program
- Troubleshooting classloading or window event-time problems

## Workflow Steps

- {'step': 1, 'action': 'Obtain execution environment', 'detail': 'Create or retrieve the StreamExecutionEnvironment that serves as the entry point for the Flink program.'}
- {'step': 2, 'action': 'Load or create initial data', 'detail': 'Add a data source to the environment to create the initial DataStream. Sources can be external systems, collections, or generated data.'}
- {'step': 3, 'action': 'Specify transformations', 'detail': 'Apply API methods such as map, filter, and other transformations to derive new streams and combine them as needed.'}
- {'step': 4, 'action': 'Specify sink destination', 'detail': 'Define where the results of computations are written (e.g., file system, database, message queue).'}
- {'step': 5, 'action': 'Trigger execution', 'detail': 'Call the execute method on the environment to start the Flink program.'}

## Constraints

- DataStream is immutable; transformations produce new streams rather than modifying in place.
- DataStream can represent finite or unbounded data; the same API applies to both.
- Execution environment must be obtained before any source or transformation can be added.

## Output Contract

- Executable Flink program with source → transformation → sink chain ready for deployment. The program is runnable and can be submitted to a Flink cluster or local environment.

## Triggers

- Starting a new Flink streaming application or integrating a new data pipeline
