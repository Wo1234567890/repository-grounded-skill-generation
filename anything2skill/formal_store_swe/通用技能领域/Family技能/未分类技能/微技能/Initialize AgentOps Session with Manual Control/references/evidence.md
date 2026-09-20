# Initialize AgentOps Session with Manual Control Evidence

- family: 未分类技能
- skill_id: 080b9d08-e952-56df-8d89-d09f39ae4f19
- support_count: 1

## Evidence 1

- support_id: 7034e3e4-3fdd-5dc2-a450-76a89d16d7dd
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 63069:63310
- confidence: 0.85
- quote: ```python python
	import agentops
	from agentops.sdk.decorators import trace

agentops.init(, auto_start_session=False)

@trace(name="my-workflow", tags=["production"])
	def my_workflow():
		# Your code here
		return "Workflow completed"
