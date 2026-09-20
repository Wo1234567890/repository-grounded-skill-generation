---
id: "d7d4fe24-c5e3-5fde-b029-96d37867df33"
name: "Job Description Writer Agent Configuration"
description: "Initialize and configure a Job Description Writer agent with web search, Serper Dev, and file read tools to draft engaging job postings based on research insights from a Research Analyst."
version: "0.1.0"
tags:
  - "agent_configuration"
  - "job_posting"
  - "writer_agent"
  - "multi_agent_workflow"
  - "tool_integration"
triggers:
  - "Second phase of job description workflow"
  - "Research insights available and ready to draft posting"
---

# Job Description Writer Agent Configuration

Initialize and configure a Job Description Writer agent with web search, Serper Dev, and file read tools to draft engaging job postings based on research insights from a Research Analyst.

## Prompt

Initialize a Job Description Writer agent by setting role to 'Job Description Writer', goal to create detailed and engaging job postings using research insights, and equip with web_search_tool, serper_dev_tool, and file_read_tool. Set backstory to reflect expertise in crafting compelling job descriptions aligned with company values. Enable verbose mode for execution transparency.

## Objective

Initialize writer agent with appropriate role, goal, tools, and backstory for job posting composition
## Applicable Signals

- Research phase completed and insights available
- Job description template or file reference ready
- Multi-phase job posting workflow in progress

## Contraindications

- Research phase incomplete or insights unavailable
- Job description template or file path not provided
- Writing phase skipped or not required in workflow

## Intervention Moves

- Instantiate Agent class with writer-specific role and goal
- Attach web_search_tool, serper_dev_tool, and file_read_tool
- Set backstory emphasizing job description crafting expertise
- Enable verbose mode for execution logging

## Workflow Steps

- {'step': 1, 'action': 'Instantiate Agent class', 'detail': "Create Agent object with role='Job Description Writer'"}
- {'step': 2, 'action': 'Set goal', 'detail': "goal='Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting'"}
- {'step': 3, 'action': 'Attach tools', 'detail': 'tools=[web_search_tool, serper_dev_tool, file_read_tool]'}
- {'step': 4, 'action': 'Set backstory', 'detail': "backstory='Skilled in crafting compelling job descriptions that resonate with the company's values and attract the right candidates'"}
- {'step': 5, 'action': 'Enable verbose mode', 'detail': 'verbose=True'}

## Constraints

- All three tools (web_search, serper_dev, file_read) must be instantiated before agent creation
- File path for job description reference must be valid and accessible
- Agent must be created within a class or callable context

## Cautions

- Ensure research insights are passed to writer agent before execution
- Verify file_read_tool points to correct job description template
- Verbose mode may produce large logs in production environments

## Output Contract

- Returns instantiated Agent object with Job Description Writer role, all three tools configured and accessible, ready to accept research insights and draft job posting

## Triggers

- Second phase of job description workflow
- Research insights available and ready to draft posting
