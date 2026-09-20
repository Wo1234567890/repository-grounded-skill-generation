# TicToc Concurrency Control Protocol 子技能地图

## 子技能列表

- [Agent Failure Detection and Response](通用技能领域/Family技能/未分类技能/二级技能/Agent Failure Detection and Response/SKILL.md) ｜ 二级技能
  - 适用：Identify, classify, and respond to agent failures and multi-agent interaction issues in real time. Monitors live agent sessions for anomalies, errors, and unexpected behavior, then triggers appropriate escalation or remediation actions.
  - 线索：Agent is running in production, Anomalies or errors detected in session telemetry, Unexpected agent behavior observed in live monitoring, agent_monitoring, failure_detection
- [LLM Alignment Method Comparative Evaluation](通用技能领域/Family技能/未分类技能/二级技能/LLM Alignment Method Comparative Evaluation/SKILL.md) ｜ 二级技能
  - 适用：Apply @operation and @session decorators to functions and methods to automatically record inputs, outputs, exceptions, and support async/generator execution with minimal code overhead.
  - 线索：Comparing multiple preference-based alignment methods, Validating training stability and output quality, Detecting unintended behaviors like length exploitation, observability, instrumentation
- [LLM and API Cost Monitoring](通用技能领域/Family技能/未分类技能/二级技能/LLM and API Cost Monitoring/SKILL.md) ｜ 二级技能
  - 适用：Track and manage spending on LLM and API calls to prevent budget overruns and optimize resource allocation. Provides real-time cost metrics, spending alerts, and budget guardrails for agent sessions.
  - 线索：Agent makes frequent LLM or API calls; budget constraints exist; cost optimization is required, cost_control, budget_management, observability, financial_metrics
- [ProcessPoolExecutor Setup and Execution](通用技能领域/Family技能/未分类技能/二级技能/ProcessPoolExecutor Setup and Execution/SKILL.md) ｜ 二级技能
  - 适用：Wraps a workflow function with @session decorator to establish a monitoring session for agent execution. Creates and manages a session context for agent workflow execution, enabling centralized logging and session tracking across multiple agent operations.
  - 线索：Need to parallelize CPU-intensive operations across multiple cores, Tasks are independent and do not require shared mutable state, GIL contention is a performance bottleneck, session_management, workflow_initialization
- [Semantic Attribute Capture and Documentation](通用技能领域/Family技能/未分类技能/二级技能/Semantic Attribute Capture and Documentation/SKILL.md) ｜ 二级技能
  - 适用：Session-level workflow for identifying, capturing, and documenting all attributes that an instrumentor should extract from API calls using semantic convention standards. Ensures consistent attribute naming and documentation across instrumentors by mapping API response fields to standard semantic attributes with inline code comments.
  - 线索：Designing a new instrumentor, Need to map API response fields to standard semantic attributes, Documenting what data is captured, instrumentation, semantic_conventions
- [Session Drilldown Analysis](通用技能领域/Family技能/未分类技能/二级技能/Session Drilldown Analysis/SKILL.md) ｜ 二级技能
  - 适用：Review and analyze a recorded agent session by examining LLM calls, action events, tool calls, errors, and execution timeline in a waterfall view. Use this to debug agent behavior and understand event sequences.
  - 线索：Need to understand what happened in a past agent execution, Require inspection of LLM prompts and completions, Tracing the sequence of events that led to an error or unexpected behavior, debugging, session_analysis
