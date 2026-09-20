# Singleton Instance Deduplication Evidence

- family: 未分类技能
- skill_id: afacfee3-2f37-5749-8466-43fae31d33f8
- support_count: 1

## Evidence 1

- support_id: a0f89720-2808-5f27-9510-e5a6f316d811
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 57729:59031
- confidence: 0.68
- quote: # ------------------------------------------------------------
    # Remove the old __instance = None at the end of the class definition if it's a repeat
    # __instance = None # This was a class variable, should be defined once

# Make _init_trace_context and _legacy_session_for_init_trace accessible
    # to the atexit handler if it becomes a static/class method or needs access
    # For now, the atexit handler is global and uses global vars copied from these.

# Deprecate and remove the old global _active_session from this module.
    # Consumers should use agentops.start_trace() or rely on the auto-init trace.
    # For a transition, the auto-init trace's legacy wrapper is set to legacy module's globals.

# Ensure the global _active_session (if needed for some very old compatibility) points to the client's legacy session for init trace.
# This specific global _active_session in client.py is problematic and should be phased out.
# For now, _client_legacy_session_for_init_trace is the primary global for the auto-init trace's legacy Session.

# Remove the old global _active_session defined at the top of this file if it's no longer the primary mechanism.
# The new globals _client_init_trace_context and _client_legacy_session_for_init_trace handle the auto-init trace.

```
