# Trace Lifecycle Management Evidence

- family: 未分类技能
- skill_id: 2088b931-a182-5233-b4ad-880545601196
- support_count: 1

## Evidence 1

- support_id: c123027f-67f3-5ca8-8a19-cb9e9f74873b
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 39514:40406
- confidence: 0.75
- quote: return tracer.start_trace(trace_name=trace_name, tags=tags)

def end_trace(
    trace_context: Optional[TraceContext] = None, end_state: Union[TraceState, StatusCode, str] = TraceState.SUCCESS
) -> None:
    """
    Ends a trace (its root span) and finalizes it.
    If no trace_context is provided, ends all active session spans.

def update_trace_metadata(metadata: Dict[str, Any], prefix: str = "trace.metadata") -> bool:
    """
    Update metadata on the current running trace.
