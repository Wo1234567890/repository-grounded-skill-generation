---
id: "b22fc17b-e60f-5a3a-a54d-915628daeaa5"
name: "Isolation Level Performance Comparison"
description: "Execute a controlled performance evaluation comparing multiple concurrency control algorithms under identical workload conditions but with different isolation levels (Serializable, Snapshot Isolation, Repeatable Read). Measure throughput and abort rates across medium and high contention workloads to isolate the performance impact of isolation level choice from other optimization variables."
version: "0.1.0"
tags:
  - "concurrency_control"
  - "isolation_levels"
  - "performance_evaluation"
  - "benchmarking"
  - "YCSB"
  - "throughput"
triggers:
  - "Need to assess how isolation level choice affects throughput and abort rates"
  - "Comparing multiple concurrency control algorithms under identical workload conditions"
  - "Evaluating trade-offs between isolation strength and performance"
examples:
  - input: "TICTOC algorithm, Serializable isolation, medium contention YCSB workload, 40 threads"
    output: "Throughput: 2.57 Million txn/s, Abort Rate: 1.76%"
    notes: "Baseline serializable result for TICTOC under medium contention"
  - input: "TICTOC algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads"
    output: "Throughput: 2.69 Million txn/s, Abort Rate: 0.72%"
    notes: "RR isolation shows 4.7% throughput improvement and lower abort rate due to fewer conflicts"
  - input: "DL_DETECT algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads"
    output: "Throughput: 0.72 Million txn/s, Abort Rate: 0.10%"
    notes: "Pessimistic 2PL algorithm shows 67.4% improvement from SR to RR under medium contention"
---

# Isolation Level Performance Comparison

Execute a controlled performance evaluation comparing multiple concurrency control algorithms under identical workload conditions but with different isolation levels (Serializable, Snapshot Isolation, Repeatable Read). Measure throughput and abort rates across medium and high contention workloads to isolate the performance impact of isolation level choice from other optimization variables.

## Prompt

Execute a controlled performance evaluation comparing multiple concurrency control algorithms under the same workload but with different isolation levels (Serializable, Snapshot Isolation, Repeatable Read). For each algorithm-isolation level combination, measure throughput in Million txn/s and abort rate in percentage. Use medium and high contention YCSB workloads with consistent thread count (e.g., 40 threads). Record results in a comparative table format.

## Objective

Measure isolation level impact on DBMS concurrency control performance
## Applicable Signals

- Multiple algorithms available for testing
- Workload supports variable isolation levels
- Baseline performance metrics needed for decision-making

## Contraindications

- Single-algorithm tuning or optimization (use algorithm-specific tuning instead)
- Workloads with no isolation level variation support
- Systems that do not support multiple isolation levels
- Scenarios where isolation level is fixed by requirement

## Workflow Steps

- {'step': 1, 'action': 'Prepare test environment', 'detail': 'Configure DBMS with all target concurrency control algorithms (e.g., DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC). Set thread count to 40 and prepare medium and high contention YCSB workloads.'}
- {'step': 2, 'action': 'Execute baseline run', 'detail': 'Run each algorithm under Serializable (SR) isolation level with medium contention workload. Record throughput and abort rate.'}
- {'step': 3, 'action': 'Test lower isolation levels', 'detail': 'For each algorithm that supports Repeatable Read (RR) and Snapshot Isolation (SI), execute runs under those isolation levels. Record throughput and abort rate for each combination.'}
- {'step': 4, 'action': 'Repeat with high contention', 'detail': 'Execute the same isolation level tests using high contention YCSB workload. Record all metrics.'}
- {'step': 5, 'action': 'Compile results', 'detail': 'Organize results into comparative tables showing throughput (Million txn/s) and abort rate (%) for each algorithm-isolation level combination, separated by contention level.'}
- {'step': 6, 'action': 'Analyze patterns', 'detail': 'Identify which algorithms benefit most from lower isolation levels, note abort rate reductions, and document any algorithms that do not support certain isolation levels.'}

## Constraints

- All algorithms must be tested under identical workload conditions
- Thread count and contention level must remain constant across runs
- Only test isolation levels supported by each algorithm (e.g., SI may not be available for all schemes)
- Use consistent YCSB workload configurations (medium and high contention)

## Cautions

- Lower isolation levels may not be supported by all algorithms; document which algorithms support which levels
- Abort rate improvements at lower isolation levels may be due to fewer conflicts rather than algorithm efficiency
- High contention workloads may show minimal abort rate differences across isolation levels

## Output Contract

- Comparative performance table(s) with rows for each algorithm (DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC, etc.) and columns for each isolation level (SR, SI, RR), showing throughput in Million txn/s and abort rate in percentage. Results must be separated by contention level (medium and high). All tested algorithm-isolation combinations must be documented; unsupported combinations must be explicitly marked.

## Example Executions

### Example 1

- Input: TICTOC algorithm, Serializable isolation, medium contention YCSB workload, 40 threads
- Output: Throughput: 2.57 Million txn/s, Abort Rate: 1.76%
- Notes: Baseline serializable result for TICTOC under medium contention

### Example 2

- Input: TICTOC algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads
- Output: Throughput: 2.69 Million txn/s, Abort Rate: 0.72%
- Notes: RR isolation shows 4.7% throughput improvement and lower abort rate due to fewer conflicts

### Example 3

- Input: DL_DETECT algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads
- Output: Throughput: 0.72 Million txn/s, Abort Rate: 0.10%
- Notes: Pessimistic 2PL algorithm shows 67.4% improvement from SR to RR under medium contention

## Triggers

- Need to assess how isolation level choice affects throughput and abort rates
- Comparing multiple concurrency control algorithms under identical workload conditions
- Evaluating trade-offs between isolation strength and performance

## Examples

### Example 1

Input:

  TICTOC algorithm, Serializable isolation, medium contention YCSB workload, 40 threads

Output:

  Throughput: 2.57 Million txn/s, Abort Rate: 1.76%

Notes:

  Baseline serializable result for TICTOC under medium contention

### Example 2

Input:

  TICTOC algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads

Output:

  Throughput: 2.69 Million txn/s, Abort Rate: 0.72%

Notes:

  RR isolation shows 4.7% throughput improvement and lower abort rate due to fewer conflicts

### Example 3

Input:

  DL_DETECT algorithm, Repeatable Read isolation, medium contention YCSB workload, 40 threads

Output:

  Throughput: 0.72 Million txn/s, Abort Rate: 0.10%

Notes:

  Pessimistic 2PL algorithm shows 67.4% improvement from SR to RR under medium contention
