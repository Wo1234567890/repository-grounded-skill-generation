---
id: "c7bdb01f-ceb5-5bff-a2dd-d8278711e259"
name: "Adaptive Queue Size Balancing for Staged Cache"
description: "Dynamically adjust the size of an initial FIFO queue in a two-queue cache system by tracking hit rates on evicted objects from each queue via ghost queues and rebalancing when one queue's evicted objects receive significantly more hits than the other."
version: "0.1.0"
tags:
  - "cache_management"
  - "adaptive_algorithm"
  - "queue_sizing"
  - "two_queue_cache"
  - "runtime_tuning"
  - "ghost_queue"
triggers:
  - "Two-queue cache system is active with variable or unknown workload"
  - "Manual queue size configuration is undesirable or impractical"
  - "Ghost queues have accumulated more than 100 hits total"
examples:
  - input: "Cache size 1000 objects; initial S=100 (10%), M=900. After 500 requests, ghost_queue_S has 60 hits, ghost_queue_M has 30 hits. Total hits = 90 (not yet > 100)."
    output: "No rebalancing yet. Continue monitoring."
    notes: "Threshold not met; wait for more hits to accumulate."
  - input: "After 1000 requests, ghost_queue_S has 120 hits, ghost_queue_M has 50 hits. Total = 170 > 100. Ratio: 120/50 = 2.4 (exceeds 2×)."
    output: "Rebalance triggered. Transfer 0.1% of 1000 = 1 object from S to M. New sizes: S=99, M=901. Reset hit counters to 0."
    notes: "S had more hits on evicted objects, so S is shrinking (faster demotion). M is growing."
  - input: "After another 1000 requests, ghost_queue_S has 40 hits, ghost_queue_M has 110 hits. Total = 150 > 100. Ratio: 110/40 = 2.75 (exceeds 2×)."
    output: "Rebalance triggered. Transfer 0.1% of 1000 = 1 object from M to S. New sizes: S=100, M=900. Reset hit counters to 0."
    notes: "M now has more hits on evicted objects, so M is shrinking and S is growing (slower demotion)."
---

# Adaptive Queue Size Balancing for Staged Cache

Dynamically adjust the size of an initial FIFO queue in a two-queue cache system by tracking hit rates on evicted objects from each queue via ghost queues and rebalancing when one queue's evicted objects receive significantly more hits than the other.

## Prompt

Monitor ghost queues tracking evicted objects from the initial queue (S) and main queue (M). When both ghost queues accumulate more than 100 hits and one has 2× more hits than the other, transfer 0.1% of cache space from the queue with fewer hits to the queue with more hits. Repeat this balancing cycle throughout the cache's runtime to maintain equilibrium.

## Objective

maintain optimal queue size split without manual tuning
## Applicable Signals

- Hit count on evicted objects from initial queue (S) exceeds hit count from main queue (M) by 2× or more
- Hit count on evicted objects from main queue (M) exceeds hit count from initial queue (S) by 2× or more
- Cache workload characteristics are changing over time
- Ghost queues have accumulated more than 100 hits total

## Contraindications

- Queue size is fixed by design requirement or SLA
- Workload is static and already manually tuned
- Ghost queue memory overhead is unacceptable in the deployment environment
- Real-time latency constraints prohibit periodic rebalancing checks

## Workflow Steps

- {'step': 1, 'action': 'Initialize two ghost queues, each sized to 5% of the cache size (metadata only)', 'input': 'cache_size, initial_queue_size_S, main_queue_size_M', 'output': 'ghost_queue_S, ghost_queue_M (empty, ready to track evictions)'}
- {'step': 2, 'action': 'On each eviction from queue S, record the object key in ghost_queue_S; on each eviction from queue M, record the object key in ghost_queue_M', 'input': 'evicted_object_key, source_queue', 'output': 'ghost_queue_S and ghost_queue_M updated with new entries'}
- {'step': 3, 'action': 'On each cache hit, check if the hit object exists in ghost_queue_S or ghost_queue_M; if found, increment the corresponding hit counter', 'input': 'hit_object_key', 'output': 'hit_count_S, hit_count_M (cumulative)'}
- {'step': 4, 'action': 'Periodically (e.g., after every N requests or on a timer), check if hit_count_S + hit_count_M > 100 and max(hit_count_S, hit_count_M) >= 2 × min(hit_count_S, hit_count_M)', 'input': 'hit_count_S, hit_count_M', 'output': 'rebalance_needed (boolean)'}
- {'step': 5, 'action': 'If rebalance_needed is true, identify the queue with fewer hits (lower hit count). Transfer 0.1% of cache space from the queue with more hits to the queue with fewer hits.', 'input': 'hit_count_S, hit_count_M, current_size_S, current_size_M', 'output': 'new_size_S, new_size_M (adjusted by ±0.1% of cache_size)'}
- {'step': 6, 'action': 'Reset hit_count_S and hit_count_M to 0; optionally clear or rotate ghost queues to prevent unbounded growth', 'input': 'hit_count_S, hit_count_M', 'output': 'hit_count_S = 0, hit_count_M = 0'}
- {'step': 7, 'action': 'Return to step 3 and continue monitoring', 'input': 'ongoing cache operations', 'output': 'continuous adaptive tuning'}

