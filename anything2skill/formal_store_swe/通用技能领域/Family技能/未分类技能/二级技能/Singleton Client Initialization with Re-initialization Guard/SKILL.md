---
id: "cf2aafba-8a0b-5349-96e3-578d8595f10b"
name: "Singleton Client Initialization with Re-initialization Guard"
description: "Ensures a single Client instance is created and safely re-initialized only when a different API key is explicitly provided, preventing unintended state conflicts and cleaning up trace context on re-init."
version: "0.1.0"
tags:
  - "singleton"
  - "initialization"
  - "client_lifecycle"
  - "api_key_management"
  - "trace_cleanup"
  - "re-initialization_guard"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "First instantiation of Client class"
  - "Subsequent access to Client instance"
  - "Re-initialization attempt with different API key"
---

# Singleton Client Initialization with Re-initialization Guard

Ensures a single Client instance is created and safely re-initialized only when a different API key is explicitly provided, preventing unintended state conflicts and cleaning up trace context on re-init.

## Prompt

1. Check if Client instance already exists via __new__; if not, create one and initialize trace context holders to None.
2. In __init__, verify _initialized flag; if not set, create Config and set _initialized to False.
3. Extract provided_api_key from kwargs; if Client is already initialized and a different non-None API key is provided, log warning, reset _initialized, end any active trace, and clear trace context.
4. If already initialized and auto_start_session is true, return existing legacy session wrapper; otherwise return None.
5. If no API key is configured, raise NoApiKeyException.
6. Return the singleton Client instance with _initialized set to True.

## Objective

Initialize and manage singleton Client lifecycle with API key change detection and trace cleanup
## Applicable Signals

- cls.__instance is None (first creation)
- provided_api_key differs from self.config.api_key
- self.initialized is True and auto_start_session is True

## Contraindications

- Attempting to create multiple independent Client instances
- Re-initializing with the same API key (should return existing instance without reset)
- No API key provided or configured

## Workflow Steps

- {'step': 1, 'action': 'Check singleton instance existence', 'detail': 'In __new__, if cls.__instance is None, create new instance and initialize _init_trace_context and _legacy_session_for_init_trace to None'}
- {'step': 2, 'action': 'Initialize configuration', 'detail': 'In __init__, if _initialized is not set or False, create Config() and set _initialized to False'}
- {'step': 3, 'action': 'Detect API key change', 'detail': 'Extract provided_api_key from kwargs; compare with self.config.api_key'}
- {'step': 4, 'action': 'Handle re-initialization', 'detail': 'If initialized and provided_api_key is not None and differs from config.api_key: log warning, reset _initialized, end active trace if recording, clear trace context holders'}
- {'step': 5, 'action': 'Return appropriate instance state', 'detail': 'If already initialized: return legacy session wrapper if auto_start_session is True, else return None; otherwise proceed to API key validation'}
- {'step': 6, 'action': 'Validate API key', 'detail': 'If self.config.api_key is not set, raise NoApiKeyException'}

## Constraints

- Only one Client instance may exist per process (singleton pattern enforced)
- Re-initialization with a different API key must explicitly provide api_key kwarg
- Trace context must be ended before re-initialization if recording

## Cautions

- Re-initialization with a different API key is logged as unusual; verify intent
- If auto_start_session is False and Client is already initialized, None is returned instead of instance

## Output Contract

- Single Client instance with _initialized flag set to True and config properly loaded; trace context cleaned up if re-initialization occurred; legacy session wrapper returned if auto_start_session is enabled and already initialized; NoApiKeyException raised if API key is missing

## 子技能目录
- [ProcessPoolExecutor Worker Lifecycle Configuration](通用技能领域/Family技能/未分类技能/微技能/ProcessPoolExecutor Worker Lifecycle Configuration/SKILL.md) ｜ 适用：Register and execute a global atexit handler that safely ends the client's auto-initialized trace context during application shutdown, with error recovery and resource cleanup.
- [Singleton Client Initialization](通用技能领域/Family技能/未分类技能/微技能/Singleton Client Initialization/SKILL.md) ｜ 适用：Initialize and manage a singleton Client instance for AgentOps service, ensuring only one active client exists throughout the application lifecycle.
- [Trace Context Cleanup on Re-initialization](通用技能领域/Family技能/未分类技能/微技能/Trace Context Cleanup on Re-initialization/SKILL.md) ｜ 适用：Ends any active trace recording and clears trace context when Client is re-initialized with a different API key, preventing orphaned or misattributed traces.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `ProcessPoolExecutor Worker Lifecycle Configuration` 时，优先调用它。 线索：Need to control fork vs. spawn behavior for worker processes, Require setup code (e.g., database connection) to run in each worker, Want to limit worker lifetime to prevent memory leaks, Must ensure consistent worker state across task batches, shutdown
- 当目标、阶段或方法更接近 `Singleton Client Initialization` 时，优先调用它。 线索：Application startup requires AgentOps client connection, First invocation of Client() constructor, singleton, initialization, client_lifecycle
- 当目标、阶段或方法更接近 `Trace Context Cleanup on Re-initialization` 时，优先调用它。 线索：Client re-initialization detected with a different API key, _init_trace_context is not None, _init_trace_context.span.is_recording() returns True, trace_cleanup, re-initialization

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- First instantiation of Client class
- Subsequent access to Client instance
- Re-initialization attempt with different API key
