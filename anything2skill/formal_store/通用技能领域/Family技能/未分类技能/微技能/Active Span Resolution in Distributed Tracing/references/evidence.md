# Active Span Resolution in Distributed Tracing Evidence

- family: 未分类技能
- skill_id: f7f4d305-3894-5d88-8f74-41d498d0b6e8
- support_count: 1

## Evidence 1

- support_id: 3259b7fc-d130-551f-94a5-cff16de3f3d9
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 43264:44818
- confidence: 0.75
- quote: # Get the current span from OpenTelemetry context
    current_span = get_current_span()

# Check if the current span is valid and recording
    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
        # Check if this is a trace/session span or a child span
        span_name = getattr(current_span, "name", "")

# If it's a session/trace span, use it directly
        if span_name.endswith(f".{SpanKind.SESSION}"):
            span = current_span
        else:
            # It's a child span, try to find the root trace span
            # Get all active traces
            active_traces = tracer.get_active_traces()
            if active_traces:
                # Find the trace that contains the current span
                current_trace_id = current_span.get_span_context().trace_id

# If we couldn't find the parent trace, use the current span
                if not span:
                    span = current_span
            else:
                # No active traces, use the current span
                span = current_span
