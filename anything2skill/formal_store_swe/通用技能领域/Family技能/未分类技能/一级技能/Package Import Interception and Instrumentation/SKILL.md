---
id: "5cb1141a-bd9a-5686-a22e-969b744a44a8"
name: "Package Import Interception and Instrumentation"
description: "Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code."
version: "0.1.0"
tags:
  - "import_interception"
  - "instrumentation"
  - "observability"
  - "runtime_initialization"
  - "package_monitoring"
  - "agent_ops"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "AgentOps runtime initialization begins"
  - "User code imports a monitored package (e.g., LLM client, memory system, concurrent execution library)"
examples:
  - input: "User code: import openai"
    output: "openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored."
    notes: "Standard case: package name matches PROVIDERS registry exactly."
  - input: "User code: from google.adk import something"
    output: "google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored."
    notes: "Nested package case: fromlist item is combined with parent name to form full candidate."
  - input: "User code: import mem0; then import concurrent.futures"
    output: "mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active."
    notes: "Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency."
---

# Package Import Interception and Instrumentation

Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code.

## Prompt

When AgentOps runtime initializes, install an import monitor that intercepts all module imports. For each import, check if the package matches a configured instrumentor target. If matched and not already instrumented, instantiate the appropriate instrumentor and register it. Handle special cases (e.g., concurrent.futures when mem0 is instrumented). Skip instrumentation if an agentic library is already active to prevent double-instrumentation.

## Objective

Transparently instrument third-party packages at import time without modifying user code
## Applicable Signals

- Runtime startup signal
- Module import event intercepted by custom import hook
- Package name matches configured PROVIDERS or AGENTIC_LIBRARIES registry

## Contraindications

- User explicitly disables instrumentation via configuration
- An agentic library is already instrumented (flag _has_agentic_library is True)
- Package is already in _instrumenting_packages or marked as instrumented

## Workflow Steps

- {'step': 1, 'action': 'Install custom import monitor', 'detail': 'Replace built-in __import__ with _import_monitor function to intercept all module imports'}
- {'step': 2, 'action': 'Check agentic library flag', 'detail': 'If _has_agentic_library is True, delegate to original import and skip instrumentation'}
- {'step': 3, 'action': 'Perform actual import', 'detail': 'Call _original_builtins_import to load the module normally'}
- {'step': 4, 'action': 'Identify matching packages', 'detail': 'Check imported name and fromlist items against PROVIDERS and AGENTIC_LIBRARIES registries; build set of packages_to_check'}
- {'step': 5, 'action': 'Instrument matching packages', 'detail': 'For each package in packages_to_check: verify not already instrumented, retrieve config, instantiate InstrumentorLoader, call instrument_one, register in _active_instrumentors'}
- {'step': 6, 'action': 'Handle special cases', 'detail': "If package_name is 'mem0' and newly added, also instrument concurrent.futures with concurrent_config"}
- {'step': 7, 'action': 'Return instrumented module', 'detail': 'Return the module object to caller; instrumentation is now active for subsequent calls'}

## Constraints

- Must preserve original import behavior; return the actual module object after instrumentation
- Must check version compatibility before instantiating instrumentor
- Must handle optional package_name field in InstrumentorLoader config
- Must detect and handle special cases (e.g., concurrent.futures dependency on mem0)

## Cautions

- Double-instrumentation can cause performance degradation or conflicting hooks; enforce single-instrumentation per package
- Import interception is global; ensure no circular dependencies or import-time side effects break the chain
- Version mismatches between instrumentor and target package may cause runtime errors; validate min_version before instantiation

## Output Contract

- Target packages are instrumented and registered in _active_instrumentors; the original module object is returned to the caller; subsequent calls to instrumented packages are monitored and logged by AgentOps.

## Example Executions

### Example 1

- Input: User code: import openai
- Output: openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored.
- Notes: Standard case: package name matches PROVIDERS registry exactly.

### Example 2

- Input: User code: from google.adk import something
- Output: google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored.
- Notes: Nested package case: fromlist item is combined with parent name to form full candidate.

### Example 3

- Input: User code: import mem0; then import concurrent.futures
- Output: mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active.
- Notes: Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency.

