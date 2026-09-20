---
id: "90f42a7d-b069-58fd-a0fa-c21c9cc0c3d4"
name: "Parallel URL Fetch with ThreadPoolExecutor"
description: "Fetch multiple URLs concurrently using ThreadPoolExecutor with per-request timeout handling. Load and return response content for each URL, isolating failures per request to enable robust batch HTTP operations."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "ThreadPoolExecutor"
  - "urllib"
  - "parallel_http"
  - "I/O_bound"
  - "timeout_handling"
triggers:
  - "Multiple remote resources (URLs) need to be fetched"
  - "Network latency dominates execution time"
  - "Requests are independent and can be parallelized"
  - "Timeout protection is required per request"
examples:
  - input: "urls=['http://example.com/', 'http://example.org/'], timeout=5"
    output: "{'http://example.com/': b'<html>...', 'http://example.org/': b'<html>...'}"
    notes: "Both requests complete concurrently; total time ≈ max(individual timeouts), not sum"
  - input: "urls=['http://example.com/', 'http://nonexistent.invalid/'], timeout=5"
    output: "{'http://example.com/': b'<html>...', 'http://nonexistent.invalid/': URLError(...)}"
    notes: "Failed URL captured with exception; successful URL still returned"
---

# Parallel URL Fetch with ThreadPoolExecutor

Fetch multiple URLs concurrently using ThreadPoolExecutor with per-request timeout handling. Load and return response content for each URL, isolating failures per request to enable robust batch HTTP operations.

## Prompt

Use ThreadPoolExecutor to submit concurrent HTTP fetch tasks. Each task calls load_url(url, timeout) which opens the URL with urllib.request.urlopen and returns the response body. Collect results and exceptions per URL using as_completed() or map(). Return a dictionary mapping each URL to its response content (bytes) on success or exception details on failure.

## Objective

Execute concurrent HTTP requests with per-request timeout and error isolation
## Applicable Signals

- Caller has a list of URLs to fetch
- Caller expects concurrent execution to reduce total wall-clock time
- Caller needs per-URL error handling

## Contraindications

- Single URL fetch (no parallelism benefit)
- CPU-bound processing of responses (use ProcessPoolExecutor instead)
- Requests requiring strict ordering or shared session state
- Interactive interpreter context (use ThreadPoolExecutor, not ProcessPoolExecutor)

## Workflow Steps

- {'step': 1, 'action': 'Initialize ThreadPoolExecutor with appropriate max_workers', 'detail': 'Use default max_workers=min(32, os.cpu_count() + 4) as of Python 3.8+. Executor will reuse idle threads before creating new ones up to max_workers limit.'}
- {'step': 2, 'action': 'Define load_url(url, timeout) function', 'detail': 'Use urllib.request.urlopen(url, timeout=timeout) within a context manager; return conn.read() to get response body as bytes.'}
- {'step': 3, 'action': 'Submit each URL as a separate task to executor.submit(load_url, url, timeout)', 'detail': 'Returns a Future object for each submission; do not block on submission. All tasks are queued immediately.'}
- {'step': 4, 'action': 'Collect futures and retrieve results using as_completed() or map()', 'detail': 'Handle exceptions per future; map each URL to its result or exception object.'}
- {'step': 5, 'action': 'Return aggregated results as dictionary or list', 'detail': 'Ensure caller can distinguish success from failure per URL. All URLs processed; no partial results lost due to single failure.'}

## Constraints

- ThreadPoolExecutor default max_workers is min(32, os.cpu_count() + 4) as of Python 3.8+
- Each request must have an independent timeout value
- urllib.request.urlopen must be called within the worker task
- Idle worker threads are reused before spawning new ones

## Cautions

- Network timeouts may raise urllib.error.URLError; caller must handle or propagate
- Large response bodies consume memory; consider streaming for very large payloads
- DNS resolution is blocking; consider connection pooling for many requests to same host

## Output Contract

- Dictionary or list mapping each URL to its response content (bytes) on success, or to exception details on failure. All URLs processed; no partial results lost due to single failure.

## Example Executions

### Example 1

- Input: urls=['http://example.com/', 'http://example.org/'], timeout=5
- Output: {'http://example.com/': b'<html>...', 'http://example.org/': b'<html>...'}
- Notes: Both requests complete concurrently; total time ≈ max(individual timeouts), not sum

### Example 2

- Input: urls=['http://example.com/', 'http://nonexistent.invalid/'], timeout=5
- Output: {'http://example.com/': b'<html>...', 'http://nonexistent.invalid/': URLError(...)}
- Notes: Failed URL captured with exception; successful URL still returned

## Triggers

- Multiple remote resources (URLs) need to be fetched
- Network latency dominates execution time
- Requests are independent and can be parallelized
- Timeout protection is required per request

## Examples

### Example 1

Input:

  urls=['http://example.com/', 'http://example.org/'], timeout=5

Output:

  {'http://example.com/': b'<html>...', 'http://example.org/': b'<html>...'}

Notes:

  Both requests complete concurrently; total time ≈ max(individual timeouts), not sum

### Example 2

Input:

  urls=['http://example.com/', 'http://nonexistent.invalid/'], timeout=5

Output:

  {'http://example.com/': b'<html>...', 'http://nonexistent.invalid/': URLError(...)}

Notes:

  Failed URL captured with exception; successful URL still returned
