# LLM Event Capture and Tracking Evidence

- family: 未分类技能
- skill_id: fbff9862-db86-58a4-9cdc-06e659adf674
- support_count: 1

## Evidence 1

- support_id: ad4d6e65-e70a-5223-89b5-ea8d691946e3
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 25984:26613
- confidence: 0.80
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
