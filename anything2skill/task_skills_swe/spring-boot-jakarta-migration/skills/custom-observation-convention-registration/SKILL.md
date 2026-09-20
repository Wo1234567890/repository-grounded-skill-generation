---
id: "eed4bf5c-2af1-5f32-8692-5c6ec42285fc"
name: "Custom Observation Convention Registration"
description: "Register custom ServerRequestObservationConvention beans to replace default Micrometer observation conventions in Spring Boot 3.0 applications. Use when you need to customize high and low cardinality key values for HTTP request observations."
version: "0.1.0"
tags:
  - "spring-boot-3"
  - "micrometer"
  - "observation"
  - "metrics"
  - "bean-registration"
triggers:
  - "Custom HTTP request observation metadata (key-value pairs) is required; default Micrometer conventions do not capture needed cardinality dimensions"
examples:
  - input: "Spring Boot 3.0 application with default Micrometer observation conventions; need to add custom 'tenant-id' and 'request-source' dimensions to HTTP observations"
    output: "Custom ExtendedServerRequestObservationConvention bean registered; HTTP observations now include KeyValue.of('tenant-id', extractedTenantId) and KeyValue.of('request-source', extractedSource)"
    notes: "Bean auto-discovery replaces default convention without additional configuration"
---

# Custom Observation Convention Registration

Register custom ServerRequestObservationConvention beans to replace default Micrometer observation conventions in Spring Boot 3.0 applications. Use when you need to customize high and low cardinality key values for HTTP request observations.

## Prompt

Implement a custom observation convention class that extends ServerRequestObservationConvention or similar base. Override getHighCardinalityKeyValues() and getLowCardinalityKeyValues() methods to return custom KeyValue pairs. Register the implementation as a @Bean in a @Configuration class. The auto-configuration will detect and use your bean instead of the default convention.

## Objective

Replace default observation convention with custom implementation
## Applicable Signals

- Custom HTTP request observation metadata (key-value pairs) is required
- Default Micrometer conventions do not capture needed cardinality dimensions
- Need to extract or transform observation context into custom KeyValue format

## Contraindications

- Default observation conventions are sufficient for your use case
- No custom key-value extraction or transformation is needed
- ObservationFilter post-processing approach is preferred for your scenario

## Intervention Moves

- Create custom class implementing ServerRequestObservationConvention
- Override getHighCardinalityKeyValues(ServerRequestObservationContext context)
- Override getLowCardinalityKeyValues(ServerRequestObservationContext context)
- Return KeyValues with custom KeyValue.of() entries
- Wrap implementation in @Configuration class with @Bean method
- Ensure bean is discoverable by Spring auto-configuration

## Workflow Steps

- {'step': 1, 'action': 'Create custom observation convention class', 'detail': 'Implement ServerRequestObservationConvention with getHighCardinalityKeyValues() and getLowCardinalityKeyValues() methods'}
- {'step': 2, 'action': 'Extract context data', 'detail': 'Use ServerRequestObservationContext to access carrier (HTTP request) and other observation metadata'}
- {'step': 3, 'action': 'Build KeyValue pairs', 'detail': 'Return KeyValues.of() with custom KeyValue entries; reuse ObservationDocumentation constants for key names'}
- {'step': 4, 'action': 'Register as bean', 'detail': 'Create @Configuration class with @Bean method returning custom convention instance'}
- {'step': 5, 'action': 'Verify registration', 'detail': 'Confirm bean is picked up by auto-configuration and replaces default convention in observation pipeline'}

## Constraints

- Custom bean must be registered in application context before auto-configuration runs
- Implementation must follow ServerRequestObservationConvention contract
- KeyValue names should reuse corresponding ObservationDocumentation constants where possible

## Cautions

- Custom convention completely replaces default; ensure all necessary key-value pairs are provided
- High cardinality keys may impact metrics storage and query performance if not carefully designed
- Test observation output to verify custom convention is being picked up by auto-configuration

## Output Contract

- Custom ExtendedServerRequestObservationConvention bean is registered in application context and auto-configuration detects and uses it to replace default observation convention. HTTP request observations now include custom high and low cardinality key-value pairs.

## Example Executions

### Example 1

- Input: Spring Boot 3.0 application with default Micrometer observation conventions; need to add custom 'tenant-id' and 'request-source' dimensions to HTTP observations
- Output: Custom ExtendedServerRequestObservationConvention bean registered; HTTP observations now include KeyValue.of('tenant-id', extractedTenantId) and KeyValue.of('request-source', extractedSource)
- Notes: Bean auto-discovery replaces default convention without additional configuration

## Triggers

- Custom HTTP request observation metadata (key-value pairs) is required; default Micrometer conventions do not capture needed cardinality dimensions

## Examples

### Example 1

Input:

  Spring Boot 3.0 application with default Micrometer observation conventions; need to add custom 'tenant-id' and 'request-source' dimensions to HTTP observations

Output:

  Custom ExtendedServerRequestObservationConvention bean registered; HTTP observations now include KeyValue.of('tenant-id', extractedTenantId) and KeyValue.of('request-source', extractedSource)

Notes:

  Bean auto-discovery replaces default convention without additional configuration
