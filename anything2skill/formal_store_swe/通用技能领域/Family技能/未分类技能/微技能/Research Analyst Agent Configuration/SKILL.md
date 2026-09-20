---
id: "98be3b8a-ee9e-56c2-9888-3e3bf060548c"
name: "Research Analyst Agent Configuration"
description: "Configure and instantiate a Research Analyst agent with web search and Serper Dev tools to extract company culture, values, and needs from websites and descriptions."
version: "0.1.0"
tags:
  - "agent_configuration"
  - "research"
  - "initialization"
  - "multi_agent_workflow"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting job description generation workflow; need to analyze company website and cultural signals"
---

# Research Analyst Agent Configuration

Configure and instantiate a Research Analyst agent with web search and Serper Dev tools to extract company culture, values, and needs from websites and descriptions.

## Prompt

Initialize a Research Analyst agent by instantiating an Agent object with the following configuration:
- Role: Research Analyst
- Goal: Analyze the company website and provided description to extract insights on culture, values, and specific needs
- Tools: web_search_tool and serper_dev_tool
- Backstory: Expert in analyzing company cultures and identifying key values and needs from various sources, including websites and brief descriptions
- Set verbose=True for detailed execution logging
Return the configured Agent object ready for execution.

## Objective

Initialize research agent with appropriate role, goal, tools, and backstory for culture analysis
## Applicable Signals

- Starting job description generation workflow
- Need to analyze company website and cultural signals
- Research phase required before content creation

## Contraindications

- Company culture already documented and available
- Research phase explicitly skipped in workflow
- No web access or network connectivity available
- Company information restricted or confidential

## Workflow Steps

- Instantiate WebsiteSearchTool and SerperDevTool objects
- Create Agent object with role='Research Analyst'
- Set goal to analyze company website and description for culture, values, and needs
- Assign web_search_tool and serper_dev_tool to tools parameter
- Set backstory describing expertise in company culture analysis
- Enable verbose=True for execution transparency
- Return configured Agent object

## Constraints

- Both web_search_tool and serper_dev_tool must be initialized before agent creation
- Agent role must be exactly 'Research Analyst' for downstream workflow compatibility
- verbose flag must be True for debugging and monitoring

## Output Contract

- Returns an instantiated Agent object with Research Analyst role, web_search_tool and serper_dev_tool configured, ready to execute analysis tasks and extract company culture insights

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting job description generation workflow; need to analyze company website and cultural signals
