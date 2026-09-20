---
id: "7a1343a0-b541-5d25-9d66-ffe28001b8e2"
name: "Research Analyst Agent Setup"
description: "Configures a research-focused agent with web search and Serper tools to extract company culture, values, and specific hiring needs from websites and descriptions. Invoke as the first stage to gather insights before job description drafting."
version: "0.1.0"
tags:
  - "agent_setup"
  - "research"
  - "job_description"
  - "multi_agent_workflow"
  - "company_analysis"
triggers:
  - "Starting job description creation workflow"
  - "Company website and brief description available"
  - "Need to gather structured insights on company culture and values before drafting"
---

# Research Analyst Agent Setup

Configures a research-focused agent with web search and Serper tools to extract company culture, values, and specific hiring needs from websites and descriptions. Invoke as the first stage to gather insights before job description drafting.

## Prompt

Initialize a Research Analyst agent with role='Research Analyst', goal set to analyze company website and provided description to extract insights on culture, values, and specific needs. Attach web_search_tool and serper_dev_tool. Set backstory to emphasize expertise in analyzing company cultures and identifying key values from various sources. Enable verbose output for transparency.

## Objective

Extract company culture and values insights from web sources
## Applicable Signals

- Initial phase of job posting creation
- Company metadata provided but insights not yet extracted
- Multi-agent workflow initiated

## Contraindications

- Company insights already gathered from prior research
- Only writing or editing phase needed
- No web access or company website available

## Workflow Steps

- Instantiate WebsiteSearchTool and SerperDevTool
- Create Agent with role='Research Analyst'
- Set goal to analyze company website and description for culture, values, and needs
- Attach web_search_tool and serper_dev_tool to agent
- Set backstory emphasizing expertise in company culture analysis
- Enable verbose=True for execution transparency
- Return configured agent instance

## Constraints

- Web search tools must be initialized and functional
- Company description input required
- Agent must be invoked before writer_agent in the workflow sequence

## Cautions

- Ensure web_search_tool and serper_dev_tool are properly configured before agent initialization
- Verbose output may generate large logs; consider log management in production

## Output Contract

- Returns a fully configured Research Analyst agent instance ready to execute research tasks. Output is structured insights on company culture, values, and specific hiring needs, formatted for handoff to writer_agent.

## Triggers

- Starting job description creation workflow
- Company website and brief description available
- Need to gather structured insights on company culture and values before drafting
