# Singleton Client Initialization with Re-initialization Guard Evidence

- family: 未分类技能
- skill_id: cf2aafba-8a0b-5349-96e3-578d8595f10b
- support_count: 1

## Evidence 1

- support_id: e444ebfb-0fe4-5122-a9c4-b06064f9189c
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 50324:53091
- confidence: 0.85
- quote: api: ApiClient

def __new__(cls, *args: Any, **kwargs: Any) -> "Client":
        if cls.__instance is None:
            cls.__instance = super(Client, cls).__new__(cls)
            # Initialize instance variables that should only be set once per instance
            cls.__instance._init_trace_context = None
            cls.__instance._legacy_session_for_init_trace = None
        return cls.__instance

def __init__(self):
        # Initialization of attributes like config, _initialized should happen here if they are instance-specific
        # and not shared via __new__ for a true singleton that can be re-configured.
        # However, the current pattern re-initializes config in init().
        if (
            not hasattr(self, "_initialized") or not self._initialized
        ):  # Ensure init logic runs only once per actual initialization intent
            self.config = Config()  # Initialize config here for the instance
            self._initialized = False
            # self._init_trace_context = None # Already done in __new__
            # self._legacy_session_for_init_trace = None # Already done in __new__

# Only treat as re-initialization if a different non-None API key is explicitly provided
        provided_api_key = kwargs.get("api_key")
        if self.initialized and provided_api_key is not None and provided_api_key != self.config.api_key:
            logger.warning("AgentOps Client being re-initialized with a different API key. This is unusual.")
            # Reset initialization status to allow re-init with new key/config
            self._initialized = False
            if self._init_trace_context and self._init_trace_context.span.is_recording():
                logger.warning("Ending previously auto-started trace due to re-initialization.")
                tracer.end_trace(self._init_trace_context, "Reinitialized")
            self._init_trace_context = None
            self._legacy_session_for_init_trace = None

if self.initialized:
            logger.debug("AgentOps Client already initialized.")
            # If auto_start_session was true, return the existing legacy session wrapper
            if self.config.auto_start_session:
                return self._legacy_session_for_init_trace
            return None  # If not auto-starting, and already initialized, return None

if not self.config.api_key:
            raise NoApiKeyException
