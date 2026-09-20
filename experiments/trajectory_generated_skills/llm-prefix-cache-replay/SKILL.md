---
name: llm-prefix-cache-s3fifo-replay
description: Replay LLM request traces through a block-level prefix cache using longest-contiguous-prefix hit semantics and S3FIFO resident/ghost bookkeeping.
---

# LLM Prefix Cache Replay with S3FIFO

## When to Use

Use this skill for trace-driven evaluation of block-level KV prefix caches where prompt hashes identify blocks and cache hits are counted only for the reusable prefix present when a request arrives.

## Correct Replay Order

1. Load cache parameters and initialize resident queues, ghost metadata, and per-block frequency state.
2. For each request in trace order, compute hits **before** mutating the cache for that request.
3. Starting from the first prompt block, count the longest contiguous sequence of block hashes that are currently resident. Stop at the first miss even if later blocks are resident.
4. Convert the prefix length to hit tokens with a cap for a partial final block: never report more hit tokens than the request's `input_length`.
5. After recording the request statistics, process the referenced blocks through the cache policy so they become/access resident state for future requests.
6. Keep frequency counters saturating at the configured maximum.

## S3FIFO State Discipline

Treat the policy as three logically distinct structures: a small FIFO region, a main FIFO region, and ghost history. The ghost structure is metadata, not resident KV data, so ghost entries must never count toward prefix hits or final resident-block totals. Respect the configured small-queue ratio, main-queue second-chance behavior, and maximum frequency counter rather than approximating S3FIFO as a single FIFO or LRU queue.

## Reporting

Accumulate total requests, prompt tokens, hit tokens, overall hit rate, and the number of distinct resident blocks after the final request. Also retain one per-request record in original trace order containing request index, prompt tokens, and hit tokens.

## Validation

Build tiny synthetic traces that test: complete prefix hit; first-block miss with later blocks resident; partial final block; repeated access/frequency saturation; eviction from a full cache; and a ghost entry that must not count as resident.

## Trajectory-Derived Caution

The no-skill trajectories produced plausible reports but received zero task reward. The main risk is implementing a superficially similar FIFO policy while missing exact prefix or S3FIFO semantics. Validate the state machine on small hand-computable traces before replaying the full file.
