---
id: "d9ae34fe-6ad4-52cb-9e53-d9e457a22d10"
name: "Custom Sink Integration with Checkpointing"
description: "Registers a custom sink function via `addSink()` that participates in Flink's checkpointing mechanism to guarantee exactly-once delivery semantics to external systems."
version: "0.1.0"
tags:
  - "sink"
  - "checkpointing"
  - "fault_tolerance"
  - "exactly_once"
  - "custom_implementation"
triggers:
  - "Delivering stream to external system (database, message queue, file) where exactly-once semantics are required; custom serialization or business logic is needed."
---

# Custom Sink Integration with Checkpointing

Registers a custom sink function via `addSink()` that participates in Flink's checkpointing mechanism to guarantee exactly-once delivery semantics to external systems.

## Prompt

Use `addSink(sinkFunction)` to register a custom sink that implements checkpoint-aware state management. Ensure the sink function participates in Flink's checkpointing protocol to achieve exactly-once delivery guarantees. Verify that the sink can handle state snapshots and recovery from checkpoints.

## Objective

Ensure reliable, exactly-once delivery of stream data to external systems through custom sink implementation with checkpoint participation
## Applicable Signals

- Stream requires delivery to external system (database, message queue, file system)
- Exactly-once delivery semantics are required
- Custom serialization or business logic is needed for sink behavior

## Contraindications

- At-least-once or best-effort delivery is acceptable
- Using built-in connectors (e.g., Kafka sink) that already handle checkpointing
- Sink does not support checkpoint state participation

## Workflow Steps

- Implement custom sink function with checkpoint participation logic
- Register sink via `dataStream.addSink(customSinkFunction)`
- Enable checkpointing in execution environment
- Verify sink state is captured in checkpoint snapshots
- Test recovery behavior after simulated failure

## Constraints

- Sink function must implement checkpoint-aware interface or callback
- Checkpointing must be enabled in the Flink execution environment
- External system must support idempotent writes or transactional semantics

## Cautions

- Custom sink implementations require careful handling of checkpoint state to avoid data loss or duplication
- Verify that the sink function correctly serializes and deserializes state across checkpoint boundaries

## Output Contract

- Sink function is registered and confirmed to participate in checkpoint state; data is delivered with exactly-once guarantee to the external system.

## Triggers

- Delivering stream to external system (database, message queue, file) where exactly-once semantics are required; custom serialization or business logic is needed.
