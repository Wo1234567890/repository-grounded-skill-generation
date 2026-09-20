# LLM API Call Tracking Evidence

- family: 未分类技能
- skill_id: 1ee9b37e-ec9b-5576-80e8-6df9e2f57d51
- support_count: 1

## Evidence 1

- support_id: be7b3cdc-7bfc-54b4-bc90-988844144d75
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 77728:78229
- confidence: 0.75
- quote: AgentOps automatically tracks LLM API calls from supported providers, collecting valuable information like:

- **Model**: The specific model used (e.g., "gpt-4", "claude-3-opus")
- **Provider**: The LLM provider (e.g., "OpenAI", "Anthropic")
- **Prompt Tokens**: Number of tokens in the input
- **Completion Tokens**: Number of tokens in the output
- **Cost**: The estimated cost of the interaction
- **Messages**: The prompt and completion content

```python
import agentops
from openai import OpenAI
