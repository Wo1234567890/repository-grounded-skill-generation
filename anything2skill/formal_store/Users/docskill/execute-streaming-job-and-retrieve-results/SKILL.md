---
id: "00e4814f-ebf9-52a9-ad31-ea4126ea24a5"
name: "Execute Streaming Job and Retrieve Results"
description: "Trigger a Flink streaming job execution and retrieve execution results including timing and accumulator metrics. Supports both synchronous and asynchronous execution modes with proper result handling."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "job_execution"
  - "execution_result"
  - "async_execution"
triggers:
  - "Pipeline definition is complete and ready to run; need to start job and monitor execution results"
examples:
  - input: "StreamExecutionEnvironment with complete pipeline (source → transformations → sink)"
    output: "JobExecutionResult with execution duration and accumulator metrics"
    notes: "Synchronous execution using execute()"
  - input: "StreamExecutionEnvironment with complete pipeline, non-blocking requirement"
    output: "JobClient object; calling getJobExecutionResult().get() yields JobExecutionResult"
    notes: "Asynchronous execution using executeAsync()"
---

# Execute Streaming Job and Retrieve Results

Trigger a Flink streaming job execution and retrieve execution results including timing and accumulator metrics. Supports both synchronous and asynchronous execution modes with proper result handling.

## Prompt

Call execute() for synchronous execution or executeAsync() for non-blocking execution on the StreamExecutionEnvironment. Synchronous execute() waits for job completion and returns JobExecutionResult directly. Asynchronous executeAsync() returns a JobClient; call getJobExecutionResult().get() on the client to retrieve the final JobExecutionResult containing execution times and accumulator values.

## Objective

Execute streaming job and collect execution metadata
## Applicable Signals

- Pipeline definition is complete
- All transformations and sinks are attached
- Ready to start job execution

## Contraindications

- Pipeline not fully defined
- Sinks not yet attached to DataStream
- Execution environment not initialized

## Intervention Moves

- Invoke execute() for blocking execution with immediate result
- Invoke executeAsync() for non-blocking execution with JobClient callback
- Call getJobExecutionResult().get() on JobClient to await and retrieve results

## Workflow Steps

- {'step': 1, 'action': 'Verify pipeline is complete with all transformations and sinks attached'}
- {'step': 2, 'action': 'Choose execution mode: call execute() for synchronous or executeAsync() for asynchronous'}
- {'step': 3, 'action': 'If using executeAsync(), obtain JobClient and call getJobExecutionResult().get() to retrieve results'}
- {'step': 4, 'action': 'Inspect JobExecutionResult for execution times and accumulator values'}

## Constraints

- StreamExecutionEnvironment must be instantiated before calling execute() or executeAsync()
- All DataStream transformations must be defined before execution
- At least one sink must be attached to the pipeline

## Cautions

- Synchronous execute() blocks until job completion; use executeAsync() for non-blocking behavior in interactive environments
- JobClient.getJobExecutionResult().get() is a blocking call; consider timeout handling in production

## Output Contract

- Returns JobExecutionResult containing execution times, accumulator results, and job completion status. Synchronous execute() returns result directly; asynchronous executeAsync() returns JobClient from which result is retrieved via getJobExecutionResult().get().

## Example Therapist Responses

### Example 1

- Client/Input: StreamExecutionEnvironment with complete pipeline (source → transformations → sink)
- Therapist/Output: JobExecutionResult with execution duration and accumulator metrics
- Notes: Synchronous execution using execute()

### Example 2

- Client/Input: StreamExecutionEnvironment with complete pipeline, non-blocking requirement
- Therapist/Output: JobClient object; calling getJobExecutionResult().get() yields JobExecutionResult
- Notes: Asynchronous execution using executeAsync()

## Triggers

- Pipeline definition is complete and ready to run; need to start job and monitor execution results

## Examples

### Example 1

Input:

  StreamExecutionEnvironment with complete pipeline (source → transformations → sink)

Output:

  JobExecutionResult with execution duration and accumulator metrics

Notes:

  Synchronous execution using execute()

### Example 2

Input:

  StreamExecutionEnvironment with complete pipeline, non-blocking requirement

Output:

  JobClient object; calling getJobExecutionResult().get() yields JobExecutionResult

Notes:

  Asynchronous execution using executeAsync()
