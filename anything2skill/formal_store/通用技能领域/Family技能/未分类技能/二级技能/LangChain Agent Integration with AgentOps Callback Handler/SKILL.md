---
id: "9414dd2d-c870-517a-bca5-3f031cafdbe2"
name: "LangChain Agent Integration with AgentOps Callback Handler"
description: "Initialize and configure AgentOps callback handler for LangChain LLM instances to automatically record agent sessions, LLM calls, and tool usage."
version: "0.1.0"
tags:
  - "langchain"
  - "agentops"
  - "callback_handler"
  - "agent_monitoring"
  - "observability"
  - "integration"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Setting up a new LangChain LLM instance"
  - "Need to monitor and debug agent behavior via AgentOps dashboard"
  - "Integrating LangChain agents with observability infrastructure"
---

# LangChain Agent Integration with AgentOps Callback Handler

Initialize and configure AgentOps callback handler for LangChain LLM instances to automatically record agent sessions, LLM calls, and tool usage.

## Prompt

Before creating your LangChain LLM instance, import the AgentOpsLangchainCallbackHandler from agentops.integration.callbacks.langchain. Instantiate the handler with your API key and optional tags for session identification. Pass the handler instance to the LLM's callbacks parameter and to each tool's callbacks parameter. Bind tools to the LLM using llm.bind_tools(). Verify session recording by checking the AgentOps dashboard or programmatically inspecting recorded spans.

## Objective

Enable automatic session recording and monitoring of LangChain-based agents via AgentOps callback integration
## Applicable Signals

- LangChain ChatOpenAI or similar LLM instantiation
- Agent uses tools that require tracking
- Session-level debugging or audit trail needed

## Contraindications

- Using non-LangChain frameworks (e.g., CrewAI without LangChain adapter)
- Agent already has alternative monitoring or callback system in place
- AgentOps API key not available or service unavailable

## Workflow Steps

- {'step': 1, 'action': 'Import AgentOpsLangchainCallbackHandler from agentops.integration.callbacks.langchain'}
- {'step': 2, 'action': 'Instantiate handler with API key and optional tags: agentops_handler = AgentOpsLangchainCallbackHandler(tags=[...])'}
- {'step': 3, 'action': 'Create LLM instance with handler in callbacks: llm = ChatOpenAI(callbacks=[agentops_handler], model=...)'}
- {'step': 4, 'action': 'Define tools and assign handler to each: for t in tools: t.callbacks = [agentops_handler]'}
- {'step': 5, 'action': 'Bind tools to LLM: llm_with_tools = llm.bind_tools([...])'}
- {'step': 6, 'action': 'Execute agent workflow; session is recorded automatically'}
- {'step': 7, 'action': 'Verify session on AgentOps dashboard or via programmatic span inspection'}

## Constraints

- AgentOps API key must be provided to handler initialization
- Handler must be assigned to both LLM and all tools before execution
- LLM and tools must support callbacks parameter

## Cautions

- Ensure callback handler is instantiated before LLM creation to capture all calls
- Tool callbacks must be set explicitly; default tool binding does not inherit LLM callbacks
- Session recording begins immediately upon handler initialization; manage API quota accordingly

## Output Contract

- AgentOps session created and actively recording: LLM calls, tool invocations, agent state transitions, and execution traces are captured and accessible via AgentOps dashboard or API

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Setting up a new LangChain LLM instance
- Need to monitor and debug agent behavior via AgentOps dashboard
- Integrating LangChain agents with observability infrastructure
