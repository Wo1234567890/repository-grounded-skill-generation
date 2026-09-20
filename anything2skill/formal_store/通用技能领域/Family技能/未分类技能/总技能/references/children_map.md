# 未分类技能 子技能地图

- parent: `未分类技能/总技能/SKILL.md`

## 子技能列表

1. [Active Span Resolution in Distributed Tracing](通用技能领域/Family技能/未分类技能/微技能/Active Span Resolution in Distributed Tracing/SKILL.md)
   - 层级：微技能
   - 类型：distributed_tracing
   - 适用条件：Retrieve and validate the current OpenTelemetry span from context, then resolve it to the appropriate session or root trace span for logging and debugging.
2. [Agent Class Definition with ID Binding](通用技能领域/Family技能/未分类技能/微技能/Agent Class Definition with ID Binding/SKILL.md)
   - 层级：微技能
   - 类型：agent_instantiation
   - 适用条件：Define an agent class using the @agent decorator, binding a unique agent_id that persists across method calls and enables agent-level logging and tracing.
3. [Agent Cost and Spend Management](通用技能领域/Family技能/未分类技能/二级技能/Agent Cost and Spend Management/SKILL.md)
   - 层级：二级技能
   - 类型：cost_optimization
   - 适用条件：Monitor and control spending on LLM and API calls to optimize agent operational costs and prevent budget overruns.
4. [Agent Operation Span Tracking](通用技能领域/Family技能/未分类技能/微技能/Agent Operation Span Tracking/SKILL.md)
   - 层级：微技能
   - 类型：observability_instrumentation
   - 适用条件：Decorator-based pattern to create an agent span for tracking agent-specific operations and decisions within a session. Use when instrumenting agent behavior for observability.
5. [Agent Session Replay and Analytics Review](通用技能领域/Family技能/未分类技能/微技能/Agent Session Replay and Analytics Review/SKILL.md)
   - 层级：微技能
   - 类型：agent_debugging
   - 适用条件：Access and review recorded agent session replays and summary analytics via the AgentOps dashboard to identify and debug agent behavior issues.
