# AgentOps Client Configuration Validation Evidence

- family: 未分类技能
- skill_id: 4d929a45-8acb-52fc-a9ff-d895f5661c60
- support_count: 1

## Evidence 1

- support_id: 660cf513-fe40-51c4-9a6a-0f06e54bbcdf
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 36309:38094
- confidence: 0.85
- quote: Args:
        **kwargs: Configuration parameters. Supported parameters include:
            - api_key: API Key for AgentOps services
            - endpoint: The endpoint for the AgentOps service
            - app_url: The dashboard URL for the AgentOps app
            - max_wait_time: Maximum time to wait in milliseconds before flushing the queue
            - max_queue_size: Maximum size of the event queue
            - default_tags: Default tags for the sessions
            - instrument_llm_calls: Whether to instrument LLM calls
            - auto_start_session: Whether to start a session automatically
            - skip_auto_end_session: Don't automatically end session
            - env_data_opt_out: Whether to opt out of collecting environment data
            - log_level: The log level to use for the client
            - fail_safe: Whether to suppress errors and continue execution
            - exporter: Custom span exporter for OpenTelemetry trace data
            - processor: Custom span processor for OpenTelemetry trace data
            - exporter_endpoint: Endpoint for the exporter
    """
    global _client

# List of valid parameters that can be passed to configure
    valid_params = {
        "api_key",
        "endpoint",
        "app_url",
        "max_wait_time",
        "max_queue_size",
        "default_tags",
        "instrument_llm_calls",
        "auto_start_session",
        "skip_auto_end_session",
        "env_data_opt_out",
        "log_level",
        "fail_safe",
        "exporter",
        "processor",
        "exporter_endpoint",
    }

# Check for invalid parameters
    invalid_params = set(kwargs.keys()) - valid_params
    if invalid_params:
        logger.warning(f"Invalid configuration parameters: {invalid_params}")
