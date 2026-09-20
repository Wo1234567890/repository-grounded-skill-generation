---
id: "6989d4f7-d8c6-5219-91aa-f731edabf5a2"
name: "Multi-Agent Job Description Generation Workflow"
description: "Orchestrate a three-agent sequential pipeline to generate polished job descriptions from company data. Research Analyst analyzes company culture and values; Job Description Writer creates engaging posting using research insights; Review Specialist refines for clarity, engagement, grammar, and alignment. Agents execute in strict sequence with output handoff between stages."
version: "0.1.0"
tags:
  - "multi-agent"
  - "orchestration"
  - "job-posting"
  - "content-generation"
  - "sequential-workflow"
  - "agent-coordination"
triggers:
  - "Need to create job postings that reflect company culture and values"
  - "Company website and job description template are available"
  - "Multiple perspectives (research, writing, editing) required for quality output"
---

# Multi-Agent Job Description Generation Workflow

Orchestrate a three-agent sequential pipeline to generate polished job descriptions from company data. Research Analyst analyzes company culture and values; Job Description Writer creates engaging posting using research insights; Review Specialist refines for clarity, engagement, grammar, and alignment. Agents execute in strict sequence with output handoff between stages.

## Prompt

Initialize three agents with specialized roles: Research Analyst (analyzes company website and description for culture/values/needs using web search and Serper tools), Job Description Writer (creates detailed posting using research insights and file reading), and Review Specialist (refines for clarity, engagement, grammar, and alignment). Execute agents sequentially: research → writing → review. Pass outputs between agents as context. Return final polished job posting.

## Objective

Generate polished job description through coordinated multi-agent analysis and refinement
## Applicable Signals

- Job posting request with company context
- Availability of company website or cultural documentation
- Template or example job description provided

## Contraindications

- Job description already finalized and approved
- No company website or cultural data available for research phase
- Single-agent task sufficient (e.g., minor edits only)
- Insufficient time for sequential multi-agent execution

## Workflow Steps

- {'step': 1, 'name': 'Initialize Research Agent', 'action': "Create Research Analyst agent with role='Research Analyst', goal='Analyze the company website and provided description to extract insights on culture, values, and specific needs', tools=[web_search_tool, serper_dev_tool], and backstory='Expert in analyzing company cultures and identifying key values and needs from various sources, including websites and brief descriptions'"}
- {'step': 2, 'name': 'Execute Research Phase', 'action': 'Run research agent to analyze company website and provided description; extract insights on culture, values, and specific needs'}
- {'step': 3, 'name': 'Initialize Writer Agent', 'action': "Create Job Description Writer agent with role='Job Description Writer', goal='Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting', tools=[web_search_tool, serper_dev_tool, file_read_tool], and backstory='Skilled in crafting compelling job descriptions that resonate with the company's values and attract the right candidates'"}
- {'step': 4, 'name': 'Execute Writing Phase', 'action': 'Run writer agent using research insights to create detailed, engaging, enticing job posting aligned with company values'}
- {'step': 5, 'name': 'Initialize Review Agent', 'action': "Create Review and Editing Specialist agent with role='Review and Editing Specialist', goal='Review the job posting for clarity, engagement, grammatical accuracy, and alignment with company values and refine it to ensure perfection', tools=[web_search_tool, serper_dev_tool, file_read_tool], and backstory='A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect'"}
- {'step': 6, 'name': 'Execute Review Phase', 'action': 'Run review agent to assess job posting for clarity, engagement, grammatical accuracy, and alignment with company values; refine to perfection'}
- {'step': 7, 'name': 'Return Final Output', 'action': 'Deliver polished job posting ready for publication'}

## Constraints

- All three agents must execute in sequence: research → writing → review
- Research agent output must inform writer agent context
- Writer agent output must be available for review agent refinement
- File read tool requires valid job_description_example.md path

## Cautions

- Ensure company website is accessible and contains relevant cultural information
- Verify file paths for job description template before workflow execution
- Set verbose=True for debugging; consider disabling in production for performance

## Output Contract

- Polished, grammatically correct job posting that reflects company culture and values, ready for immediate publication. Output includes final refined text from review agent with all clarity, engagement, and alignment requirements met.

## Triggers

- Need to create job postings that reflect company culture and values
- Company website and job description template are available
- Multiple perspectives (research, writing, editing) required for quality output
