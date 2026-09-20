# Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator 子技能地图

## 子技能列表

- [Add Framework Example to Repository](通用技能领域/Family技能/未分类技能/二级技能/Add Framework Example to Repository/SKILL.md) ｜ 二级技能
  - 适用：Structured workflow for integrating a new framework or provider example into the AgentOps repository. Guides contributors through creating a self-contained, documented example, generating website-visible documentation, and submitting a pull request for review and merge.
  - 线索：Contributor has a working framework or provider example ready to share, New integration example needs to be added to the repository, Framework support is being extended with a new provider variant, repository_contribution, example_integration
- [Initialize AgentOps Client with API Keys](通用技能领域/Family技能/未分类技能/二级技能/Initialize AgentOps Client with API Keys/SKILL.md) ｜ 二级技能
  - 适用：Load environment variables for API authentication and initialize the AgentOps client with session configuration, trace naming, and metadata tags. This skill sets up an authenticated AgentOps session for agent tracing and monitoring before any agent execution begins.
  - 线索：Starting a new agent application that requires OpenAI and AgentOps integration, Before any agent execution or tracing begins, When environment variables are available and session is not yet initialized, initialization, authentication
- [Logarithmic Scale Configuration](通用技能领域/Family技能/未分类技能/二级技能/Logarithmic Scale Configuration/SKILL.md) ｜ 二级技能
  - 适用：Initialize AgentOps monitoring with automatic or manual session creation, associating all subsequent events and API calls with a tracking session.
  - 线索：Data spans multiple orders of magnitude, Logarithmic visual encoding is required, Tick labels and domain bounds need standardization, monitoring, session_management
- [Start Managed Trace with Context](通用技能领域/Family技能/未分类技能/二级技能/Start Managed Trace with Context/SKILL.md) ｜ 二级技能
  - 适用：Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback.
  - 线索：Starting a new logical trace or session, Need to attach tags or custom trace names to a trace, Require concurrent independent traces managed by caller, trace_management, session_lifecycle
