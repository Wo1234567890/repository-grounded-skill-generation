# LLM Chat Completion with AgentOps Tracking Evidence

- family: 未分类技能
- skill_id: 4862f3b3-8d5d-5992-8f28-f11b25465da9
- support_count: 1

## Evidence 1

- support_id: e042633d-6597-5e15-b98d-2d3af128c1a7
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 10031:10348
- confidence: 0.75
- quote: message = client.chat.complete(
        messages=[
            {
                "role": "user",
                "content": "Tell me a cool fact about AgentOps",
            }
        ],
        model="open-mistral-nemo",
    )
print(message.choices[0].message.content)

agentops.end_session('Success')
```

Streaming
