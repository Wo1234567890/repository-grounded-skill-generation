# Group iterable into nested structure Evidence

- family: 未分类技能
- skill_id: 64a5ce52-07a9-52f9-808d-dbdc2659a314
- support_count: 2

## Evidence 1

- support_id: 94281866-ae51-574b-98a0-ca62f1288e34
- relation_type: support
- document: d3-docs.md
- doc_id: 6cdc3f25-9cd8-59fc-987c-27814dbcdcb1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/d3-docs.md
- section: API index ​
- span: 3855:4557
- confidence: 0.85
- quote: Group ​
Group discrete values.

- d3.group - group an iterable into a nested Map.
- d3.groups - group an iterable into a nested array.
- d3.rollup - reduce an iterable into a nested Map.
- d3.rollups - reduce an iterable into a nested array.
- d3.index - index an iterable into a nested Map.
- d3.indexes - index an iterable into a nested array.
- d3.flatGroup - group an iterable into a flat array.
- d3.flatRollup - reduce an iterable into a flat array.
- d3.groupSort - sort keys according to grouped values.

Intern ​
Create maps and sets with non-primitive values such as dates.

- new InternMap - a key-interning Map.
- new InternSet - a value-interning Set.

Sets ​
Logical operations on sets.

## Evidence 2

- support_id: 4264f43c-4a64-5b6f-8be0-94c98c0baa10
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 1930:2249
- confidence: 0.80
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
