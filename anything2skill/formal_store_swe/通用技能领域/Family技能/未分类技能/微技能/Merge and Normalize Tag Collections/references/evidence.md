# Merge and Normalize Tag Collections Evidence

- family: 未分类技能
- skill_id: 5a6fb1c5-9833-5a9c-82ec-fc347161461e
- support_count: 1

## Evidence 1

- support_id: afc9ce48-8c2e-525a-84f9-1ee07fadc3ba
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 34859:36165
- confidence: 0.85
- quote: # Merge tags and default_tags if both are provided
    merged_tags = None
    if tags and default_tags:
        merged_tags = list(set(tags + default_tags))
    elif tags:
        merged_tags = tags
    elif default_tags:
        merged_tags = default_tags

# Check if in a Jupyter Notebook (manual start/end_trace())
    try:
        get_ipython().__class__.__name__ == "ZMQInteractiveShell"  # type: ignore
        auto_start_session = False
    except NameError:
        pass

# Prepare initialization arguments
    init_kwargs = {
        "api_key": api_key,
        "endpoint": endpoint,
        "app_url": app_url,
        "max_wait_time": max_wait_time,
        "max_queue_size": max_queue_size,
        "default_tags": merged_tags,
        "trace_name": trace_name,
        "instrument_llm_calls": instrument_llm_calls,
        "auto_start_session": auto_start_session,
        "auto_init": auto_init,
        "skip_auto_end_session": skip_auto_end_session,
        "env_data_opt_out": env_data_opt_out,
        "log_level": log_level,
        "fail_safe": fail_safe,
        "log_session_replay_url": log_session_replay_url,
        "exporter_endpoint": exporter_endpoint,
        **kwargs,
    }

# Get the current client instance (creates new one if needed)
    client = get_client()
