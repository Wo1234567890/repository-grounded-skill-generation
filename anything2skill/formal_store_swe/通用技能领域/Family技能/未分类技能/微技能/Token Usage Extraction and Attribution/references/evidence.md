# Token Usage Extraction and Attribution Evidence

- family: 未分类技能
- skill_id: d0c0577d-6e2d-5153-a42c-06b985df0433
- support_count: 1

## Evidence 1

- support_id: a1ebf207-5d45-5276-b614-a55d36dda2da
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 111781:114110
- confidence: 0.82
- quote: Use the span management utilities for consistent span creation:

```python
from agentops.instrumentation.common import create_span, SpanAttributeManager

# Create an attribute manager
attr_manager = SpanAttributeManager(service_name="my-service")

# Use the create_span context manager
with create_span(
    tracer,
    "my.operation",
    attributes={"my.attribute": "value"},
    attribute_manager=attr_manager
) as span:
    # Your operation code here
    pass
```

### Token Counting

Use the token counting utilities for consistent token usage extraction:

```python
from agentops.instrumentation.common import TokenUsageExtractor, set_token_usage_attributes

# Extract token usage from a response
usage = TokenUsageExtractor.extract_from_response(response)

# Set token usage attributes on a span
set_token_usage_attributes(span, response)
```

### Streaming Support

Use streaming utilities for handling streaming responses:

```python
from agentops.instrumentation.common import create_stream_wrapper_factory, StreamingResponseHandler

# Create a stream wrapper factory
wrapper = create_stream_wrapper_factory(
    tracer,
    "my.stream",
    extract_chunk_content=StreamingResponseHandler.extract_generic_chunk_content,
    initial_attributes={"stream.type": "text"}
)

# Apply to streaming methods
wrap_function_wrapper("my_module", "stream_method", wrapper)
```

### Metrics

Use standard metrics for consistency across instrumentations:

```python
from agentops.instrumentation.common import StandardMetrics, MetricsRecorder

# Create standard metrics
metrics = StandardMetrics.create_standard_metrics(meter)

# Use the metrics recorder
recorder = MetricsRecorder(metrics)
recorder.record_token_usage(prompt_tokens=100, completion_tokens=50)
recorder.record_duration(1.5)
```

## Creating a New Instrumentor

1. Create a new directory under `agentops/instrumentation/` for your provider
2. Create an `__init__.py` file with version information
3. Create an `instrumentor.py` file extending `CommonInstrumentor`
4. Create attribute handlers in an `attributes/` subdirectory
5. Add your instrumentor to the main `__init__.py` configuration

Example structure:
```
agentops/instrumentation/
 my_provider/
    __init__.py
    instrumentor.py
    attributes/
        __init__.py
        handlers.py
```

## Best Practices