## Constraints

- Ghost queues must be sized to store 5% of cached objects (metadata only, no data)
- Rebalancing trigger requires both ghost queues to have more than 100 cumulative hits
- Rebalancing trigger requires a 2× hit ratio imbalance between the two ghost queues
- Each rebalancing step transfers exactly 0.1% of cache space
- Rebalancing must not violate minimum or maximum queue size bounds if defined

## Cautions

- Ghost queue overhead is non-zero; verify acceptable in memory-constrained environments
- Rebalancing granularity (0.1% per step) may be slow to converge on highly dynamic workloads
- Hit tracking on ghost queues requires additional instrumentation; ensure clock or request counter is available

## Output Contract

- Queue size ratio is adjusted incrementally; ghost queue hit counts remain balanced such that neither queue's evicted objects receive 2× more hits than the other. The system converges toward a stable queue size split that minimizes miss ratio without manual intervention.

## Example Executions

### Example 1

- Input: Cache size 1000 objects; initial S=100 (10%), M=900. After 500 requests, ghost_queue_S has 60 hits, ghost_queue_M has 30 hits. Total hits = 90 (not yet > 100).
- Output: No rebalancing yet. Continue monitoring.
- Notes: Threshold not met; wait for more hits to accumulate.

### Example 2

- Input: After 1000 requests, ghost_queue_S has 120 hits, ghost_queue_M has 50 hits. Total = 170 > 100. Ratio: 120/50 = 2.4 (exceeds 2×).
- Output: Rebalance triggered. Transfer 0.1% of 1000 = 1 object from S to M. New sizes: S=99, M=901. Reset hit counters to 0.
- Notes: S had more hits on evicted objects, so S is shrinking (faster demotion). M is growing.

### Example 3

- Input: After another 1000 requests, ghost_queue_S has 40 hits, ghost_queue_M has 110 hits. Total = 150 > 100. Ratio: 110/40 = 2.75 (exceeds 2×).
- Output: Rebalance triggered. Transfer 0.1% of 1000 = 1 object from M to S. New sizes: S=100, M=900. Reset hit counters to 0.
- Notes: M now has more hits on evicted objects, so M is shrinking and S is growing (slower demotion).

## Triggers

- Two-queue cache system is active with variable or unknown workload
- Manual queue size configuration is undesirable or impractical
- Ghost queues have accumulated more than 100 hits total

## Examples

### Example 1

Input:

  Cache size 1000 objects; initial S=100 (10%), M=900. After 500 requests, ghost_queue_S has 60 hits, ghost_queue_M has 30 hits. Total hits = 90 (not yet > 100).

Output:

  No rebalancing yet. Continue monitoring.

Notes:

  Threshold not met; wait for more hits to accumulate.

### Example 2

Input:

  After 1000 requests, ghost_queue_S has 120 hits, ghost_queue_M has 50 hits. Total = 170 > 100. Ratio: 120/50 = 2.4 (exceeds 2×).

Output:

  Rebalance triggered. Transfer 0.1% of 1000 = 1 object from S to M. New sizes: S=99, M=901. Reset hit counters to 0.

Notes:

  S had more hits on evicted objects, so S is shrinking (faster demotion). M is growing.

### Example 3

Input:

  After another 1000 requests, ghost_queue_S has 40 hits, ghost_queue_M has 110 hits. Total = 150 > 100. Ratio: 110/40 = 2.75 (exceeds 2×).

Output:

  Rebalance triggered. Transfer 0.1% of 1000 = 1 object from M to S. New sizes: S=100, M=900. Reset hit counters to 0.

Notes:

  M now has more hits on evicted objects, so M is shrinking and S is growing (slower demotion).
