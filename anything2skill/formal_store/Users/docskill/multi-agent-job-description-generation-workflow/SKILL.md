---
id: "597e46ee-c643-5724-8005-2d5c6b4a272f"
name: "Multi-Agent Job Description Generation Workflow"
description: "Orchestrates three specialized agents (Research Analyst, Job Description Writer, Review Specialist) in sequence to analyze company information, generate job postings, and refine them for quality and alignment with company values."
version: "0.1.0"
tags:
  - "multi_agent"
  - "job_posting"
  - "content_generation"
  - "workflow_orchestration"
  - "company_alignment"
triggers:
  - "User needs to create a job posting from company website and brief description"
  - "Multiple review cycles are acceptable and desired for quality assurance"
  - "Company culture and values alignment is a priority"
---

# Multi-Agent Job Description Generation Workflow

Orchestrates three specialized agents (Research Analyst, Job Description Writer, Review Specialist) in sequence to analyze company information, generate job postings, and refine them for quality and alignment with company values.

## Prompt

Initialize three agents with distinct roles and tools:
1. Research Analyst: Analyzes company website and description to extract insights on culture, values, and specific needs using web search and file read tools.
2. Job Description Writer: Uses research insights to create detailed, engaging job posting using web search, file read, and search tools.
3. Review Specialist: Reviews job posting for clarity, engagement, grammar, and company value alignment, then refines to ensure perfection.
Execute agents in sequence, passing outputs from Research to Writer, then Writer output to Review. Return finalized job posting from Review agent.

## Objective

Generate polished, company-aligned job postings through collaborative multi-agent workflow
## Applicable Signals

- Job posting creation request with company context provided
- Availability of company website or description document
- Time available for iterative refinement

## Contraindications

- Job description template already exists and only minor edits are needed
- Real-time job posting required with no iteration time available
- Company information sources are unavailable or inaccessible

## Workflow Steps

- {'step': 1, 'name': 'Initialize Tools', 'action': 'Create instances of WebsiteSearchTool, SerperDevTool, and FileReadTool with appropriate file path and description'}
- {'step': 2, 'name': 'Execute Research Agent', 'action': "Invoke research_agent with role 'Research Analyst' to analyze company website and description, extracting insights on culture, values, and specific needs"}
- {'step': 3, 'name': 'Execute Writer Agent', 'action': "Invoke writer_agent with role 'Job Description Writer' using research insights to create detailed, engaging job posting"}
- {'step': 4, 'name': 'Execute Review Agent', 'action': "Invoke review_agent with role 'Review and Editing Specialist' to review job posting for clarity, engagement, grammar, and company value alignment"}
- {'step': 5, 'name': 'Return Finalized Output', 'action': 'Return refined job posting from review agent as final deliverable'}

## Constraints

- All three agents must execute in sequence: Research → Writer → Review
- File read tool requires valid file path to job description or company information
- Web search tools (WebsiteSearchTool, SerperDevTool) must be initialized before agent execution
- Verbose mode enabled for transparency and debugging

## Cautions

- Ensure company website is accessible before initiating research agent
- Verify file paths are correct for file read tool initialization
- Review agent output should be treated as final; additional cycles require re-execution

## Output Contract

- Finalized job posting reviewed and refined for clarity, engagement, grammatical accuracy, and alignment with company values and culture. Output is ready for publication or further distribution.

## Triggers

- User needs to create a job posting from company website and brief description
- Multiple review cycles are acceptable and desired for quality assurance
- Company culture and values alignment is a priority
