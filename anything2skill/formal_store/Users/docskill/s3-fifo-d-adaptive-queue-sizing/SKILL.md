---
id: "cc894006-3e71-56b5-ad1a-15eb6bb6553d"
name: "S3-FIFO-d Adaptive Queue Sizing"
description: "Dynamically adjust FIFO queue sizes (S and M) using ghost queues that track evicted objects and balance marginal hits, automatically expanding or contracting queue space to minimize miss ratio gradient."
version: "0.1.0"
tags:
  - "cache_eviction"
  - "adaptive_algorithm"
  - "queue_management"
  - "ghost_queue"
  - "runtime_optimization"
  - "s3fifo"
triggers:
  - "Workload characteristics are unknown or highly variable"
  - "Manual queue size tuning is impractical or unavailable"
  - "Hit/miss patterns change over time"
  - "System requires continuous optimization without human intervention"
examples:
  - input: "Workload with dynamic access patterns; initial S=10% of cache, M=90%; ghost_S hits=120, ghost_M hits=45 over observation window"
    output: "Trigger condition met (120+45>100 and 120≥2×45). Move 0.1% of cache from M to S. New S≈10.1%, M≈89.9%. Reset counters."
    notes: "S receives more hits on evicted objects, indicating S is too small; expansion improves precision."
  - input: "Workload with stable access patterns; S=8%, M=92%; ghost_S hits=60, ghost_M hits=55 over observation window"
    output: "Trigger condition not met (60+55=115>100 but 60<2×55). No adjustment. Continue monitoring."
    notes: "Hit disparity is insufficient; system is near equilibrium."
---

# S3-FIFO-d Adaptive Queue Sizing

Dynamically adjust FIFO queue sizes (S and M) using ghost queues that track evicted objects and balance marginal hits, automatically expanding or contracting queue space to minimize miss ratio gradient.

## Prompt

Maintain two ghost queues, each sized to 5% of cached objects (without data), to track objects evicted from S and M respectively. Monitor cumulative hits on each ghost queue. When both ghost queues accumulate more than 100 hits and one queue has 2× more hits than the other, move 0.1% of cache space from the lower-hit queue to the higher-hit queue. This balancing minimizes the gradient of hits on evicted objects, allowing the system to automatically converge toward optimal queue sizes.

## Objective

automate_cache_queue_adaptation
## Applicable Signals

- Ghost queue hit count exceeds 100
- Disparity between S and M ghost queue hits reaches 2× ratio
- Miss ratio shows instability or degradation over time

## Contraindications

- Memory is extremely constrained and ghost queue overhead (5% per queue) cannot be afforded
- Workload is static and pre-tuned S size is sufficient
- Latency-critical systems cannot tolerate ghost queue lookups
- Cache size is very small (ghost queues may consume prohibitive fraction)

## Workflow Steps

- {'step': 1, 'action': 'Initialize ghost queues', 'detail': 'Create two ghost queues, each sized to store 5% of the cached objects (metadata only, no data)'}
- {'step': 2, 'action': 'Track evictions', 'detail': 'Log object IDs evicted from S to ghost_S and from M to ghost_M'}
- {'step': 3, 'action': 'Monitor ghost queue hits', 'detail': 'Increment hit counter for ghost_S or ghost_M when an evicted object is requested again'}
- {'step': 4, 'action': 'Check adjustment trigger', 'detail': 'Evaluate: (hits_S + hits_M > 100) AND (max(hits_S, hits_M) >= 2 × min(hits_S, hits_M))'}
- {'step': 5, 'action': 'Rebalance queue sizes', 'detail': 'If trigger is true, move 0.1% of cache space from the queue with fewer hits to the queue with more hits'}
- {'step': 6, 'action': 'Reset ghost queue counters', 'detail': 'Reset hit counters to 0 after adjustment; continue monitoring'}

## Constraints

- Ghost queues must be maintained at exactly 5% of cached objects
- Adjustment trigger requires both conditions: hits > 100 AND 2× disparity
- Each adjustment moves exactly 0.1% of cache space
- Ghost queues store metadata only, not object data

## Cautions

- Ghost queue overhead increases memory footprint by ~10% (two 5% queues)
- Adjustment frequency depends on workload hit rate; low-hit workloads may never trigger rebalancing
- Convergence time varies; system may take multiple adjustment cycles to stabilize

## Output Contract

- Ghost queues maintained at 5% of cached objects
- Queue size adjustments executed when trigger conditions are met
- Miss ratio stabilized and gradient minimized over time
- System converges toward workload-optimal S and M sizes without manual intervention

## Example Therapist Responses

### Example 1

- Client/Input: Workload with dynamic access patterns; initial S=10% of cache, M=90%; ghost_S hits=120, ghost_M hits=45 over observation window
- Therapist/Output: Trigger condition met (120+45>100 and 120≥2×45). Move 0.1% of cache from M to S. New S≈10.1%, M≈89.9%. Reset counters.
- Notes: S receives more hits on evicted objects, indicating S is too small; expansion improves precision.

### Example 2

- Client/Input: Workload with stable access patterns; S=8%, M=92%; ghost_S hits=60, ghost_M hits=55 over observation window
- Therapist/Output: Trigger condition not met (60+55=115>100 but 60<2×55). No adjustment. Continue monitoring.
- Notes: Hit disparity is insufficient; system is near equilibrium.

## Triggers

- Workload characteristics are unknown or highly variable
- Manual queue size tuning is impractical or unavailable
- Hit/miss patterns change over time
- System requires continuous optimization without human intervention

## Examples

### Example 1

Input:

  Workload with dynamic access patterns; initial S=10% of cache, M=90%; ghost_S hits=120, ghost_M hits=45 over observation window

Output:

  Trigger condition met (120+45>100 and 120≥2×45). Move 0.1% of cache from M to S. New S≈10.1%, M≈89.9%. Reset counters.

Notes:

  S receives more hits on evicted objects, indicating S is too small; expansion improves precision.

### Example 2

Input:

  Workload with stable access patterns; S=8%, M=92%; ghost_S hits=60, ghost_M hits=55 over observation window

Output:

  Trigger condition not met (60+55=115>100 but 60<2×55). No adjustment. Continue monitoring.

Notes:

  Hit disparity is insufficient; system is near equilibrium.
