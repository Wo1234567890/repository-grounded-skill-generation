# Agent Operation Span Tracking Evidence

- family: 未分类技能
- skill_id: 7b643d32-9ba8-5dcc-accc-a035b57be10f
- support_count: 1

## Evidence 1

- support_id: 44869675-4034-5665-a491-2e3b7d1a01dc
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 1129:1474
- confidence: 0.80
- quote: Refer to our [documentation](http://docs.agentops.ai)

```python
# Create a session span (root for all other spans)
from agentops.sdk.decorators import session

@session
def my_workflow():
    # Your session code here
    return result
```

```python
# Create an agent span for tracking agent operations
from agentops.sdk.decorators import agent
