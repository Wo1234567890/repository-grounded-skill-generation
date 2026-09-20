---
name: parallel-tfidf-search
description: Parallelize CPU-bound TF-IDF indexing and batch search with multiprocessing while preserving the sequential index/results exactly and controlling process overhead.
---

# Parallel TF-IDF Search

## When to Use

Use this skill when a correct sequential TF-IDF engine must exploit multiple CPU cores without changing its index structure, ranking semantics, or public API.

## Workflow

1. **Read the sequential implementation first.** Treat its tokenization, term frequency, document frequency, IDF formula, vector normalization, scoring, tie behavior, and result structure as the correctness oracle.
2. **Partition only independent CPU-heavy stages.** Good candidates include per-document tokenization/TF work and per-term or per-document TF-IDF computation. Keep cheap global reductions such as DF/IDF combination sequential when parallel overhead would dominate.
3. **Use process-safe worker functions.** Multiprocessing workers must be module-level/picklable. Avoid nested closures. For large read-only shared state, initialize worker globals once with a pool initializer instead of serializing the same index for every task.
4. **Chunk work coarsely enough to amortize IPC.** Respect the caller's chunk-size/worker controls and avoid creating one process task per tiny document or query.
5. **Preserve deterministic merge semantics.** Merge partial indexes/counts in a way that reproduces the exact sequential `TFIDFIndex` structure.
6. **Batch search across queries, not across tiny inner score operations.** Reuse one pool for the batch. For very small query batches, a sequential fallback can be faster because process startup/IPC dominates.
7. **Return the exact required shape.** Batch search should return one ordered result list per input query plus elapsed time; do not flatten the nested results.
8. **Benchmark correctness before speed.** Compare index fields and ranked search outputs against the sequential engine, then measure speedup under the benchmark's worker count and workload.

## Proven Pattern from the Successful Trajectory

The successful run fixed two important multiprocessing mistakes: nested worker functions that could not be pickled, and excessive overhead for small units of work. It then used module-level workers, pool initialization, adaptive batching, and exact result-shape checks before measuring performance.

## Common Failure Modes

- Rebuilding a process pool for every query.
- Benchmarking on a workload so small that overhead dominates.
- Changing TF-IDF math while trying to parallelize it.
- Returning one result object per query instead of a list of top-k results per query.
- Reporting speedup without first proving equality with the sequential implementation.
