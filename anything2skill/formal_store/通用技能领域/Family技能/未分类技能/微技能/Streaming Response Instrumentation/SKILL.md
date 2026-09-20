---
id: "e97f4cb1-501f-54d3-9e55-96cbd7d70a31"
name: "Streaming Response Instrumentation"
description: "Wrap streaming methods with instrumentation that extracts chunk content and tracks streaming lifecycle. Emits spans for each chunk with extracted content and stream metadata."
version: "0.1.0"
tags:
  - "streaming"
  - "instrumentation"
  - "tracing"
  - "chunk-tracking"
  - "observability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Method returns streaming or generator-based response that must be traced chunk-by-chunk"
---

# Streaming Response Instrumentation

Wrap streaming methods with instrumentation that extracts chunk content and tracks streaming lifecycle. Emits spans for each chunk with extracted content and stream metadata.

## Prompt

Use create_stream_wrapper_factory to wrap streaming methods. Provide a tracer, operation name, chunk content extractor, and initial attributes. Apply the wrapper to streaming methods using wrap_function_wrapper. Each chunk emission will generate a span with extracted content and stream metadata.

## Objective

Instrument streaming responses with chunk-level tracing and content extraction
## Applicable Signals

- Method returns streaming or generator-based response
- Chunk-by-chunk tracing is required
- Response content extraction is needed for observability

## Contraindications

- Response is non-streaming or synchronous
- Streaming instrumentation overhead is not justified for the use case
- Chunk-level tracing is not required

## Intervention Moves

- Import create_stream_wrapper_factory and StreamingResponseHandler from agentops.instrumentation.common
- Create a stream wrapper factory with tracer, operation name, and chunk content extractor
- Apply wrapper to streaming methods using wrap_function_wrapper
- Verify spans are emitted for each chunk with extracted content

## Workflow Steps

- {'step': 1, 'action': 'Import streaming utilities', 'detail': 'from agentops.instrumentation.common import create_stream_wrapper_factory, StreamingResponseHandler'}
- {'step': 2, 'action': 'Create stream wrapper factory', 'detail': "wrapper = create_stream_wrapper_factory(tracer, 'my.stream', extract_chunk_content=StreamingResponseHandler.extract_generic_chunk_content, initial_attributes={'stream.type': 'text'})"}
- {'step': 3, 'action': 'Apply wrapper to streaming method', 'detail': "wrap_function_wrapper('my_module', 'stream_method', wrapper)"}
- {'step': 4, 'action': 'Verify instrumentation', 'detail': 'Confirm spans are emitted for each chunk with extracted content and stream metadata'}

## Constraints

- Tracer must be initialized and available
- Chunk content extractor must be compatible with response format
- wrap_function_wrapper must target the correct module and method name

## Output Contract

- Wrapped function that emits spans for each chunk with extracted content and stream metadata
- Downstream callers receive streaming response with transparent tracing

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Method returns streaming or generator-based response that must be traced chunk-by-chunk
