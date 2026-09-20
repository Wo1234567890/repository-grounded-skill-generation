# Singleton Client Initialization Evidence

- family: 未分类技能
- skill_id: 0a2a2531-de87-56a6-b24c-ab18b66de26d
- support_count: 1

## Evidence 1

- support_id: 97bad3d0-0a2f-533b-9395-5ead56505fc1
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 49909:50318
- confidence: 0.75
- quote: class Client:
    """Singleton client for AgentOps service"""

config: Config
    _initialized: bool
    _init_trace_context: Optional[TraceContext] = None  # Stores the context of the auto-started trace
    _legacy_session_for_init_trace: Optional[
        Session
    ] = None  # Stores the legacy Session wrapper for the auto-started trace

__instance = None  # Class variable for singleton pattern
