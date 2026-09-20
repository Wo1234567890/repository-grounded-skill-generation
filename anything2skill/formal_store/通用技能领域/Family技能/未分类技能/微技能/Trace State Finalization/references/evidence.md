# Trace State Finalization Evidence

- family: 未分类技能
- skill_id: ba5eb02b-fe16-5890-9e8b-ae1603bd4178
- support_count: 1

## Evidence 1

- support_id: e6c65580-cb50-5878-bec4-e8cd01f1703e
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 39514:40406
- confidence: 0.80
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
