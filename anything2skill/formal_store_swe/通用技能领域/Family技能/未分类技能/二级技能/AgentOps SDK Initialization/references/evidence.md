# AgentOps SDK Initialization Evidence

- family: 未分类技能
- skill_id: c20f49cc-1854-560a-9f83-89494b3d0cc1
- support_count: 1

## Evidence 1

- support_id: 5de145d5-feb6-56a1-bfe9-9fe3f1707628
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 31577:32383
- confidence: 0.75
- quote: return event

def init(
    api_key: Optional[str] = None,
    endpoint: Optional[str] = None,
    app_url: Optional[str] = None,
    max_wait_time: Optional[int] = None,
    max_queue_size: Optional[int] = None,
    tags: Optional[List[str]] = None,
    default_tags: Optional[List[str]] = None,
    trace_name: Optional[str] = None,
    instrument_llm_calls: Optional[bool] = None,
    auto_start_session: Optional[bool] = None,
    auto_init: Optional[bool] = None,
    skip_auto_end_session: Optional[bool] = None,
    env_data_opt_out: Optional[bool] = None,
    log_level: Optional[Union[str, int]] = None,
    fail_safe: Optional[bool] = None,
    log_session_replay_url: Optional[bool] = None,
    exporter_endpoint: Optional[str] = None,
    **kwargs,
):
    """
    Initializes the AgentOps SDK.
