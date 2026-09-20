# AgentOps Session Lifecycle Management Evidence

- family: 未分类技能
- skill_id: a7c386e7-6b98-5ac6-8fbe-c7d3468b741d
- support_count: 1

## Evidence 1

- support_id: f5a16d03-9a06-52b1-a9d0-38a9a6671a44
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 10031:10348
- confidence: 0.80
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
