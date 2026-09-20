# AgentOps Session Initialization Evidence

- family: 未分类技能
- skill_id: 2207c09a-ca7c-54bc-9033-d9731247c4d0
- support_count: 1

## Evidence 1

- support_id: c0107497-c77f-50dd-8617-57e38f1e6970
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 129461:131114
- confidence: 0.75
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