## 子技能目录
- [AgentOps Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Integration Setup/SKILL.md) ｜ 适用：Scaffold for integrating AgentOps monitoring and debugging into AI/ML projects. Use when starting a new agent project or adding observability to an existing framework.
- [AgentOps Session Lifecycle Management](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Session Lifecycle Management/SKILL.md) ｜ 适用：Initialize and terminate an AgentOps observability session, wrapping agent or LLM interactions for end-to-end tracking and debugging.
- [Assemble and Retrieve Tracing Client Instance](通用技能领域/Family技能/未分类技能/二级技能/Assemble and Retrieve Tracing Client Instance/SKILL.md) ｜ 适用：Construct a complete initialization parameter dictionary from user inputs and configuration, then retrieve or create a singleton client instance for tracing operations.
- [CamelAI Agent Tracking Setup](通用技能领域/Family技能/未分类技能/二级技能/CamelAI Agent Tracking Setup/SKILL.md) ｜ 适用：Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity tracking and monitoring.
- [Cohere SDK Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/Cohere SDK Integration Setup/SKILL.md) ｜ 适用：Install and configure AgentOps with Cohere SDK (version >=5.4.0) to enable agent monitoring and observability for Cohere-based applications.
- [Conditional Package Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Conditional Package Instrumentation/SKILL.md) ｜ 适用：Evaluates whether a package should be instrumented based on eligibility checks and prior state, then loads and instantiates the appropriate instrumentor. Handles special cases such as dependent package instrumentation (e.g., concurrent.futures when mem0 is instrumented).
- [Decorator-based Observability Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Decorator-based Observability Instrumentation/SKILL.md) ｜ 适用：Apply decorator patterns (@workflow, @agent, @operation) to instrument functions and classes with observability spans, enabling hierarchical tracing of agent execution with minimal code overhead.
- [Initialize Package Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Initialize Package Instrumentation/SKILL.md) ｜ 适用：Start monitoring and instrumenting Python packages using import hooks if not already active. Prevents duplicate instrumentation and respects agentic library precedence by checking _has_agentic_library flag and _active_instrumentors collection.
- [Jakarta EE Package Import Migration](通用技能领域/Family技能/未分类技能/二级技能/Jakarta EE Package Import Migration/SKILL.md) ｜ 适用：Initialize and configure the AgentOps SDK by importing core tracing decorators, semantic conventions, and client infrastructure. Establishes the public API surface for agent instrumentation and tracing context setup.
- [LiteLLM Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LiteLLM Integration Setup/SKILL.md) ｜ 适用：Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ LLMs through a standardized Input/Output interface.
- [Notebook-Based Integration Testing for LLM Providers](通用技能领域/Family技能/未分类技能/二级技能/Notebook-Based Integration Testing for LLM Providers/SKILL.md) ｜ 适用：Execute Jupyter notebooks as integration tests to verify end-to-end LLM provider functionality, real-world usage patterns, and API compatibility across multiple Python versions. Notebooks are located in examples/ directory, executed via CI workflow on PR merges and manual triggers, with provider API keys configured in GitHub Actions secrets.
- [Standard Metrics Recording](通用技能领域/Family技能/未分类技能/二级技能/Standard Metrics Recording/SKILL.md) ｜ 适用：Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumented operations.
- [Third-Party Script Performance Optimization](通用技能领域/Family技能/未分类技能/二级技能/Third-Party Script Performance Optimization/SKILL.md) ｜ 适用：Set up AgentOps client in 2 lines of code to automatically capture and replay LLM call analytics and session traces.
- [Time Format and Parse Operations](通用技能领域/Family技能/未分类技能/二级技能/Time Format and Parse Operations/SKILL.md) ｜ 适用：Automates extraction of Jupyter notebook content and conversion to Markdown documentation with frontmatter, metadata, and MDX file generation for website publishing.
- [Trace and Tag Workflow Execution](通用技能领域/Family技能/未分类技能/二级技能/Trace and Tag Workflow Execution/SKILL.md) ｜ 适用：Decorator-based pattern to wrap a workflow function with execution tracing, naming, and semantic tags for observability and workflow discovery.

