# Multi-Agent Job Description Generation Workflow 子技能地图

## 子技能列表

- [Job Description Writer Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Job Description Writer Agent Setup/SKILL.md) ｜ 微技能
  - 适用：Configures a writer agent with web search, Serper, and file read tools to craft engaging job postings using research insights. Invoke after research phase to generate initial job description draft.
  - 线索：Research insights available from prior research agent execution, Ready to draft initial job posting, Company culture and values analysis complete, agent_configuration, job_posting
- [Research Analyst Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Research Analyst Agent Setup/SKILL.md) ｜ 微技能
  - 适用：Configures a research-focused agent with web search and Serper tools to extract company culture, values, and specific hiring needs from websites and descriptions. Invoke as the first stage to gather insights before job description drafting.
  - 线索：Starting job description creation workflow, Company website and brief description available, Need to gather structured insights on company culture and values before drafting, agent_setup, research
- [Review and Editing Specialist Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Review and Editing Specialist Agent Setup/SKILL.md) ｜ 微技能
  - 适用：Configures a review agent with web search, Serper, and file read tools to refine job postings for clarity, grammar, engagement, and company value alignment. Invoke as final stage to polish and validate job description.
  - 线索：Job description draft complete; quality assurance and refinement needed, job_description, review, editing, quality_assurance
