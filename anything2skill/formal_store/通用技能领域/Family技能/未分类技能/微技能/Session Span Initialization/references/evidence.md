# Session Span Initialization Evidence

- family: 未分类技能
- skill_id: 58f1d777-5d14-5893-b5da-1edab414b682
- support_count: 1

## Evidence 1

- support_id: a1092a36-8d1a-541e-9602-d38348317f88
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 1129:1474
- confidence: 0.75
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
