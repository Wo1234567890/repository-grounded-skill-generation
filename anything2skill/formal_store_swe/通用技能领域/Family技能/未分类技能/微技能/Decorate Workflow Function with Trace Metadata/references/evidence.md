# Decorate Workflow Function with Trace Metadata Evidence

- family: 未分类技能
- skill_id: df5ba5a4-e5af-5af4-9d48-740d751e9ca4
- support_count: 1

## Evidence 1

- support_id: 696e24f3-32ce-55f2-b324-a4f55dfc362d
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 63069:63310
- confidence: 0.88
- quote: ```python python
	import agentops
	from agentops.sdk.decorators import trace

agentops.init(, auto_start_session=False)

@trace(name="my-workflow", tags=["production"])
	def my_workflow():
		# Your code here
		return "Workflow completed"
