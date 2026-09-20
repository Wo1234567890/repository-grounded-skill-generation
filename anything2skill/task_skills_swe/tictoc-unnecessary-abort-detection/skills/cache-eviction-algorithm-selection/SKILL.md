---
id: "a00caf52-b473-5159-9eaf-9a90857af105"
name: "Cache Eviction Algorithm Selection"
description: "Comparative evaluation protocol for measuring throughput and abort rates across multiple transaction isolation and concurrency control algorithms (DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC) under identical workload conditions. Enables side-by-side performance assessment to identify trade-offs and scalability characteristics."
version: "0.1.1"
tags:
  - "benchmarking"
  - "concurrency_control"
  - "transaction_processing"
  - "performance_comparison"
  - "throughput_measurement"
  - "abort_rate_analysis"
triggers:
  - "Designing or tuning a new cache system"
  - "Comparing eviction algorithm candidates for performance optimization"
  - "Workload characteristics are known or measurable"
  - "Cache efficiency is a primary design constraint"
examples:
  - input: "Benchmark configuration: TPC-C workload, 1 warehouse, low contention"
    output: "Throughput and abort rate table: DL_DETECT (3.0 Mtxn/s, 0.2 abort rate), HEKATON (2.5 Mtxn/s, 0.15), NO_WAIT (2.8 Mtxn/s, 0.18), SILO (3.2 Mtxn/s, 0.22), TICTOC (3.1 Mtxn/s, 0.19)"
    notes: "Lower contention favors algorithms with lower abort overhead"
  - input: "Benchmark configuration: TPC-C workload, variable warehouses, high contention"
    output: "Throughput and abort rate table showing degradation patterns; TICTOC maintains higher throughput with moderate abort rate increase"
    notes: "High contention reveals algorithm scalability differences"
---

# Cache Eviction Algorithm Selection

Comparative evaluation protocol for measuring throughput and abort rates across multiple transaction isolation and concurrency control algorithms (DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC) under identical workload conditions. Enables side-by-side performance assessment to identify trade-offs and scalability characteristics.

## Prompt

Execute a benchmark session comparing transaction concurrency control algorithms. Measure throughput (million transactions per second) and abort rate for each algorithm variant under the same workload conditions. Record results in a structured format suitable for normalized comparison. Ensure workload parameters are held constant across all algorithm runs.

## Objective

Benchmark and compare concurrency control algorithm performance across throughput and abort rate metrics
## Applicable Signals

- Need to evaluate multiple transaction processing algorithms
- Comparing throughput and abort rate trade-offs across implementations
- Assessing algorithm scalability under contention
- Selecting optimal concurrency control strategy for workload

## Contraindications

- Single-algorithm tuning or optimization (use algorithm-specific profiling instead)
- Non-comparative analysis or single-run validation
- Systems without transaction isolation requirements
- Workloads with highly variable or uncontrolled parameters

## Workflow Steps

- {'step': 1, 'action': 'Prepare benchmark environment', 'detail': 'Initialize test harness with all algorithm variants (DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC) in isolated execution contexts'}
- {'step': 2, 'action': 'Define workload specification', 'detail': 'Establish consistent workload parameters (transaction mix, contention level, warehouse count, data distribution) to be applied uniformly across all algorithm runs'}
- {'step': 3, 'action': 'Execute benchmark for each algorithm', 'detail': 'Run each algorithm variant under identical workload conditions, collecting throughput (million txn/s) and abort rate metrics'}
- {'step': 4, 'action': 'Normalize and aggregate results', 'detail': 'Align metrics across algorithms, normalize for workload conditions, and prepare comparative output'}
- {'step': 5, 'action': 'Validate and report', 'detail': 'Verify data consistency, generate comparative charts or tables, and document workload parameters used'}

## Constraints

- All algorithms must run under identical workload conditions to ensure valid comparison
- Throughput and abort rate must be measured simultaneously for each algorithm
- Results must be normalized for workload parameters before comparison
- Sufficient runtime per algorithm to reach steady-state performance

## Cautions

- Abort rate and throughput often exhibit inverse trade-offs; do not optimize for one metric alone
- Contention level significantly affects relative algorithm performance; test across multiple contention scenarios
- Warm-up phase required before measurement to stabilize system state

## Output Contract

- Structured comparative metrics including throughput (million txn/s) and abort rate for each algorithm variant (DL_DETECT, HEKATON, NO_WAIT, SILO, TICTOC), normalized for workload conditions, suitable for side-by-side performance analysis and algorithm selection

## Example Executions

### Example 1

- Input: Benchmark configuration: TPC-C workload, 1 warehouse, low contention
- Output: Throughput and abort rate table: DL_DETECT (3.0 Mtxn/s, 0.2 abort rate), HEKATON (2.5 Mtxn/s, 0.15), NO_WAIT (2.8 Mtxn/s, 0.18), SILO (3.2 Mtxn/s, 0.22), TICTOC (3.1 Mtxn/s, 0.19)
- Notes: Lower contention favors algorithms with lower abort overhead

### Example 2

- Input: Benchmark configuration: TPC-C workload, variable warehouses, high contention
- Output: Throughput and abort rate table showing degradation patterns; TICTOC maintains higher throughput with moderate abort rate increase
- Notes: High contention reveals algorithm scalability differences

## Triggers

- Designing or tuning a new cache system
- Comparing eviction algorithm candidates for performance optimization
- Workload characteristics are known or measurable
- Cache efficiency is a primary design constraint

## Examples

### Example 1

Input:

  Benchmark configuration: TPC-C workload, 1 warehouse, low contention

Output:

  Throughput and abort rate table: DL_DETECT (3.0 Mtxn/s, 0.2 abort rate), HEKATON (2.5 Mtxn/s, 0.15), NO_WAIT (2.8 Mtxn/s, 0.18), SILO (3.2 Mtxn/s, 0.22), TICTOC (3.1 Mtxn/s, 0.19)

Notes:

  Lower contention favors algorithms with lower abort overhead

### Example 2

Input:

  Benchmark configuration: TPC-C workload, variable warehouses, high contention

Output:

  Throughput and abort rate table showing degradation patterns; TICTOC maintains higher throughput with moderate abort rate increase

Notes:

  High contention reveals algorithm scalability differences
