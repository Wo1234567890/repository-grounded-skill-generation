# 未分类技能 子技能地图

- parent: `未分类技能/总技能/SKILL.md`

## 子技能列表

1. [Access AgentOps Session Replay and Debugging Dashboard](通用技能领域/Family技能/未分类技能/一级技能/Access AgentOps Session Replay and Debugging Dashboard/SKILL.md)
   - 层级：一级技能
   - 类型：agent_debugging
   - 适用条件：Retrieve and review recorded agent session execution history, decision logs, and summary analytics through the AgentOps dashboard for post-execution analysis and troubleshooting.
2. [Add Framework Example to Repository](通用技能领域/Family技能/未分类技能/二级技能/Add Framework Example to Repository/SKILL.md)
   - 层级：二级技能
   - 类型：repository_contribution
   - 适用条件：Structured workflow for integrating a new framework or provider example into the AgentOps repository. Guides contributors through creating a self-contained, documented example, generating website-visible documentation, and submitting a pull request for review and merge.
3. [Agent Design Pattern Selection](通用技能领域/Family技能/未分类技能/一级技能/Agent Design Pattern Selection/SKILL.md)
   - 层级：一级技能
   - 类型：agent_design
   - 适用条件：Identify and reference appropriate agent design patterns for a given use case. Provides access to catalog of reusable patterns across multiple frameworks (LangChain, CrewAI, OpenAI Agents, SmolAgents, Google Gemini, LiteLLM, Watsonx, xAI) covering single-agent and multi-agent scenarios, tool orchestration, human-in-the-loop workflows, and domain-specific conversions.
4. [Agent Failure Detection and Response](通用技能领域/Family技能/未分类技能/二级技能/Agent Failure Detection and Response/SKILL.md)
   - 层级：二级技能
   - 类型：agent_reliability
   - 适用条件：Identify, classify, and respond to agent failures and multi-agent interaction issues in real time. Monitors live agent sessions for anomalies, errors, and unexpected behavior, then triggers appropriate escalation or remediation actions.
5. [Agent Instantiation and Task Invocation](通用技能领域/Family技能/未分类技能/微技能/Agent Instantiation and Task Invocation/SKILL.md)
   - 层级：微技能
   - 类型：agent_execution
   - 适用条件：Creates a named agent instance and executes a single synchronous task method on it. Reusable pattern for spawning and executing agent operations within an active session context.
6. [Agent Operation Span Tracking](通用技能领域/Family技能/未分类技能/微技能/Agent Operation Span Tracking/SKILL.md)
   - 层级：微技能
   - 类型：observability_instrumentation
   - 适用条件：Decorator-based pattern to create an agent span for tracking individual agent operations and decisions within a session. Use when instrumenting specific agent actions or tool invocations to capture operation metadata and outcomes as distinct observability records.