6. [Agentic Library Detection and Instrumentation Halt](通用技能领域/Family技能/未分类技能/二级技能/Agentic Library Detection and Instrumentation Halt/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_safety
   - 适用条件：Detect when an agentic library (e.g., CrewAI, AutoGen) is instrumented during module iteration and halt further instrumentation to prevent conflicts and redundant instrumentation.
7. [AgentOps Client Configuration Validation](通用技能领域/Family技能/未分类技能/微技能/AgentOps Client Configuration Validation/SKILL.md)
   - 层级：微技能
   - 类型：client_initialization
   - 适用条件：Validates configuration parameters against a whitelist of supported parameters during AgentOps client initialization or reconfiguration. Logs warnings for invalid parameters and applies only valid parameters to the global client instance.
8. [AgentOps Session Initialization](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Session Initialization/SKILL.md)
   - 层级：二级技能
   - 类型：agent_orchestration
   - 适用条件：Initialize and configure AgentOps client for multi-agent workflow monitoring and tracing. Sets up session tracking with custom tags and trace naming for debugging and observability.
9. [AgentOps Session Initialization with Tracing](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Session Initialization with Tracing/SKILL.md)
   - 层级：二级技能
   - 类型：agent_observability
   - 适用条件：Initialize AgentOps SDK with deferred session startup and decorate workflow functions with trace metadata to enable session tracking, debugging, and observability. Establishes manual control over session lifecycle and instruments functions with name and tag annotations.
10. [AgentOps Session Lifecycle Management](通用技能领域/Family技能/未分类技能/二级技能/AgentOps Session Lifecycle Management/SKILL.md)
   - 层级：二级技能
   - 类型：agent_monitoring
   - 适用条件：Initialize, stream events, and terminate an AgentOps monitoring session for agent applications. Captures text-generation events and logs session completion status.
11. [AgentOps SwarmZero Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/AgentOps SwarmZero Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Initialize AgentOps observability for SwarmZero multi-agent systems by setting environment credentials and configuring the integration. Enables full tracking of agent actions, decisions, and performance metrics.
12. [Anthropic Claude API Message Creation with AgentOps Tracking](通用技能领域/Family技能/未分类技能/微技能/Anthropic Claude API Message Creation with AgentOps Tracking/SKILL.md)
   - 层级：微技能
   - 类型：api_integration
   - 适用条件：Execute a single non-streaming message creation call to Anthropic's Claude model with AgentOps session tracking enabled. Captures API interactions for debugging and monitoring multi-agent workflows.
13. [Application Performance Monitoring with OpenTelemetry](通用技能领域/Family技能/未分类技能/二级技能/Application Performance Monitoring with OpenTelemetry/SKILL.md)
   - 层级：二级技能
   - 类型：monitoring_and_instrumentation
   - 适用条件：Configures and initializes the AgentOps monitoring and debugging SDK with API credentials, session parameters, and instrumentation options. Establishes observability infrastructure for agent applications.
14. [Async and Generator Function Instrumentation](通用技能领域/Family技能/未分类技能/微技能/Async and Generator Function Instrumentation/SKILL.md)
   - 层级：微技能
   - 类型：observability_instrumentation
   - 适用条件：Enable observability decorators to correctly instrument async/await and generator functions, capturing execution state at each await or yield boundary without introducing performance overhead or altering function semantics.
15. [Attribute Extraction from Method Calls](通用技能领域/Family技能/未分类技能/微技能/Attribute Extraction from Method Calls/SKILL.md)
   - 层级：微技能
   - 类型：telemetry_extraction
   - 适用条件：Extract telemetry attributes (e.g., model name, token usage) from LLM method arguments and return values using a structured AttributeMap handler. Normalizes observable metadata into OpenTelemetry-compliant keys for downstream observability systems.
16. [Auto-start Trace Session Initialization](通用技能领域/Family技能/未分类技能/二级技能/Auto-start Trace Session Initialization/SKILL.md)
   - 层级：二级技能
   - 类型：observability_setup
   - 适用条件：Automatically initialize and start a tracing session when configured, registering exit handlers and creating trace contexts for observability.
17. [BrokenProcessPool Exception Handling](通用技能领域/Family技能/未分类技能/二级技能/BrokenProcessPool Exception Handling/SKILL.md)
   - 层级：二级技能
   - 类型：error_handling
   - 适用条件：Detect and handle BrokenProcessPool exception raised when a worker process in ProcessPoolExecutor terminates abruptly. Prevents undefined behavior such as freezing or deadlock by catching the exception, logging the failure, and ensuring graceful cleanup before escalating to caller. Complements mandatory credential validation at initialization to ensure only properly configured clients enter execution phase.
18. [CamelAI Agent Tracking Setup](通用技能领域/Family技能/未分类技能/二级技能/CamelAI Agent Tracking Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Install and configure AgentOps integration with CamelAI Python SDK (>=0.32.0) to enable agent activity monitoring and debugging.
19. [Client Configuration Update](通用技能领域/Family技能/未分类技能/微技能/Client Configuration Update/SKILL.md)
   - 层级：微技能
   - 类型：configuration
   - 适用条件：Apply configuration parameter changes to an initialized client instance by delegating to the internal config object. Use this micro-skill when the client is already running and you need to modify settings without reinitializing.
20. [Cohere Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/Cohere Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：integration_setup
   - 适用条件：Install and configure AgentOps with Cohere (>=5.4.0) to enable agent monitoring and observability for Cohere-based LLM applications.
21. [CommonInstrumentor Configuration and Wrapping](通用技能领域/Family技能/未分类技能/二级技能/CommonInstrumentor Configuration and Wrapping/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_setup
   - 适用条件：Configure and instantiate a CommonInstrumentor with InstrumentorConfig and WrapConfig to create reusable instrumentation templates for LLM providers and agentic frameworks.
22. [Conditional Package Instrumentation Dispatch](通用技能领域/Family技能/未分类技能/二级技能/Conditional Package Instrumentation Dispatch/SKILL.md)
   - 层级：二级技能
   - 类型：observability_instrumentation
   - 适用条件：Routes a detected package import to the correct instrumentor configuration by consulting the PROVIDERS or AGENTIC_LIBRARIES registry, validates instrumentation eligibility, and instantiates the appropriate InstrumentorLoader with version checking. Handles special-case cascading (e.g., mem0 → concurrent.futures).
23. [Create Reusable Pytest Fixtures in conftest.py](通用技能领域/Family技能/未分类技能/二级技能/Create Reusable Pytest Fixtures in conftest.py/SKILL.md)
   - 层级：二级技能
   - 类型：testing_infrastructure
   - 适用条件：Define and manage reusable pytest fixtures in conftest.py to standardize mock objects and test dependencies across test suites. Establishes consistent test infrastructure for unit and integration tests by centralizing fixture definitions and ensuring proper scope alignment.
24. [CrewAI Multi-Tool Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/CrewAI Multi-Tool Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_orchestration
   - 适用条件：Configure and instantiate multiple specialized tools (WebsiteSearchTool, SerperDevTool, FileReadTool) for use within a CrewAI agent workflow. Each tool is initialized with specific parameters and descriptions to enable web search, external API queries, and file I/O capabilities.
25. [Custom Reward Function Design](通用技能领域/Family技能/未分类技能/微技能/Custom Reward Function Design/SKILL.md)
   - 层级：微技能
   - 类型：reward_engineering
   - 适用条件：Apply the @operation decorator to wrap functions and automatically track their execution, parameters, and return values as spans in session visualization. Use when you need to monitor internal function behavior alongside LLM calls.
26. [Custom ServerRequestObservationConvention Implementation](通用技能领域/Family技能/未分类技能/微技能/Custom ServerRequestObservationConvention Implementation/SKILL.md)
   - 层级：微技能
   - 类型：metrics_instrumentation
   - 适用条件：Extract and log standardized attributes from API requests and responses using semantic conventions. Ensures consistent metadata (model name, token counts, latency, error codes) across all instrumented API calls.
27. [Custom Source Function Integration](通用技能领域/Family技能/未分类技能/二级技能/Custom Source Function Integration/SKILL.md)
   - 层级：二级技能
   - 类型：data_source_setup
   - 适用条件：Attach and configure custom or third-party source functions (e.g., Kafka consumer) to a Flink DataStream using the addSource() API. Use this skill when connecting to managed message brokers, databases, or proprietary systems where a source function implementation is already available or provided by the Flink connectors library.
28. [DataStream Sink Configuration](通用技能领域/Family技能/未分类技能/二级技能/DataStream Sink Configuration/SKILL.md)
   - 层级：二级技能
   - 类型：data_output
   - 适用条件：Automatically capture and log LLM API interactions (model, provider, tokens, cost, messages) from supported providers for observability and debugging.
29. [Decorator Backward Compatibility Bridge](通用技能领域/Family技能/未分类技能/微技能/Decorator Backward Compatibility Bridge/SKILL.md)
   - 层级：微技能
   - 类型：api_migration
   - 适用条件：Wrapper that maps a deprecated @session decorator to the new @trace decorator, handling both direct and parameterized invocation patterns while emitting deprecation warnings. Maintains API compatibility during decorator naming migration without breaking existing code.
30. [Decorator-Based Observability Instrumentation](通用技能领域/Family技能/未分类技能/二级技能/Decorator-Based Observability Instrumentation/SKILL.md)
   - 层级：二级技能
   - 类型：observability_setup
   - 适用条件：Apply Python decorators (@workflow, @agent, @operation) to functions and classes to automatically capture execution spans and observability data with minimal code overhead.
31. [Development Environment Setup](通用技能领域/Family技能/未分类技能/二级技能/Development Environment Setup/SKILL.md)
   - 层级：二级技能
   - 类型：environment_setup
   - 适用条件：Configure local development environment with API keys, virtual environment, and pre-commit hooks for code quality enforcement. Bundles environment variable configuration, Python virtual environment activation, and pre-commit hook installation into one reproducible session-level workflow.
32. [Entity Decorator Factory Pattern](通用技能领域/Family技能/未分类技能/二级技能/Entity Decorator Factory Pattern/SKILL.md)
   - 层级：二级技能
   - 类型：observability_instrumentation
   - 适用条件：Factory-based system for creating reusable decorators that instrument agent operations (agents, tasks, workflows, tools, guardrails, HTTP endpoints) with semantic span kinds for observability and tracing.
33. [Environment Metadata Collection](通用技能领域/Family技能/未分类技能/微技能/Environment Metadata Collection/SKILL.md)
   - 层级：微技能
   - 类型：agent_initialization
   - 适用条件：Automatically capture and log runtime environment details (OS type/version, Python version, anonymized hostname, SDK version) at agent startup for debugging and reproducibility.
34. [Error Handling and Logging Protocol](通用技能领域/Family技能/未分类技能/微技能/Error Handling and Logging Protocol/SKILL.md)
   - 层级：微技能
   - 类型：error_management
   - 适用条件：Standardize error handling by using specific exception types, logging errors with meaningful messages, and including context in error reports. Apply when implementing error paths or reviewing exception handling.
35. [Exit Handler Registration for Trace Cleanup](通用技能领域/Family技能/未分类技能/微技能/Exit Handler Registration for Trace Cleanup/SKILL.md)
   - 层级：微技能
   - 类型：resource_management
   - 适用条件：Register a single atexit handler to ensure trace cleanup occurs on process termination, preventing duplicate handler registration through idempotent flag checking.
36. [Filesystem Mocking](通用技能领域/Family技能/未分类技能/微技能/Filesystem Mocking/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Create and manipulate fake filesystem objects in tests using pyfakefs to avoid side effects on real disk. Isolates filesystem operations by intercepting file I/O calls and routing them to an in-memory fake filesystem.
37. [Future State Transition Control](通用技能领域/Family技能/未分类技能/微技能/Future State Transition Control/SKILL.md)
   - 层级：微技能
   - 类型：concurrent_task_lifecycle
   - 适用条件：Synchronize current session and trace context state to legacy module globals for backward compatibility. Handles ImportError gracefully when legacy module is unavailable.
38. [Graceful Trace Shutdown on Process Exit](通用技能领域/Family技能/未分类技能/微技能/Graceful Trace Shutdown on Process Exit/SKILL.md)
   - 层级：微技能
   - 类型：trace_lifecycle_management
   - 适用条件：Registers and executes a global atexit handler to cleanly end an auto-initialized trace context when the application shuts down, preventing resource leaks and incomplete trace records.
39. [HTTP Interaction Recording and Replay with VCR](通用技能领域/Family技能/未分类技能/微技能/HTTP Interaction Recording and Replay with VCR/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Record and replay HTTP interactions in tests using VCR to eliminate external API calls and ensure test reproducibility. Captures request/response pairs on first run and replays them in subsequent runs without making network calls.
40. [HTTP Request Mocking](通用技能领域/Family技能/未分类技能/微技能/HTTP Request Mocking/SKILL.md)
   - 层级：微技能
   - 类型：test_isolation
   - 适用条件：Mock HTTP requests at the client level using requests_mock to inject predefined responses without network calls. Use when test code calls HTTP client methods and response content or status code must be controlled deterministically.
41. [Identify CLS causes using DevTools and Performance Observer](通用技能领域/Family技能/未分类技能/二级技能/Identify CLS causes using DevTools and Performance Observer/SKILL.md)
   - 层级：二级技能
   - 类型：web_performance_debugging
   - 适用条件：Systematic workflow for selecting and navigating dashboard views to inspect agent execution, span relationships, and LLM interactions. Enables review of session performance across Timeline, Tree, Message, and Analytics modes.
42. [Instrumentor Instance Factory](通用技能领域/Family技能/未分类技能/微技能/Instrumentor Instance Factory/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation_setup
   - 适用条件：Create and return a new instance of a specified instrumentor class from a dynamically loaded module. Encapsulates the instantiation logic for instrumentation handlers.
43. [InstrumentorLoader Configuration](通用技能领域/Family技能/未分类技能/一级技能/InstrumentorLoader Configuration/SKILL.md)
   - 层级：一级技能
   - 类型：observability_instrumentation
   - 适用条件：Encapsulates metadata and instantiation contract for dynamically loading instrumentor classes. Validates package version constraints and provides module name, class name, and minimum version required for safe instrumentation.
44. [Job Description Writer Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Job Description Writer Agent Setup/SKILL.md)
   - 层级：微技能
   - 类型：job_description_generation
   - 适用条件：Configures a writer agent with web search, Serper, and file read tools to craft engaging job postings using research insights. Invoke after research phase to generate initial job description draft.
45. [Jupyter Notebook to MDX Documentation Conversion](通用技能领域/Family技能/未分类技能/二级技能/Jupyter Notebook to MDX Documentation Conversion/SKILL.md)
   - 层级：二级技能
   - 类型：documentation_generation
   - 适用条件：Automated workflow to convert Jupyter notebooks into MDX documentation files, handling frontmatter, GitHub links, code formatting, and installation sections. Orchestrates notebook transformation from examples/ directory into publishable docs/v2/examples/ MDX files.
46. [LangChain Agent Integration with AgentOps Callback Handler](通用技能领域/Family技能/未分类技能/二级技能/LangChain Agent Integration with AgentOps Callback Handler/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Initialize and configure AgentOps callback handler for LangChain LLM instances to automatically record agent sessions, LLM calls, and tool usage.
47. [LiteLLM Integration Setup](通用技能领域/Family技能/未分类技能/二级技能/LiteLLM Integration Setup/SKILL.md)
   - 层级：二级技能
   - 类型：llm_integration
   - 适用条件：Configure and install AgentOps support for LiteLLM (>=1.3.1) to enable unified access to 100+ language models through a standardized Input/Output interface.
48. [LLM Event Capture and Error Handling](通用技能领域/Family技能/未分类技能/微技能/LLM Event Capture and Error Handling/SKILL.md)
   - 层级：微技能
   - 类型：event_instrumentation
   - 适用条件：Captures LLM request/response lifecycle events (parameters, outputs, timestamps) and wraps exceptions in error events for safe recording. Use when instrumenting LLM API calls to build an audit trail of interactions and failures.
49. [LLM Provider Integration Pattern](通用技能领域/Family技能/未分类技能/二级技能/LLM Provider Integration Pattern/SKILL.md)
   - 层级：二级技能
   - 类型：llm_provider_integration
   - 适用条件：Establish a reusable provider class that inherits from BaseProvider, implements required LLM response handling methods, and manages event tracking for prompts, tokens, and errors.
50. [Mistral SDK Agent Tracking Setup](通用技能领域/Family技能/未分类技能/二级技能/Mistral SDK Agent Tracking Setup/SKILL.md)
   - 层级：二级技能
   - 类型：agent_integration
   - 适用条件：Configure and initialize AgentOps integration with Mistral Python SDK (>=0.32.0) to enable agent activity tracking and monitoring.
51. [Module Availability and Version Check](通用技能领域/Family技能/未分类技能/微技能/Module Availability and Version Check/SKILL.md)
   - 层级：微技能
   - 类型：dependency_validation
   - 适用条件：Verify that a required Python package or module is installed and meets minimum version requirements before attempting to use it. Returns a boolean indicating readiness for instrumentation or import.
52. [Multi-Agent Crew Execution with Session Tracing](通用技能领域/Family技能/未分类技能/二级技能/Multi-Agent Crew Execution with Session Tracing/SKILL.md)
   - 层级：二级技能
   - 类型：agent_orchestration
   - 适用条件：Orchestrate multiple specialized agents in a crew workflow and record the complete execution trace with final state. Coordinates agent kickoff, captures results, and ends the session trace with success confirmation.
53. [Multi-Agent Job Description Generation Workflow](通用技能领域/Family技能/未分类技能/二级技能/Multi-Agent Job Description Generation Workflow/SKILL.md)
   - 层级：二级技能
   - 类型：job_description_generation
   - 适用条件：Orchestrates three specialized agents (Research Analyst, Job Description Writer, Review Specialist) in sequence to analyze company information, generate job postings, and refine them for quality and alignment with company values.
54. [Nested Operation Execution Tracking](通用技能领域/Family技能/未分类技能/微技能/Nested Operation Execution Tracking/SKILL.md)
   - 层级：微技能
   - 类型：observability_instrumentation
   - 适用条件：Track and record execution flow when decorated operations call other decorated operations, preserving call hierarchy and state across nesting levels.
55. [Notebook-Based Integration Testing](通用技能领域/Family技能/未分类技能/一级技能/Notebook-Based Integration Testing/SKILL.md)
   - 层级：一级技能
   - 类型：integration_testing
   - 适用条件：Automated workflow to test LLM provider integrations using Jupyter notebooks as executable integration tests. Verifies real-world usage patterns and end-to-end functionality across multiple Python versions and actual LLM APIs.
56. [Organize Test Data with Documentation](通用技能领域/Family技能/未分类技能/二级技能/Organize Test Data with Documentation/SKILL.md)
   - 层级：二级技能
   - 类型：testing_infrastructure
   - 适用条件：Create and maintain a dedicated test data directory structure with meaningful naming conventions and format documentation to ensure test data is discoverable, maintainable, and accessible across test suites.
57. [Package Import Interception and Instrumentation](通用技能领域/Family技能/未分类技能/一级技能/Package Import Interception and Instrumentation/SKILL.md)
   - 层级：一级技能
   - 类型：observability_instrumentation
   - 适用条件：Intercepts Python module imports and dynamically instruments matching packages with observability hooks. Replaces the built-in import function to detect and configure instrumentors for agentic libraries and their dependencies without modifying user code.
58. [Package Installation Detection](通用技能领域/Family技能/未分类技能/微技能/Package Installation Detection/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation_setup
   - 适用条件：Determine whether a Python module is an installed library (in site-packages) or a local module, to decide whether to apply instrumentation. Uses normalized path comparison against site-packages directories.
59. [Package Instrumentation Initialization](通用技能领域/Family技能/未分类技能/二级技能/Package Instrumentation Initialization/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation_setup
   - 适用条件：Conditionally start monitoring and instrumenting Python packages using import hooks, with safeguards to prevent redundant or conflicting instrumentation of agentic libraries.
60. [Parallel Task Completion Polling](通用技能领域/Family技能/未分类技能/二级技能/Parallel Task Completion Polling/SKILL.md)
   - 层级：二级技能
   - 类型：concurrent_coordination
   - 适用条件：Initialize AgentOps client with optional automatic session and trace startup. Configures internal state, optionally starts tracing, and returns a session handle or None based on auto_start_session setting.
61. [Pre-commit Hook Installation](通用技能领域/Family技能/未分类技能/微技能/Pre-commit Hook Installation/SKILL.md)
   - 层级：微技能
   - 类型：code_quality_enforcement
   - 适用条件：Configures and installs pre-commit hooks to enforce code quality and compliance checks before each commit. Ensures consistent code standards across the development team.
62. [ProcessPoolExecutor Initialization with Worker Setup](通用技能领域/Family技能/未分类技能/二级技能/ProcessPoolExecutor Initialization with Worker Setup/SKILL.md)
   - 层级：二级技能
   - 类型：parallel_task_execution
   - 适用条件：Initializes the AgentOps SDK with environment variables or defaults when not yet initialized. Handles initialization failures gracefully by logging warnings and errors, returning None if initialization cannot proceed. Use this as a guard before starting traces to ensure SDK readiness.
63. [ProcessPoolExecutor Worker Lifecycle Configuration](通用技能领域/Family技能/未分类技能/微技能/ProcessPoolExecutor Worker Lifecycle Configuration/SKILL.md)
   - 层级：微技能
   - 类型：pool_configuration
   - 适用条件：Initialize AgentOps client with API key loaded from environment variables and configure session lifecycle management for decorator-based tracing.
64. [Project Dependency Installation](通用技能领域/Family技能/未分类技能/微技能/Project Dependency Installation/SKILL.md)
   - 层级：微技能
   - 类型：environment_setup
   - 适用条件：Installs project dependencies in editable mode to enable local development and testing. Execute after branch setup and before running development tasks.
65. [Provider Method Override and Restoration](通用技能领域/Family技能/未分类技能/微技能/Provider Method Override and Restoration/SKILL.md)
   - 层级：微技能
   - 类型：llm_provider_integration
   - 适用条件：Patch and restore LLM provider methods to enable transparent event capture (prompts, completions, tokens, timestamps, errors, tool usage) without modifying client code. Implements override() to inject wrapper functions and undo_override() to restore original methods.
66. [Provider Test Coverage Checklist](通用技能领域/Family技能/未分类技能/二级技能/Provider Test Coverage Checklist/SKILL.md)
   - 层级：二级技能
   - 类型：integration_testing
   - 适用条件：Structured checklist defining required test scenarios for each LLM provider integration: basic completion calls, streaming responses, async operations, error handling, and tool usage. Use when onboarding a new provider or reviewing test completeness.
67. [Python Code Style and Documentation Enforcement](通用技能领域/Family技能/未分类技能/二级技能/Python Code Style and Documentation Enforcement/SKILL.md)
   - 层级：二级技能
   - 类型：code_review
   - 适用条件：Enforce consistent Python code formatting, type hints, and documentation standards using Black formatter and structured docstrings during code review and development to maintain codebase quality.
68. [Read Timestamp Extension with Delta Overflow Handling](通用技能领域/Family技能/未分类技能/微技能/Read Timestamp Extension with Delta Overflow Handling/SKILL.md)
   - 层级：微技能
   - 类型：timestamp_extension
   - 适用条件：Determine whether a software package should be instrumented for monitoring by evaluating three conditions: whether it is already instrumented by AgentOps, whether it is a targeted agentic library, and whether it is a known provider. Returns a boolean decision to proceed with or skip instrumentation.
69. [Research Analyst Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Research Analyst Agent Setup/SKILL.md)
   - 层级：微技能
   - 类型：job_description_generation
   - 适用条件：Configures a research-focused agent with web search and Serper tools to extract company culture, values, and specific hiring needs from websites and descriptions. Invoke as the first stage to gather insights before job description drafting.
70. [Review and Editing Specialist Agent Setup](通用技能领域/Family技能/未分类技能/微技能/Review and Editing Specialist Agent Setup/SKILL.md)
   - 层级：微技能
   - 类型：job_description_generation
   - 适用条件：Configures a review agent with web search, Serper, and file read tools to refine job postings for clarity, grammar, engagement, and company value alignment. Invoke as final stage to polish and validate job description.
71. [Reward Function Contract Definition](通用技能领域/Family技能/未分类技能/微技能/Reward Function Contract Definition/SKILL.md)
   - 层级：微技能
   - 类型：reward_function_design
   - 适用条件：Register a callable tool function with cost annotation using the @tool decorator, enabling cost-aware tool invocation and automatic cost tracking in agent workflows.
72. [Session Overview Meta-Analysis](通用技能领域/Family技能/未分类技能/二级技能/Session Overview Meta-Analysis/SKILL.md)
   - 层级：二级技能
   - 类型：session_debugging
   - 适用条件：Aggregate and display summary statistics and trends across all recorded sessions in a single consolidated view for high-level performance and behavior pattern analysis.
73. [Session Span Initialization](通用技能领域/Family技能/未分类技能/微技能/Session Span Initialization/SKILL.md)
   - 层级：微技能
   - 类型：observability_setup
   - 适用条件：Decorator-based pattern to create a root session span that wraps and tracks all nested operations within a workflow function. Establishes the observability root context for end-to-end operation tracking.
74. [Session Tagging and Organization](通用技能领域/Family技能/未分类技能/微技能/Session Tagging and Organization/SKILL.md)
   - 层级：微技能
   - 类型：session_management
   - 适用条件：A micro-skill for adding and managing tags during AgentOps session initialization or startup to organize, filter, and categorize sessions by environment, application type, or service tier.
75. [Singleton Client Initialization with Re-initialization Guard](通用技能领域/Family技能/未分类技能/一级技能/Singleton Client Initialization with Re-initialization Guard/SKILL.md)
   - 层级：一级技能
   - 类型：client_lifecycle_management
   - 适用条件：Enforces single-instance Client lifecycle per process. Detects and safely handles re-initialization attempts with different API keys by resetting state and ending active traces. Manages trace context lifecycle across initialization cycles.
76. [Span Management with Attribute Tracking](通用技能领域/Family技能/未分类技能/微技能/Span Management with Attribute Tracking/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata.
77. [Spring Boot 2.x to 3.0 Instrumentation Migration Reference](通用技能领域/Family技能/未分类技能/一级技能/Spring Boot 2.x to 3.0 Instrumentation Migration Reference/SKILL.md)
   - 层级：一级技能
   - 类型：metrics_instrumentation
   - 适用条件：Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system.
78. [Spring Boot 3.0 Migration Sequencing](通用技能领域/Family技能/未分类技能/一级技能/Spring Boot 3.0 Migration Sequencing/SKILL.md)
   - 层级：一级技能
   - 类型：framework_upgrade
   - 适用条件：Ordered macro-protocol for migrating a Spring Boot 2.7.x application to 3.0. Executes pre-flight validation (latest 2.7.x version, dependency review, system requirements), deprecation removal, and incremental upgrade steps with properties migration support.
79. [Spring Boot 3.0 Session Management Configuration Migration](通用技能领域/Family技能/未分类技能/二级技能/Spring Boot 3.0 Session Management Configuration Migration/SKILL.md)
   - 层级：二级技能
   - 类型：software_migration
   - 适用条件：Initialize and manage an AgentOps session for a single user interaction with an agent. Automatically creates a session context when the init function is called, enabling telemetry collection and tracking throughout the interaction.
80. [Standard Metrics Recording](通用技能领域/Family技能/未分类技能/二级技能/Standard Metrics Recording/SKILL.md)
   - 层级：二级技能
   - 类型：instrumentation
   - 适用条件：Create and record standard metrics (token usage, duration) using StandardMetrics and MetricsRecorder for consistent observability across instrumentation implementations.
81. [Start Trace with Context](通用技能领域/Family技能/未分类技能/二级技能/Start Trace with Context/SKILL.md)
   - 层级：二级技能
   - 类型：tracing
   - 适用条件：Initiates a new root span (trace) with a user-provided name and optional tags, returning a TraceContext object for concurrent, user-managed tracing sessions.
82. [StreamExecutionEnvironment Setup](通用技能领域/Family技能/未分类技能/微技能/StreamExecutionEnvironment Setup/SKILL.md)
   - 层级：微技能
   - 类型：flink_setup
   - 适用条件：Compose @agent and @operation decorators in proper nesting order to establish correct parent-child span relationships and execution context hierarchy in observability instrumentation.
83. [StreamExecutionEnvironment Setup](通用技能领域/Family技能/未分类技能/二级技能/StreamExecutionEnvironment Setup-2/SKILL.md)
   - 层级：二级技能
   - 类型：stream_initialization
   - 适用条件：Establishes a clean feature branch from upstream main before starting development work. Ensures local repository is synchronized and isolated for new feature implementation.
84. [Streaming Response Instrumentation](通用技能领域/Family技能/未分类技能/微技能/Streaming Response Instrumentation/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Wrap streaming methods with instrumentation that extracts chunk content and tracks streaming lifecycle. Emits spans for each chunk with extracted content and stream metadata.
85. [Test Dependency Declaration](通用技能领域/Family技能/未分类技能/微技能/Test Dependency Declaration/SKILL.md)
   - 层级：微技能
   - 类型：test_orchestration
   - 适用条件：Declare and enforce test execution order using pytest markers to ensure prerequisite tests run before dependent tests.
86. [Third-Party Script Performance Optimization](通用技能领域/Family技能/未分类技能/二级技能/Third-Party Script Performance Optimization/SKILL.md)
   - 层级：二级技能
   - 类型：asset_optimization
   - 适用条件：Structured workflow for running unit tests at different scopes (all tests, specific files, with coverage reporting). Use when validating code changes or preparing for deployment.
87. [Thread-Safe Singleton Client Initialization](通用技能领域/Family技能/未分类技能/微技能/Thread-Safe Singleton Client Initialization/SKILL.md)
   - 层级：微技能
   - 类型：resource_initialization
   - 适用条件：Implements double-checked locking pattern to safely instantiate and return a singleton Client instance across multiple threads without race conditions.
88. [Token Usage Extraction and Attribution](通用技能领域/Family技能/未分类技能/微技能/Token Usage Extraction and Attribution/SKILL.md)
   - 层级：微技能
   - 类型：instrumentation
   - 适用条件：Extract token usage metrics from LLM/API responses and record them as span attributes for observability and cost tracking. Parses response metadata using TokenUsageExtractor and applies prompt/completion token counts to active instrumentation spans.
89. [Tool Definition and Callback Registration for Agent Monitoring](通用技能领域/Family技能/未分类技能/微技能/Tool Definition and Callback Registration for Agent Monitoring/SKILL.md)
   - 层级：微技能
   - 类型：tool_instrumentation
   - 适用条件：Define reusable tools with type hints and register AgentOps callback handlers to each tool for granular execution tracking and visibility into tool invocations.
90. [Trace Context Lifecycle Management on Re-initialization](通用技能领域/Family技能/未分类技能/微技能/Trace Context Lifecycle Management on Re-initialization/SKILL.md)
   - 层级：微技能
   - 类型：trace_lifecycle_management
   - 适用条件：Detects active trace recording and cleanly ends the trace context when Client is re-initialized with a different API key. Logs warnings and resets trace state to prevent orphaned spans.
91. [Trace Grouping for Operation Sequencing](通用技能领域/Family技能/未分类技能/微技能/Trace Grouping for Operation Sequencing/SKILL.md)
   - 层级：微技能
   - 类型：agent_operation_instrumentation
   - 适用条件：Use @trace decorator or manual trace management to group and record sequences of agent operations as logical units of work. Essential when auto_start_session=False to ensure data capture.
92. [Trace Lifecycle Management](通用技能领域/Family技能/未分类技能/二级技能/Trace Lifecycle Management/SKILL.md)
   - 层级：二级技能
   - 类型：agent_debugging
   - 适用条件：Initialize, finalize, and update metadata for execution traces in agent debugging workflows. Manages trace context, state transitions, and metadata enrichment across the complete trace lifecycle.
93. [Trace Metadata Update](通用技能领域/Family技能/未分类技能/微技能/Trace Metadata Update/SKILL.md)
   - 层级：微技能
   - 类型：trace_instrumentation
   - 适用条件：Programmatically inject or update execution metadata into an active trace during agent processing. Enriches trace logs with runtime context such as operation name, processing stage, record counts, user ID, and custom tags for debugging and monitoring.
94. [Trace State Finalization](通用技能领域/Family技能/未分类技能/微技能/Trace State Finalization/SKILL.md)
   - 层级：微技能
   - 类型：agent_debugging
   - 适用条件：Close an active trace and record its final state (success, failure, or custom status). Handles optional trace context and ensures all active session spans are properly terminated.
95. [Understand Virtual Hub Routing Architecture](通用技能领域/Family技能/未分类技能/一级技能/Understand Virtual Hub Routing Architecture/SKILL.md)
   - 层级：一级技能
   - 类型：network_routing_knowledge
   - 适用条件：Locate and apply framework-native AgentOps instrumentation patterns for a target agent framework (Llama Stack, SwarmZero, CrewAI, LangChain, Anthropic, Mistral, etc.). Use when adding observability to an existing framework-based agent system. Consult the curated reference of supported frameworks (OpenAI, Anthropic, CrewAI, Langchain, Cohere, Mistral, LiteLLM, LlamaIndex, and others) with links to integration guides and official documentation.
96. [Update Ehcache to Jakarta EE 9 Classifier](通用技能领域/Family技能/未分类技能/微技能/Update Ehcache to Jakarta EE 9 Classifier/SKILL.md)
   - 层级：微技能
   - 类型：dependency_management
   - 适用条件：Initialize the AgentOps client in 2 lines of code to automatically capture and replay LLM session analytics and call traces.
97. [VCR Cassette Management for API Testing](通用技能领域/Family技能/未分类技能/二级技能/VCR Cassette Management for API Testing/SKILL.md)
   - 层级：二级技能
   - 类型：testing_infrastructure
   - 适用条件：Record, sanitize, and manage HTTP interactions using VCR cassettes stored in tests/cassettes/. Enables reproducible API testing without live external calls by capturing request/response pairs, removing sensitive data, and versioning cassettes to track API changes.
98. [Web Font Rendering Strategy Selection](通用技能领域/Family技能/未分类技能/微技能/Web Font Rendering Strategy Selection/SKILL.md)
   - 层级：微技能
   - 类型：web_font_rendering
   - 适用条件：Capture and log LLM interaction events including prompts, completions, token usage, timestamps, errors, and tool usage to enable debugging and monitoring of LLM provider activity.
99. [Workflow Tracing and Tagging](通用技能领域/Family技能/未分类技能/二级技能/Workflow Tracing and Tagging/SKILL.md)
   - 层级：二级技能
   - 类型：workflow_instrumentation
   - 适用条件：Wrap a multi-step workflow function with the @trace decorator to enable end-to-end logging, tagging, and observability across agent and tool calls.
