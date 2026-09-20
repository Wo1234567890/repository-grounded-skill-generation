---
id: "168e9557-8fc3-577b-8f2b-21fe7a0c6ea5"
name: "LLM Alignment Method Comparative Evaluation"
description: "Apply @operation and @session decorators to functions and methods to automatically record inputs, outputs, exceptions, and support async/generator execution with minimal code overhead."
version: "0.1.3"
tags:
  - "observability"
  - "instrumentation"
  - "decorator"
  - "agent"
  - "session"
  - "operation"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Comparing multiple preference-based alignment methods"
  - "Validating training stability and output quality"
  - "Detecting unintended behaviors like length exploitation"
examples:
  - input: "Three alignment methods: SimPO, DPO, ORPO; baseline SFT model"
    output: "SimPO: 88.5 (AlpacaEval 2), 82.1 (Arena-Hard), avg length 245 tokens; DPO: 82.1 (AlpacaEval 2), 74.6 (Arena-Hard), avg length 240 tokens; improvement delta: +6.4 (AlpacaEval 2), +7.5 (Arena-Hard)"
    notes: "SimPO shows consistent advantage with minimal length exploitation compared to SFT and DPO"
---

# LLM Alignment Method Comparative Evaluation

Apply @operation and @session decorators to functions and methods to automatically record inputs, outputs, exceptions, and support async/generator execution with minimal code overhead.

## Prompt

Use @operation decorator on methods and @session decorator on entry-point functions to enable automatic observability. The decorators handle input/output recording, exception capture, and support async/await and generator functions without additional configuration.

## Objective

Enable observability of agent operations and sessions through declarative decorator application
## Applicable Signals

- Function or method requires execution tracing
- Exception handling and logging needed
- Async or generator function support required

## Contraindications

- Already using alternative instrumentation frameworks
- Decorators cannot be applied (e.g., built-in functions)
- Performance-critical hot loops where decorator overhead is unacceptable

## Workflow Steps

- Import @operation and @session decorators from instrumentation library
- Apply @operation decorator to methods requiring operation-level observability
- Apply @session decorator to top-level session entry-point functions
- Execute decorated function; decorator automatically captures inputs and outputs
- Decorator handles exceptions and records them without interrupting flow
- Verify input/output recording and exception logs in observability backend

## Constraints

- Decorator must be applied directly to target function or method definition
- Function signature must be compatible with decorator wrapping
- Async/await and generator support requires compatible Python version

## Cautions

- Decorator overhead may impact performance in tight loops; profile before use in latency-sensitive code
- Custom attributes and names on decorators must be set before function execution
- Exception handling by decorator may mask underlying errors; verify exception logs are accessible

## Output Contract

- Decorated function executes with automatic input/output recording, exception capture, and async/generator support enabled; execution metadata available to observability system

## 子技能目录
- [Async-Sync Method Wrapping](通用技能领域/Family技能/未分类技能/微技能/Async-Sync Method Wrapping/SKILL.md) ｜ 适用：Micro-skill for wrapping both synchronous and asynchronous versions of an API method using wrapt.wrap_function_wrapper, ensuring consistent instrumentation across sync and async call paths.
- [Bind Tools to LLM with Callback Tracking](通用技能领域/Family技能/未分类技能/微技能/Bind Tools to LLM with Callback Tracking/SKILL.md) ｜ 适用：Attach tool definitions to an LLM instance and ensure each tool has the AgentOps callback handler assigned so that tool invocations are recorded as observable spans during agent execution.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Async-Sync Method Wrapping` 时，优先调用它。 线索：API library exposes both sync and async versions of the same method, Need identical instrumentation logic for both sync and async paths, Implementing comprehensive API instrumentation, instrumentation, async
- 当目标、阶段或方法更接近 `Bind Tools to LLM with Callback Tracking` 时，优先调用它。 线索：Configuring an LLM-based agent that uses external tools, Before agent execution begins, When tools need to be bound to an LLM instance, agent_instrumentation, tool_binding

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Comparing multiple preference-based alignment methods
- Validating training stability and output quality
- Detecting unintended behaviors like length exploitation

## Examples

### Example 1

Input:

  Three alignment methods: SimPO, DPO, ORPO; baseline SFT model

Output:

  SimPO: 88.5 (AlpacaEval 2), 82.1 (Arena-Hard), avg length 245 tokens; DPO: 82.1 (AlpacaEval 2), 74.6 (Arena-Hard), avg length 240 tokens; improvement delta: +6.4 (AlpacaEval 2), +7.5 (Arena-Hard)

Notes:

  SimPO shows consistent advantage with minimal length exploitation compared to SFT and DPO
