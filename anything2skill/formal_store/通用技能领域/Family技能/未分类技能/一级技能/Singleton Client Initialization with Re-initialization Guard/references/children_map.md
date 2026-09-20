# Singleton Client Initialization with Re-initialization Guard 子技能地图

## 子技能列表

- [Agent Cost and Spend Management](通用技能领域/Family技能/未分类技能/二级技能/Agent Cost and Spend Management/SKILL.md) ｜ 二级技能
  - 适用：Monitor and control spending on LLM and API calls to optimize agent operational costs and prevent budget overruns.
  - 线索：agent deployed to production, agent scaling to handle increased load, budget constraints or cost control requirements identified, need to track spend per session or per API call, cost_control
- [AgentOps SwarmZero Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/AgentOps SwarmZero Integration Setup/SKILL.md) ｜ 二级技能
  - 适用：Initialize AgentOps observability for SwarmZero multi-agent systems by setting environment credentials and configuring the integration. Enables full tracking of agent actions, decisions, and performance metrics.
  - 线索：Deploying SwarmZero agents to production or staging, Need to track agent actions, decisions, and performance metrics, Require centralized observability dashboard for multi-agent systems, agent_monitoring, swarmzero
- [Auto-start Trace Session Initialization](通用技能领域/Family技能/未分类技能/二级技能/Auto-start Trace Session Initialization/SKILL.md) ｜ 二级技能
  - 适用：Automatically initialize and start a tracing session when configured, registering exit handlers and creating trace contexts for observability.
  - 线索：System startup or client initialization, auto_start_session config is True, No active trace context exists or trace context is not recording, observability, tracing
- [LangChain Agent Integration with AgentOps Callback Handler](通用技能领域/Family技能/未分类技能/二级技能/LangChain Agent Integration with AgentOps Callback Handler/SKILL.md) ｜ 二级技能
  - 适用：Initialize and configure AgentOps callback handler for LangChain LLM instances to automatically record agent sessions, LLM calls, and tool usage.
  - 线索：Setting up a new LangChain LLM instance, Need to monitor and debug agent behavior via AgentOps dashboard, Integrating LangChain agents with observability infrastructure, langchain, agentops
- [ProcessPoolExecutor Initialization with Worker Setup](通用技能领域/Family技能/未分类技能/二级技能/ProcessPoolExecutor Initialization with Worker Setup/SKILL.md) ｜ 二级技能
  - 适用：Initializes the AgentOps SDK with environment variables or defaults when not yet initialized. Handles initialization failures gracefully by logging warnings and errors, returning None if initialization cannot proceed. Use this as a guard before starting traces to ensure SDK readiness.
  - 线索：Need to execute CPU-bound tasks with process isolation, Per-worker state setup required (e.g., database connections, shared resources), Worker processes must initialize before accepting tasks, sdk_initialization, error_handling
- [Start Trace with Context](通用技能领域/Family技能/未分类技能/二级技能/Start Trace with Context/SKILL.md) ｜ 二级技能
  - 适用：Initiates a new root span (trace) with a user-provided name and optional tags, returning a TraceContext object for concurrent, user-managed tracing sessions.
  - 线索：User wants to start a new logical trace for a session, task, or user interaction, Multiple concurrent traces are needed and must be user-managed, A new root span is required to organize related observability events, tracing, observability
- [Trace Lifecycle Management](通用技能领域/Family技能/未分类技能/二级技能/Trace Lifecycle Management/SKILL.md) ｜ 二级技能
  - 适用：Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle.
  - 线索：Agent execution begins and requires trace initialization, Metadata needs to be attached to a running trace, Trace state must be finalized at agent execution end, trace_management, agent_debugging
