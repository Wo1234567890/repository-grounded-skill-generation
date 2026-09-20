---
id: "f0b918f0-bb71-5ffe-9feb-1d266aa586ee"
name: "One-Hit Wonder Eviction Policy"
description: "Quickly demote and remove single-access cache items from the main cache queue before they pollute the working set. This micro-skill targets transient or scan-like requests that would otherwise occupy cache space without contributing to future hits. Uses a probationary queue to test item popularity before final eviction."
version: "0.1.0"
tags:
  - "cache_eviction"
  - "fifo_queue"
  - "scan_resistance"
  - "probationary_queue"
  - "one_hit_wonder"
  - "quick_demotion"
triggers:
  - "Cache item receives exactly one access"
  - "Scan, streaming, or sequential access pattern detected in workload"
  - "Probationary queue available and configured"
examples:
  - input: "Cache workload with 30% scan requests; item X accessed once, then never again"
    output: "Item X placed in probationary queue, evicted after time window expires; main cache space freed for reusable items"
    notes: "Typical scan-heavy scenario where one-hit wonders degrade hit ratio"
  - input: "Sequential streaming access pattern; 100 items accessed once each"
    output: "All 100 items moved to probationary queue; evicted in FIFO order; main cache preserved for working set"
    notes: "Batch handling of streaming requests"
---

# One-Hit Wonder Eviction Policy

Quickly demote and remove single-access cache items from the main cache queue before they pollute the working set. This micro-skill targets transient or scan-like requests that would otherwise occupy cache space without contributing to future hits. Uses a probationary queue to test item popularity before final eviction.

## Prompt

Identify cache items that have been accessed exactly once. Move them from the main FIFO queue to a probationary queue or mark them for immediate eviction. Ensure the demotion happens before the item can be promoted or aged further in the main cache. Monitor probationary queue occupancy and evict items that do not show repeated access within a defined time window.

## Objective

Remove low-reuse items from cache quickly to improve hit ratio on scan-heavy workloads
## Applicable Signals

- Item access count equals 1
- Workload contains high proportion of non-repeating requests
- Cache hit ratio degradation due to one-time accesses

## Contraindications

- All items in workload expected to have high reuse
- Cache size is very small relative to working set
- Demotion latency is critical to system performance
- Workload is uniform and does not contain scan patterns

## Workflow Steps

- {'step': 1, 'action': 'Monitor cache item access count upon each access'}
- {'step': 2, 'action': 'On first access, place item in probationary queue or mark with one-hit flag'}
- {'step': 3, 'action': 'On second access, promote item to main FIFO queue if it shows reuse'}
- {'step': 4, 'action': 'If item is not accessed again within probationary window, evict it'}
- {'step': 5, 'action': 'Track probationary queue occupancy and adjust demotion aggressiveness if needed'}

## Constraints

- Probationary queue must be pre-allocated and sized appropriately
- Demotion decision must be made before item ages further in main queue
- One-hit items must not be promoted back to main queue on subsequent access without explicit policy

## Cautions

- Overly aggressive demotion may evict items that would have been reused
- Probationary queue size must be tuned; too small causes thrashing, too large wastes space
- Policy assumes miss ratio curve behavior; may not work optimally on non-convex workloads

## Output Contract

- One-hit items successfully removed from main cache queue before polluting working set
- Probationary queue size reduced
- Cache hit ratio improved on scan-heavy traces
- Observable metric: reduction in cache misses caused by transient requests

## Example Executions

### Example 1

- Input: Cache workload with 30% scan requests; item X accessed once, then never again
- Output: Item X placed in probationary queue, evicted after time window expires; main cache space freed for reusable items
- Notes: Typical scan-heavy scenario where one-hit wonders degrade hit ratio

### Example 2

- Input: Sequential streaming access pattern; 100 items accessed once each
- Output: All 100 items moved to probationary queue; evicted in FIFO order; main cache preserved for working set
- Notes: Batch handling of streaming requests

## Triggers

- Cache item receives exactly one access
- Scan, streaming, or sequential access pattern detected in workload
- Probationary queue available and configured

## Examples

### Example 1

Input:

  Cache workload with 30% scan requests; item X accessed once, then never again

Output:

  Item X placed in probationary queue, evicted after time window expires; main cache space freed for reusable items

Notes:

  Typical scan-heavy scenario where one-hit wonders degrade hit ratio

### Example 2

Input:

  Sequential streaming access pattern; 100 items accessed once each

Output:

  All 100 items moved to probationary queue; evicted in FIFO order; main cache preserved for working set

Notes:

  Batch handling of streaming requests
