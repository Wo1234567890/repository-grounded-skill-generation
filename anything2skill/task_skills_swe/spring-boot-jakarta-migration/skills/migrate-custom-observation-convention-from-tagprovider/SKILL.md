---
id: "3a3fe5d1-7b9d-5fce-b88a-cf4d2c0ba476"
name: "Migrate Custom Observation Convention from TagProvider"
description: "Replace deprecated TagProvider/TagContributor instrumentation with custom ServerRequestObservationConvention implementation. Reimplement custom metrics tagging using the new Observation convention pattern to preserve custom metric tags during Spring Boot 3.0 migration."
version: "0.1.0"
tags:
  - "spring-boot-3-migration"
  - "metrics"
  - "observation-api"
  - "deprecation-handling"
  - "instrumentation"
triggers:
  - "Custom TagProvider or TagContributor classes exist in codebase"
  - "Migrating to Spring Boot 3.0"
  - "Need to preserve custom metric tags"
examples:
  - input: "Existing custom TagProvider that adds 'custom.method' tag to metrics"
    output: "New ExtendedServerRequestObservationConvention class extending DefaultServerRequestObservationConvention with getLowCardinalityKeyValues() returning super values plus KeyValue.of('custom.method', context.getCarrier().getMethod())"
    notes: "Preserves default tags while adding custom tag"
  - input: "Custom TagContributor implementing full tag set"
    output: "New CustomServerRequestObservationConvention implementing ServerRequestObservationConvention with getName(), getContextualName(), and getLowCardinalityKeyValues() methods returning custom KeyValues"
    notes: "Full control over all tags; no inheritance from defaults"
---

# Migrate Custom Observation Convention from TagProvider

Replace deprecated TagProvider/TagContributor instrumentation with custom ServerRequestObservationConvention implementation. Reimplement custom metrics tagging using the new Observation convention pattern to preserve custom metric tags during Spring Boot 3.0 migration.

## Prompt

When you have custom TagProvider or TagContributor classes in your Spring Boot 2.x codebase, migrate them to Spring Boot 3.0 by extending DefaultServerRequestObservationConvention or implementing ServerRequestObservationConvention directly. Override getLowCardinalityKeyValues() to add custom KeyValue pairs, and override getContextualName() to set trace names. Preserve your custom tag logic by calling super methods and appending custom KeyValues.

## Objective

Reimplement custom metrics tagging using new Observation convention pattern
## Applicable Signals

- Custom TagProvider or TagContributor classes exist in codebase
- Migrating to Spring Boot 3.0
- Need to preserve custom metric tags during upgrade
- Observation API integration is active

## Contraindications

- No custom tags are defined in codebase
- Using only default observation instrumentation without overrides
- TagProvider classes are not overridden or extended

## Intervention Moves

- Identify all custom TagProvider and TagContributor implementations
- Create new class extending DefaultServerRequestObservationConvention or implementing ServerRequestObservationConvention
- Override getLowCardinalityKeyValues() to preserve custom tags
- Override getContextualName() for custom trace naming
- Register custom convention bean in Spring configuration
- Test that custom tags appear in metrics and traces

## Workflow Steps

- {'step': 1, 'action': 'Locate all custom TagProvider, TagContributor, and *Tags classes in codebase'}
- {'step': 2, 'action': 'Create new class extending DefaultServerRequestObservationConvention or implementing ServerRequestObservationConvention'}
- {'step': 3, 'action': 'Override getLowCardinalityKeyValues(ServerRequestObservationContext context) to add custom KeyValue pairs using super.getLowCardinalityKeyValues(context).and(customKeyValue)'}
- {'step': 4, 'action': 'Override getContextualName(ServerRequestObservationContext context) to set custom trace names'}
- {'step': 5, 'action': "Override getName() to return metric name (e.g., 'http.server.requests')"}
- {'step': 6, 'action': 'Register custom convention as Spring bean'}
- {'step': 7, 'action': 'Remove or disable old TagProvider and TagContributor implementations'}
- {'step': 8, 'action': 'Test that custom tags appear in metrics and traces with expected values'}

## Constraints

- Custom convention must implement or extend ServerRequestObservationConvention interface
- getLowCardinalityKeyValues() must return KeyValues object
- getContextualName() must return String for trace naming
- Custom KeyValue pairs should use consistent naming conventions

## Cautions

- Deprecated TagProvider and TagContributor classes are kept during deprecation phase but will be removed in future versions
- Duplicate instrumentation risk if both old and new conventions are active; ensure old classes are removed
- Custom tags must have low cardinality to avoid metric explosion

## Output Contract

- Custom ServerRequestObservationConvention class implemented with overridden getLowCardinalityKeyValues() and getContextualName() methods; custom tags preserved and visible in metrics and traces; old TagProvider/TagContributor classes removed from active codebase

## Example Executions

### Example 1

- Input: Existing custom TagProvider that adds 'custom.method' tag to metrics
- Output: New ExtendedServerRequestObservationConvention class extending DefaultServerRequestObservationConvention with getLowCardinalityKeyValues() returning super values plus KeyValue.of('custom.method', context.getCarrier().getMethod())
- Notes: Preserves default tags while adding custom tag

### Example 2

- Input: Custom TagContributor implementing full tag set
- Output: New CustomServerRequestObservationConvention implementing ServerRequestObservationConvention with getName(), getContextualName(), and getLowCardinalityKeyValues() methods returning custom KeyValues
- Notes: Full control over all tags; no inheritance from defaults

## Triggers

- Custom TagProvider or TagContributor classes exist in codebase
- Migrating to Spring Boot 3.0
- Need to preserve custom metric tags

## Examples

### Example 1

Input:

  Existing custom TagProvider that adds 'custom.method' tag to metrics

Output:

  New ExtendedServerRequestObservationConvention class extending DefaultServerRequestObservationConvention with getLowCardinalityKeyValues() returning super values plus KeyValue.of('custom.method', context.getCarrier().getMethod())

Notes:

  Preserves default tags while adding custom tag

### Example 2

Input:

  Custom TagContributor implementing full tag set

Output:

  New CustomServerRequestObservationConvention implementing ServerRequestObservationConvention with getName(), getContextualName(), and getLowCardinalityKeyValues() methods returning custom KeyValues

Notes:

  Full control over all tags; no inheritance from defaults
