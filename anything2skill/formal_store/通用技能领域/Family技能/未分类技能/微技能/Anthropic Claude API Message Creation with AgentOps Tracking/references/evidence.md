# Anthropic Claude API Message Creation with AgentOps Tracking Evidence

- family: 未分类技能
- skill_id: 89774e36-8c01-5fae-83dd-52fe3afe5ca4
- support_count: 1

## Evidence 1

- support_id: 70068766-24db-55fe-b1f9-22cfac057226
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 7853:8233
- confidence: 0.75
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
