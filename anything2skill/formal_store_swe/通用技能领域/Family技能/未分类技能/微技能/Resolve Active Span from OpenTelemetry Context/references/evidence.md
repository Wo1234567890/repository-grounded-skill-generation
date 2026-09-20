# Resolve Active Span from OpenTelemetry Context Evidence

- family: 未分类技能
- skill_id: 52956153-19be-543e-882e-ea4d44eb1b9c
- support_count: 1

## Evidence 1

- support_id: eade89ce-ede9-57e2-aabe-6dbb4ba49574
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
