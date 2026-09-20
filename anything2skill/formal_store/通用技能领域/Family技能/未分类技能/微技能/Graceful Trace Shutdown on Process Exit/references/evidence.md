# Graceful Trace Shutdown on Process Exit Evidence

- family: 未分类技能
- skill_id: 221b12bc-4082-5dda-ba28-0a8424fb4c0f
- support_count: 1

## Evidence 1

- support_id: bca53ae9-2911-5e13-8345-bb09df6b073a
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 49011:49970
- confidence: 0.75
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
