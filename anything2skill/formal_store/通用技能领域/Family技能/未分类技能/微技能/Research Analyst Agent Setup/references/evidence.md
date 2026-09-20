# Research Analyst Agent Setup Evidence

- family: 未分类技能
- skill_id: 7a1343a0-b541-5d25-9d66-ffe28001b8e2
- support_count: 1

## Evidence 1

- support_id: 81c677df-28ba-52b3-b1cb-8aab6bc661c4
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 130898:132585
- confidence: 0.80
- quote: web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
file_read_tool = FileReadTool(
    file_path="job_description_example.md",
    description="A tool to read the job description example file.",
)

class Agents:
    def research_agent(self):
        return Agent(
            role="Research Analyst",
            goal="Analyze the company website and provided description to extract insights on culture, values, and specific needs.",
            tools=[web_search_tool, serper_dev_tool],
            backstory="Expert in analyzing company cultures and identifying key values and needs from various sources, including websites and brief descriptions.",
            verbose=True,
        )

def writer_agent(self):
        return Agent(
            role="Job Description Writer",
            goal="Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting.",
            tools=[web_search_tool, serper_dev_tool, file_read_tool],
            backstory="Skilled in crafting compelling job descriptions that resonate with the company's values and attract the right candidates.",
            verbose=True,
        )

def review_agent(self):
        return Agent(
            role="Review and Editing Specialist",
            goal="Review the job posting for clarity, engagement, grammatical accuracy, and alignment with company values and refine it to ensure perfection.",
            tools=[web_search_tool, serper_dev_tool, file_read_tool],
            backstory="A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect.",
            verbose=True,
        )
