---
id: "3ba1bc87-4c5c-59d5-afd4-1ff2496e3881"
name: "Deploy Mooncake Store Hierarchical KV Cache Backend"
description: "Use Accelerate library to simplify distributed training launch and management across multiple GPUs and nodes, handling data parallelism, gradient accumulation, and distributed data loading automatically."
version: "0.1.1"
tags:
  - "distributed_training"
  - "multi_node"
  - "accelerate"
  - "orchestration"
  - "data_parallelism"
  - "gradient_accumulation"
triggers:
  - "Deploying vLLM, SGLang, or xLLM with multi-tier KV cache requirements"
  - "Scaling inference across multiple nodes with memory constraints"
  - "Need to reduce GPU memory footprint while maintaining cache locality"
examples:
  - input: "vLLM deployment on 8 H100 GPUs with 80GB memory each; total KV cache demand 2TB across 128 concurrent requests"
    output: "Mooncake Store configured with device tier (80GB per GPU), host tier (500GB per node), remote tier (1TB shared storage). Prefetch logic moves frequently accessed cache to device, cold cache to remote. Achieves 95% cache hit rate on device tier."
    notes: "Based on Sept 18, 2025 vLLM Ascend KV pool backend integration"
  - input: "SGLang with multimodal encoders (ViT) generating large embeddings; cross-instance cache sharing required"
    output: "Mooncake Store enables hierarchical KV caching with RadixAttention multi-tier support. ViT embeddings cached in host/remote tiers, reused across instances. Reduces redundant GPU computation."
    notes: "Based on Sept 10, 2025 SGLang HiCache integration"
---

# Deploy Mooncake Store Hierarchical KV Cache Backend

Use Accelerate library to simplify distributed training launch and management across multiple GPUs and nodes, handling data parallelism, gradient accumulation, and distributed data loading automatically.

## Prompt

Invoke this skill when you need to launch training across multiple nodes or GPUs. Accelerate provides a unified API to manage distributed training complexities: data parallelism, gradient accumulation, and distributed data loading. Configure Accelerate with your hardware setup, then use its launcher to start training. The skill handles coordination across devices automatically.

## Objective

Simplify and standardize multi-node training orchestration
## Applicable Signals

- Model size exceeds single-GPU memory
- Multiple nodes available in cluster
- Data parallelism strategy selected
- Training script ready for distributed execution

## Contraindications

- Single-GPU training environment
- Custom low-level distributed control required
- Non-standard parallelism patterns needed
- Direct NCCL or torch.distributed API required

## Workflow Steps

- {'step': 1, 'action': 'Install and configure Accelerate', 'detail': 'Install Accelerate library; run accelerate config to detect and configure hardware setup (GPUs, nodes, parallelization strategy)'}
- {'step': 2, 'action': 'Prepare training script', 'detail': 'Ensure training script is compatible with Accelerate; wrap model and data loading with Accelerate API calls'}
- {'step': 3, 'action': 'Launch distributed training', 'detail': 'Use accelerate launch command to start training across all configured nodes; Accelerate handles device assignment and synchronization'}
- {'step': 4, 'action': 'Monitor training execution', 'detail': 'Verify data parallelism and gradient accumulation are active; check logs for synchronization issues across nodes'}

## Constraints

- Accelerate must be installed and compatible with training framework
- Hardware configuration must be accessible to Accelerate
- Training script must be compatible with Accelerate launcher
- Network connectivity between nodes must be stable

## Cautions

- Ensure all nodes have identical Python and dependency versions
- Verify network bandwidth sufficient for gradient synchronization
- Test configuration on subset of nodes before full-scale training

## Output Contract

- Accelerate configuration created and validated
- Distributed training launched successfully across all nodes
- Data parallelism and gradient accumulation active
- Training loop executing with automatic device coordination

## Triggers

- Deploying vLLM, SGLang, or xLLM with multi-tier KV cache requirements
- Scaling inference across multiple nodes with memory constraints
- Need to reduce GPU memory footprint while maintaining cache locality

## Examples

### Example 1

Input:

  vLLM deployment on 8 H100 GPUs with 80GB memory each; total KV cache demand 2TB across 128 concurrent requests

Output:

  Mooncake Store configured with device tier (80GB per GPU), host tier (500GB per node), remote tier (1TB shared storage). Prefetch logic moves frequently accessed cache to device, cold cache to remote. Achieves 95% cache hit rate on device tier.

Notes:

  Based on Sept 18, 2025 vLLM Ascend KV pool backend integration

### Example 2

Input:

  SGLang with multimodal encoders (ViT) generating large embeddings; cross-instance cache sharing required

Output:

  Mooncake Store enables hierarchical KV caching with RadixAttention multi-tier support. ViT embeddings cached in host/remote tiers, reused across instances. Reduces redundant GPU computation.

Notes:

  Based on Sept 10, 2025 SGLang HiCache integration
