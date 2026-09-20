---
id: "2b0663c7-63de-51bc-8f55-5b5afe69ec2e"
name: "Contention-Level Workload Evaluation"
description: "Execute and measure concurrency control algorithm performance under medium and high contention YCSB workloads to assess behavior across different conflict intensities and isolation levels."
version: "0.1.0"
tags:
  - "benchmarking"
  - "concurrency_control"
  - "performance_evaluation"
  - "isolation_levels"
  - "YCSB"
  - "contention_analysis"
triggers:
  - "Comparing concurrency control algorithms"
  - "Testing robustness under varying conflict rates"
  - "Validating optimization effectiveness across workload conditions"
examples:
  - input: "Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; medium-contention YCSB; 40 threads"
    output: "Medium contention: TICTOC SR throughput 2.57M txn/s (1.76% abort), RR throughput 2.69M txn/s (0.72% abort); DL_DETECT SR throughput 0.43M txn/s (0.35% abort), RR throughput 0.72M txn/s (0.10% abort)"
    notes: "Optimistic algorithms show 4.7% improvement SR→RR; pessimistic algorithms show 67.4% improvement"
  - input: "Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; high-contention YCSB; 40 threads"
    output: "High contention: TICTOC SR throughput 1.04M txn/s (1.76% abort), RR throughput 1.04M txn/s (0.72% abort); NO_WAIT SR throughput 0.35M txn/s (63.2% abort), RR throughput 1.89M txn/s (9.9% abort)"
    notes: "High contention reduces isolation level benefits; RR slightly better than SI; abort rates remain high due to hotspot saturation"
---

# Contention-Level Workload Evaluation

Execute and measure concurrency control algorithm performance under medium and high contention YCSB workloads to assess behavior across different conflict intensities and isolation levels.

## Prompt

Run YCSB benchmark with 40 threads at medium and high contention levels. For each contention level, measure throughput (Million txn/s) and abort rate (%) across all target algorithms. Test under serializable (SR), repeatable read (RR), and snapshot isolation (SI) isolation levels where supported. Record commit timestamp growth rates and relative performance deltas between contention levels.

## Objective

Characterize algorithm performance across contention spectrum to expose robustness and optimization effectiveness under varying conflict rates.
## Applicable Signals

- Comparing multiple concurrency control algorithms
- Testing algorithm robustness under varying conflict rates
- Validating optimization effectiveness across workload conditions
- Assessing isolation level performance trade-offs

## Contraindications

- Single fixed-contention workload only
- Non-transactional systems
- Workloads without tunable conflict parameters
- Systems unable to support multiple isolation levels

## Workflow Steps

- {'step': 1, 'action': 'Configure YCSB benchmark', 'detail': 'Set up medium-contention workload (sufficient parallelism for optimistic algorithms to show small improvements)'}
- {'step': 2, 'action': 'Execute medium-contention test', 'detail': 'Run all target algorithms under SR, RR, and SI isolation levels (where supported) with 40 threads; record throughput and abort rate'}
- {'step': 3, 'action': 'Configure high-contention workload', 'detail': 'Increase contention to expose algorithm behavior under significant hotspot conflicts'}
- {'step': 4, 'action': 'Execute high-contention test', 'detail': 'Run all target algorithms under SR, RR, and SI isolation levels (where supported) with 40 threads; record throughput and abort rate'}
- {'step': 5, 'action': 'Analyze timestamp growth', 'detail': 'Track commit timestamp values over time; compare growth rate relative to number of committed transactions'}
- {'step': 6, 'action': 'Compute performance deltas', 'detail': 'Calculate throughput and abort rate improvements/degradation from SR to RR and SI for each algorithm and contention level'}

## Constraints

- Use YCSB benchmark with configurable contention parameters
- Run with consistent thread count (40 threads recommended)
- Test at minimum two contention levels: medium and high
- Measure both throughput and abort rate for each configuration
- Support isolation levels appropriate to each algorithm (SR mandatory; RR and SI where applicable)

## Cautions

- Lower isolation levels (RR, SI) may not be supported by all algorithms; document unsupported combinations
- High contention workloads may show reduced abort rate improvements due to saturation on hotspot tuples
- Timestamp growth rates vary significantly by contention level; track separately for analysis

## Output Contract

- Structured performance report containing: (a) throughput (Million txn/s) and abort rate (%) tables for medium and high contention levels, organized by algorithm and isolation level; (b) relative performance improvements (%) from SR baseline to RR and SI; (c) timestamp growth rate analysis showing logical time growth relative to committed transaction count; (d) summary of algorithm robustness across contention spectrum.

## Example Executions

### Example 1

- Input: Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; medium-contention YCSB; 40 threads
- Output: Medium contention: TICTOC SR throughput 2.57M txn/s (1.76% abort), RR throughput 2.69M txn/s (0.72% abort); DL_DETECT SR throughput 0.43M txn/s (0.35% abort), RR throughput 0.72M txn/s (0.10% abort)
- Notes: Optimistic algorithms show 4.7% improvement SR→RR; pessimistic algorithms show 67.4% improvement

### Example 2

- Input: Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; high-contention YCSB; 40 threads
- Output: High contention: TICTOC SR throughput 1.04M txn/s (1.76% abort), RR throughput 1.04M txn/s (0.72% abort); NO_WAIT SR throughput 0.35M txn/s (63.2% abort), RR throughput 1.89M txn/s (9.9% abort)
- Notes: High contention reduces isolation level benefits; RR slightly better than SI; abort rates remain high due to hotspot saturation

## Triggers

- Comparing concurrency control algorithms
- Testing robustness under varying conflict rates
- Validating optimization effectiveness across workload conditions

## Examples

### Example 1

Input:

  Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; medium-contention YCSB; 40 threads

Output:

  Medium contention: TICTOC SR throughput 2.57M txn/s (1.76% abort), RR throughput 2.69M txn/s (0.72% abort); DL_DETECT SR throughput 0.43M txn/s (0.35% abort), RR throughput 0.72M txn/s (0.10% abort)

Notes:

  Optimistic algorithms show 4.7% improvement SR→RR; pessimistic algorithms show 67.4% improvement

### Example 2

Input:

  Target algorithms: DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC; high-contention YCSB; 40 threads

Output:

  High contention: TICTOC SR throughput 1.04M txn/s (1.76% abort), RR throughput 1.04M txn/s (0.72% abort); NO_WAIT SR throughput 0.35M txn/s (63.2% abort), RR throughput 1.89M txn/s (9.9% abort)

Notes:

  High contention reduces isolation level benefits; RR slightly better than SI; abort rates remain high due to hotspot saturation
