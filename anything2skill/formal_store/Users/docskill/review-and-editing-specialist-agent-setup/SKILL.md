---
id: "a78e3bad-23f4-5442-80e2-49a49c4ba754"
name: "Review and Editing Specialist Agent Setup"
description: "Configures a review agent with web search, Serper, and file read tools to refine job postings for clarity, grammar, engagement, and company value alignment. Invoke as final stage to polish and validate job description."
version: "0.1.0"
tags:
  - "job_description"
  - "review"
  - "editing"
  - "quality_assurance"
  - "agent_configuration"
  - "multi_tool"
triggers:
  - "Job description draft complete; quality assurance and refinement needed"
---

# Review and Editing Specialist Agent Setup

Configures a review agent with web search, Serper, and file read tools to refine job postings for clarity, grammar, engagement, and company value alignment. Invoke as final stage to polish and validate job description.

## Prompt

Initialize a Review and Editing Specialist agent with the following configuration:
- Role: Review and Editing Specialist
- Goal: Review the job posting for clarity, engagement, grammatical accuracy, and alignment with company values; refine to ensure perfection
- Tools: web_search_tool, serper_dev_tool, file_read_tool
- Backstory: A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect
- Verbose mode: enabled

The agent should validate the draft job posting against quality criteria: clarity of language, grammatical correctness, engagement level, and alignment with stated company values.

## Objective

Ensure job posting clarity, grammatical accuracy, and company alignment
## Applicable Signals

- Job description draft completed by writer agent
- Quality assurance and refinement needed
- Final polish before publication required

## Contraindications

- Job posting already published
- No further edits required
- Draft not yet completed by prior stages

## Intervention Moves

- Initialize agent with review specialist role and tools
- Execute review pass on draft job posting
- Validate clarity, grammar, engagement, and company value alignment
- Return refined posting to caller

## Workflow Steps

- Receive job description draft from writer agent
- Initialize Review and Editing Specialist agent with web_search_tool, serper_dev_tool, and file_read_tool
- Execute review pass validating clarity, grammar, engagement, and company value alignment
- Generate refined job posting with corrections and enhancements
- Return polished posting ready for publication

## Constraints

- Agent must have access to file_read_tool pointing to job description draft
- Web search and Serper tools must be functional for reference lookups
- Review must complete before publication handoff

## Cautions

- Ensure draft is available before invoking this agent
- Review output should be validated by human stakeholder before final publication

## Output Contract

- Polished, error-free job posting aligned with company values and ready for publication; includes clarity improvements, grammatical corrections, and engagement enhancements

## Triggers

- Job description draft complete; quality assurance and refinement needed
