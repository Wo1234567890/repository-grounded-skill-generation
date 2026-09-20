---
id: "2fcf2c8c-ee2d-5471-a738-db6f6386065f"
name: "未分类技能"
description: "未分类技能 的总导航技能：汇总适用场景、总流程、子技能地图与选用规则。"
version: "0.1.0"
tags:
  - "未分类技能"
  - "总导航"
  - "子技能地图"
  - "kind:parent"
  - "profile:default::未分类技能"
triggers:
  - "未分类技能"
  - "未分类技能 总导航"
  - "未分类技能 子技能地图"
---

# 未分类技能

未分类技能 的总导航技能：汇总适用场景、总流程、子技能地图与选用规则。

## Prompt

## 适用场景
- 当当前问题明确属于或需要路由到 未分类技能 时，先使用本总技能决定子技能选择顺序。
- 本技能用于导航与组合，不替代子技能中的具体执行 SOP。

## 不适用/风险边界
- 不要把本技能当作具体干预脚本；真正执行时必须继续调用对应子技能。
- 如存在明显高风险或危机信号，应优先调用风险/危机类子技能。

## 总流程
1. 先判断当前问题是否适合进入该家族或领域的处理路径。
2. 再根据任务类型、阶段和风险边界选择最合适的子技能。
3. 调用对应子技能执行具体步骤、规则和输出格式。
4. 最后输出所选子技能、选择理由、执行顺序与风险提示。

## 子技能目录（一级技能目录）
- Access AgentOps Session Replay and Debugging Dashboard ｜ 类型：agent_debugging ｜ 适用条件：Retrieve and review recorded agent session execution history, decision logs, and summary analytics through the AgentOps dashboard for post-execution analysis and troubleshooting.
- Agent Design Pattern Selection ｜ 类型：agent_design ｜ 适用条件：Identify and reference appropriate agent design patterns for a given use case. Provides access to catalog of reusable patterns across multiple frameworks (LangChain, CrewAI, OpenAI Agents, SmolAgents, Google Gemini, LiteLLM, Watsonx, xAI) covering single-agent and multi-agent scenarios, tool orchestration, human-in-the-loop workflows, and domain-specific conversions.
- AgentOps Client Configuration Reference ｜ 类型：client_setup ｜ 适用条件：Reference documentation of all supported AgentOps client configuration parameters, their purposes, and valid usage patterns. Provides a mapping of parameter names to their purposes and constraints to support integration planning and troubleshooting.
- Camel AI AgentOps Integration Setup ｜ 类型：agent_framework_integration ｜ 适用条件：Canonical skill for setting up AgentOps observability with Camel AI agents. Provides reference materials, integration patterns, and setup procedures to enable full agent tracking and analysis.
- InstrumentorLoader Configuration and Instantiation ｜ 类型：instrumentation ｜ 适用条件：Encapsulates metadata and instantiation logic for dynamically loading instrumentor classes. Provides a reusable dataclass and factory pattern that stores module name, class name, minimum version, and optional package name mapping for later instrumentor creation with version validation.
- LLM Provider Instrumentation Compatibility Lookup ｜ 类型：instrumentation_compatibility ｜ 适用条件：Reference skill for verifying LLM provider support and minimum version requirements before planning OpenTelemetry instrumentation integration. Provides static compatibility matrix to confirm whether a target provider can be instrumented and what minimum library version is required.
- Package Import Interception and Instrumentation ｜ 类型：instrumentation ｜ 适用条件：Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code.
- Provider Test Coverage Specification ｜ 类型：test_planning ｜ 适用条件：Reference checklist defining required functionality demonstrations for LLM provider test notebooks. Specifies what capabilities each provider notebook must cover to ensure complete integration testing across basic completion, streaming, async operations, error handling, and tool usage.
- Semantic Span Kind Reference ｜ 类型：instrumentation_taxonomy ｜ 适用条件：Canonical enumeration and mapping of semantic span kinds (AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP) used to classify instrumentation points in agent systems. Provides taxonomy for selecting appropriate decorators and instrumentation classification.
- Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator ｜ 类型：framework_upgrade ｜ 适用条件：Orchestrates a multi-phase, staged migration of Spring Boot applications from 2.7.x to 3.0, covering pre-upgrade validation, core upgrade execution, and post-upgrade verification. Ensures safe handling of Java 17+ requirement, Jakarta EE namespace migration, Spring Framework 6.0 API changes, and dependency compatibility.
- TicToc Concurrency Control Protocol ｜ 类型：transaction_concurrency_control ｜ 适用条件：Multi-stage protocol for building reusable API instrumentation modules that wrap third-party service calls with consistent error handling, async support, and semantic attribute capture. Establishes a cross-phase workflow from design through testing to ensure instrumentation consistency across multiple service integrations.
- Understand Iterator Data Sink for Testing ｜ 类型：testing ｜ 适用条件：Reference schema for organizing agent execution activities into a six-level hierarchical span structure (SESSION → AGENT → WORKFLOW → OPERATION/TASK → LLM → TOOL). Use when designing tracing, logging, or debugging infrastructure for multi-level agent workflows.

