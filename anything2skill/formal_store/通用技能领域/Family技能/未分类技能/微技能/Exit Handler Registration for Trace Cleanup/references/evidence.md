# Exit Handler Registration for Trace Cleanup Evidence

- family: 未分类技能
- skill_id: 668f2259-9ad6-5193-b5b0-d334405e5cbf
- support_count: 1

## Evidence 1

- support_id: 6e996b67-bdae-5cd6-9593-8c3954c76f07
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 54247:55648
- confidence: 0.78
- quote: global _atexit_registered
        if not _atexit_registered:
            atexit.register(_end_init_trace_atexit)  # Register new atexit handler
            _atexit_registered = True

# Auto-start trace if configured
        if self.config.auto_start_session:
            if self._init_trace_context is None or not self._init_trace_context.span.is_recording():
                logger.debug("Auto-starting init trace.")
                trace_name = self.config.trace_name or "default"
                self._init_trace_context = tracer.start_trace(
                    trace_name=trace_name,
                    tags=list(self.config.default_tags) if self.config.default_tags else None,
                    is_init_trace=True,
                )
                if self._init_trace_context:
                    self._legacy_session_for_init_trace = Session(self._init_trace_context)

# For backward compatibility, also update the global references in legacy and client modules
                    # These globals are what old code might have been using via agentops.legacy.get_session() or similar indirect access.
                    global _client_init_trace_context, _client_legacy_session_for_init_trace
                    _client_init_trace_context = self._init_trace_context
                    _client_legacy_session_for_init_trace = self._legacy_session_for_init_trace
