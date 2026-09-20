---
id: "cf65d840-f5f8-50ea-bea0-ae2bbb90ab28"
name: "Submit Callable to Thread/Process Pool"
description: "Initialize a DataStream from an Iterator or collection source, respecting serialization requirements and single-parallelism execution model. Used for bootstrapping streaming jobs from test data or small reference datasets."
version: "0.1.1"
tags:
  - "data_source"
  - "collection"
  - "initialization"
  - "serialization"
  - "testing"
  - "micro_skill"
triggers:
  - "Need to run a single function asynchronously without blocking the caller"
  - "ThreadPoolExecutor or ProcessPoolExecutor instance is available and active"
examples:
  - input: "Iterator[Long] containing numeric values"
    output: "DataStream[Long] with parallelism = 1"
    notes: "val longIt: Iterator[Long] = ...; val myLongs = env.fromCollection(longIt)"
---

# Submit Callable to Thread/Process Pool

Initialize a DataStream from an Iterator or collection source, respecting serialization requirements and single-parallelism execution model. Used for bootstrapping streaming jobs from test data or small reference datasets.

## Prompt

Call env.fromCollection(iterator) to create a DataStream from an in-memory collection. Ensure all data types and iterators implement Serializable. Note that collection data sources execute with parallelism = 1 and cannot be parallelized.

## Objective

instantiate DataStream from in-memory collection
## Applicable Signals

- development or testing phase
- data available in memory as Iterator or collection
- all elements are Serializable

## Contraindications

- large datasets
- parallel execution required
- non-serializable objects in collection
- production data ingestion from external sources

## Workflow Steps

- Verify all data types and iterators in the collection implement Serializable
- Call env.fromCollection(iterator) or env.fromCollection(collection)
- Receive DataStream object
- Proceed to transformation or sink operations

## Constraints

- All data types must implement Serializable
- All iterators must implement Serializable
- Execution parallelism is fixed at 1; cannot be increased

## Cautions

- Collection data sources cannot be executed in parallel
- Serialization failures will occur at runtime if objects are not Serializable

## Output Contract

- DataStream object ready for downstream transformation or sink operations; parallelism is 1

## Example Executions

### Example 1

- Input: Iterator[Long] containing numeric values
- Output: DataStream[Long] with parallelism = 1
- Notes: val longIt: Iterator[Long] = ...; val myLongs = env.fromCollection(longIt)

## Triggers

- Need to run a single function asynchronously without blocking the caller
- ThreadPoolExecutor or ProcessPoolExecutor instance is available and active

## Examples

### Example 1

Input:

  Iterator[Long] containing numeric values

Output:

  DataStream[Long] with parallelism = 1

Notes:

  val longIt: Iterator[Long] = ...; val myLongs = env.fromCollection(longIt)
