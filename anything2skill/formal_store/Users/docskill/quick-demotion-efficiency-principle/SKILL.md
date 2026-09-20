---
id: "da8dd853-552c-5d47-8cc8-3af6fa1a9896"
name: "Quick Demotion Efficiency Principle"
description: "Evidence-based design guidance for cache eviction algorithm selection. Establishes that rapid demotion of unpopular objects from main cache to secondary storage is critical for cache efficiency. Supported by empirical data from TinyLFU's 1% LRU window filtering and S3-FIFO's three-queue design, showing consistent miss ratio improvements across diverse cache workloads."
version: "0.1.0"
tags:
  - "cache_eviction"
  - "algorithm_design"
  - "efficiency_principle"
  - "demotion_strategy"
  - "miss_ratio_optimization"
triggers:
  - "Evaluating or designing cache eviction algorithms"
  - "Explaining why certain algorithms (TinyLFU, S3-FIFO) outperform simpler FIFO"
  - "Tuning demotion thresholds"
examples:
  - input: "Designing a cache eviction algorithm for a key-value store with mixed read-write workload"
    output: "Incorporate a quick demotion mechanism (e.g., 1–5% LRU window or multi-queue design) to filter unpopular objects early. Expect 10–32% miss ratio reduction vs. FIFO depending on cache size and workload."
    notes: "TinyLFU's 1% window is a proven pattern; S3-FIFO's three-queue design is an alternative."
  - input: "Evaluating whether to add demotion overhead to an existing FIFO cache"
    output: "Yes, if cache size is large and workload is read-heavy. Empirical data shows S3-FIFO achieves 14% mean miss ratio reduction on large caches. Avoid if cache is small or write-heavy."
    notes: "TinyLFU degrades on ~50% of small-cache traces; validate on representative traces first."
---

# Quick Demotion Efficiency Principle

Evidence-based design guidance for cache eviction algorithm selection. Establishes that rapid demotion of unpopular objects from main cache to secondary storage is critical for cache efficiency. Supported by empirical data from TinyLFU's 1% LRU window filtering and S3-FIFO's three-queue design, showing consistent miss ratio improvements across diverse cache workloads.

## Prompt

When evaluating or designing cache eviction algorithms, apply this principle: prioritize mechanisms that quickly demote unpopular objects to secondary tiers. Reference TinyLFU's 1% LRU window filter and S3-FIFO's queue-based demotion as proven patterns. Use miss ratio reduction data (e.g., 32% improvement at P90, 14% mean on large cache sizes) to justify demotion overhead in design trade-offs.

## Objective

Provide evidence-based design guidance for cache eviction algorithm selection and optimization
## Applicable Signals

- Evaluating cache eviction algorithms for efficiency improvements
- Designing new cache replacement policies
- Explaining performance gaps between FIFO and advanced algorithms
- Tuning demotion thresholds or window sizes

## Contraindications

- Fixed-window caches without demotion capability
- Write-heavy workloads where demotion cost exceeds benefit
- Memory-constrained systems where secondary tier overhead is prohibitive

## Constraints

- Principle applies primarily to read-heavy and mixed workloads
- Effectiveness varies by cache size; TinyLFU shows degradation on small caches (worse than FIFO on ~50% of traces at small sizes)
- Requires measurable miss ratio data to validate demotion strategy

## Cautions

- TinyLFU's 1% window does not work uniformly across all traces; P10 point falls below -0.05 on ~20% of traces
- Demotion strategy must be tuned per workload type (block, key-value, object)

## Output Contract

- Design decision documented with reference to comparative miss ratio reduction data (vs. FIFO baseline) and demotion mechanism rationale
- Caller receives actionable guidance on whether quick demotion is justified for their cache workload and size profile

## Example Therapist Responses

### Example 1

- Client/Input: Designing a cache eviction algorithm for a key-value store with mixed read-write workload
- Therapist/Output: Incorporate a quick demotion mechanism (e.g., 1–5% LRU window or multi-queue design) to filter unpopular objects early. Expect 10–32% miss ratio reduction vs. FIFO depending on cache size and workload.
- Notes: TinyLFU's 1% window is a proven pattern; S3-FIFO's three-queue design is an alternative.

### Example 2

- Client/Input: Evaluating whether to add demotion overhead to an existing FIFO cache
- Therapist/Output: Yes, if cache size is large and workload is read-heavy. Empirical data shows S3-FIFO achieves 14% mean miss ratio reduction on large caches. Avoid if cache is small or write-heavy.
- Notes: TinyLFU degrades on ~50% of small-cache traces; validate on representative traces first.

## Triggers

- Evaluating or designing cache eviction algorithms
- Explaining why certain algorithms (TinyLFU, S3-FIFO) outperform simpler FIFO
- Tuning demotion thresholds

## Examples

### Example 1

Input:

  Designing a cache eviction algorithm for a key-value store with mixed read-write workload

Output:

  Incorporate a quick demotion mechanism (e.g., 1–5% LRU window or multi-queue design) to filter unpopular objects early. Expect 10–32% miss ratio reduction vs. FIFO depending on cache size and workload.

Notes:

  TinyLFU's 1% window is a proven pattern; S3-FIFO's three-queue design is an alternative.

### Example 2

Input:

  Evaluating whether to add demotion overhead to an existing FIFO cache

Output:

  Yes, if cache size is large and workload is read-heavy. Empirical data shows S3-FIFO achieves 14% mean miss ratio reduction on large caches. Avoid if cache is small or write-heavy.

Notes:

  TinyLFU degrades on ~50% of small-cache traces; validate on representative traces first.
