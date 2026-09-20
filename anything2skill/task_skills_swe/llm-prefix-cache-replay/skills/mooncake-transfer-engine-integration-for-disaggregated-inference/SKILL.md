---
id: "bd5f8745-78e3-58fe-b2d8-e5d9a5e511aa"
name: "Mooncake Transfer Engine Integration for Disaggregated Inference"
description: "Protocol for integrating Mooncake Transfer Engine as a backend connector in distributed inference and KV cache systems. Enables zero-copy RDMA-based data transfer across compute nodes for disaggregated prefill-decode pipelines."
version: "0.1.0"
tags:
  - "disaggregated_inference"
  - "kv_cache_transfer"
  - "rdma"
  - "multi_node"
  - "llm_serving"
triggers:
  - "Integrating disaggregated prefill-decode inference"
  - "Deploying multi-node LLM serving"
  - "Implementing KV cache transfer between compute and cache nodes"
examples:
  - input: "vLLM v1 deployment with prefill-decode disaggregation on 2 H100 nodes"
    output: "MooncakeTransferEngineConnector registered as KV cache backend; prefill node encodes multimodal input, transfers embeddings via RDMA to decode node; decode node generates tokens at 288k tokens/sec throughput"
    notes: "Based on Kimi K2 deployment pattern on 128 H200 GPUs"
  - input: "SGLang with Encode-Prefill-Decode (EPD) disaggregation across 3 nodes"
    output: "Vision Transformer encoder on node 1 produces embeddings; Mooncake Transfer Engine transfers embeddings to prefill node 2; decode node 3 receives KV cache via same backend; zero-copy verified"
    notes: "EPD disaggregation pattern with multimodal encoder decoupling"
---

# Mooncake Transfer Engine Integration for Disaggregated Inference

Protocol for integrating Mooncake Transfer Engine as a backend connector in distributed inference and KV cache systems. Enables zero-copy RDMA-based data transfer across compute nodes for disaggregated prefill-decode pipelines.

## Prompt

To integrate Mooncake Transfer Engine: (1) Identify target inference framework (vLLM, SGLang, TensorRT LLM, or equivalent). (2) Register MooncakeTransferEngineConnector or MooncakeStoreConnector as the KV cache transfer backend. (3) Configure RDMA network paths between prefill and decode nodes. (4) Verify zero-copy transfer by monitoring cross-node data movement without GPU memory staging. (5) Validate throughput and latency against baseline non-disaggregated pipeline.

## Objective

Enable high-performance cross-node data transfer in disaggregated LLM inference
## Applicable Signals

- Deploying multi-node LLM serving with prefill-decode separation
- Implementing KV cache transfer between compute and cache nodes
- Integrating disaggregated inference connectors in vLLM, SGLang, TensorRT LLM, or similar frameworks
- Requiring zero-copy cross-device or cross-machine data movement

## Contraindications

- Single-node inference without disaggregation
- Non-disaggregated pipelines where encoder and decoder run on same node
- Systems without RDMA hardware support or high-speed interconnect
- Environments where GPU memory staging is acceptable and latency is not critical

## Intervention Moves

- Register Mooncake connector (MooncakeTransferEngineConnector or MooncakeStoreConnector) in target framework
- Configure RDMA network paths and device mappings
- Enable hierarchical KV cache storage across device, host, and remote layers
- Validate zero-copy transfer and measure cross-node throughput

## Workflow Steps

- {'step': 1, 'action': 'Identify target inference framework and version', 'detail': 'Confirm framework supports Mooncake integration (vLLM v1+, SGLang with HiCache, TensorRT LLM, vLLM-Omni, vLLM-Ascend, or LMDeploy)'}
- {'step': 2, 'action': 'Register Mooncake connector as KV cache backend', 'detail': "Instantiate MooncakeTransferEngineConnector or MooncakeStoreConnector and bind to framework's cache transfer interface"}
- {'step': 3, 'action': 'Configure RDMA network and node topology', 'detail': 'Set up RDMA paths between prefill nodes, decode nodes, and cache nodes; verify network connectivity'}
- {'step': 4, 'action': 'Enable disaggregated prefill-decode pipeline', 'detail': 'Activate encoder/transformer service decoupling; route multimodal embeddings or KV cache through Mooncake Transfer Engine'}
- {'step': 5, 'action': 'Verify zero-copy transfer and measure performance', 'detail': 'Monitor cross-node data movement; confirm no GPU memory staging; measure throughput (tokens/sec) and latency'}

## Constraints

- RDMA hardware and high-speed interconnect required
- Target framework must have Mooncake connector support or plugin interface
- Disaggregated inference topology must be explicitly configured
- Network latency and bandwidth must be suitable for cross-node KV cache transfer

## Cautions

- Verify RDMA driver and firmware compatibility before deployment
- Monitor network saturation during high-throughput inference; adjust batch sizes if needed
- Ensure encoder and decoder node placement minimizes cross-node hops
- Test failover and recovery paths in production-like environments

## Output Contract

- Mooncake Transfer Engine connector successfully registered and operational in target inference framework; zero-copy transfer verified; cross-node KV cache or embedding transfer achieves expected throughput and latency without GPU memory staging

## Example Executions

### Example 1

- Input: vLLM v1 deployment with prefill-decode disaggregation on 2 H100 nodes
- Output: MooncakeTransferEngineConnector registered as KV cache backend; prefill node encodes multimodal input, transfers embeddings via RDMA to decode node; decode node generates tokens at 288k tokens/sec throughput
- Notes: Based on Kimi K2 deployment pattern on 128 H200 GPUs

### Example 2

- Input: SGLang with Encode-Prefill-Decode (EPD) disaggregation across 3 nodes
- Output: Vision Transformer encoder on node 1 produces embeddings; Mooncake Transfer Engine transfers embeddings to prefill node 2; decode node 3 receives KV cache via same backend; zero-copy verified
- Notes: EPD disaggregation pattern with multimodal encoder decoupling

## Triggers

- Integrating disaggregated prefill-decode inference
- Deploying multi-node LLM serving
- Implementing KV cache transfer between compute and cache nodes

## Examples

### Example 1

Input:

  vLLM v1 deployment with prefill-decode disaggregation on 2 H100 nodes

Output:

  MooncakeTransferEngineConnector registered as KV cache backend; prefill node encodes multimodal input, transfers embeddings via RDMA to decode node; decode node generates tokens at 288k tokens/sec throughput

Notes:

  Based on Kimi K2 deployment pattern on 128 H200 GPUs

### Example 2

Input:

  SGLang with Encode-Prefill-Decode (EPD) disaggregation across 3 nodes

Output:

  Vision Transformer encoder on node 1 produces embeddings; Mooncake Transfer Engine transfers embeddings to prefill node 2; decode node 3 receives KV cache via same backend; zero-copy verified

Notes:

  EPD disaggregation pattern with multimodal encoder decoupling
