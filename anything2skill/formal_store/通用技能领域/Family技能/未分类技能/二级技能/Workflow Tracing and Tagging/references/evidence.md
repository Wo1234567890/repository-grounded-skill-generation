# Workflow Tracing and Tagging Evidence

- family: 未分类技能
- skill_id: 7c32f9a3-248f-5476-b184-3b15af1891d9
- support_count: 1

## Evidence 1

- support_id: 41e70afa-1178-5d02-b75a-351ba5873907
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 72711:73841
- confidence: 0.88
- quote: # Define a tool
@tool(name="AdvancedSearch", cost=0.02)
def advanced_web_search(query: str) -> str:
    # Simulate a more advanced search
    return f"Advanced search results for '{query}': [Details...]"

# Define an agent class
@agent(name="ResearchSpecialistAgent")
class ResearchAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id # This will be used as the agent_id in AgentOps

# Define a workflow using the @trace decorator
@trace(name="FullResearchWorkflow", tags=["research", "analysis", "example"])
def run_full_research_workflow(topic: str) -> str:
    specialist_agent = ResearchAgent(agent_id="researcher-alpha-007")
    research_findings = specialist_agent.conduct_research(topic)
