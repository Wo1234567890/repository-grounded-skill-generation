---
id: "78496037-2dd2-5178-a01a-438dbf1e4770"
name: "Mooncake P2P Checkpoint Distribution"
description: "Micro-skill for distributing large model checkpoints across thousands of GPUs using Mooncake P2P Store and checkpoint-engine. Optimized for rapid model state synchronization during production training with sub-30-second latency for 1T+ parameter models."
version: "0.1.0"
tags:
  - "checkpoint_distribution"
  - "p2p_transfer"
  - "training_synchronization"
  - "large_scale_gpu"
  - "mooncake_engine"
  - "checkpoint-engine"
triggers:
  - "Updating model weights across thousands of GPUs during training"
  - "Distributing checkpoints in production training pipelines"
  - "Synchronizing large model states (1T+ parameters)"
examples:
  - input: "Checkpoint file (1TB) from training node; target list of 1000 GPUs across 128 nodes"
    output: "Checkpoint distributed to all 1000 GPUs in ~20 seconds; all nodes synchronized and ready to resume training"
    notes: "Based on K1.5 and K2 production training application; 1T parameter model update across thousands of GPUs"
---

# Mooncake P2P Checkpoint Distribution

Micro-skill for distributing large model checkpoints across thousands of GPUs using Mooncake P2P Store and checkpoint-engine. Optimized for rapid model state synchronization during production training with sub-30-second latency for 1T+ parameter models.

## Prompt

Use this skill to distribute model checkpoints to large GPU clusters during training. Invoke when you need to synchronize model weights across thousands of GPUs with minimal latency. The skill leverages Mooncake's P2P checkpoint engine (checkpoint-engine) for zero-copy, high-performance distribution. Ensure all target GPUs are registered and reachable before initiating distribution. Monitor completion status across all nodes.

## Objective

Distribute model checkpoints to large GPU clusters with minimal update latency
## Applicable Signals

- Model weight update required during training
- Checkpoint synchronization across multi-GPU cluster
- Production training pipeline checkpoint save event
- Large model state (1T+ parameters) ready for distribution

## Contraindications

- Single-node training environments
- Inference-only deployments without training loop
- Checkpoint sizes under 100GB (overhead not justified)
- Nodes without RDMA or high-speed interconnect capability

## Intervention Moves

- Prepare checkpoint artifact on source node
- Register all target GPU nodes in P2P network
- Initiate checkpoint-engine distribution protocol
- Monitor transfer progress and node acknowledgments
- Verify state synchronization across all targets

## Workflow Steps

- {'step': 1, 'action': 'Prepare checkpoint', 'detail': 'Serialize model state and stage on source node'}
- {'step': 2, 'action': 'Register targets', 'detail': 'Confirm all destination GPUs are reachable and registered in P2P network'}
- {'step': 3, 'action': 'Initiate distribution', 'detail': 'Invoke checkpoint-engine with source checkpoint path and target GPU list'}
- {'step': 4, 'action': 'Monitor transfer', 'detail': 'Track progress and collect acknowledgments from all target nodes'}
- {'step': 5, 'action': 'Verify synchronization', 'detail': 'Confirm all nodes report successful state load and are ready to resume training'}

## Constraints

- All target GPUs must be pre-registered in the P2P network
- Network connectivity and bandwidth must support concurrent multi-node transfer
- Checkpoint must be serialized and ready before distribution initiation
- No concurrent checkpoint distributions on overlapping GPU sets

## Cautions

- Verify checkpoint integrity before distribution to avoid propagating corrupted state
- Monitor network saturation during large-scale distribution
- Ensure sufficient storage on target nodes for checkpoint staging
- Plan distribution windows to avoid interference with active compute

## Output Contract

- Checkpoint successfully distributed to all target GPUs
- Distribution latency under 30 seconds for 1T parameter models
- All nodes report successful state synchronization and are ready to resume training from the new checkpoint

## Example Executions

### Example 1

- Input: Checkpoint file (1TB) from training node; target list of 1000 GPUs across 128 nodes
- Output: Checkpoint distributed to all 1000 GPUs in ~20 seconds; all nodes synchronized and ready to resume training
- Notes: Based on K1.5 and K2 production training application; 1T parameter model update across thousands of GPUs

## Triggers

- Updating model weights across thousands of GPUs during training
- Distributing checkpoints in production training pipelines
- Synchronizing large model states (1T+ parameters)

## Examples

### Example 1

Input:

  Checkpoint file (1TB) from training node; target list of 1000 GPUs across 128 nodes

Output:

  Checkpoint distributed to all 1000 GPUs in ~20 seconds; all nodes synchronized and ready to resume training

Notes:

  Based on K1.5 and K2 production training application; 1T parameter model update across thousands of GPUs
