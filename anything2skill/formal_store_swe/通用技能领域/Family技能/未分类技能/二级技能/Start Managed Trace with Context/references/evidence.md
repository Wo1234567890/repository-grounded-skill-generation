# Start Managed Trace with Context Evidence

- family: 未分类技能
- skill_id: 2fefe2f0-790d-5e47-99c5-c441046648cf
- support_count: 1

## Evidence 1

- support_id: 4b8ade7f-4aa7-5d20-b197-26ff4c427db8
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 38100:39573
- confidence: 0.88
- quote: client = get_client()
    client.configure(**kwargs)

def start_trace(
    trace_name: str = "session", tags: Optional[Union[Dict[str, Any], List[str]]] = None
) -> Optional[TraceContext]:
    """
    Starts a new trace (root span) and returns its context.
    This allows for multiple concurrent, user-managed traces.

Args:
        trace_name: Name for the trace (e.g., "session", "my_custom_task").
        tags: Optional tags to attach to the trace span (list of strings or dict).

Returns:
        A TraceContext object containing the span and context token, or None if SDK not initialized.
    """
    if not tracer.initialized:
        # Optionally, attempt to initialize the client if not already, or log a more severe warning.
        # For now, align with legacy start_session that would try to init.
        # However, explicit init is preferred before starting traces.
        logger.warning("AgentOps SDK not initialized. Attempting to initialize with defaults before starting trace.")
        try:
            init()  # Attempt to initialize with environment variables / defaults
            if not tracer.initialized:
                logger.error("SDK initialization failed. Cannot start trace.")
                return None
        except Exception as e:
            logger.error(f"SDK auto-initialization failed during start_trace: {e}. Cannot start trace.")
            return None

return tracer.start_trace(trace_name=trace_name, tags=tags)
