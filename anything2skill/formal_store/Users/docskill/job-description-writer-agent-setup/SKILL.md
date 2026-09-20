---
id: "43ff7405-9b97-53d7-9c32-119269deec7d"
name: "Job Description Writer Agent Setup"
description: "Configures a writer agent with web search, Serper, and file read tools to craft engaging job postings using research insights. Invoke after research phase to generate initial job description draft."
version: "0.1.0"
tags:
  - "agent_configuration"
  - "job_posting"
  - "writing_phase"
  - "multi_tool_agent"
  - "workflow_step"
triggers:
  - "Research insights available from prior research agent execution"
  - "Ready to draft initial job posting"
  - "Company culture and values analysis complete"
---

# Job Description Writer Agent Setup

Configures a writer agent with web search, Serper, and file read tools to craft engaging job postings using research insights. Invoke after research phase to generate initial job description draft.

## Prompt

Initialize a Job Description Writer agent with role='Job Description Writer', goal to create detailed and engaging job postings that resonate with company values, and tools: web_search_tool, serper_dev_tool, file_read_tool. Set verbose=True for execution transparency.

## Objective

Create detailed, engaging job posting from research insights
## Applicable Signals

- research_agent output received
- job_description_example.md file accessible
- web_search_tool and serper_dev_tool initialized

## Contraindications

- Job description already written; use review_agent instead
- Only review or editing needed; skip to review phase
- Research phase incomplete or insights unavailable

## Intervention Moves

- Instantiate Agent with writer role and backstory
- Attach web_search_tool, serper_dev_tool, file_read_tool
- Set verbose=True for debugging and transparency
- Execute agent to generate initial draft

## Workflow Steps

- {'step': 1, 'action': 'Initialize web_search_tool, serper_dev_tool, and file_read_tool with correct file_path', 'input': 'Tool configuration parameters', 'output': 'Initialized tool instances'}
- {'step': 2, 'action': "Create Agent instance with role='Job Description Writer', goal focused on crafting engaging postings", 'input': 'Role, goal, tools list, backstory', 'output': 'Configured writer_agent instance'}
- {'step': 3, 'action': 'Pass research insights from prior phase as context to writer_agent', 'input': 'Research analyst output (culture, values, needs)', 'output': 'Agent receives context for composition'}
- {'step': 4, 'action': 'Execute writer_agent with verbose=True', 'input': 'Initialized agent and research context', 'output': 'Initial job posting draft'}

## Constraints

- Requires file_read_tool configured with valid file_path to job_description_example.md
- Web search and Serper tools must be initialized before agent instantiation
- Agent must receive research insights as context input

## Cautions

- Ensure research_agent completes before invoking writer_agent
- Verify file_path points to accessible job description template
- Monitor verbose output for tool execution errors

## Output Contract

- Initial job posting draft that is detailed, engaging, and aligned with company values and identified candidate needs. Draft ready for review_agent refinement.

## Triggers

- Research insights available from prior research agent execution
- Ready to draft initial job posting
- Company culture and values analysis complete
