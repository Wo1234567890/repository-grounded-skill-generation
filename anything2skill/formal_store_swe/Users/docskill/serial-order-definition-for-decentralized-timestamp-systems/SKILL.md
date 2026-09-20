---
id: "1225d1be-ed28-5ad7-be41-3e6d5a8038af"
name: "Serial Order Definition for Decentralized Timestamp Systems"
description: "Establishes a total order among transactions using commit timestamp as primary ordering key and physical commit time as tiebreaker when timestamps are equal. Enables proving schedule equivalence in optimistic concurrency control systems where no global timestamp coordination occurs and multiple transactions may receive identical logical timestamps."
version: "0.1.0"
tags:
  - "concurrency_control"
  - "timestamp_ordering"
  - "schedule_equivalence"
  - "formal_verification"
  - "OCC"
  - "serializability"
triggers:
  - "Proving schedule serializability"
  - "Comparing actual concurrent execution against a reference serial schedule"
---

# Serial Order Definition for Decentralized Timestamp Systems

Establishes a total order among transactions using commit timestamp as primary ordering key and physical commit time as tiebreaker when timestamps are equal. Enables proving schedule equivalence in optimistic concurrency control systems where no global timestamp coordination occurs and multiple transactions may receive identical logical timestamps.

## Prompt

To define serial order for schedule correctness verification in decentralized timestamp systems: Transaction A is ordered before transaction B (A <s B) if and only if A has a smaller commit timestamp, or if both have the same commit timestamp but A's physical commit time (time between validation and write phase) is earlier. This creates a total order that enables proving actual concurrent schedules are equivalent to a serializable reference schedule. If A and B have identical logical and physical commit times, arbitrary serial order is acceptable.

## Objective

Define canonical serial order for schedule equivalence proofs in decentralized timestamp systems
## Applicable Signals

- Proving schedule serializability in OCC systems
- Comparing actual concurrent execution against reference serial schedule
- Validating correctness when transactions may commit with identical logical timestamps

## Contraindications

- Global timestamp coordination is available and enforces unique commit timestamps
- Transactions must be ordered by commit timestamp alone without tiebreaker
- System uses strict serialization timestamp assignment

## Constraints

- Commit timestamp is derived from accessed tuples, not globally coordinated
- Multiple transactions may have identical commit timestamps
- Physical time order is defined as time between a transaction's validation phase and write phase

## Cautions

- Physical time measurement must be consistent across validation and write phases
- Transactions with identical logical and physical times do not create conflicts

## Output Contract

- Total order relation <s is defined such that all transactions can be uniquely positioned in serial sequence. For any two transactions A and B: A <s B if and only if (A has smaller commit timestamp) OR (A and B have equal commit timestamp AND A has earlier physical commit time). If A and B have identical logical and physical commit times, arbitrary serial order is acceptable.

## Triggers

- Proving schedule serializability
- Comparing actual concurrent execution against a reference serial schedule