7. [Agent Performance Observability Setup](通用技能领域/Family技能/未分类技能/二级技能/Agent Performance Observability Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_observability
   - 适用条件：Configure and enable comprehensive observability for AI agents, including performance tracking, user interaction logging, and API usage monitoring. Establishes the foundational instrumentation and data collection layer required for downstream analysis, cost control, and failure detection.
8. [Agent Session Observation via Dashboard](通用技能领域/Family技能/未分类技能/二级技能/Agent Session Observation via Dashboard/SKILL.md)
   - 层级：二级技能
   - 类型：agent_debugging
   - 适用条件：Execute an agent program and navigate to the AgentOps dashboard to observe real-time or post-run session activity. Use this to inspect agent behavior, logs, and outcomes after execution.
9. [Agent Step Execution and Response Handling](通用技能领域/Family技能/未分类技能/微技能/Agent Step Execution and Response Handling/SKILL.md)
   - 层级：微技能
   - 类型：agent_interaction
   - 适用条件：Execute a single step of agent reasoning with a user query and capture the structured response. Invoke this micro-skill when you need to run one agent reasoning cycle, pass a query string, and retrieve the output for logging or downstream processing.
10. [AgentOps Client Configuration Reference](通用技能领域/Family技能/未分类技能/一级技能/AgentOps Client Configuration Reference/SKILL.md)
   - 层级：一级技能
   - 类型：client_setup
   - 适用条件：Reference documentation of all supported AgentOps client configuration parameters, their purposes, and valid usage patterns. Provides a mapping of parameter names to their purposes and constraints to support integration planning and troubleshooting.
11. [AgentOps Client Configuration Validation](通用技能领域/Family技能/未分类技能/微技能/AgentOps Client Configuration Validation/SKILL.md)
   - 层级：微技能
   - 类型：client_setup
   - 适用条件：Validates incoming configuration parameters against a whitelist of supported AgentOps client settings, logging warnings for invalid parameters before client initialization.
12. [AgentOps Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Scaffold for integrating AgentOps monitoring and debugging into AI/ML projects. Use when starting a new agent project or adding observability to an existing framework.
13. [AgentOps SDK Initialization](通用技能领域/Family技能/未分类技能/二级技能/AgentOps SDK Initialization/SKILL.md)
   - 层级：二级技能
   - 类型：sdk_setup
   - 适用条件：Configures and initializes the AgentOps monitoring SDK with API credentials, session parameters, and instrumentation options to establish agent observability and session tracking.
14. [AgentOps Session Initialization](通用技能领域/Family技能/未分类技能/微技能/AgentOps Session Initialization/SKILL.md)
   - 层级：微技能
   - 类型：agent_setup
   - 适用条件：Initialize AgentOps with API key and session configuration, setting auto_start_session=False when session lifecycle is managed externally via decorators.
15. [AgentOps Session Lifecycle Management](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Session Lifecycle Management/SKILL.md)
   - 层级：二级技能
   - 类型：agent_observability
   - 适用条件：Initialize and terminate an AgentOps observability session, wrapping agent or LLM interactions for end-to-end tracking and debugging.
16. [Anthropic Message Creation with AgentOps Tracking](通用技能领域/Family技能/未分类技能/微技能/Anthropic Message Creation with AgentOps Tracking/SKILL.md)
   - 层级：微技能
   - 类型：agent_integration
   - 适用条件：Execute a single Claude API message call within an AgentOps-tracked session. Captures model interactions for debugging and monitoring multi-agent workflows.
17. [Anthropic Streaming Message Handler](通用技能领域/Family技能/未分类技能/微技能/Anthropic Streaming Message Handler/SKILL.md)
   - 层级：微技能
   - 类型：agent_integration
   - 适用条件：Consume streamed message tokens from Anthropic Claude API within an AgentOps session. Handles incremental token delivery for real-time agent response processing.
18. [API Key Presence Validation](通用技能领域/Family技能/未分类技能/二级技能/API Key Presence Validation/SKILL.md)
   - 层级：二级技能
   - 类型：credential_validation
   - 适用条件：Validates that an API key is present and non-empty in the Client configuration during initialization. Raises NoApiKeyException if the API key is missing, preventing Client initialization from completing without valid credentials.
19. [Application Performance Monitoring with OpenTelemetry](通用技能领域/Family技能/未分类技能/二级技能/Application Performance Monitoring with OpenTelemetry/SKILL.md)
   - 层级：二级技能
   - 类型：monitoring_and_observability
   - 适用条件：Choose and apply the appropriate test category (unit, integration, end-to-end, or performance) based on the scope and objective of the component or workflow being validated. This skill routes test design decisions to the correct category before fixture setup and data organization.
20. [Assemble and Retrieve Tracing Client Instance](通用技能领域/Family技能/未分类技能/二级技能/Assemble and Retrieve Tracing Client Instance/SKILL.md)
   - 层级：二级技能
   - 类型：session_initialization
   - 适用条件：Construct a complete initialization parameter dictionary from user inputs and configuration, then retrieve or create a singleton client instance for tracing operations.
21. [Async-Sync Method Wrapping](通用技能领域/Family技能/未分类技能/微技能/Async-Sync Method Wrapping/SKILL.md)
   - 层级：微技能
   - 类型：api_instrumentation
   - 适用条件：Micro-skill for wrapping both synchronous and asynchronous versions of an API method using wrapt.wrap_function_wrapper, ensuring consistent instrumentation across sync and async call paths.
22. [Bind Tools to LLM with Callback Tracking](通用技能领域/Family技能/未分类技能/微技能/Bind Tools to LLM with Callback Tracking/SKILL.md)
   - 层级：微技能
   - 类型：agent_instrumentation
   - 适用条件：Attach tool definitions to an LLM instance and ensure each tool has the AgentOps callback handler assigned so that tool invocations are recorded as observable spans during agent execution.
23. [Camel AI AgentOps Integration Setup](通用技能领域/Family技能/未分类技能/一级技能/Camel AI AgentOps Integration Setup/SKILL.md)
   - 层级：一级技能
   - 类型：agent_framework_integration
   - 适用条件：Canonical skill for setting up AgentOps observability with Camel AI agents. Provides reference materials, integration patterns, and setup procedures to enable full agent tracking and analysis.
24. [CamelAI Agent Tracking Setup](通用技能领域/Family技能/未分类技能/二级技能/CamelAI Agent Tracking Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity tracking and monitoring.
25. [Client Configuration Update](通用技能领域/Family技能/未分类技能/微技能/Client Configuration Update/SKILL.md)
   - 层级：微技能
   - 类型：configuration
   - 适用条件：Apply runtime configuration changes to an initialized client. Modify client behavior after instantiation without reinitializing.
26. [Cohere SDK Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/Cohere SDK Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：integration_setup
   - 适用条件：Install and configure AgentOps with Cohere SDK (version >=5.4.0) to enable agent monitoring and observability for Cohere-based applications.
27. [Collect Agent Runtime Environment Metadata](通用技能领域/Family技能/未分类技能/微技能/Collect Agent Runtime Environment Metadata/SKILL.md)
   - 层级：微技能
   - 类型：agent_diagnostics
   - 适用条件：Automatically gather and log basic system and SDK information (OS type/version, Python version, anonymized hostname, SDK version) from the agent execution environment for debugging and diagnostics.
28. [Conditional Package Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Conditional Package Instrumentation/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation
   - 适用条件：Evaluates whether a package should be instrumented based on eligibility checks and prior state, then loads and instantiates the appropriate instrumentor. Handles special cases such as dependent package instrumentation (e.g., concurrent.futures when mem0 is instrumented).
29. [Configure AgentOps Trace Session](通用技能领域/Family技能/未分类技能/微技能/Configure AgentOps Trace Session/SKILL.md)
   - 层级：微技能
   - 类型：agent_tracing
   - 适用条件：Set up an AgentOps trace session with custom trace name and metadata tags to enable monitoring and debugging of agent execution.
30. [Configure GitHub Actions Notebook Test Workflow](通用技能领域/Family技能/未分类技能/微技能/Configure GitHub Actions Notebook Test Workflow/SKILL.md)
   - 层级：微技能
   - 类型：ci_cd_configuration
   - 适用条件：Set up and maintain the test-notebooks.yml CI workflow to automatically execute Jupyter notebooks on pull requests, manage provider API secrets in the GitHub Actions environment, and exclude notebooks requiring manual testing.
31. [Configure Multiple Repository Sources](通用技能领域/Family技能/未分类技能/二级技能/Configure Multiple Repository Sources/SKILL.md)
   - 层级：二级技能
   - 类型：dependency_management
   - 适用条件：Workflow for selecting and navigating multiple dashboard views to analyze agent execution and performance metrics. Enables inspection of session behavior, execution flow tracing, and LLM interaction review across single or multiple sessions.
32. [Configure Page Metadata](通用技能领域/Family技能/未分类技能/二级技能/Configure Page Metadata/SKILL.md)
   - 层级：二级技能
   - 类型：metadata_configuration
   - 适用条件：Apply OpenTelemetry decorators to instrument functions and methods with automatic span creation and lifecycle management. Use when adding tracing to agent operations, tool calls, workflows, or endpoints without manual span control.
33. [Configure Pre-commit Hooks](通用技能领域/Family技能/未分类技能/微技能/Configure Pre-commit Hooks/SKILL.md)
   - 层级：微技能
   - 类型：code_quality
   - 适用条件：Install and activate pre-commit hooks for automated code quality checks before commits. Enforces code standards at the point of commit in a development environment.
34. [Convert Jupyter Notebooks to MDX Documentation](通用技能领域/Family技能/未分类技能/微技能/Convert Jupyter Notebooks to MDX Documentation/SKILL.md)
   - 层级：微技能
   - 类型：documentation_generation
   - 适用条件：Automated micro-skill to transform Jupyter notebooks into MDX-formatted documentation files. Handles frontmatter injection, GitHub link resolution, and conversion of pip install commands to CodeGroup format. Designed for batch processing example notebooks into a versioned documentation directory.
35. [Create OpenAI Instrumentation Metrics](通用技能领域/Family技能/未分类技能/微技能/Create OpenAI Instrumentation Metrics/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation_setup
   - 适用条件：Initialize a standardized metrics dictionary for OpenAI API instrumentation by invoking StandardMetrics.create_standard_metrics with a provided Meter instance. This skill is invoked during instrumentation setup to establish observability metrics collection.
36. [CrewAI Tool Integration Setup](通用技能领域/Family技能/未分类技能/微技能/CrewAI Tool Integration Setup/SKILL.md)
   - 层级：微技能
   - 类型：tool_provisioning
   - 适用条件：Import and instantiate CrewAI tools (WebsiteSearchTool, SerperDevTool, FileReadTool) with required configuration parameters. Prepares a multi-tool agent environment for task execution.
37. [Custom Reward Function Signature Compliance](通用技能领域/Family技能/未分类技能/微技能/Custom Reward Function Signature Compliance/SKILL.md)
   - 层级：微技能
   - 类型：reward_function_integration
   - 适用条件：Decorate Python functions with @operation to automatically create execution spans that track function calls, parameters, and return values for session visualization.
38. [D3 Scale Type Selection and Configuration](通用技能领域/Family技能/未分类技能/二级技能/D3 Scale Type Selection and Configuration/SKILL.md)
   - 层级：二级技能
   - 类型：data_encoding
   - 适用条件：Choose the appropriate scale type (linear, time, log, ordinal, band, sequential, diverging, quantile, quantize, threshold) based on data domain and range requirements, then configure its domain and range mappings to map data values to visual encoding channels.
39. [Dataset trace filtering and preparation](通用技能领域/Family技能/未分类技能/微技能/Dataset trace filtering and preparation/SKILL.md)
   - 层级：微技能
   - 类型：data_preparation
   - 适用条件：Inject or update structured metadata into an active trace session during agent or workflow execution to enrich observability and debugging context with operation name, processing stage, record counts, user context, and execution tags.
40. [Declare and Manage Local Variables](通用技能领域/Family技能/未分类技能/微技能/Declare and Manage Local Variables/SKILL.md)
   - 层级：微技能
   - 类型：state_management
   - 适用条件：Enable automatic monitoring and observability for CrewAI agents by setting the AGENTOPS_API_KEY environment variable. Minimal-overhead configuration that routes CrewAI crew execution data to the AgentOps dashboard without code modification.
41. [Decorate Workflow Function with Trace Metadata](通用技能领域/Family技能/未分类技能/微技能/Decorate Workflow Function with Trace Metadata/SKILL.md)
   - 层级：微技能
   - 类型：agent_instrumentation
   - 适用条件：Apply @trace decorator to a function with name and tags parameters to mark it as a traced workflow unit. Captures workflow execution context and enables filtering by metadata such as environment tags.
42. [Decorator Backward Compatibility Wrapper](通用技能领域/Family技能/未分类技能/微技能/Decorator Backward Compatibility Wrapper/SKILL.md)
   - 层级：微技能
   - 类型：api_migration
   - 适用条件：Provide a deprecated @session decorator that delegates to @trace for backward compatibility, handling both direct decoration and parameterized invocation patterns.
43. [Decorator-based Observability Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Decorator-based Observability Instrumentation/SKILL.md)
   - 层级：二级技能
   - 类型：observability_instrumentation
   - 适用条件：Apply decorator patterns (@workflow, @agent, @operation) to instrument functions and classes with observability spans, enabling hierarchical tracing of agent execution with minimal code overhead.
44. [Define Agent Class with Identity](通用技能领域/Family技能/未分类技能/微技能/Define Agent Class with Identity/SKILL.md)
   - 层级：微技能
   - 类型：agent_instantiation
   - 适用条件：Decorator-based pattern to define an agent class with a unique agent_id, enabling agent identity tracking and state management in multi-agent systems.
45. [Dependent Package Instrumentation Trigger](通用技能领域/Family技能/未分类技能/微技能/Dependent Package Instrumentation Trigger/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Automatically instruments dependent packages (e.g., concurrent.futures when mem0 is instrumented) to ensure complete observability of related execution contexts.
46. [Detect Installed Package vs Local Module](通用技能领域/Family技能/未分类技能/微技能/Detect Installed Package vs Local Module/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation_setup
   - 适用条件：Classify whether a Python module is an installed library (in site-packages) or a local development module by normalizing file paths and comparing against site-packages directories. Used during instrumentation initialization to decide whether to apply monitoring.
47. [Detect Jupyter Notebook Execution Context](通用技能领域/Family技能/未分类技能/微技能/Detect Jupyter Notebook Execution Context/SKILL.md)
   - 层级：微技能
   - 类型：environment_detection
   - 适用条件：Check whether code is running inside a Jupyter Notebook (ZMQInteractiveShell) and conditionally disable auto-start behavior for manual trace control. Returns a flag indicating the execution environment to enable environment-aware session initialization.
48. [Development Environment Setup](通用技能领域/Family技能/未分类技能/二级技能/Development Environment Setup/SKILL.md)
   - 层级：二级技能
   - 类型：environment_setup
   - 适用条件：Initialize a local development environment with API credentials, Python virtual environment, and pre-commit hooks for code quality enforcement.
49. [Diagnose CLS Score Discrepancies](通用技能领域/Family技能/未分类技能/二级技能/Diagnose CLS Score Discrepancies/SKILL.md)
   - 层级：二级技能
   - 类型：performance_diagnostics
   - 适用条件：Identify whether layout shifts occur during page load or post-load by comparing CrUX field data against lab-based Lighthouse measurements. Use this to pinpoint the source of CLS issues and determine investigation strategy.
50. [End AgentOps Trace with State](通用技能领域/Family技能/未分类技能/微技能/End AgentOps Trace with State/SKILL.md)
   - 层级：微技能
   - 类型：agent_instrumentation
   - 适用条件：Explicitly close an AgentOps trace session by calling end_trace() with a final state (e.g., 'Success', 'Failure'). This marks the session boundary and finalizes recording of all spans and events.
51. [End Trace and Finalize](通用技能领域/Family技能/未分类技能/微技能/End Trace and Finalize/SKILL.md)
   - 层级：微技能
   - 类型：trace_management
   - 适用条件：Terminates the current trace (root span) and finalizes its state. If no trace context is provided, closes all active session spans. Use when completing a debugging session or marking trace completion status.
52. [Entity Decorator Factory Pattern](通用技能领域/Family技能/未分类技能/微技能/Entity Decorator Factory Pattern/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Create reusable decorators for instrumentation of agent entities (agent, task, operation, workflow, session, tool, guardrail, HTTP endpoint) using a factory function that maps semantic span kinds to decorator implementations.
53. [Event listener management](通用技能领域/Family技能/未分类技能/微技能/Event listener management/SKILL.md)
   - 层级：微技能
   - 类型：event_handling
   - 适用条件：Collect and buffer streamed event data from an LLM response, checking for completion signals and concatenating text chunks until the stream terminates.
54. [Exception-to-ErrorEvent Conversion](通用技能领域/Family技能/未分类技能/微技能/Exception-to-ErrorEvent Conversion/SKILL.md)
   - 层级：微技能
   - 类型：error_handling
   - 适用条件：Wraps any exception that occurs during LLM response processing into a structured ErrorEvent linked to the triggering LLMEvent, preserving causality for debugging.
55. [Execute Model Evaluation on Standard Benchmarks](通用技能领域/Family技能/未分类技能/二级技能/Execute Model Evaluation on Standard Benchmarks/SKILL.md)
   - 层级：二级技能
   - 类型：model_evaluation
   - 适用条件：Execute TPC-C and high-contention benchmark workloads against multiple concurrency control protocols. Measure throughput (million txn/s) and abort rate under variable warehouse counts and contention levels. Compare results across protocol variants to validate performance characteristics.
56. [Executor Failure Detection and Recovery](通用技能领域/Family技能/未分类技能/二级技能/Executor Failure Detection and Recovery/SKILL.md)
   - 层级：二级技能
   - 类型：concurrent_task_management
   - 适用条件：Consolidate duplicate global session object references into a single authoritative global (_client_legacy_session_for_init_trace) to prevent state corruption and initialization race conditions. Deprecate old _active_session references and migrate consumers to auto-init trace context.
57. [Extract LLM Call Attributes](通用技能领域/Family技能/未分类技能/微技能/Extract LLM Call Attributes/SKILL.md)
   - 层级：微技能
   - 类型：telemetry_extraction
   - 适用条件：Extract structured attributes (model, tokens, usage) from LLM method calls and return values for telemetry recording. Maps call arguments and responses to OpenTelemetry attribute keys.
58. [Feature Branch Setup](通用技能领域/Family技能/未分类技能/微技能/Feature Branch Setup/SKILL.md)
   - 层级：微技能
   - 类型：version_control
   - 适用条件：Initialize a local feature branch from upstream main with proper git workflow. Use when starting development on a new feature to ensure clean, isolated work.
59. [Fork and Clone Repository](通用技能领域/Family技能/未分类技能/微技能/Fork and Clone Repository/SKILL.md)
   - 层级：微技能
   - 类型：repository_setup
   - 适用条件：Micro-skill for forking a GitHub repository and cloning it locally to establish a development workspace. Use when starting contribution or local development on a shared codebase.
60. [Future Cancellation and State Inspection](通用技能领域/Family技能/未分类技能/微技能/Future Cancellation and State Inspection/SKILL.md)
   - 层级：微技能
   - 类型：async_coordination
   - 适用条件：Synchronize current session and trace context state to legacy module globals for backward compatibility. Invoked during client initialization when auto-trace is enabled and legacy code paths must remain functional.
61. [Future Exception Inspection with Timeout](通用技能领域/Family技能/未分类技能/微技能/Future Exception Inspection with Timeout/SKILL.md)
   - 层级：微技能
   - 类型：async_task_completion
   - 适用条件：Decorator-based pattern to define a reusable tool with name and cost attributes, enabling cost tracking and tool discovery in agent workflows.
62. [Group iterable into nested structure](通用技能领域/Family技能/未分类技能/微技能/Group iterable into nested structure/SKILL.md)
   - 层级：微技能
   - 类型：data_transformation
   - 适用条件：Structure decorator nesting (e.g., @agent containing @operation) to create proper parent-child span relationships in observability traces, ensuring execution hierarchy is accurately reflected in debugging output.
63. [Implement Contextual Error Logging](通用技能领域/Family技能/未分类技能/微技能/Implement Contextual Error Logging/SKILL.md)
   - 层级：微技能
   - 类型：error_handling
   - 适用条件：Implement specific exception types with meaningful error messages and contextual logging to ensure errors are logged with sufficient context for debugging and production issue resolution.
64. [Initialize AgentOps Client with API Keys](通用技能领域/Family技能/未分类技能/二级技能/Initialize AgentOps Client with API Keys/SKILL.md)
   - 层级：二级技能
   - 类型：agent_initialization
   - 适用条件：Load environment variables for API authentication and initialize the AgentOps client with session configuration, trace naming, and metadata tags. This skill sets up an authenticated AgentOps session for agent tracing and monitoring before any agent execution begins.
65. [Initialize AgentOps for Camel AI Observability](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps for Camel AI Observability/SKILL.md)
   - 层级：微技能
   - 类型：agent_observability_setup
   - 适用条件：Set up AgentOps environment variable and initialize the observability client to track and analyze Camel AI agents with full observability.
66. [Initialize AgentOps Monitoring for Llama Stack](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps Monitoring for Llama Stack/SKILL.md)
   - 层级：微技能
   - 类型：agent_integration
   - 适用条件：Set up AgentOps integration with Llama Stack Python Client (>=0.0.53) to enable observability and monitoring of agentic applications.
67. [Initialize AgentOps Session](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps Session/SKILL.md)
   - 层级：微技能
   - 类型：agent_observability
   - 适用条件：Create and configure a new observability session for agent interaction tracking using the AgentOps init function. Establishes OpenTelemetry context and session ID for telemetry collection.
68. [Initialize AgentOps Session with Callback Handler](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps Session with Callback Handler/SKILL.md)
   - 层级：微技能
   - 类型：agent_instrumentation
   - 适用条件：Set up AgentOps tracking by instantiating a LangchainCallbackHandler and attaching it to LLM and tool instances. This enables automatic session recording and span tracking for observability of agent workflows.
69. [Initialize AgentOps Session with Manual Control](通用技能领域/Family技能/未分类技能/微技能/Initialize AgentOps Session with Manual Control/SKILL.md)
   - 层级：微技能
   - 类型：agent_instrumentation
   - 适用条件：Initialize the AgentOps SDK with auto_start_session=False to enable manual session lifecycle management. Use when you need explicit control over when tracing begins and ends.
70. [Initialize Package Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Initialize Package Instrumentation/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_setup
   - 适用条件：Start monitoring and instrumenting Python packages using import hooks if not already active. Prevents duplicate instrumentation and respects agentic library precedence by checking _has_agentic_library flag and _active_instrumentors collection.
71. [Initialize SDK with Fallback](通用技能领域/Family技能/未分类技能/微技能/Initialize SDK with Fallback/SKILL.md)
   - 层级：微技能
   - 类型：sdk_initialization
   - 适用条件：Automatically initialize the AgentOps SDK using environment variables or defaults if not already initialized, with error logging and graceful failure handling. Ensures the tracer is ready before downstream operations attempt to use it.
72. [Install OpenAI Agents Python SDK](通用技能领域/Family技能/未分类技能/微技能/Install OpenAI Agents Python SDK/SKILL.md)
   - 层级：微技能
   - 类型：agent_framework_setup
   - 适用条件：Install the OpenAI Agents SDK package into a Python environment using pip, enabling agent development and framework integration.
73. [Instantiate Instrumentation Handler](通用技能领域/Family技能/未分类技能/微技能/Instantiate Instrumentation Handler/SKILL.md)
   - 层级：微技能
   - 类型：object_instantiation
   - 适用条件：Create a new instance of a specified instrumentor class from a loaded module, returning a ready-to-use BaseInstrumentor object.
74. [Instrumentation Error Handling and Graceful Degradation](通用技能领域/Family技能/未分类技能/二级技能/Instrumentation Error Handling and Graceful Degradation/SKILL.md)
   - 层级：二级技能
   - 类型：api_instrumentation
   - 适用条件：Safety rule that wraps instrumentation operations in try-except blocks to prevent instrumentation failures from breaking the underlying API call. Ensures errors are logged but not propagated to the caller, preserving original API behavior.
75. [InstrumentorLoader Configuration and Instantiation](通用技能领域/Family技能/未分类技能/一级技能/InstrumentorLoader Configuration and Instantiation/SKILL.md)
   - 层级：一级技能
   - 类型：instrumentation
   - 适用条件：Encapsulates metadata and instantiation logic for dynamically loading instrumentor classes. Provides a reusable dataclass and factory pattern that stores module name, class name, minimum version, and optional package name mapping for later instrumentor creation with version validation.
76. [Iterative Stream Loop Construction](通用技能领域/Family技能/未分类技能/二级技能/Iterative Stream Loop Construction/SKILL.md)
   - 层级：二级技能
   - 类型：stream_iteration
   - 适用条件：Group a sequence of agent operations or define logical units of work using the @trace decorator or manual trace management. Use when you need to organize related operations into traceable logical blocks for debugging and monitoring.
77. [Jakarta EE Package Import Migration](通用技能领域/Family技能/未分类技能/二级技能/Jakarta EE Package Import Migration/SKILL.md)
   - 层级：二级技能
   - 类型：dependency_upgrade
   - 适用条件：Initialize and configure the AgentOps SDK by importing core tracing decorators, semantic conventions, and client infrastructure. Establishes the public API surface for agent instrumentation and tracing context setup.
78. [Job Description Writer Agent Configuration](通用技能领域/Family技能/未分类技能/微技能/Job Description Writer Agent Configuration/SKILL.md)
   - 层级：微技能
   - 类型：agent_setup
   - 适用条件：Initialize and configure a Job Description Writer agent with web search, Serper Dev, and file read tools to draft engaging job postings based on research insights from a Research Analyst.
79. [LiteLLM Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LiteLLM Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：integration_setup
   - 适用条件：Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ LLMs through a standardized Input/Output interface.
80. [LLM Alignment Method Comparative Evaluation](通用技能领域/Family技能/未分类技能/二级技能/LLM Alignment Method Comparative Evaluation/SKILL.md)
   - 层级：二级技能
   - 类型：llm_evaluation
   - 适用条件：Apply @operation and @session decorators to functions and methods to automatically record inputs, outputs, exceptions, and support async/generator execution with minimal code overhead.
81. [LLM and API Cost Monitoring](通用技能领域/Family技能/未分类技能/二级技能/LLM and API Cost Monitoring/SKILL.md)
   - 层级：二级技能
   - 类型：cost_management
   - 适用条件：Track and manage spending on LLM and API calls to prevent budget overruns and optimize resource allocation. Provides real-time cost metrics, spending alerts, and budget guardrails for agent sessions.
82. [LLM API Call Tracking](通用技能领域/Family技能/未分类技能/二级技能/LLM API Call Tracking/SKILL.md)
   - 层级：二级技能
   - 类型：llm_observability
   - 适用条件：Automatically capture and log LLM API interactions from supported providers, extracting model, provider, token counts, cost, and message content for observability and debugging.
83. [LLM Chat Completion with AgentOps Tracking](通用技能领域/Family技能/未分类技能/微技能/LLM Chat Completion with AgentOps Tracking/SKILL.md)
   - 层级：微技能
   - 类型：llm_integration
   - 适用条件：Execute a chat completion request to an LLM endpoint with AgentOps session tracking enabled. Captures the API call, model selection, and response for observability and debugging.
84. [LLM Event Capture and Safe Recording](通用技能领域/Family技能/未分类技能/二级技能/LLM Event Capture and Safe Recording/SKILL.md)
   - 层级：二级技能
   - 类型：event_logging
   - 适用条件：Captures LLM request-response lifecycle events (parameters, outputs, timestamps) and safely records them to a session, with automatic error event generation on exception.
85. [LLM Event Capture and Tracking](通用技能领域/Family技能/未分类技能/微技能/LLM Event Capture and Tracking/SKILL.md)
   - 层级：微技能
   - 类型：event_capture
   - 适用条件：Micro operation to intercept and log LLM interactions including prompts, completions, token usage, timestamps, errors, and tool calls. Invoked within provider handle_response() to record observable LLM behavior for debugging and monitoring.
86. [LLM Framework Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LLM Framework Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_framework_setup
   - 适用条件：Establish and configure AgentOps monitoring for a chosen LLM framework (OpenAI, LangChain, LiteLLM, Gemini, Google ADK, CrewAI, OpenAI Agents, SmolAgents, Watsonx, or xAI). Selects the appropriate integration module, initializes the client, and validates connection.
87. [LLM Interaction Inspection](通用技能领域/Family技能/未分类技能/微技能/LLM Interaction Inspection/SKILL.md)
   - 层级：微技能
   - 类型：agent_debugging
   - 适用条件：Retrieve and display detailed LLM prompt and completion content from a specific agent interaction for debugging and validation purposes.
88. [LLM Provider Instrumentation Compatibility Lookup](通用技能领域/Family技能/未分类技能/一级技能/LLM Provider Instrumentation Compatibility Lookup/SKILL.md)
   - 层级：一级技能
   - 类型：instrumentation_compatibility
   - 适用条件：Reference skill for verifying LLM provider support and minimum version requirements before planning OpenTelemetry instrumentation integration. Provides static compatibility matrix to confirm whether a target provider can be instrumented and what minimum library version is required.
89. [LLM Provider Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LLM Provider Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：provider_integration
   - 适用条件：Scaffold for implementing a new LLM provider by inheriting from BaseProvider, configuring provider metadata, and wiring required override/undo methods. Use when adding support for a new LLM service to the provider directory.
90. [Load and Inject Environment Variables Safely](通用技能领域/Family技能/未分类技能/微技能/Load and Inject Environment Variables Safely/SKILL.md)
   - 层级：微技能
   - 类型：credential_management
   - 适用条件：Retrieve API keys from environment or configuration source and inject them into os.environ with fallback defaults, ensuring secure credential handling without hardcoding secrets.
91. [Local Streaming Program Development and Debugging](通用技能领域/Family技能/未分类技能/二级技能/Local Streaming Program Development and Debugging/SKILL.md)
   - 层级：二级技能
   - 类型：streaming_program_development
   - 适用条件：Initialize and automatically record agent program executions as timestamped sessions in a monitoring dashboard with minimal setup overhead. Captures agent behavior data during live execution for post-run analysis and visualization.
92. [Locale-Specific Time Formatter Creation](通用技能领域/Family技能/未分类技能/微技能/Locale-Specific Time Formatter Creation/SKILL.md)
   - 层级：微技能
   - 类型：time_handling
   - 适用条件：Invoke the generate_documentation.py script to automatically create documentation files from example notebooks. Use this micro operation after creating or updating notebooks and before publishing to the website.
93. [Logarithmic Scale Configuration](通用技能领域/Family技能/未分类技能/二级技能/Logarithmic Scale Configuration/SKILL.md)
   - 层级：二级技能
   - 类型：scale_configuration
   - 适用条件：Initialize AgentOps monitoring with automatic or manual session creation, associating all subsequent events and API calls with a tracking session.
94. [Manage Active Instrumentor Lifecycle](通用技能领域/Family技能/未分类技能/二级技能/Manage Active Instrumentor Lifecycle/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_lifecycle
   - 适用条件：Track and maintain the list of active BaseInstrumentor instances during runtime, enabling selective activation, deactivation, and cleanup of instrumentation for monitored packages.
95. [Manual Session Control Pattern](通用技能领域/Family技能/未分类技能/微技能/Manual Session Control Pattern/SKILL.md)
   - 层级：微技能
   - 类型：agent_monitoring_setup
   - 适用条件：Defer automatic session creation and manually start sessions with custom tags when finer control over session lifecycle is needed. Use this when multiple independent agent tasks run in sequence and session boundaries must align with business events.
96. [Merge and Normalize Tag Collections](通用技能领域/Family技能/未分类技能/微技能/Merge and Normalize Tag Collections/SKILL.md)
   - 层级：微技能
   - 类型：data_preparation
   - 适用条件：Combine user-provided tags with default tags into a single deduplicated collection. Handles cases where one or both tag sources are present, absent, or null. Prepares normalized tag input for downstream session initialization.
97. [Mock Filesystem Operations](通用技能领域/Family技能/未分类技能/微技能/Mock Filesystem Operations/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Use pyfakefs fixture to create and manipulate a fake filesystem in tests, isolating file I/O operations from the real filesystem without affecting actual disk state.
98. [Mock HTTP Requests with Assertions](通用技能领域/Family技能/未分类技能/微技能/Mock HTTP Requests with Assertions/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Use requests_mock to intercept and mock HTTP requests in tests, allowing assertion of request behavior and response validation without external API calls.
99. [Monitor Live CLS During User Interaction](通用技能领域/Family技能/未分类技能/微技能/Monitor Live CLS During User Interaction/SKILL.md)
   - 层级：微技能
   - 类型：performance_diagnostics
   - 适用条件：Install project dependencies in editable mode for local development. Use after cloning or when setting up a fresh development environment.
100. [Multi-Agent Job Description Generation Workflow](通用技能领域/Family技能/未分类技能/二级技能/Multi-Agent Job Description Generation Workflow/SKILL.md)
   - 层级：二级技能
   - 类型：content_generation
   - 适用条件：Orchestrate a three-agent sequential pipeline to generate polished job descriptions from company data. Research Analyst analyzes company culture and values; Job Description Writer creates engaging posting using research insights; Review Specialist refines for clarity, engagement, grammar, and alignment. Agents execute in strict sequence with output handoff between stages.
101. [Multi-Tool Agent Orchestration](通用技能领域/Family技能/未分类技能/二级技能/Multi-Tool Agent Orchestration/SKILL.md)
   - 层级：二级技能
   - 类型：agent_orchestration
   - 适用条件：Coordinate multiple tools or agents in a single execution flow, managing tool selection, parameter passing, and result aggregation. Handles complex tool chains and multi-agent system coordination across frameworks like CrewAI, LangChain, OpenAI, and SmolAgents.
102. [Nested Operation Execution Pattern](通用技能领域/Family技能/未分类技能/微技能/Nested Operation Execution Pattern/SKILL.md)
   - 层级：微技能
   - 类型：operation_composition
   - 适用条件：Structure agent operations as nested method calls where parent operations invoke child operations, enabling hierarchical observability and execution tracing.
103. [Notebook-Based Integration Testing for LLM Providers](通用技能领域/Family技能/未分类技能/二级技能/Notebook-Based Integration Testing for LLM Providers/SKILL.md)
   - 层级：二级技能
   - 类型：integration_testing
   - 适用条件：Execute Jupyter notebooks as integration tests to verify end-to-end LLM provider functionality, real-world usage patterns, and API compatibility across multiple Python versions. Notebooks are located in examples/ directory, executed via CI workflow on PR merges and manual triggers, with provider API keys configured in GitHub Actions secrets.
104. [Offscreen Content Loading with User Notification](通用技能领域/Family技能/未分类技能/微技能/Offscreen Content Loading with User Notification/SKILL.md)
   - 层级：微技能
   - 类型：content_loading
   - 适用条件：Set up AgentOps observability integration with SwarmZero multi-agent framework by configuring API key and initializing the tracking client.
105. [OpenAI Library Instrumentation Setup](通用技能领域/Family技能/未分类技能/二级技能/OpenAI Library Instrumentation Setup/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_setup
   - 适用条件：Configure and initialize OpenTelemetry instrumentation for OpenAI client library with version-specific handling and streaming wrapper registration. Establishes comprehensive observability for OpenAI API calls including chat completions, beta endpoints, and responses APIs.
106. [Package Import Interception and Instrumentation](通用技能领域/Family技能/未分类技能/一级技能/Package Import Interception and Instrumentation/SKILL.md)
   - 层级：一级技能
   - 类型：instrumentation
   - 适用条件：Intercepts Python module imports at runtime and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect packages against configured registries (PROVIDERS, AGENTIC_LIBRARIES) and instantiate instrumentors transparently, enabling monitoring of external package calls without modifying user code.
107. [Package Instrumentation Eligibility Check](通用技能领域/Family技能/未分类技能/微技能/Package Instrumentation Eligibility Check/SKILL.md)
   - 层级：微技能
   - 类型：package_instrumentation
   - 适用条件：Determine whether a package should be instrumented by AgentOps by verifying it is not already instrumented and is in the target allowlist (AGENTIC_LIBRARIES or PROVIDERS). Prevents duplicate instrumentation and filters non-target packages.
108. [Parallel Task Completion Polling](通用技能领域/Family技能/未分类技能/二级技能/Parallel Task Completion Polling/SKILL.md)
   - 层级：二级技能
   - 类型：concurrent_task_management
   - 适用条件：Wait for a collection of Futures to reach a completion condition (any, first exception, or all done) with optional timeout. Use this session-level skill to coordinate multi-task workflows and decide when to proceed based on task readiness.
109. [Path Command Execution](通用技能领域/Family技能/未分类技能/微技能/Path Command Execution/SKILL.md)
   - 层级：微技能
   - 类型：graphics_drawing
   - 适用条件：Wraps an agent method with @operation decorator to enable automatic logging and monitoring of task execution. Use when instrumenting agent methods for observability and debugging.
110. [ProcessPoolExecutor Setup and Execution](通用技能领域/Family技能/未分类技能/二级技能/ProcessPoolExecutor Setup and Execution/SKILL.md)
   - 层级：二级技能
   - 类型：parallel_execution
   - 适用条件：Wraps a workflow function with @session decorator to establish a monitoring session for agent execution. Creates and manages a session context for agent workflow execution, enabling centralized logging and session tracking across multiple agent operations.
111. [ProcessPoolExecutor Worker Lifecycle Configuration](通用技能领域/Family技能/未分类技能/微技能/ProcessPoolExecutor Worker Lifecycle Configuration/SKILL.md)
   - 层级：微技能
   - 类型：pool_configuration
   - 适用条件：Register and execute a global atexit handler that safely ends the client's auto-initialized trace context during application shutdown, with error recovery and resource cleanup.
112. [Provider Method Override and Restoration](通用技能领域/Family技能/未分类技能/微技能/Provider Method Override and Restoration/SKILL.md)
   - 层级：微技能
   - 类型：method_patching
   - 适用条件：Micro operation to patch provider client methods for interception and restore original methods on cleanup. Enables transparent event capture without modifying provider source code.
113. [Provider Test Coverage Specification](通用技能领域/Family技能/未分类技能/一级技能/Provider Test Coverage Specification/SKILL.md)
   - 层级：一级技能
   - 类型：test_planning
   - 适用条件：Reference checklist defining required functionality demonstrations for LLM provider test notebooks. Specifies what capabilities each provider notebook must cover to ensure complete integration testing across basic completion, streaming, async operations, error handling, and tool usage.
114. [Python Code Style Compliance](通用技能领域/Family技能/未分类技能/二级技能/Python Code Style Compliance/SKILL.md)
   - 层级：二级技能
   - 类型：code_review
   - 适用条件：Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and docstring conventions. Apply before code review or merge to standardize code style across the repository.
115. [Qualify and Resolve XML Namespaces](通用技能领域/Family技能/未分类技能/微技能/Qualify and Resolve XML Namespaces/SKILL.md)
   - 层级：微技能
   - 类型：xml_handling
   - 适用条件：Set up AgentOps monitoring for LLM and agent framework calls by importing the library and calling init() with an API key. Use this as the entry point to enable observability in Python agent scripts.
116. [Record and Replay HTTP Interactions with pytest-vcr](通用技能领域/Family技能/未分类技能/微技能/Record and Replay HTTP Interactions with pytest-vcr/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Use pytest-vcr to record HTTP requests and responses during test execution, then replay them in subsequent runs to avoid external API calls. Enables deterministic, fast test runs by isolating tests from external HTTP dependencies.
117. [Register atexit cleanup handler](通用技能领域/Family技能/未分类技能/微技能/Register atexit cleanup handler/SKILL.md)
   - 层级：微技能
   - 类型：resource_cleanup
   - 适用条件：Register a single atexit handler to ensure trace cleanup runs at process exit, guarding against duplicate registrations via idempotent flag check.
118. [Research Analyst Agent Configuration](通用技能领域/Family技能/未分类技能/微技能/Research Analyst Agent Configuration/SKILL.md)
   - 层级：微技能
   - 类型：agent_setup
   - 适用条件：Configure and instantiate a Research Analyst agent with web search and Serper Dev tools to extract company culture, values, and needs from websites and descriptions.
119. [Resolve Active Span from OpenTelemetry Context](通用技能领域/Family技能/未分类技能/微技能/Resolve Active Span from OpenTelemetry Context/SKILL.md)
   - 层级：微技能
   - 类型：distributed_tracing
   - 适用条件：Retrieve and validate the current span from OpenTelemetry context, then locate the root trace span if the current span is a child span. Use this when instrumenting distributed tracing and need to attach operations to the correct parent trace.
120. [Resolve and Import Instrumentation Module](通用技能领域/Family技能/未分类技能/微技能/Resolve and Import Instrumentation Module/SKILL.md)
   - 层级：微技能
   - 类型：module_loading
   - 适用条件：Dynamically import an instrumentation module by name and return the module object for subsequent class instantiation or method access.
121. [Route Private Inquiries to Contact Form](通用技能领域/Family技能/未分类技能/二级技能/Route Private Inquiries to Contact Form/SKILL.md)
   - 层级：二级技能
   - 类型：support_routing
   - 适用条件：Identify user inquiries containing sensitive business information, personal data, or explicit confidentiality requests, and redirect them to the contact form to maintain privacy and prevent exposure in public channels.
122. [Run All Tests with Tox](通用技能领域/Family技能/未分类技能/微技能/Run All Tests with Tox/SKILL.md)
   - 层级：微技能
   - 类型：testing
   - 适用条件：Execute the complete test suite using tox to validate all test environments and configurations in one command.
123. [Run Specific Test File with Pytest](通用技能领域/Family技能/未分类技能/微技能/Run Specific Test File with Pytest/SKILL.md)
   - 层级：微技能
   - 类型：testing
   - 适用条件：Execute a single test file with verbose output to isolate and debug specific test cases or modules.
124. [SDK Initialization State Check and Recovery](通用技能领域/Family技能/未分类技能/二级技能/SDK Initialization State Check and Recovery/SKILL.md)
   - 层级：二级技能
   - 类型：sdk_lifecycle
   - 适用条件：Validate SDK initialization state before critical tracer operations. Attempt automatic recovery if uninitialized; escalate to error logging and return None if recovery fails. Prevents silent failures and ensures SDK readiness.
125. [Semantic Attribute Capture and Documentation](通用技能领域/Family技能/未分类技能/二级技能/Semantic Attribute Capture and Documentation/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_design
   - 适用条件：Session-level workflow for identifying, capturing, and documenting all attributes that an instrumentor should extract from API calls using semantic convention standards. Ensures consistent attribute naming and documentation across instrumentors by mapping API response fields to standard semantic attributes with inline code comments.
126. [Semantic Span Kind Reference](通用技能领域/Family技能/未分类技能/一级技能/Semantic Span Kind Reference/SKILL.md)
   - 层级：一级技能
   - 类型：instrumentation_taxonomy
   - 适用条件：Canonical enumeration and mapping of semantic span kinds (AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP) used to classify instrumentation points in agent systems. Provides taxonomy for selecting appropriate decorators and instrumentation classification.
127. [Session Drawer Navigation](通用技能领域/Family技能/未分类技能/微技能/Session Drawer Navigation/SKILL.md)
   - 层级：微技能
   - 类型：debugging
   - 适用条件：Locate and retrieve a previously recorded session from the Session Drawer by browsing session history and metadata such as execution time and SDK versions.
128. [Session Drilldown Analysis](通用技能领域/Family技能/未分类技能/二级技能/Session Drilldown Analysis/SKILL.md)
   - 层级：二级技能
   - 类型：debugging
   - 适用条件：Review and analyze a recorded agent session by examining LLM calls, action events, tool calls, errors, and execution timeline in a waterfall view. Use this to debug agent behavior and understand event sequences.
129. [Session Overview Aggregation](通用技能领域/Family技能/未分类技能/二级技能/Session Overview Aggregation/SKILL.md)
   - 层级：二级技能
   - 类型：debugging
   - 适用条件：Consolidate and analyze aggregate metrics across all recorded sessions in a single view. Identify patterns, performance trends, and high-level session statistics without drilling into individual session details.
130. [Session Span Initialization](通用技能领域/Family技能/未分类技能/微技能/Session Span Initialization/SKILL.md)
   - 层级：微技能
   - 类型：observability_instrumentation
   - 适用条件：Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Use when starting observability instrumentation for an agent workflow.
131. [Session Tagging for Organization and Filtering](通用技能领域/Family技能/未分类技能/微技能/Session Tagging for Organization and Filtering/SKILL.md)
   - 层级：微技能
   - 类型：session_management
   - 适用条件：Attach organizational tags to AgentOps sessions at initialization or session start to enable later filtering and categorization of session records by environment, feature, service tier, or other organizational dimensions.
132. [Singleton Client Initialization](通用技能领域/Family技能/未分类技能/微技能/Singleton Client Initialization/SKILL.md)
   - 层级：微技能
   - 类型：client_lifecycle
   - 适用条件：Initialize and manage a singleton Client instance for AgentOps service, ensuring only one active client exists throughout the application lifecycle.
133. [Singleton Client Initialization with Re-initialization Guard](通用技能领域/Family技能/未分类技能/二级技能/Singleton Client Initialization with Re-initialization Guard/SKILL.md)
   - 层级：二级技能
   - 类型：client_initialization
   - 适用条件：Ensures a single Client instance is created and safely re-initialized only when a different API key is explicitly provided, preventing unintended state conflicts and cleaning up trace context on re-init.
134. [Singleton Instance Deduplication](通用技能领域/Family技能/未分类技能/微技能/Singleton Instance Deduplication/SKILL.md)
   - 层级：微技能
   - 类型：class_structure_cleanup
   - 适用条件：Remove duplicate class variable definitions (e.g., __instance = None) that appear multiple times in a class definition. Apply when consolidating singleton initialization to prevent accidental re-initialization or state corruption.
135. [Span Management with Attribute Tracking](通用技能领域/Family技能/未分类技能/微技能/Span Management with Attribute Tracking/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata.
136. [Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator](通用技能领域/Family技能/未分类技能/一级技能/Spring Boot 2.7.x to 3.0 Phased Migration Orchestrator/SKILL.md)
   - 层级：一级技能
   - 类型：framework_upgrade
   - 适用条件：Orchestrates a multi-phase, staged migration of Spring Boot applications from 2.7.x to 3.0, covering pre-upgrade validation, core upgrade execution, and post-upgrade verification. Ensures safe handling of Java 17+ requirement, Jakarta EE namespace migration, Spring Framework 6.0 API changes, and dependency compatibility.
137. [Standard Metrics Recording](通用技能领域/Family技能/未分类技能/二级技能/Standard Metrics Recording/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation
   - 适用条件：Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumented operations.
138. [Start Managed Trace with Context](通用技能领域/Family技能/未分类技能/二级技能/Start Managed Trace with Context/SKILL.md)
   - 层级：二级技能
   - 类型：trace_management
   - 适用条件：Create a new root span (trace) with optional name and tags, returning a TraceContext object for concurrent user-managed tracing sessions. Includes precondition validation and automatic initialization fallback.
139. [Start Trace Session](通用技能领域/Family技能/未分类技能/微技能/Start Trace Session/SKILL.md)
   - 层级：微技能
   - 类型：trace_management
   - 适用条件：Initiates a named trace with optional tags and returns a trace context for subsequent span operations. Use when beginning a new debugging or monitoring session.
140. [Stream Event Processing for Agent Output](通用技能领域/Family技能/未分类技能/微技能/Stream Event Processing for Agent Output/SKILL.md)
   - 层级：微技能
   - 类型：agent_output_handling
   - 适用条件：Iterate over agent event streams, filter by event type, and output text-generation events in real-time. Use when consuming streaming responses from agent frameworks that emit structured event objects.
141. [Streaming API Wrapper Registration](通用技能领域/Family技能/未分类技能/微技能/Streaming API Wrapper Registration/SKILL.md)
   - 层级：微技能
   - 类型：wrapper_registration
   - 适用条件：Register function wrappers for OpenAI v1 streaming endpoints to capture telemetry for sync and async calls. Attaches tracing wrappers to chat completions, beta completions, and responses API entry points.
142. [Streaming Response Instrumentation](通用技能领域/Family技能/未分类技能/微技能/Streaming Response Instrumentation/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Wrap streaming methods to capture and trace chunk-by-chunk responses with consistent content extraction. Use when instrumenting APIs that return streaming or chunked responses.
143. [Test Data Organization](通用技能领域/Family技能/未分类技能/微技能/Test Data Organization/SKILL.md)
   - 层级：微技能
   - 类型：testing
   - 适用条件：Organize and maintain test data assets in a standardized directory structure with clear naming conventions and format documentation. This micro-skill ensures test data is discoverable, reusable, and well-documented for reproducible test execution across multiple test suites.
144. [Test Fixture Setup](通用技能领域/Family技能/未分类技能/微技能/Test Fixture Setup/SKILL.md)
   - 层级：微技能
   - 类型：testing
   - 适用条件：Create and manage reusable pytest fixtures in conftest.py for consistent test initialization. Fixtures provide mock objects, stubs, and test dependencies that can be injected across unit, integration, and end-to-end test cases.
145. [Third-Party Script Performance Optimization](通用技能领域/Family技能/未分类技能/二级技能/Third-Party Script Performance Optimization/SKILL.md)
   - 层级：二级技能
   - 类型：asset_optimization
   - 适用条件：Set up AgentOps client in 2 lines of code to automatically capture and replay LLM call analytics and session traces.
146. [Thread-Safe Singleton Client Retrieval](通用技能领域/Family技能/未分类技能/微技能/Thread-Safe Singleton Client Retrieval/SKILL.md)
   - 层级：微技能
   - 类型：client_initialization
   - 适用条件：Retrieve or initialize a singleton client instance using double-checked locking pattern to ensure thread safety and prevent race conditions during concurrent access.
147. [TicToc Concurrency Control Protocol](通用技能领域/Family技能/未分类技能/一级技能/TicToc Concurrency Control Protocol/SKILL.md)
   - 层级：一级技能
   - 类型：transaction_concurrency_control
   - 适用条件：Multi-stage protocol for building reusable API instrumentation modules that wrap third-party service calls with consistent error handling, async support, and semantic attribute capture. Establishes a cross-phase workflow from design through testing to ensure instrumentation consistency across multiple service integrations.
148. [Time Format and Parse Operations](通用技能领域/Family技能/未分类技能/二级技能/Time Format and Parse Operations/SKILL.md)
   - 层级：二级技能
   - 类型：time_handling
   - 适用条件：Automates extraction of Jupyter notebook content and conversion to Markdown documentation with frontmatter, metadata, and MDX file generation for website publishing.
149. [Token Usage Extraction and Attribution](通用技能领域/Family技能/未分类技能/微技能/Token Usage Extraction and Attribution/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Extract token usage metrics from API responses and attach them as span attributes for cost and quota tracking. Applies to instrumented LLM or API calls that return token consumption data.
150. [Trace and Tag Workflow Execution](通用技能领域/Family技能/未分类技能/二级技能/Trace and Tag Workflow Execution/SKILL.md)
   - 层级：二级技能
   - 类型：workflow_instrumentation
   - 适用条件：Decorator-based pattern to wrap a workflow function with execution tracing, naming, and semantic tags for observability and workflow discovery.
151. [Trace Context Cleanup on Re-initialization](通用技能领域/Family技能/未分类技能/微技能/Trace Context Cleanup on Re-initialization/SKILL.md)
   - 层级：微技能
   - 类型：trace_management
   - 适用条件：Ends any active trace recording and clears trace context when Client is re-initialized with a different API key, preventing orphaned or misattributed traces.
152. [Trace context safe termination with fallback](通用技能领域/Family技能/未分类技能/微技能/Trace context safe termination with fallback/SKILL.md)
   - 层级：微技能
   - 类型：trace_lifecycle_management
   - 适用条件：Safely terminate an active trace span by verifying tracer initialization and span recording status, then end the trace with exception handling and state cleanup. Designed to prevent dangling trace references and unhandled exceptions during shutdown or session termination.
153. [Track Mistral Agent Execution](通用技能领域/Family技能/未分类技能/二级技能/Track Mistral Agent Execution/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Integrate AgentOps monitoring with Mistral Python SDK (>=0.32.0) to track agent behavior, decisions, and outcomes in real time.
154. [Understand Iterator Data Sink for Testing](通用技能领域/Family技能/未分类技能/一级技能/Understand Iterator Data Sink for Testing/SKILL.md)
   - 层级：一级技能
   - 类型：testing
   - 适用条件：Reference schema for organizing agent execution activities into a six-level hierarchical span structure (SESSION → AGENT → WORKFLOW → OPERATION/TASK → LLM → TOOL). Use when designing tracing, logging, or debugging infrastructure for multi-level agent workflows.
155. [Update legacy global references for backward compatibility](通用技能领域/Family技能/未分类技能/微技能/Update legacy global references for backward compatibility/SKILL.md)
   - 层级：微技能
   - 类型：compatibility_maintenance
   - 适用条件：Synchronize internal trace context and session objects to global module-level variables to maintain compatibility with legacy code paths using indirect access patterns.
156. [Validate Span Recording State](通用技能领域/Family技能/未分类技能/二级技能/Validate Span Recording State/SKILL.md)
   - 层级：二级技能
   - 类型：distributed_tracing
   - 适用条件：Check whether the current span exists, has the is_recording attribute, and is actively recording. Use this as a guard before attempting to attach operations or metadata to a span.
157. [Validate User Flows Against CLS Regression](通用技能领域/Family技能/未分类技能/二级技能/Validate User Flows Against CLS Regression/SKILL.md)
   - 层级：二级技能
   - 类型：performance_testing
   - 适用条件：Instrument test execution with coverage tracking and generate a coverage report to identify untested code paths and assess test completeness.
158. [VCR Cassette Management](通用技能领域/Family技能/未分类技能/微技能/VCR Cassette Management/SKILL.md)
   - 层级：微技能
   - 类型：testing
   - 适用条件：Record, store, and maintain HTTP interaction cassettes for deterministic testing. Sanitize sensitive data from recorded interactions and update cassettes when API contracts change.
159. [Version-Specific OpenAI Instrumentor Initialization](通用技能领域/Family技能/未分类技能/微技能/Version-Specific OpenAI Instrumentor Initialization/SKILL.md)
   - 层级：微技能
   - 类型：version_routing
   - 适用条件：Detect OpenAI library version at runtime and apply the appropriate instrumentation strategy: delegate to legacy instrumentor for v0, or proceed with standard v1 initialization. Ensures instrumentation compatibility across library versions by routing initialization logic based on version detection.
