---
id: "f2b36c3b-3cba-56ab-9b08-7c7fb4b33b93"
name: "Execute Flink Job and Retrieve Results"
description: "Trigger job execution on the configured StreamExecutionEnvironment and optionally wait for completion to retrieve execution metrics and accumulator results."
version: "0.1.0"
tags:
  - "flink"
  - "datastream"
  - "job_execution"
  - "execution_control"
  - "async_execution"
triggers:
  - "All sources, transformations, and sinks are defined in the DataStream pipeline"
  - "Ready to run the job and need execution metrics"
  - "Need to obtain a JobClient for asynchronous monitoring"
examples:
  - input: "StreamExecutionEnvironment with complete pipeline (sources, map transformation, text sink)"
    output: "JobExecutionResult with execution duration and any registered accumulator values"
    notes: "Synchronous execution; caller blocks until job finishes"
  - input: "StreamExecutionEnvironment with complete pipeline; caller needs non-blocking submission"
    output: "JobClient; caller later calls getJobExecutionResult().get() to retrieve JobExecutionResult"
    notes: "Asynchronous execution; caller can perform other work while job runs"
---

# Execute Flink Job and Retrieve Results

Trigger job execution on the configured StreamExecutionEnvironment and optionally wait for completion to retrieve execution metrics and accumulator results.

## Prompt

Call execute() on the StreamExecutionEnvironment to submit the job synchronously and block until completion, returning a JobExecutionResult. Alternatively, call executeAsync() to submit asynchronously and obtain a JobClient, then call getJobExecutionResult().get() on the client to retrieve results when ready. The JobExecutionResult contains execution times and accumulator values.

## Objective

Submit and monitor job execution
## Applicable Signals

- Pipeline definition complete
- Caller requires execution results or job handle
- Synchronous or asynchronous execution mode selected

## Contraindications

- Job definition is incomplete
- Still adding sources or sinks to the pipeline
- Testing without actual execution required

## Workflow Steps

- {'step': 1, 'action': 'Verify pipeline is complete with sources, transformations, and sinks', 'condition': 'All DataStream operations defined'}
- {'step': 2, 'action': 'Choose execution mode: synchronous via execute() or asynchronous via executeAsync()', 'condition': 'Caller determines blocking vs. non-blocking requirement'}
- {'step': 3, 'action': 'Call execute() on StreamExecutionEnvironment to submit and wait for completion', 'condition': 'Synchronous execution desired; returns JobExecutionResult'}
- {'step': 4, 'action': 'Alternatively, call executeAsync() to submit without blocking', 'condition': 'Asynchronous execution desired; returns JobClient'}
- {'step': 5, 'action': 'Retrieve results via JobExecutionResult (synchronous) or jobClient.getJobExecutionResult().get() (asynchronous)', 'condition': 'Job execution complete or results needed'}

## Constraints

- StreamExecutionEnvironment must be configured before calling execute() or executeAsync()
- All DataStream transformations and sinks must be defined
- Execution will block (synchronous) or return immediately with a JobClient (asynchronous)

## Cautions

- execute() blocks until job completion; use executeAsync() for non-blocking submission
- JobExecutionResult is only available after job completion
- Accumulator results are populated only if accumulators were registered in the job

## Output Contract

- Returns JobExecutionResult containing execution times and accumulator results (synchronous mode), or JobClient handle for asynchronous monitoring and later result retrieval

## Example Executions

### Example 1

- Input: StreamExecutionEnvironment with complete pipeline (sources, map transformation, text sink)
- Output: JobExecutionResult with execution duration and any registered accumulator values
- Notes: Synchronous execution; caller blocks until job finishes

### Example 2

- Input: StreamExecutionEnvironment with complete pipeline; caller needs non-blocking submission
- Output: JobClient; caller later calls getJobExecutionResult().get() to retrieve JobExecutionResult
- Notes: Asynchronous execution; caller can perform other work while job runs

## Triggers

- All sources, transformations, and sinks are defined in the DataStream pipeline
- Ready to run the job and need execution metrics
- Need to obtain a JobClient for asynchronous monitoring

## Examples

### Example 1

Input:

  StreamExecutionEnvironment with complete pipeline (sources, map transformation, text sink)

Output:

  JobExecutionResult with execution duration and any registered accumulator values

Notes:

  Synchronous execution; caller blocks until job finishes

### Example 2

Input:

  StreamExecutionEnvironment with complete pipeline; caller needs non-blocking submission

Output:

  JobClient; caller later calls getJobExecutionResult().get() to retrieve JobExecutionResult

Notes:

  Asynchronous execution; caller can perform other work while job runs
