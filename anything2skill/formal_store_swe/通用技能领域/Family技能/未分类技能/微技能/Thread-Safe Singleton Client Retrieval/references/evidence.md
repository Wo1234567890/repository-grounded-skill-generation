# Thread-Safe Singleton Client Retrieval Evidence

- family: 未分类技能
- skill_id: 3e22b66d-a038-50aa-8d16-63975d9361be
- support_count: 1

## Evidence 1

- support_id: cc666b44-f35a-5a5c-8806-9d16a829750a
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 30736:31044
- confidence: 0.85
- quote: def get_client() -> Client:
    """Get the singleton client instance in a thread-safe manner"""
    global _client

# Double-checked locking pattern for thread safety
    if _client is None:
        with _client_lock:
            if _client is None:
                _client = Client()

return _client
