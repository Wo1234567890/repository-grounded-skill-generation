---
id: "cc343101-3e7f-581c-8368-f0ac6ecafdbe"
name: "Collection Data Source Setup"
description: "Initialize a DataStream from an in-memory collection or iterator for testing and local development. Use when you need to inject test data into a Flink pipeline without external connectors."
version: "0.1.0"
tags:
  - "data_source"
  - "testing"
  - "local_development"
  - "collection"
  - "iterator"
  - "setup"
triggers:
  - "Testing Flink programs locally"
  - "Debugging transformations with controlled input"
  - "Prototyping pipelines without external data sources"
---

# Collection Data Source Setup

Initialize a DataStream from an in-memory collection or iterator for testing and local development. Use when you need to inject test data into a Flink pipeline without external connectors.

## Prompt

Call env.fromCollection(collection) or env.fromCollection(iterator) to initialize a DataStream from local data. Ensure all data types and iterators implement Serializable. Be aware that collection data sources execute with parallelism=1 and cannot be parallelized.

## Objective

Initialize a DataStream from a local collection or iterator
## Applicable Signals

- Development or test environment active
- Small dataset available in memory
- Need for deterministic, repeatable test data

## Contraindications

- Production pipelines requiring parallel execution
- Large datasets exceeding available memory
- Real-time streaming from external systems
- Data types that do not implement Serializable

## Workflow Steps

- Prepare in-memory collection or iterator with Serializable data types
- Obtain execution environment (env)
- Call env.fromCollection(collection) or env.fromCollection(iterator)
- Receive DataStream object ready for downstream transformations

## Constraints

- Parallelism is fixed at 1; cannot be increased
- All data types and iterators must implement Serializable
- Data must fit entirely in memory

## Cautions

- Collection data sources are not suitable for performance testing or production workloads
- Memory constraints may limit dataset size during testing

## Output Contract

- A DataStream object initialized from the collection, ready for downstream transformations and operators

## Triggers

- Testing Flink programs locally
- Debugging transformations with controlled input
- Prototyping pipelines without external data sources
