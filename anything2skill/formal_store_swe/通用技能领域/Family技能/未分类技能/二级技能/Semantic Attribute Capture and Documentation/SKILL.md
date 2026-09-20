---
id: "533b0a44-f1a4-550a-adac-5e6d4d165112"
name: "Semantic Attribute Capture and Documentation"
description: "Session-level workflow for identifying, capturing, and documenting all attributes that an instrumentor should extract from API calls using semantic convention standards. Ensures consistent attribute naming and documentation across instrumentors by mapping API response fields to standard semantic attributes with inline code comments."
version: "0.1.0"
tags:
  - "instrumentation"
  - "semantic_conventions"
  - "documentation"
  - "api_integration"
  - "attribute_mapping"
  - "未分类技能"
  - "profile:default::未分类技能"
  - "kind:parent"
triggers:
  - "Designing a new instrumentor"
  - "Need to map API response fields to standard semantic attributes"
  - "Documenting what data is captured"
---

# Semantic Attribute Capture and Documentation

Session-level workflow for identifying, capturing, and documenting all attributes that an instrumentor should extract from API calls using semantic convention standards. Ensures consistent attribute naming and documentation across instrumentors by mapping API response fields to standard semantic attributes with inline code comments.

## Prompt

When designing a new instrumentor: (1) Identify all API response fields that should be captured. (2) Map each field to the corresponding semantic convention attribute from the standard library (e.g., agentops.semconv). (3) Document each captured attribute with an inline code comment explaining its purpose and semantic meaning. (4) Verify that attribute names follow the semantic convention naming scheme. (5) Ensure documentation is complete and accessible to other developers using this instrumentor.

## Objective

Ensure consistent semantic attribute naming and documentation across instrumentors
## Applicable Signals

- Designing a new instrumentor
- Need to map API response fields to standard semantic attributes
- Documentation of captured data is required
- Onboarding new instrumentation patterns

## Contraindications

- No semantic convention standard is available or applicable
- Attributes are one-off and non-reusable across instrumentors
- Documentation is not required or not feasible
- API contract is unstable or undocumented

## Workflow Steps

- {'step': 1, 'action': 'Identify API response fields', 'detail': 'List all fields returned by the API endpoint or method being instrumented'}
- {'step': 2, 'action': 'Map to semantic convention attributes', 'detail': 'For each field, find the corresponding attribute in the semantic convention standard library (e.g., agentops.semconv)'}
- {'step': 3, 'action': 'Document with inline comments', 'detail': 'Add code comments above each captured attribute explaining its purpose, semantic meaning, and relationship to the API field'}
- {'step': 4, 'action': 'Verify naming consistency', 'detail': 'Ensure all attribute names follow the semantic convention naming scheme and are consistent with other instrumentors'}
- {'step': 5, 'action': 'Validate documentation completeness', 'detail': 'Review documentation for clarity and ensure it is accessible to developers using or extending this instrumentor'}

## Constraints

- Attribute names must conform to the semantic convention standard
- Documentation must be inline and co-located with attribute capture code
- All captured attributes must have a documented purpose
- Mapping must be traceable from API field to semantic attribute

## Cautions

- Do not rename semantic attributes to match local naming conventions; use the standard names
- Do not skip documentation for attributes that seem self-evident; clarity aids maintenance
- Do not capture attributes that are not defined in the semantic convention standard without explicit justification

## Output Contract

- Documented list of captured attributes with semantic convention mappings and inline code comments explaining each attribute's purpose, ready for code review and integration into the instrumentor implementation

## 子技能目录
- [Span Management with Attribute Tracking](通用技能领域/Family技能/未分类技能/微技能/Span Management with Attribute Tracking/SKILL.md) ｜ 适用：Create and manage instrumentation spans with consistent attribute assignment using SpanAttributeManager and create_span context manager. Use when instrumenting operations that need distributed tracing and attribute metadata.

## 选用规则（微技能目录）
- 当目标、阶段或方法更接近 `Span Management with Attribute Tracking` 时，优先调用它。 线索：Instrumenting a discrete operation that requires tracing context, Need to assign and track attribute metadata on a span, Require consistent span lifecycle management across operations, instrumentation, distributed-tracing

## Files

- `references/children_manifest.json`
- `references/children_map.md`
- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Designing a new instrumentor
- Need to map API response fields to standard semantic attributes
- Documenting what data is captured
