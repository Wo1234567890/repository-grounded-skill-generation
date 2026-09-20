---
id: "7e3d87d6-6dab-5e89-927c-6191378be8fe"
name: "Semantic Span Kind Reference"
description: "Canonical enumeration and mapping of semantic span kinds (AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP) used to classify instrumentation points in agent systems. Provides taxonomy for selecting appropriate decorators and instrumentation classification."
version: "0.1.0"
tags:
  - "instrumentation"
  - "span_classification"
  - "semantic_taxonomy"
  - "decorator_reference"
  - "observability"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Selecting or defining instrumentation decorators"
  - "Need to understand what span kinds are available and their semantics"
---

# Semantic Span Kind Reference

Canonical enumeration and mapping of semantic span kinds (AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP) used to classify instrumentation points in agent systems. Provides taxonomy for selecting appropriate decorators and instrumentation classification.

## Prompt

Consult this reference when selecting instrumentation decorators or classifying execution spans. Each span kind maps to a specific entity or operation type: AGENT for agent instances, TASK for task execution, OPERATION for discrete operations, WORKFLOW for multi-step workflows, SESSION for trace sessions, TOOL for tool invocations, GUARDRAIL for safety constraints, and HTTP for endpoint calls.

## Objective

Provide canonical span-kind taxonomy for decorator and instrumentation selection
## Applicable Signals

- Need to select or define instrumentation decorators
- Require understanding of available span kinds and their semantics
- Designing instrumentation strategy for agent system

## Contraindications

- Custom span kinds outside the standard set are required
- Instrumentation does not use semantic span classification
- Runtime span kind selection based on dynamic conditions

## Constraints

- Reference is static; does not execute instrumentation
- Span kinds are predefined and immutable
- Applies to systems using agentops semantic conventions

## Cautions

- Do not use this reference for runtime span kind generation; use decorator factory instead
- Span kind selection should align with actual entity or operation type being instrumented

## Output Contract

- Clear reference of available span kinds and their intended use contexts. Caller receives canonical mapping: AGENT, TASK, OPERATION, WORKFLOW, SESSION, TOOL, GUARDRAIL, HTTP with semantic meaning for each.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Selecting or defining instrumentation decorators
- Need to understand what span kinds are available and their semantics
