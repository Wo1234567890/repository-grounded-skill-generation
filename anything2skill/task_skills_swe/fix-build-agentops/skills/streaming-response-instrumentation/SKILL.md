---
id: "349bba6e-84a4-5c14-9203-5a926dfbe7a0"
name: "Streaming Response Instrumentation"
description: "Wrap streaming methods to capture and trace chunk-by-chunk responses with consistent content extraction. Use when instrumenting APIs that return streaming or chunked responses."
version: "0.1.0"
tags:
  - "instrumentation"
  - "streaming"
  - "tracing"
  - "chunk-handling"
  - "span-management"
triggers:
  - "Method returns a streaming or iterable response"
  - "Per-chunk tracing and content extraction is required"
  - "Using wrap_function_wrapper pattern for instrumentation"
examples:
  - input: "Streaming method in module 'my_module' named 'stream_method' that yields text chunks"
    output: "Wrapped method that creates child spans for each chunk with stream.type='text' and chunk content attributes"
    notes: "Uses StreamingResponseHandler.extract_generic_chunk_content for content extraction"
---

# Streaming Response Instrumentation

Wrap streaming methods to capture and trace chunk-by-chunk responses with consistent content extraction. Use when instrumenting APIs that return streaming or chunked responses.

## Prompt

Apply streaming utilities to instrument a method that returns streaming or iterable responses. Use create_stream_wrapper_factory to create a wrapper that extracts chunk content and records attributes on each chunk. Apply the wrapper to the target streaming method using wrap_function_wrapper. Ensure stream.type and chunk content attributes are recorded for each chunk event.

## Objective

Instrument a streaming method to extract and trace individual chunks
## Applicable Signals

- streaming_response_detected
- iterable_response_type
- chunk_based_output

## Contraindications

- Response is non-streaming or fully buffered
- Chunk content extraction is custom and incompatible with StreamingResponseHandler
- Streaming is handled by client library without need for additional instrumentation

## Workflow Steps

- Import create_stream_wrapper_factory and StreamingResponseHandler from agentops.instrumentation.common
- Create a stream wrapper factory with tracer, operation name, chunk content extractor, and initial attributes
- Apply the wrapper to the target streaming method using wrap_function_wrapper with module name and method name
- Verify that stream.type and chunk content attributes are recorded for each chunk event

## Constraints

- StreamingResponseHandler.extract_generic_chunk_content must be compatible with response format
- Tracer must be available and initialized
- Target module and method name must be correctly specified for wrap_function_wrapper

## Cautions

- Ensure the chunk content extractor is compatible with the response format
- Verify tracer is properly initialized before wrapping
- Test with actual streaming responses to confirm chunk extraction works as expected

## Output Contract

- Wrapped streaming method that emits span events or child spans for each chunk; stream.type and chunk content attributes recorded on each chunk

## Example Executions

### Example 1

- Input: Streaming method in module 'my_module' named 'stream_method' that yields text chunks
- Output: Wrapped method that creates child spans for each chunk with stream.type='text' and chunk content attributes
- Notes: Uses StreamingResponseHandler.extract_generic_chunk_content for content extraction

## Triggers

- Method returns a streaming or iterable response
- Per-chunk tracing and content extraction is required
- Using wrap_function_wrapper pattern for instrumentation

## Examples

### Example 1

Input:

  Streaming method in module 'my_module' named 'stream_method' that yields text chunks

Output:

  Wrapped method that creates child spans for each chunk with stream.type='text' and chunk content attributes

Notes:

  Uses StreamingResponseHandler.extract_generic_chunk_content for content extraction
