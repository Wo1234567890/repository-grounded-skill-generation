# LLM Provider Integration Pattern Evidence

- family: 未分类技能
- skill_id: 9c94fdb4-079e-5b48-9d89-aa66d04b09e6
- support_count: 1

## Evidence 1

- support_id: 46761a90-3ee6-52bc-a285-d5e81c3c2094
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 25984:26613
- confidence: 0.85
- quote: The `agentops/llms/` directory contains provider implementations. Each provider must:

1. **Inherit from BaseProvider**:
   ```python
   @singleton
   class NewProvider(BaseProvider):
       def __init__(self, client):
           super().__init__(client)
           self._provider_name = "ProviderName"
   ```

2. **Implement Required Methods**:
   - `handle_response()`: Process LLM responses
   - `override()`: Patch the provider's methods
   - `undo_override()`: Restore original methods

3. **Handle Events**:
   Track:
   - Prompts and completions
   - Token usage
   - Timestamps
   - Errors
   - Tool usage (if applicable)
