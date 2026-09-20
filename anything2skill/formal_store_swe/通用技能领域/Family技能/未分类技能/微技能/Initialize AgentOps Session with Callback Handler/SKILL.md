---
id: "fcc283e5-39e8-5411-815b-93730df3e8a8"
name: "Initialize AgentOps Session with Callback Handler"
description: "Set up AgentOps tracking by instantiating a LangchainCallbackHandler and attaching it to LLM and tool instances. This enables automatic session recording and span tracking for observability of agent workflows."
version: "0.1.0"
tags:
  - "observability"
  - "instrumentation"
  - "session_tracking"
  - "callback_handler"
  - "initialization"
  - "langchain"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Starting a new agent or LLM workflow"
  - "Requiring observability and session recording in AgentOps dashboard"
  - "Before agent kickoff or LLM instantiation"
examples:
  - input: "LLM instance (ChatOpenAI) and list of tools to be instrumented; optional tags list"
    output: "Handler attached to LLM and all tools; session recording active in AgentOps dashboard"
    notes: "Handler instantiation with tags enables easier session lookup in dashboard. Tool callbacks assignment is critical for tool usage tracking."
---

# Initialize AgentOps Session with Callback Handler

Set up AgentOps tracking by instantiating a LangchainCallbackHandler and attaching it to LLM and tool instances. This enables automatic session recording and span tracking for observability of agent workflows.

## Prompt

Create an AgentOps LangchainCallbackHandler instance, pass it to the LLM callbacks list, and attach it to each tool's callbacks. This must occur before agent execution begins. Optionally provide tags for session identification in the AgentOps dashboard.

## Objective

Enable AgentOps instrumentation for an agent session with automatic LLM call and tool usage tracking
## Applicable Signals

- Agent initialization phase
- LLM instance creation
- Tool registration

## Contraindications

- Running offline agents without external monitoring
- AgentOps API key unavailable or not configured
- Session recording explicitly disabled by caller

## Workflow Steps

- Import AgentOpsLangchainCallbackHandler from agentops.integration.callbacks.langchain
- Instantiate handler with optional tags parameter for session identification
- Pass handler instance to LLM callbacks parameter during ChatOpenAI or equivalent LLM instantiation
- Iterate through all tools and assign handler to each tool's callbacks attribute
- Proceed with agent execution; session recording begins automatically

## Constraints

- Handler must be instantiated before LLM creation
- Handler must be attached to all tools in the workflow
- API key or authentication credentials must be available and valid

## Cautions

- Ensure callback handler is passed to all tool instances, not just the LLM
- Verify API key is valid before session starts
- Handler must be assigned to both LLM callbacks parameter and each tool's callbacks attribute

## Output Contract

- AgentOps handler instance created and attached to LLM and all tools; session begins recording automatically with LLM calls and tool usage tracked in AgentOps dashboard; session can be verified programmatically via agentops module

## Example Executions

### Example 1

- Input: LLM instance (ChatOpenAI) and list of tools to be instrumented; optional tags list
- Output: Handler attached to LLM and all tools; session recording active in AgentOps dashboard
- Notes: Handler instantiation with tags enables easier session lookup in dashboard. Tool callbacks assignment is critical for tool usage tracking.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Starting a new agent or LLM workflow
- Requiring observability and session recording in AgentOps dashboard
- Before agent kickoff or LLM instantiation

## Examples

### Example 1

Input:

  LLM instance (ChatOpenAI) and list of tools to be instrumented; optional tags list

Output:

  Handler attached to LLM and all tools; session recording active in AgentOps dashboard

Notes:

  Handler instantiation with tags enables easier session lookup in dashboard. Tool callbacks assignment is critical for tool usage tracking.
