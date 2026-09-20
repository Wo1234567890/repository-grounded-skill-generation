# Nested Operation Execution Pattern Evidence

- family: 未分类技能
- skill_id: e3893ef5-8d06-5356-8a44-7ed3b1cca418
- support_count: 1

## Evidence 1

- support_id: dd48d39b-98b2-5b5d-8f58-ac425f3a274e
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
