# Web Font Rendering Strategy Selection Evidence

- family: 未分类技能
- skill_id: 5d54ebac-052c-525f-b1ac-d6c81c8e8b19
- support_count: 2

## Evidence 1

- support_id: 9d697b81-ecf3-591b-a81f-909c74b0d379
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Understand the causes of layout shifts
- span: 27421:27784
- confidence: 0.72
- quote: Web fonts
Downloading and rendering web fonts is typically handled in one of two ways before the web font is downloaded:

- The fallback font is swapped with the web font, incurring a Flash of Unstyled Text (FOUT).

- "Invisible" text is displayed using the fallback font until a web font is available and the text is made visible (FOIT—flash of invisible text).

## Evidence 2

- support_id: 7543dce4-f0b2-5787-9d6c-39ce90a67e6b
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 25984:26613
- confidence: 0.82
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
