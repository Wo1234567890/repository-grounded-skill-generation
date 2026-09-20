---
id: "fc348fe7-a9c1-59c5-9ae6-b130d17058a2"
name: "Collection-Based Test Data Injection"
description: "Atomically extend a tuple's read timestamp (rts) during validation by updating the TS_word encoding, with fallback logic to increase write timestamp (wts) if delta overflows the 15-bit limit. Invoked during validation phase when commit_ts exceeds current rts and serializability constraints permit extension."
version: "0.1.1"
tags:
  - "timestamp_management"
  - "validation_phase"
  - "atomic_operation"
  - "delta_encoding"
  - "overflow_handling"
  - "lock_free"
triggers:
  - "Writing unit tests for Flink transformations"
  - "Validating transformation logic with known inputs"
  - "Replacing external sources temporarily during development"
  - "Testing without access to live data sources"
examples:
  - input: "commit_ts=5, current rts=3, wts=1, delta=2 (fits in 15 bits)"
    output: "TS_word updated: wts=1, delta=4 (rts now 5), lock bit unset"
    notes: "Simple extension without overflow"
  - input: "commit_ts=70000, current rts=60000, wts=1, delta=59999 (exceeds 15-bit limit)"
    output: "wts incremented to 60001, delta recomputed to 9999, TS_word atomically applied"
    notes: "Delta overflow handled by wts increment; dummy write recorded"
---

# Collection-Based Test Data Injection

Atomically extend a tuple's read timestamp (rts) during validation by updating the TS_word encoding, with fallback logic to increase write timestamp (wts) if delta overflows the 15-bit limit. Invoked during validation phase when commit_ts exceeds current rts and serializability constraints permit extension.

## Prompt

During validation, if commit_ts > current rts, attempt to extend rts to commit_ts by atomically updating TS_word. TS_word encodes: lock bit (1 bit), delta = rts − wts (15 bits), wts (48 bits). If delta would overflow 15 bits, increment wts to keep delta within range (dummy write with same data), then atomically apply new TS_word via compare-and-swap. Repeat until TS_word is consistent and lock bit is unset. Validation fails if rts cannot be extended without violating serializability.

## Objective

Extend tuple rts to commit_ts while managing delta encoding overflow via atomic operations
## Applicable Signals

- commit_ts exceeds tuple's current rts
- Validation phase active
- No dependency cycle detected with other committed transactions

## Contraindications

- Tuple's rts cannot be extended without violating serializability; validation must fail instead
- Concurrent writes are actively modifying TS_word (lock bit set)
- Transaction forms a dependency cycle with other committed transactions

## Workflow Steps

- {'step': 1, 'action': 'Load TS_word (v1) before reading tuple data', 'condition': 'Validation phase active'}
- {'step': 2, 'action': 'Read tuple data into local buffer', 'condition': 'v1 loaded successfully'}
- {'step': 3, 'action': 'Load TS_word again (v2) after reading data', 'condition': 'Data read complete'}
- {'step': 4, 'action': 'Check consistency: v1 == v2 and lock bit unset', 'condition': 'Both TS_word loads complete'}
- {'step': 5, 'action': 'If inconsistent, retry from step 1', 'condition': 'v1 != v2 or lock bit set'}
- {'step': 6, 'action': 'Extract wts and delta from v1; compute new rts = wts + delta', 'condition': 'Consistency check passed'}
- {'step': 7, 'action': 'If commit_ts > current rts, compute new delta = commit_ts - wts', 'condition': 'Extension needed'}
- {'step': 8, 'action': 'If new delta > 15-bit limit, increment wts and recompute delta', 'condition': 'Delta overflow detected'}
- {'step': 9, 'action': 'Construct new TS_word with updated wts and delta', 'condition': 'Delta within 15-bit range'}
- {'step': 10, 'action': 'Atomically apply new TS_word via compare-and-swap', 'condition': 'New TS_word constructed'}
- {'step': 11, 'action': 'If compare-and-swap fails, retry from step 1', 'condition': 'TS_word modified by concurrent transaction'}

## Constraints

- TS_word must be read twice (before and after data load) to ensure consistency
- Lock bit must be unset before proceeding
- Delta encoding limited to 15 bits; overflow requires wts increment
- Atomic compare-and-swap must succeed; retry on conflict
- wts overflow (48-bit counter) handled by background reset process

## Cautions

- If compare-and-swap repeatedly fails, consider reverting to heavier-weight latching to avoid starvation
- Incrementing wts on delta overflow may increase abort rate for other transactions observing the version as changed
- 15-bit delta encoding is empirically sufficient; overflow effect is negligible in typical OLTP workloads

## Output Contract

- TS_word atomically updated with new rts and delta encoding. If delta overflow occurred, wts incremented and dummy write recorded without affecting serializability. Validation phase proceeds with extended rts; if extension fails, validation aborts.

## Example Executions

### Example 1

- Input: commit_ts=5, current rts=3, wts=1, delta=2 (fits in 15 bits)
- Output: TS_word updated: wts=1, delta=4 (rts now 5), lock bit unset
- Notes: Simple extension without overflow

### Example 2

- Input: commit_ts=70000, current rts=60000, wts=1, delta=59999 (exceeds 15-bit limit)
- Output: wts incremented to 60001, delta recomputed to 9999, TS_word atomically applied
- Notes: Delta overflow handled by wts increment; dummy write recorded

## Triggers

- Writing unit tests for Flink transformations
- Validating transformation logic with known inputs
- Replacing external sources temporarily during development
- Testing without access to live data sources

## Examples

### Example 1

Input:

  commit_ts=5, current rts=3, wts=1, delta=2 (fits in 15 bits)

Output:

  TS_word updated: wts=1, delta=4 (rts now 5), lock bit unset

Notes:

  Simple extension without overflow

### Example 2

Input:

  commit_ts=70000, current rts=60000, wts=1, delta=59999 (exceeds 15-bit limit)

Output:

  wts incremented to 60001, delta recomputed to 9999, TS_word atomically applied

Notes:

  Delta overflow handled by wts increment; dummy write recorded
