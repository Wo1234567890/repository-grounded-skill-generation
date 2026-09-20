# Agent Instantiation and Task Invocation Evidence

- family: 未分类技能
- skill_id: c88710bc-82ee-5768-8451-985dc318299f
- support_count: 1

## Evidence 1

- support_id: 4e6fbcd4-bc8c-52a0-8bc4-dc866ff138f9
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 83534:83923
- confidence: 0.72
- quote: @operation
    def perform_task(self, task):
        # Agent task logic here
        return f"Completed {task}"

# Create a session
@session
def my_workflow():
    # Your session code here
    agent = MyAgent("research-agent")
    result = agent.perform_task("data analysis")
    return result

# Run the session
my_workflow()
```

Jupyter Notebook with sample code that you can run!
