# Nested Operation Execution Tracking Evidence

- family: 未分类技能
- skill_id: c760e181-5ed7-50d6-906d-c4ccabd12c56
- support_count: 1

## Evidence 1

- support_id: 67f8b623-55ea-56bd-a672-bf328bb32aef
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 2263:2615
- confidence: 0.78
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
