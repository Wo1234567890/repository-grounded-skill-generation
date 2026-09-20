# Provider Method Override and Restoration Evidence

- family: 未分类技能
- skill_id: 4bc5936a-e929-5bda-8cc5-44ccef2e4384
- support_count: 1

## Evidence 1

- support_id: 7cbea0a4-4f47-51d0-979e-699c97b6b093
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 25984:26613
- confidence: 0.78
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