## 选用规则（二级技能目录）
- 当目标、阶段或方法更接近 `AgentOps Integration Setup` 时，优先调用它。 线索：Starting new AI/ML agent project, Adding debugging or monitoring to existing codebase, Evaluating AgentOps capabilities for observability, observability, agent_monitoring
- 当目标、阶段或方法更接近 `AgentOps Session Lifecycle Management` 时，优先调用它。 线索：starting an agent or multi-step LLM workflow that requires end-to-end observability, debugging logs, or audit trail, observability, session_management, debugging, audit_trail
- 当目标、阶段或方法更接近 `Assemble and Retrieve Tracing Client Instance` 时，优先调用它。 线索：Starting a new tracing session, Resuming an existing tracing session, All configuration parameters (API key, endpoint, tags, queue settings) are available, initialization, client_factory
- 当目标、阶段或方法更接近 `CamelAI Agent Tracking Setup` 时，优先调用它。 线索：Starting a new CamelAI agent project, Adding observability to an existing CamelAI system, Enabling agent activity monitoring for CamelAI-based agents, agent_integration, camelai
- 当目标、阶段或方法更接近 `Cohere SDK Integration Setup` 时，优先调用它。 线索：Starting a new Cohere-based agent project, Adding AgentOps monitoring to an existing Cohere application, integration, cohere, agentops
- 当目标、阶段或方法更接近 `Conditional Package Instrumentation` 时，优先调用它。 线索：Package import is detected via _import_monitor, Package name is not yet in _instrumenting_packages, Package is not already marked as instrumented, instrumentation, package_loading
- 当目标、阶段或方法更接近 `Decorator-based Observability Instrumentation` 时，优先调用它。 线索：Adding tracing to agent workflows, Instrumenting nested operations in class-based agents, Requiring minimal code changes for observability, Need for hierarchical span hierarchy in agent execution, observability
- 当目标、阶段或方法更接近 `Initialize Package Instrumentation` 时，优先调用它。 线索：AgentOps monitoring needs to begin, _active_instrumentors is empty, No agentic library is already instrumented, instrumentation, import_hook
- 当目标、阶段或方法更接近 `Jakarta EE Package Import Migration` 时，优先调用它。 线索：Upgrading Spring Boot 2.x application to 3.0, Jakarta EE 10 dependencies added to project, Import statements reference javax packages, initialization, sdk_setup
- 当目标、阶段或方法更接近 `LiteLLM Integration Setup` 时，优先调用它。 线索：Starting a new AgentOps project requiring multi-LLM support, Switching from direct LLM calls to unified LiteLLM interface, Need to abstract multiple LLM providers behind a single API, integration, litellm
- 当目标、阶段或方法更接近 `Notebook-Based Integration Testing for LLM Providers` 时，优先调用它。 线索：Adding or updating LLM provider support, Running CI/CD on PR merges to main, Verifying provider API compatibility across Python versions, integration_testing, llm_providers
- 当目标、阶段或方法更接近 `Standard Metrics Recording` 时，优先调用它。 线索：Need to record token usage and duration metrics across multiple operations, Using OpenTelemetry meter for observability, Want standardized metric names and types across instrumentations, observability, metrics
- 当目标、阶段或方法更接近 `Third-Party Script Performance Optimization` 时，优先调用它。 线索：application integrates analytics scripts, application integrates tracking scripts, application integrates vendor scripts, page performance metrics show script-related bottlenecks, setup
- 当目标、阶段或方法更接近 `Time Format and Parse Operations` 时，优先调用它。 线索：Need to format Date objects to strings or parse time strings to Date objects; working with locale-specific or UTC timestamps, documentation, notebook, markdown, mdx
- 当目标、阶段或方法更接近 `Trace and Tag Workflow Execution` 时，优先调用它。 线索：Defining a reusable workflow that spans multiple agent operations, Need for observability, replay, or semantic categorization of workflow execution, Workflow involves coordinated multi-step operations requiring traceability, workflow, tracing

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- AgentOps runtime initialization begins
- User code imports a monitored package (e.g., LLM client, memory system, concurrent execution library)

## Examples

### Example 1

Input:

  User code: import openai

Output:

  openai module is loaded, InstrumentorLoader for openai is instantiated with config from PROVIDERS, instrumentor is registered in _active_instrumentors, openai module is returned to user code. Subsequent openai.ChatCompletion.create() calls are now monitored.

Notes:

  Standard case: package name matches PROVIDERS registry exactly.

### Example 2

Input:

  User code: from google.adk import something

Output:

  google module is imported, full_item_name_candidate 'google.adk' is checked against registries, InstrumentorLoader for google.adk is instantiated if found, instrumentor is registered, module is returned. Subsequent google.adk calls are monitored.

Notes:

  Nested package case: fromlist item is combined with parent name to form full candidate.

### Example 3

Input:

  User code: import mem0; then import concurrent.futures

Output:

  mem0 is instrumented and registered. Because package_name == 'mem0' and is_newly_added, concurrent.futures is also instrumented with concurrent_config. Both instrumentors are active.

Notes:

  Special case: mem0 triggers automatic instrumentation of concurrent.futures dependency.
