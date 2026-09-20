---
id: "c5c4ecd1-c049-5160-b173-3c8967796f9d"
name: "Execute Model Evaluation on Standard Benchmarks"
description: "Execute TPC-C and high-contention benchmark workloads against multiple concurrency control protocols. Measure throughput (million txn/s) and abort rate under variable warehouse counts and contention levels. Compare results across protocol variants to validate performance characteristics."
version: "0.1.1"
tags:
  - "performance_evaluation"
  - "concurrency_control"
  - "benchmarking"
  - "tpc_c"
  - "throughput_measurement"
  - "abort_rate"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to assess model performance on established benchmarks"
  - "Comparing model variants or releases"
  - "Post-training model assessment required"
---

# Execute Model Evaluation on Standard Benchmarks

Execute TPC-C and high-contention benchmark workloads against multiple concurrency control protocols. Measure throughput (million txn/s) and abort rate under variable warehouse counts and contention levels. Compare results across protocol variants to validate performance characteristics.

## Prompt

1. Configure benchmark environment with stable timestamp generation (≥5 million timestamps/second).
2. Execute TPC-C workload with variable warehouse counts (e.g., 1, 4, 8, 16).
3. Execute high-contention workload variant.
4. For each configuration, measure and record: throughput (million txn/s), abort rate.
5. Repeat measurements across all protocol variants being compared (e.g., DL_DETECT, HEKATON, NO_WAIT, SILO, TicToc).
6. Generate comparative charts and summary metrics.
7. Validate that TicToc performance is captured relative to baseline protocols.

## Objective

Systematically measure and report transaction throughput and abort rate under controlled workload conditions to enable protocol performance comparison
## Applicable Signals

- Need to validate protocol performance under realistic workloads
- Comparing multiple concurrency control implementations
- Varying warehouse count or contention parameters
- Evaluating timestamp-based protocol variants

## Contraindications

- Single-transaction testing or non-comparative evaluation
- Systems without stable timestamp generation capability (target: ≥5 million timestamps/second)
- Environments where workload isolation or repeatability cannot be guaranteed

## Workflow Steps

- {'step': 1, 'action': 'Initialize benchmark environment', 'detail': 'Verify timestamp generation capability (≥5 million/second); configure workload parameters'}
- {'step': 2, 'action': 'Execute TPC-C workload', 'detail': 'Run with variable warehouse counts; measure throughput and abort rate for each protocol variant'}
- {'step': 3, 'action': 'Execute high-contention workload', 'detail': 'Apply contention variant; measure throughput and abort rate for each protocol variant'}
- {'step': 4, 'action': 'Collect and aggregate metrics', 'detail': 'Record throughput (million txn/s) and abort rate for all configurations and protocol variants'}
- {'step': 5, 'action': 'Generate comparative analysis', 'detail': 'Create charts and summary showing TicToc performance relative to baseline protocols'}

## Constraints

- Timestamp generation must be stable and high-frequency
- All protocol variants must be tested under identical workload configurations
- Measurements must be taken after warm-up period to exclude initialization overhead
- Abort rate and throughput must be recorded for each configuration

## Cautions

- Ensure workload repeatability across runs to avoid spurious performance variance
- Account for system warm-up time before recording measurements
- Verify that timestamp generation does not become a bottleneck

## Output Contract

- Deliverable: Throughput and abort rate metrics for each protocol variant across all workload configurations. Format: Comparative charts and tabular summary showing TicToc performance relative to DL_DETECT, HEKATON, NO_WAIT, SILO. Success condition: All protocol variants measured under identical conditions with clear performance differentiation visible.

## 子技能目录
- [Run All Tests with Tox](通用技能领域/Family技能/未分类技能/微技能/Run All Tests with Tox/SKILL.md) ｜ 适用：Execute the complete test suite using tox to validate all test environments and configurations in one command.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Run All Tests with Tox` 时，优先调用它。 线索：Need to run all tests across all configured environments, Before committing or merging code, testing, validation, tox

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to assess model performance on established benchmarks
- Comparing model variants or releases
- Post-training model assessment required
