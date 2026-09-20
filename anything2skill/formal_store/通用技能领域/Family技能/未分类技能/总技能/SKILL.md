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
- InstrumentorLoader Configuration ｜ 类型：observability_instrumentation ｜ 适用条件：Encapsulates metadata and instantiation contract for dynamically loading instrumentor classes. Validates package version constraints and provides module name, class name, and minimum version required for safe instrumentation.
- Notebook-Based Integration Testing ｜ 类型：integration_testing ｜ 适用条件：Automated workflow to test LLM provider integrations using Jupyter notebooks as executable integration tests. Verifies real-world usage patterns and end-to-end functionality across multiple Python versions and actual LLM APIs.
- Package Import Interception and Instrumentation ｜ 类型：observability_instrumentation ｜ 适用条件：Intercepts Python module imports and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect and configure instrumentors for agentic libraries and their dependencies without modifying user code.
- Singleton Client Initialization with Re-initialization Guard ｜ 类型：client_lifecycle_management ｜ 适用条件：Enforces single-instance Client lifecycle per process. Detects and safely handles re-initialization attempts with different API keys by resetting state and ending active traces. Manages trace context lifecycle across initialization cycles.
- Spring Boot 2.x to 3.0 Instrumentation Migration Reference ｜ 类型：metrics_instrumentation ｜ 适用条件：Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system.
- Spring Boot 3.0 Migration Sequencing ｜ 类型：framework_upgrade ｜ 适用条件：Ordered macro-protocol for migrating a Spring Boot 2.7.x application to 3.0. Executes pre-flight validation (latest 2.7.x version, dependency review, system requirements), deprecation removal, and incremental upgrade steps with properties migration support.
- Understand Virtual Hub Routing Architecture ｜ 类型：network_routing_knowledge ｜ 适用条件：Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system. Consult the curated reference of supported frameworks (OpenAI, Anthropic, CrewAI, Langchain, Cohere, Mistral, LiteLLM, LlamaIndex, and others) with links to integration guides and official documentation.

## 选用规则（一级技能目录）
- 当问题命中“An instrumentor must be loaded dynamically and version constraints must be checked before instantiation、instrumentation、configuration、metadata”这类线索时，优先选择 InstrumentorLoader Configuration。
- 当问题命中“Adding or modifying LLM provider integrations、Running PR validation before merge to main、Ensuring example notebooks remain functional、integration_testing”这类线索时，优先选择 Notebook-Based Integration Testing。
- 当问题命中“Python application imports an agentic library (e.g., mem0, LangChain, AutoGen)、Import statement targets a package in PROVIDERS or AGENTIC_LIBRARIES registry、No agentic library instrumentation is currently active、import_hooking”这类线索时，优先选择 Package Import Interception and Instrumentation。
- 当问题命中“Client instantiation or __init__ call、Re-initialization attempt with different API key detected、Trace context lifecycle boundary crossed、singleton”这类线索时，优先选择 Singleton Client Initialization with Re-initialization Guard。
- 当问题命中“assessing Spring Boot 2.x instrumentation code for 3.0 compatibility; identifying which classes and patterns must be refactored、integration、observability、agent_framework”这类线索时，优先选择 Spring Boot 2.x to 3.0 Instrumentation Migration Reference。
- 当问题命中“Team is planning or executing a Spring Boot 2.7.x to 3.0 upgrade、spring-boot、migration、framework-upgrade”这类线索时，优先选择 Spring Boot 3.0 Migration Sequencing。
- 当问题命中“Learning virtual hub routing architecture、Planning routing policies for virtual hub、Troubleshooting routing behavior in hub、framework_selection”这类线索时，优先选择 Understand Virtual Hub Routing Architecture。

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
