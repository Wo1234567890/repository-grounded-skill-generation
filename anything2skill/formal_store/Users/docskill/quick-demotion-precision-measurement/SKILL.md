---
id: "7d3fb3c1-926f-5f1e-a4a6-30e1371a5d82"
name: "Quick Demotion Precision Measurement"
description: "Measure the precision of object eviction from a FIFO queue by determining what fraction of evicted objects are not reused within a threshold window. Use to validate that demotion decisions are correct and not prematurely evicting reusable objects."
version: "0.1.0"
tags:
  - "cache_eviction"
  - "measurement"
  - "precision"
  - "fifo"
  - "demotion"
  - "correctness"
triggers:
  - "Comparing cache eviction algorithms"
  - "Tuning FIFO queue size parameter"
  - "Validating that quick demotion is not too aggressive"
  - "Analyzing miss ratio cliffs or performance anomalies"
examples:
  - input: "Trace with 1M requests; cache size 10K; S size 1K (10% of cache); computed miss ratio 0.05"
    output: "Precision = 0.78; threshold = 10K / 0.05 = 200K requests; 78% of objects evicted from S are not reused within 200K requests"
    notes: "Moderate precision indicates balanced demotion; correlates with lower miss ratio compared to LRU"
  - input: "Same trace; S size 100 (1% of cache)"
    output: "Precision = 0.62; faster demotion but lower precision; more objects evicted before accumulating hits"
    notes: "Smaller S increases miss ratio on some traces due to precision loss"
---

# Quick Demotion Precision Measurement

Measure the precision of object eviction from a FIFO queue by determining what fraction of evicted objects are not reused within a threshold window. Use to validate that demotion decisions are correct and not prematurely evicting reusable objects.

## Prompt

For each object evicted from the FIFO queue (S), check if it is reused within a threshold of (cache_size / miss_ratio) requests. Count objects that are NOT reused within this threshold as correctly early-evicted. Compute precision as the fraction of evicted objects that meet this criterion. Plot precision against queue size parameter to identify peak precision and correlate with miss ratio changes.

## Objective

measure_eviction_correctness
## Applicable Signals

- Trace data with request sequence and object reuse patterns available
- Need to correlate demotion speed with eviction correctness
- Investigating why certain queue size settings produce unexpected miss ratios

## Contraindications

- Trace data is unavailable or incomplete
- Reuse distance cannot be computed from available logs
- Only throughput or latency metrics matter; correctness is not a concern

## Workflow Steps

- {'step': 1, 'action': 'Extract eviction events from FIFO queue S', 'detail': 'Record each object evicted from S and the logical time (request count) at eviction'}
- {'step': 2, 'action': 'Compute reuse distance for each evicted object', 'detail': 'For each evicted object, find the next request to that object in the trace and calculate the number of requests between eviction and reuse'}
- {'step': 3, 'action': 'Calculate threshold', 'detail': 'Compute threshold as cache_size / miss_ratio (in request counts)'}
- {'step': 4, 'action': 'Classify evictions as correct or incorrect', 'detail': 'Mark eviction as correct early eviction if reuse distance > threshold; otherwise mark as incorrect (object was needed soon)'}
- {'step': 5, 'action': 'Compute precision score', 'detail': 'Precision = (count of correct early evictions) / (total evictions from S)'}
- {'step': 6, 'action': 'Plot and analyze', 'detail': 'Plot precision against queue size parameter S; identify peak precision; correlate with miss ratio curve'}

## Constraints

- Requires complete request trace with object identifiers and timestamps
- Threshold calculation depends on accurate miss ratio measurement
- Logical time (request count) must be used consistently throughout measurement

## Cautions

- Small S leads to faster demotion but lower precision (objects evicted before accumulating hits)
- Large S leads to higher precision but slower demotion (unpopular objects accumulate hits before eviction)
- Precision peak occurs at intermediate S values; both extremes degrade performance

## Output Contract

- Precision score (0.0–1.0) representing fraction of correctly early-evicted objects
- Precision curve plotted against S size
- Peak precision value identified
- Correlation between precision and miss ratio confirmed or noted

## Example Therapist Responses

### Example 1

- Client/Input: Trace with 1M requests; cache size 10K; S size 1K (10% of cache); computed miss ratio 0.05
- Therapist/Output: Precision = 0.78; threshold = 10K / 0.05 = 200K requests; 78% of objects evicted from S are not reused within 200K requests
- Notes: Moderate precision indicates balanced demotion; correlates with lower miss ratio compared to LRU

### Example 2

- Client/Input: Same trace; S size 100 (1% of cache)
- Therapist/Output: Precision = 0.62; faster demotion but lower precision; more objects evicted before accumulating hits
- Notes: Smaller S increases miss ratio on some traces due to precision loss

## Triggers

- Comparing cache eviction algorithms
- Tuning FIFO queue size parameter
- Validating that quick demotion is not too aggressive
- Analyzing miss ratio cliffs or performance anomalies

## Examples

### Example 1

Input:

  Trace with 1M requests; cache size 10K; S size 1K (10% of cache); computed miss ratio 0.05

Output:

  Precision = 0.78; threshold = 10K / 0.05 = 200K requests; 78% of objects evicted from S are not reused within 200K requests

Notes:

  Moderate precision indicates balanced demotion; correlates with lower miss ratio compared to LRU

### Example 2

Input:

  Same trace; S size 100 (1% of cache)

Output:

  Precision = 0.62; faster demotion but lower precision; more objects evicted before accumulating hits

Notes:

  Smaller S increases miss ratio on some traces due to precision loss
