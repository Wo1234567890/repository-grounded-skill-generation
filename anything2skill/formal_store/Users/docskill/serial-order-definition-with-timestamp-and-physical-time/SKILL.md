---
id: "a5061a43-509a-5b3e-99a1-eb1ad74f8732"
name: "Serial Order Definition with Timestamp and Physical Time"
description: "Establishes a total order among transactions using commit timestamp as primary criterion and physical commit time as tiebreaker, enabling correctness proofs for optimistic concurrency control schedules. Resolves transaction ordering when commit timestamps are identical by comparing wall-clock times between validation and write phases."
version: "0.1.0"
tags:
  - "serializability"
  - "timestamp_ordering"
  - "optimistic_concurrency_control"
  - "correctness_proof"
  - "total_order"
triggers:
  - "Proving schedule equivalence in optimistic concurrency control"
  - "Resolving transaction ordering when commit timestamps are equal"
  - "Establishing dependencies for serializability proof"
examples:
  - input: "Two transactions A and B with commit_ts(A) = 100, commit_ts(B) = 100, physical_time(A) = 1000ms, physical_time(B) = 1050ms"
    output: "A <s B (A ordered before B because they have equal commit timestamps but A has earlier physical commit time)"
    notes: "Demonstrates tiebreaker rule when timestamps are equal"
  - input: "Transaction C with commit_ts(C) = 95, Transaction D with commit_ts(D) = 100"
    output: "C <s D (C ordered before D because commit_ts(C) < commit_ts(D), regardless of physical times)"
    notes: "Demonstrates primary ordering criterion"
---

# Serial Order Definition with Timestamp and Physical Time

Establishes a total order among transactions using commit timestamp as primary criterion and physical commit time as tiebreaker, enabling correctness proofs for optimistic concurrency control schedules. Resolves transaction ordering when commit timestamps are identical by comparing wall-clock times between validation and write phases.

## Prompt

To establish serial order among transactions in an optimistic concurrency control system:
1. Use commit timestamp as the primary ordering criterion.
2. When two transactions have equal commit timestamps, use physical commit time (the actual wall-clock time between validation and write phases) as the tiebreaker.
3. Define the serial order relation A <s B as: A <ts B ∨ (A =ts B ∧ A ≤pt B), where <ts is commit timestamp order and ≤pt is physical commit time order.
4. This definition creates a total order among all transactions, allowing any schedule to be mapped to an equivalent serial schedule.
5. Use this order to prove that read operations always return the value of the last store in the equivalent serial schedule.

## Objective

define_serializability_order
## Applicable Signals

- Multiple transactions with identical commit timestamps
- Need to establish total order for correctness proof
- Requirement to map actual schedule to serial schedule

## Contraindications

- Transactions have distinct commit timestamps only (no tie resolution needed)
- Physical time ordering is unavailable or not tracked
- Proof does not require total order among all transactions

## Constraints

- Commit timestamps must be derived from accessed tuples without global coordination
- Physical commit time must be measurable between validation and write phases
- The relation must form a total order (transitive, antisymmetric, total)

## Cautions

- Transactions with identical logical and physical commit times may have arbitrary serial order; this does not affect correctness
- The definition assumes no global timestamp coordination; local timestamp derivation is sufficient

## Output Contract

- A formal definition of serial order (A <s B) that establishes a total order among all transactions; enables proof that any actual schedule is equivalent to a serial schedule respecting this order; provides foundation for proving that read operations return correct values.

## Example Therapist Responses

### Example 1

- Client/Input: Two transactions A and B with commit_ts(A) = 100, commit_ts(B) = 100, physical_time(A) = 1000ms, physical_time(B) = 1050ms
- Therapist/Output: A <s B (A ordered before B because they have equal commit timestamps but A has earlier physical commit time)
- Notes: Demonstrates tiebreaker rule when timestamps are equal

### Example 2

- Client/Input: Transaction C with commit_ts(C) = 95, Transaction D with commit_ts(D) = 100
- Therapist/Output: C <s D (C ordered before D because commit_ts(C) < commit_ts(D), regardless of physical times)
- Notes: Demonstrates primary ordering criterion

## Triggers

- Proving schedule equivalence in optimistic concurrency control
- Resolving transaction ordering when commit timestamps are equal
- Establishing dependencies for serializability proof

## Examples

### Example 1

Input:

  Two transactions A and B with commit_ts(A) = 100, commit_ts(B) = 100, physical_time(A) = 1000ms, physical_time(B) = 1050ms

Output:

  A <s B (A ordered before B because they have equal commit timestamps but A has earlier physical commit time)

Notes:

  Demonstrates tiebreaker rule when timestamps are equal

### Example 2

Input:

  Transaction C with commit_ts(C) = 95, Transaction D with commit_ts(D) = 100

Output:

  C <s D (C ordered before D because commit_ts(C) < commit_ts(D), regardless of physical times)

Notes:

  Demonstrates primary ordering criterion
