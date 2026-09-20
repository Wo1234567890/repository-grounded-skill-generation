# Manual Session Control Pattern Evidence

- family: 未分类技能
- skill_id: 9494ffe2-c1cc-5ca4-977e-3dd37018fc5c
- support_count: 1

## Evidence 1

- support_id: b7466686-7520-58d7-a12e-b91bff7d724c
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 76123:76630
- confidence: 0.78
- quote: ```python
import agentops

# Initialize AgentOps with automatic session creation
agentops.init(api_key="YOUR_API_KEY")
```

By default, all events and API calls will be associated with this session. For more advanced use cases, you can control session creation manually:

```python
# Initialize without auto-starting a session
agentops.init(api_key="YOUR_API_KEY", auto_start_session=False)

# Later, manually start a session when needed
agentops.start_session(tags=["customer-query"])
```

# Span Hierarchy
