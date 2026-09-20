# Decorator-Based Observability Instrumentation Evidence

- family: 未分类技能
- skill_id: eace1bd8-b8f0-5539-bde6-e9f7deaa0c40
- support_count: 1

## Evidence 1

- support_id: 23c8a995-6269-5cda-8e70-a16c0a95e7aa
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 1930:2249
- confidence: 0.75
- quote: @workflow
def my_workflow(data):
    # Workflow implementation
    return result
```

```python
# Nest decorators for proper span hierarchy
from agentops.sdk.decorators import session, agent, operation

@agent
class MyAgent:
    @operation
    def nested_operation(self, message):
        return f"Processed: {message}"
