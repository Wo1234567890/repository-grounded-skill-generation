---
id: "a22bec4f-6c88-51ba-8d89-6d1fe474d415"
name: "LLM Interaction Inspection"
description: "Retrieve and display detailed LLM prompt and completion content from a specific agent interaction for debugging and validation purposes."
version: "0.1.0"
tags:
  - "agent_debugging"
  - "llm_inspection"
  - "message_view"
  - "prompt_validation"
triggers:
  - "Debugging unexpected agent behavior or validating LLM output quality; select Message View in dashboard."
---

# LLM Interaction Inspection

Retrieve and display detailed LLM prompt and completion content from a specific agent interaction for debugging and validation purposes.

## Prompt

Select the Message View in the AgentOps dashboard to inspect a specific LLM interaction. Locate the target interaction by session or timestamp, then retrieve and examine the full prompt text and completion response.

## Objective

Inspect LLM prompt and completion
## Applicable Signals

- Unexpected agent behavior detected
- Need to validate LLM output quality
- Investigating specific interaction outcome
- Caller selects Message View in dashboard

## Contraindications

- Analyzing aggregate metrics across sessions
- Generating high-level session overview
- Reviewing timeline or hierarchical span relationships

## Workflow Steps

- Navigate to AgentOps dashboard
- Select Message View from available visualization options
- Locate target LLM interaction by session, timestamp, or operation ID
- Retrieve and display full prompt text
- Retrieve and display full completion response
- Examine content for debugging or validation

## Constraints

- Requires access to AgentOps dashboard
- Target interaction must exist in session history
- Message View must be available in dashboard UI

## Cautions

- Large prompt or completion content may require scrolling or export
- Sensitive data in prompts or completions should be handled per security policy

## Output Contract

- Detailed prompt and completion text displayed for the selected LLM interaction; caller receives full message content ready for analysis.

## Triggers

- Debugging unexpected agent behavior or validating LLM output quality; select Message View in dashboard.
