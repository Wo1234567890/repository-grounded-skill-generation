---
id: "fe993e71-1d14-566c-a5f1-fe1e6a039fd1"
name: "Disaggregated Prefill-Decode Deployment Pattern"
description: "Macro protocol for decoupling compute-intensive encoder/prefill stages from decode stages across multiple nodes using a transfer engine as the data backbone. Enables encoder service isolation, multimodal embedding caching, and cross-instance cache sharing to maximize throughput and resource utilization in large-scale distributed inference."
version: "0.1.0"
tags:
  - "distributed_inference"
  - "disaggregation"
  - "prefill_decode"
  - "multimodal"
  - "kv_cache"
  - "transfer_engine"
triggers:
  - "Deploying large-scale LLM inference with high prefill throughput requirements"
  - "Multimodal models with expensive encoder stages (e.g., Vision Transformers)"
  - "Heterogeneous hardware clusters with specialized prefill and decode nodes"
  - "Need to share embeddings or KV cache across multiple inference instances"
examples:
  - input: "Multimodal LLM inference on 128 H100 GPUs with Vision Transformer encoder and language model decoder; 10k concurrent requests with shared image inputs"
    output: "Prefill nodes (32 GPUs) handle encoder and prefill; decode nodes (96 GPUs) handle token generation; embeddings cached in transfer engine; 224k tokens/sec prefill throughput, 288k tokens/sec decode throughput achieved"
    notes: "Large-scale deployment with expert parallelism; disaggregation enables efficient resource allocation"
  - input: "SGLang Encode-Prefill-Decode (EPD) disaggregation setup with multimodal encoders decoupled from language model nodes"
    output: "Encoder outputs transferred via RDMA to decode nodes; zero-copy embedding transfer; reduced GPU memory pressure on decode nodes"
    notes: "Typical multimodal serving scenario; transfer engine handles large embedding tensors efficiently"
---

# Disaggregated Prefill-Decode Deployment Pattern

Macro protocol for decoupling compute-intensive encoder/prefill stages from decode stages across multiple nodes using a transfer engine as the data backbone. Enables encoder service isolation, multimodal embedding caching, and cross-instance cache sharing to maximize throughput and resource utilization in large-scale distributed inference.

## Prompt

Deploy a disaggregated prefill-decode pipeline by: (1) isolating encoder and prefill compute on dedicated nodes; (2) routing multimodal embeddings through a transfer engine with zero-copy RDMA support; (3) establishing a hierarchical KV cache layer shared across prefill and decode instances; (4) validating end-to-end throughput and latency against baseline single-node inference. Use this pattern when prefill and decode have asymmetric compute requirements or when encoder stages are bottlenecks.

## Objective

Maximize throughput and resource utilization by separating prefill and decode compute across specialized nodes
## Applicable Signals

- Prefill latency dominates end-to-end inference time
- Encoder compute is a bottleneck in multimodal pipelines
- Multiple inference requests can share cached embeddings
- Network bandwidth supports high-throughput embedding transfer

## Contraindications

- Latency-critical single-request inference where disaggregation overhead exceeds benefit
- Homogeneous single-node setups without multi-node infrastructure
- Systems with insufficient network bandwidth for embedding transfer
- Workloads where prefill and decode compute are balanced and co-location is optimal

## Workflow Steps

- {'step': 1, 'action': 'Partition inference pipeline into encoder/prefill and decode stages', 'detail': 'Identify compute-intensive encoder or prefill operations; allocate dedicated nodes for each stage'}
- {'step': 2, 'action': 'Configure transfer engine as data backbone', 'detail': 'Set up RDMA or high-performance network transport; enable zero-copy embedding transfer between prefill and decode nodes'}
- {'step': 3, 'action': 'Establish hierarchical KV cache storage', 'detail': 'Implement multi-tier cache (device, host, remote storage) with prefill node as primary cache writer and decode nodes as readers'}
- {'step': 4, 'action': 'Enable cross-instance embedding sharing', 'detail': 'Configure cache manager to detect duplicate encoder inputs and reuse cached embeddings across concurrent requests'}
- {'step': 5, 'action': 'Validate end-to-end metrics', 'detail': 'Measure prefill throughput, decode latency, embedding cache hit rate, and network utilization; compare against baseline'}

## Constraints

- Transfer engine must support zero-copy RDMA or equivalent high-performance data movement
- Prefill and decode nodes must have synchronized clock and compatible tensor formats
- KV cache coherency must be maintained across distributed instances
- Network latency between prefill and decode nodes must be acceptable for embedding transfer

## Cautions

- Disaggregation introduces network round-trip latency; validate that throughput gains outweigh latency overhead
- Embedding cache invalidation and consistency require careful coordination
- Scaling to many decode instances may saturate prefill node bandwidth

## Output Contract

- Disaggregated pipeline operational with encoder/prefill and decode stages running on separate nodes; multimodal embeddings cached and shared across instances; end-to-end throughput and latency metrics validated and documented; cache coherency verified under concurrent load.

## Example Executions

### Example 1

- Input: Multimodal LLM inference on 128 H100 GPUs with Vision Transformer encoder and language model decoder; 10k concurrent requests with shared image inputs
- Output: Prefill nodes (32 GPUs) handle encoder and prefill; decode nodes (96 GPUs) handle token generation; embeddings cached in transfer engine; 224k tokens/sec prefill throughput, 288k tokens/sec decode throughput achieved
- Notes: Large-scale deployment with expert parallelism; disaggregation enables efficient resource allocation

### Example 2

- Input: SGLang Encode-Prefill-Decode (EPD) disaggregation setup with multimodal encoders decoupled from language model nodes
- Output: Encoder outputs transferred via RDMA to decode nodes; zero-copy embedding transfer; reduced GPU memory pressure on decode nodes
- Notes: Typical multimodal serving scenario; transfer engine handles large embedding tensors efficiently

## Triggers

- Deploying large-scale LLM inference with high prefill throughput requirements
- Multimodal models with expensive encoder stages (e.g., Vision Transformers)
- Heterogeneous hardware clusters with specialized prefill and decode nodes
- Need to share embeddings or KV cache across multiple inference instances

## Examples

### Example 1

Input:

  Multimodal LLM inference on 128 H100 GPUs with Vision Transformer encoder and language model decoder; 10k concurrent requests with shared image inputs

Output:

  Prefill nodes (32 GPUs) handle encoder and prefill; decode nodes (96 GPUs) handle token generation; embeddings cached in transfer engine; 224k tokens/sec prefill throughput, 288k tokens/sec decode throughput achieved

Notes:

  Large-scale deployment with expert parallelism; disaggregation enables efficient resource allocation

### Example 2

Input:

  SGLang Encode-Prefill-Decode (EPD) disaggregation setup with multimodal encoders decoupled from language model nodes

Output:

  Encoder outputs transferred via RDMA to decode nodes; zero-copy embedding transfer; reduced GPU memory pressure on decode nodes

Notes:

  Typical multimodal serving scenario; transfer engine handles large embedding tensors efficiently
