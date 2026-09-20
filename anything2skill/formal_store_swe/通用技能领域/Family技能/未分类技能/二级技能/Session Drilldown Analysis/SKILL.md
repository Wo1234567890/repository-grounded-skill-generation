---
id: "8b033f5e-712b-5e4c-86e8-5fdb401f8479"
name: "Session Drilldown Analysis"
description: "Review and analyze a recorded agent session by examining LLM calls, action events, tool calls, errors, and execution timeline in a waterfall view. Use this to debug agent behavior and understand event sequences."
version: "0.1.0"
tags:
  - "debugging"
  - "session_analysis"
  - "agent_inspection"
  - "event_tracing"
  - "waterfall_view"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Need to understand what happened in a past agent execution"
  - "Require inspection of LLM prompts and completions"
  - "Tracing the sequence of events that led to an error or unexpected behavior"
---

# Session Drilldown Analysis

Review and analyze a recorded agent session by examining LLM calls, action events, tool calls, errors, and execution timeline in a waterfall view. Use this to debug agent behavior and understand event sequences.

## Prompt

Open the Session Drawer to locate a past session. Navigate to the Session Waterfall view. On the left side, examine the time visualization showing all LLM calls, Action events, Tool calls, and Errors in chronological order. Select specific events on the waterfall to view detailed information on the right panel, including exact prompts and completions for LLM calls. Review the chat history view of LLM calls and event breakdown charts to understand execution timing and event types.

## Objective

Inspect and diagnose a single recorded session to identify root causes of errors or unexpected behavior
## Applicable Signals

- Session execution completed and recorded
- Error or unexpected behavior observed in agent run
- Need for event-level detail retrieval

## Contraindications

- Comparing multiple sessions across time periods
- Generating aggregate metrics across sessions
- Analyzing cross-session patterns or trends

## Workflow Steps

- Locate and open the target session from the Session Drawer
- Navigate to Session Waterfall view
- Examine left-side time visualization of LLM calls, Action events, Tool calls, and Errors
- Select individual events on the waterfall timeline
- Review right-side event details panel for prompt, completion, and metadata
- Cross-reference with chat history view and event breakdown charts
- Identify root cause or unexpected behavior pattern

## Constraints

- Session must be previously recorded
- Waterfall view requires SDK version compatibility with supported agent frameworks (Crew, AutoGen)
- Event details are automatically captured; manual instrumentation not required

## Output Contract

- Clear identification of the event sequence
- Specific LLM call details including exact prompts and completions
- Root cause identification for any errors or unexpected behavior

## 子技能目录
- [Event listener management](通用技能领域/Family技能/未分类技能/微技能/Event listener management/SKILL.md) ｜ 适用：Collect and buffer streamed event data from an LLM response, checking for completion signals and concatenating text chunks until the stream terminates.
- [LLM Interaction Inspection](通用技能领域/Family技能/未分类技能/微技能/LLM Interaction Inspection/SKILL.md) ｜ 适用：Retrieve and display detailed LLM prompt and completion content from a specific agent interaction for debugging and validation purposes.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Event listener management` 时，优先调用它。 线索：Interactive element requires event response, User interaction must trigger a callback, streaming, llm_integration, response_handling
- 当目标、阶段或方法更接近 `LLM Interaction Inspection` 时，优先调用它。 线索：Debugging unexpected agent behavior or validating LLM output quality; select Message View in dashboard., agent_debugging, llm_inspection, message_view, prompt_validation

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Need to understand what happened in a past agent execution
- Require inspection of LLM prompts and completions
- Tracing the sequence of events that led to an error or unexpected behavior
