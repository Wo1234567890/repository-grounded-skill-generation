# AgentOps Session Initialization Evidence

- family: 未分类技能
- skill_id: 9abe764e-fbfb-5b76-876e-59bdd1b73d66
- support_count: 2

## Evidence 1

- support_id: ff970c13-5343-5a6b-963e-3d3337cb6dec
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 72426:72914
- confidence: 0.85
- quote: # Load environment variables
load_dotenv()
AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")

# Initialize AgentOps. 
# Set auto_start_session=False because @trace will manage the session.
agentops.init(AGENTOPS_API_KEY, auto_start_session=False, tags=["quickstart-complete-example"])

# Define a tool
@tool(name="AdvancedSearch", cost=0.02)
def advanced_web_search(query: str) -> str:
    # Simulate a more advanced search
    return f"Advanced search results for '{query}': [Details...]"

## Evidence 2

- support_id: c0107497-c77f-50dd-8617-57e38f1e6970
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 129461:131114
- confidence: 0.85
- quote: # First let's install the required packages
# %pip install -U 'crewai[tools]'
# Then import them
from crewai import Crew, Agent, Task
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
import agentops
import os
from dotenv import load_dotenv
from textwrap import dedent

# Initialize AgentOps client
agentops.init(
    auto_start_session=False, trace_name="CrewAI Job Posting", tags=["crewai", "job-posting", "agentops-example"]
)

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
file_read_tool = FileReadTool(
    file_path="job_description_example.md",
    description="A tool to read the job description example file.",
)