## 选用规则（一级技能目录）
- 当问题命中“Investigating agent behavior anomalies, understanding decision paths, or validating agent outputs after session completion、debugging、observability、session_analysis”这类线索时，优先选择 Access AgentOps Session Replay and Debugging Dashboard。
- 当问题命中“Designing a new agent from scratch、Need to understand common agent patterns and best practices、Looking for a template or example for a specific use case、agent_design”这类线索时，优先选择 Agent Design Pattern Selection。
- 当问题命中“Developer needs to understand available configuration options during AgentOps client initialization、Integration planning phase requires parameter reference、Troubleshooting client behavior requires understanding configuration contract、configuration”这类线索时，优先选择 AgentOps Client Configuration Reference。
- 当问题命中“Developer needs to understand Camel AI integration patterns、Setup procedures for AgentOps with Camel AI are required、Troubleshooting guidance for Camel AI agent tracking is needed、integration”这类线索时，优先选择 Camel AI AgentOps Integration Setup。
- 当问题命中“Instrumentor configuration needs to be stored, validated, or instantiated dynamically、instrumentation、loader、configuration”这类线索时，优先选择 InstrumentorLoader Configuration and Instantiation。
- 当问题命中“Caller needs to verify if a specific LLM provider can be instrumented、Caller must check minimum version requirements before integration、Caller is planning instrumentation scope and needs provider support confirmation、instrumentation”这类线索时，优先选择 LLM Provider Instrumentation Compatibility Lookup。
- 当问题命中“AgentOps runtime initialization begins、User code imports a monitored package (e.g., LLM client, memory system, concurrent execution library)、import_interception、instrumentation”这类线索时，优先选择 Package Import Interception and Instrumentation。
- 当问题命中“Creating a new provider notebook、Reviewing provider test completeness、Onboarding new LLM integrations、testing”这类线索时，优先选择 Provider Test Coverage Specification。
- 当问题命中“Selecting or defining instrumentation decorators、Need to understand what span kinds are available and their semantics、instrumentation、span_classification”这类线索时，优先选择 Semantic Span Kind Reference。
- 当问题命中“Planning or executing a Spring Boot version upgrade from 2.7.x line to 3.0 or later、spring-boot、version-upgrade、migration”这类线索时，优先选择 Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator。
- 当问题命中“High-concurrency OLTP workload detected、Variable contention levels across transaction mix、Need to compare concurrency control protocols、In-memory database transaction management required”这类线索时，优先选择 TicToc Concurrency Control Protocol。
- 当问题命中“collecting and inspecting DataStream results for validation、designing test assertions、debugging DataStream output、observability”这类线索时，优先选择 Understand Iterator Data Sink for Testing。

## 输出格式
- family_route:
  - family: 未分类技能
  - selected_children: [子技能名称列表]
  - rationale: 说明为什么选择这些子技能
  - cautions: 风险边界与切换条件

## Files

- `references/children_manifest.json`
- `references/children_map.md`

## Triggers

- 未分类技能
- 未分类技能 总导航
- 未分类技能 子技能地图
