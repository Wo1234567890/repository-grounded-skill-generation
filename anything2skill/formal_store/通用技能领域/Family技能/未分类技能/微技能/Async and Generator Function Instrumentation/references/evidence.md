# Async and Generator Function Instrumentation Evidence

- family: 未分类技能
- skill_id: 78bc835d-8aaf-5956-93db-9f22c46d5a61
- support_count: 1

## Evidence 1

- support_id: e447d934-ca1d-59b3-a428-884407b50f8c
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 2263:2615
- confidence: 0.75
- quote: @operation
    def main_operation(self):
        result = self.nested_operation("test message")
        return result

@session
def my_session():
    agent = MyAgent()
    return agent.main_operation()
```

All decorators support:
- Input/Output Recording
- Exception Handling
- Async/await functions
- Generator functions
- Custom attributes and names
