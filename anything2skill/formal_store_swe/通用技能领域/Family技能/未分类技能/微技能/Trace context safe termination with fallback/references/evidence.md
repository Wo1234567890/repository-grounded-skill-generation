# Trace context safe termination with fallback Evidence

- family: 未分类技能
- skill_id: 0c6d7ac8-d8d1-54d8-8cbd-55c5a2dac5ec
- support_count: 1

## Evidence 1

- support_id: 17106275-81ae-5b14-889e-449f26f43ee1
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 49011:49970
- confidence: 0.72
- quote: # Single atexit handler registered flag
_atexit_registered = False

def _end_init_trace_atexit():
    """Global atexit handler to end the client's auto-initialized trace during shutdown."""
    global _client_init_trace_context, _client_legacy_session_for_init_trace
    if _client_init_trace_context is not None:
        logger.debug("Auto-ending client's init trace during shutdown.")
        try:
            # Use global tracer to end the trace directly
            if tracer.initialized and _client_init_trace_context.span.is_recording():
                tracer.end_trace(_client_init_trace_context, end_state="Shutdown")
        except Exception as e:
            logger.warning(f"Error ending client's init trace during shutdown: {e}")
        finally:
            _client_init_trace_context = None
            _client_legacy_session_for_init_trace = None  # Clear its legacy wrapper too

class Client:
    """Singleton client for AgentOps service"""
