# Stream Event Processing for Agent Output Evidence

- family: 未分类技能
- skill_id: fb8ebdf4-e71c-5087-8a57-7bcf85d7244c
- support_count: 1

## Evidence 1

- support_id: 9faac656-f85b-523d-b91a-3ccdd12b6828
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 7171:7561
- confidence: 0.75
- quote: for event in stream:
    if event.event_type == "text-generation":
        print(event.text, end='')

agentops.end_session('Success')
```

Anthropic
Track agents built with the Anthropic Python SDK (>=0.32.0).

- [AgentOps integration guide](https://docs.agentops.ai/v1/integrations/anthropic)
- [Official Anthropic documentation](https://docs.anthropic.com/en/docs/welcome)

Installation
