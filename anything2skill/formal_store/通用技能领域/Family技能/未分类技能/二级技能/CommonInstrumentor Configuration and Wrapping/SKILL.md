---
id: "68d2ebdb-9167-542f-8604-e8b7fac3db57"
name: "CommonInstrumentor Configuration and Wrapping"
description: "Configure and instantiate a CommonInstrumentor with InstrumentorConfig and WrapConfig to create reusable instrumentation templates for LLM providers and agentic frameworks."
version: "0.1.0"
tags:
  - "instrumentation"
  - "opentelemetry"
  - "llm_provider"
  - "agentic_framework"
  - "telemetry"
  - "configuration"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Adding support for a new LLM provider (OpenAI, Anthropic, Google GenAI, IBM WatsonX, etc.)"
  - "Adding support for a new agentic framework (CrewAI, AutoGen, Agno, Mem0, smolagents, etc.)"
  - "A standardized instrumentation pattern is needed for telemetry collection"
---

# CommonInstrumentor Configuration and Wrapping

Configure and instantiate a CommonInstrumentor with InstrumentorConfig and WrapConfig to create reusable instrumentation templates for LLM providers and agentic frameworks.

## Prompt

Import CommonInstrumentor, InstrumentorConfig, and WrapConfig from agentops.instrumentation.common. Define InstrumentorConfig with target library name and version constraints. Create WrapConfig instances specifying which methods to wrap and their attribute handlers. Instantiate CommonInstrumentor with the config objects. The instrumentor is then ready to wrap target library methods and extract telemetry attributes.

## Objective

Set up a reusable instrumentation template for a specific LLM provider or agentic library
## Applicable Signals

- New library integration requirement
- Need for OpenTelemetry instrumentation
- Method-level telemetry extraction needed

## Contraindications

- Instrumentation for the target library is already complete
- Target library version is below the minimum supported version
- Library does not expose wrappable methods

## Workflow Steps

- {'step': 1, 'action': 'Import CommonInstrumentor, InstrumentorConfig, and WrapConfig', 'detail': 'from agentops.instrumentation.common import CommonInstrumentor, InstrumentorConfig, WrapConfig'}
- {'step': 2, 'action': 'Define InstrumentorConfig with library metadata', 'detail': 'Specify target library name, version constraints, and initialization parameters'}
- {'step': 3, 'action': 'Create WrapConfig instances for target methods', 'detail': 'For each method to instrument, define WrapConfig with method path and attribute handler'}
- {'step': 4, 'action': 'Define attribute handlers', 'detail': 'Create handler functions that extract telemetry attributes from args, kwargs, and return values; return AttributeMap'}
- {'step': 5, 'action': 'Instantiate CommonInstrumentor', 'detail': 'Pass InstrumentorConfig and list of WrapConfig objects to CommonInstrumentor constructor'}
- {'step': 6, 'action': 'Verify instrumentor is ready', 'detail': 'Confirm CommonInstrumentor instance is created and ready to wrap methods'}

## Constraints

- InstrumentorConfig must specify a supported library name
- WrapConfig must reference methods that exist in the target library
- Attribute handlers must return AttributeMap objects
- CommonInstrumentor must be instantiated before wrapping begins

## Cautions

- Verify target library version meets minimum requirements before configuration
- Attribute handlers should gracefully handle missing return values or kwargs
- Do not configure multiple instrumentors for the same library in the same session

## Output Contract

- CommonInstrumentor instance is created with InstrumentorConfig and WrapConfig, ready to instrument target library methods and extract attributes. The instrumentor can be used to wrap methods and collect telemetry data.

## 子技能目录
- [Attribute Extraction from Method Calls](通用技能领域/Family技能/未分类技能/微技能/Attribute Extraction from Method Calls/SKILL.md) ｜ 适用：Extract telemetry attributes (e.g., model name, token usage) from LLM method arguments and return values using a structured AttributeMap handler. Normalizes observable metadata into OpenTelemetry-compliant keys for downstream observability systems.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Attribute Extraction from Method Calls` 时，优先调用它。 线索：An instrumented LLM method is called; args, kwargs, or return_value contain model, usage, or other observable metadata., observability, telemetry, instrumentation, attribute_extraction

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Adding support for a new LLM provider (OpenAI, Anthropic, Google GenAI, IBM WatsonX, etc.)
- Adding support for a new agentic framework (CrewAI, AutoGen, Agno, Mem0, smolagents, etc.)
- A standardized instrumentation pattern is needed for telemetry collection
