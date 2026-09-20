# Trace Grouping for Operation Sequencing Evidence

- family: 未分类技能
- skill_id: 65286d8c-4994-55fa-8fd2-b4ffad35b6cc
- support_count: 1

## Evidence 1

- support_id: b6b5461a-1478-5b71-87ae-2cbea26b5378
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 69905:70474
- confidence: 0.75
- quote: # Example usage:
# search_result = web_search("AgentOps features")
# calculation = calculator("2 + 2")
```

### Grouping with Traces (`@trace` or manual)
Create custom traces to group a sequence of operations or define logical units of work. You can use the `@trace` decorator or manage traces manually for more complex scenarios.
If `auto_start_session=False` in `agentops.init()`, you must use `@trace` or `agentops.start_trace()` for any data to be recorded.

```python
from agentops.sdk.decorators import trace
# Assuming MyAgent and web_search are defined as above
