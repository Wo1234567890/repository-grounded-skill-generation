# Trace Metadata Update Evidence

- family: 未分类技能
- skill_id: 3196bcac-f0d9-56c4-9f76-d7964def7deb
- support_count: 1

## Evidence 1

- support_id: b1c9aaa7-5cf5-58fa-9f50-76800e07b86f
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 71860:72209
- confidence: 0.75
- quote: ```python
from agentops import update_trace_metadata

# Update metadata during trace execution
update_trace_metadata({
    "operation_name": "AI Agent Processing",
    "processing_stage": "data_validation",
    "records_processed": 1500,
    "user_id": "user_123",
    "tags": ["validation", "production"]
})
```

## Complete Example with Decorators
