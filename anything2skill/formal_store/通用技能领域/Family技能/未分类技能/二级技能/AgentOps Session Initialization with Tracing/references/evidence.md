# AgentOps Session Initialization with Tracing Evidence

- family: 未分类技能
- skill_id: aa70b4ce-2bbe-5641-9ec3-765f02288449
- support_count: 1

## Evidence 1

- support_id: ef09cd31-cffd-5a27-b416-f737de3c3bb0
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 63069:63310
- confidence: 0.75
- quote: ```python python
	import agentops
	from agentops.sdk.decorators import trace

agentops.init(, auto_start_session=False)

@trace(name="my-workflow", tags=["production"])
	def my_workflow():
		# Your code here
		return "Workflow completed"
