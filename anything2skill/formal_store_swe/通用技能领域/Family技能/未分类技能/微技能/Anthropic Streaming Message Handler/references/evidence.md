# Anthropic Streaming Message Handler Evidence

- family: 未分类技能
- skill_id: 44161230-0147-5338-8218-7c5c95ef22d1
- support_count: 1

## Evidence 1

- support_id: 7d668286-0f65-55d6-9f58-2aca4cd938af
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 7853:8233
- confidence: 0.65
- quote: message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Tell me a cool fact about AgentOps",
            }
        ],
        model="claude-3-opus-20240229",
    )
print(message.content)

agentops.end_session('Success')
```

Streaming
```python python
import anthropic
import agentops
