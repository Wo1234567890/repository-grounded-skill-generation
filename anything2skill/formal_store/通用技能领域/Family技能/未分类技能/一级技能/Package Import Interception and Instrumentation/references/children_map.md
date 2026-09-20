# Package Import Interception and Instrumentation 子技能地图

## 子技能列表

- [CommonInstrumentor Configuration and Wrapping](通用技能领域/Family技能/未分类技能/二级技能/CommonInstrumentor Configuration and Wrapping/SKILL.md) ｜ 二级技能
  - 适用：Configure and instantiate a CommonInstrumentor with InstrumentorConfig and WrapConfig to create reusable instrumentation templates for LLM providers and agentic frameworks.
  - 线索：Adding support for a new LLM provider (OpenAI, Anthropic, Google GenAI, IBM WatsonX, etc.), Adding support for a new agentic framework (CrewAI, AutoGen, Agno, Mem0, smolagents, etc.), A standardized instrumentation pattern is needed for telemetry collection, instrumentation, opentelemetry
- [Conditional Package Instrumentation Dispatch](通用技能领域/Family技能/未分类技能/二级技能/Conditional Package Instrumentation Dispatch/SKILL.md) ｜ 二级技能
  - 适用：Routes a detected package import to the correct instrumentor configuration by consulting the PROVIDERS or AGENTIC_LIBRARIES registry, validates instrumentation eligibility, and instantiates the appropriate InstrumentorLoader with version checking. Handles special-case cascading (e.g., mem0 → concurrent.futures).
  - 线索：Package name detected in import statement, Import monitor (_import_monitor) intercepts a module load, instrumentation, package_detection, import_monitoring
- [Decorator-Based Observability Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Decorator-Based Observability Instrumentation/SKILL.md) ｜ 二级技能
  - 适用：Apply Python decorators (@workflow, @agent, @operation) to functions and classes to automatically capture execution spans and observability data with minimal code overhead.
  - 线索：Developer needs to add observability to a workflow function, Agent class requires execution span capture, Operation method needs automatic instrumentation, observability, instrumentation
- [Entity Decorator Factory Pattern](通用技能领域/Family技能/未分类技能/二级技能/Entity Decorator Factory Pattern/SKILL.md) ｜ 二级技能
  - 适用：Factory-based system for creating reusable decorators that instrument agent operations (agents, tasks, workflows, tools, guardrails, HTTP endpoints) with semantic span kinds for observability and tracing.
  - 线索：Initializing agent framework; need to instrument multiple entity types (agent, task, workflow, tool, guardrail, HTTP) with consistent span semantics, observability, instrumentation, decorator, factory_pattern
- [Package Instrumentation Initialization](通用技能领域/Family技能/未分类技能/二级技能/Package Instrumentation Initialization/SKILL.md) ｜ 二级技能
  - 适用：Conditionally start monitoring and instrumenting Python packages using import hooks, with safeguards to prevent redundant or conflicting instrumentation of agentic libraries.
  - 线索：AgentOps monitoring is first activated, No active instrumentors are currently running (_active_instrumentors is empty), Agentic library detection is needed to avoid double-instrumentation, instrumentation, initialization
