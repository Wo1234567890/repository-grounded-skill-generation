---
id: "a149e750-8011-5b7c-a6ea-479311e98bb1"
name: "S3-FIFO Quick Demotion Tuning"
description: "Adjust the static FIFO queue size (S) as a percentage of cache size to balance demotion speed and precision, filtering out low-value objects while preserving popular ones. Establishes baseline miss ratio, sets initial S configuration, measures demotion speed and precision metrics, and iteratively tunes S within 5–20% range to achieve lower miss ratio than LRU baseline."
version: "0.1.0"
tags:
  - "cache_eviction"
  - "queue_sizing"
  - "performance_tuning"
  - "fifo_algorithm"
  - "demotion_precision"
triggers:
  - "cache miss ratio is suboptimal relative to baseline"
  - "workload characteristics are known or measurable"
  - "S size adjustment is needed across multiple traces"
examples:
  - input: "Cache size 1000 objects, Twitter trace with many requests per object and constant new object generation."
    output: "S set to 1% of cache size (10 objects) for maximum demotion speed; miss ratio reduced by ~15% compared to LRU."
    notes: "Smaller S is effective when workload has high object reuse frequency."
  - input: "Cache size 10000 objects, MSR trace with moderate request patterns."
    output: "S set to 10% of cache size (1000 objects); miss ratio reduced by ~8% compared to LRU; precision and speed both balanced."
    notes: "10% is a robust default that generalizes across diverse traces."
---

# S3-FIFO Quick Demotion Tuning

Adjust the static FIFO queue size (S) as a percentage of cache size to balance demotion speed and precision, filtering out low-value objects while preserving popular ones. Establishes baseline miss ratio, sets initial S configuration, measures demotion speed and precision metrics, and iteratively tunes S within 5–20% range to achieve lower miss ratio than LRU baseline.

## Prompt

Set S to a percentage of total cache size. Start with 10% as a baseline. Measure miss ratio, demotion speed (time in S before eviction), and precision (fraction of evicted objects not reused soon). Adjust S within the range 5–20% for most workloads, or 1–10% for large caches. Log both speed and precision metrics to confirm improvement over LRU baseline.

## Objective

optimize_cache_eviction_policy
## Applicable Signals

- elevated miss ratio compared to LRU
- availability of trace data or workload profile
- need for predictable demotion behavior

## Contraindications

- cache size is extremely small (< 100 objects)
- workload is purely random with no temporal locality
- real-time latency constraints prohibit ghost queue overhead

## Workflow Steps

- {'step': 1, 'action': 'Establish baseline miss ratio using LRU eviction age as reference.'}
- {'step': 2, 'action': 'Set S to 10% of cache size as initial configuration.'}
- {'step': 3, 'action': 'Measure quick demotion speed: calculate (time in S) / (LRU eviction age) using logical time in request count.'}
- {'step': 4, 'action': 'Measure quick demotion precision: count objects evicted from S that are not reused within (cache size / miss ratio) requests.'}
- {'step': 5, 'action': 'Record miss ratio and compare to baseline.'}
- {'step': 6, 'action': 'If miss ratio is not improved, adjust S within 5–20% range and repeat steps 3–5.'}
- {'step': 7, 'action': 'Confirm that both speed and precision metrics are logged and that miss ratio is lower than LRU baseline.'}

## Constraints

- S must be a static percentage of cache size
- S size should remain between 5% and 20% for most workloads to avoid precision cliffs
- Smaller S increases demotion speed but reduces precision; larger S increases precision but slows demotion

## Cautions

- When S is very small, popular objects may not accumulate enough hits before eviction, reducing precision.
- When S is very large, many unpopular objects are moved to M, reducing precision and increasing miss ratio.
- Precision shows non-monotonic behavior; peak precision occurs at an intermediate S size.

## Output Contract

- S size is set to a percentage of cache size (typically 5–20%, or 1–10% for large caches)
- Miss ratio is reduced compared to LRU baseline
- Demotion speed and precision metrics are measured and logged

## Example Therapist Responses

### Example 1

- Client/Input: Cache size 1000 objects, Twitter trace with many requests per object and constant new object generation.
- Therapist/Output: S set to 1% of cache size (10 objects) for maximum demotion speed; miss ratio reduced by ~15% compared to LRU.
- Notes: Smaller S is effective when workload has high object reuse frequency.

### Example 2

- Client/Input: Cache size 10000 objects, MSR trace with moderate request patterns.
- Therapist/Output: S set to 10% of cache size (1000 objects); miss ratio reduced by ~8% compared to LRU; precision and speed both balanced.
- Notes: 10% is a robust default that generalizes across diverse traces.

## Triggers

- cache miss ratio is suboptimal relative to baseline
- workload characteristics are known or measurable
- S size adjustment is needed across multiple traces

## Examples

### Example 1

Input:

  Cache size 1000 objects, Twitter trace with many requests per object and constant new object generation.

Output:

  S set to 1% of cache size (10 objects) for maximum demotion speed; miss ratio reduced by ~15% compared to LRU.

Notes:

  Smaller S is effective when workload has high object reuse frequency.

### Example 2

Input:

  Cache size 10000 objects, MSR trace with moderate request patterns.

Output:

  S set to 10% of cache size (1000 objects); miss ratio reduced by ~8% compared to LRU; precision and speed both balanced.

Notes:

  10% is a robust default that generalizes across diverse traces.
