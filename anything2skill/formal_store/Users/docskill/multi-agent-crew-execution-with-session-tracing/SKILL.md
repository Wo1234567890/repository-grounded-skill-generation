---
id: "2a6551cd-1b78-5d7c-9cdb-030433a361ae"
name: "Multi-Agent Crew Execution with Session Tracing"
description: "Orchestrate multiple specialized agents in a crew workflow and record the complete execution trace with final state. Coordinates agent kickoff, captures results, and ends the session trace with success confirmation."
version: "0.1.0"
tags:
  - "multi-agent"
  - "crew"
  - "orchestration"
  - "session-tracing"
  - "agentops"
triggers:
  - "Multi-agent crew is ready for execution"
  - "Session tracing is enabled and tracer instance is available"
  - "All specialized agents have been initialized"
---

# Multi-Agent Crew Execution with Session Tracing

Orchestrate multiple specialized agents in a crew workflow and record the complete execution trace with final state. Coordinates agent kickoff, captures results, and ends the session trace with success confirmation.

## Prompt

1. Initialize your crew with multiple specialized agents (e.g., researcher, writer, reviewer).
2. Call crew.kickoff() to execute the coordinated workflow.
3. Capture the result output.
4. Call agentops.end_trace(tracer, end_state="Success") to finalize and record the session.
5. Return or log the final result for downstream processing.

## Objective

Execute coordinated multi-agent workflow and capture end-to-end session trace
## Applicable Signals

- crew object instantiated with multiple agents
- agentops tracer initialized
- agents assigned to crew roles

## Contraindications

- Single-agent workflows (use direct agent invocation instead)
- Real-time streaming required without trace buffering
- Tracer not initialized or session not started

## Intervention Moves

- Invoke crew.kickoff() to start coordinated execution
- Capture result from crew execution
- Call agentops.end_trace() with end_state parameter

## Workflow Steps

- {'step': 1, 'action': 'Initialize specialized agents', 'detail': 'Create researcher_agent, writer_agent, review_agent instances'}
- {'step': 2, 'action': 'Execute crew workflow', 'detail': 'Call crew.kickoff() to run coordinated multi-agent execution'}
- {'step': 3, 'action': 'Capture result', 'detail': 'Store result from crew.kickoff() for output'}
- {'step': 4, 'action': 'End session trace', 'detail': 'Call agentops.end_trace(tracer, end_state="Success")'}
- {'step': 5, 'action': 'Return final output', 'detail': 'Print or return result for downstream consumption'}

## Constraints

- Crew must be fully configured before kickoff
- AgentOps tracer must be active before crew execution
- end_trace() must be called after crew.kickoff() completes

## Cautions

- Ensure all agents in crew are properly initialized before kickoff
- Verify tracer instance is valid before calling end_trace()
- Handle exceptions during crew.kickoff() before calling end_trace()

## Output Contract

- Crew execution completed with final result captured and session trace ended with success state. Caller receives the result object from crew.kickoff() and confirmation that agentops.end_trace() was called.

## Triggers

- Multi-agent crew is ready for execution
- Session tracing is enabled and tracer instance is available
- All specialized agents have been initialized
