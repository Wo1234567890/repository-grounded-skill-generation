# Custom ServerRequestObservationConvention Implementation Evidence

- family: 未分类技能
- skill_id: f83a5625-f756-5405-b2a6-f2296b185081
- support_count: 2

## Evidence 1

- support_id: aded535b-0a08-5e96-8eb9-33e2583730d6
- relation_type: support
- document: spring-boot3-migration.md
- doc_id: 8a0719aa-8715-5b31-81e8-b6b7665dcece
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/spring-boot3-migration.md
- section: Spring Boot 3.0 Migration Guide
- span: 16238:19424
- confidence: 0.82
- quote: Deprecation of the Spring Boot 2.x instrumentation
As a result of the integration with the Observation support, we are now deprecating the previous instrumentation.
The filters, interceptors performing the actual instrumentation have been removed entirely, as entire classes of bugs could not be resolved and the risk of duplicate instrumentation was too high. For example, the `WebMvcMetricsFilter` has been deleted entirely and is effectively replaced by Spring Framework’s `ServerHttpObservationFilter`. On the client side, the `MetricsRestTemplateCustomizer` has been removed and a `ObservationRestTemplateCustomizer` is applied instead on the `RestTemplateBuilder` bean.
The corresponding `*TagProvider` `*TagContributor` and `*Tags` classes have been deprecated.
They are not used by default anymore by the observation instrumentation.
We are keeping them around during the deprecation phase so that developers can migrate their existing infrastructure to the new one.

If you are contributing additional `Tags` with `TagContributor` or only partially overriding a `TagProvider`, you should probably extend the `DefaultServerRequestObservationConvention` for your requirements:

```
public class ExtendedServerRequestObservationConvention extends DefaultServerRequestObservationConvention {

@Override
  public KeyValues getLowCardinalityKeyValues(ServerRequestObservationContext context) {
    // here, we just want to have an additional KeyValue to the observation, keeping the default values
    return super.getLowCardinalityKeyValues(context).and(custom(context));
  }

protected KeyValue custom(ServerRequestObservationContext context) {
    return KeyValue.of("custom.method", context.getCarrier().getMethod());
  }

}
```

```
public class CustomServerRequestObservationConvention implements ServerRequestObservationConvention {

@Override
  public String getName() {
    // will be used for the metric name
    return "http.server.requests";
  }

@Override
  public String getContextualName(ServerRequestObservationContext context) {
    // will be used for the trace name
    return "http " + context.getCarrier().getMethod().toLowerCase();
  }

@Override
  public KeyValues getLowCardinalityKeyValues(ServerRequestObservationContext context) {
    return KeyValues.of(method(context), status(context), exception(context));
  }

## Evidence 2

- support_id: 36d95095-3e5b-5420-81ad-498e40f2c7e4
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 114112:115163
- confidence: 0.70
- quote: 1. **Use Common Utilities**: Leverage the common module for consistency
2. **Follow Semantic Conventions**: Use attributes from `agentops.semconv`
3. **Handle Errors Gracefully**: Wrap operations in try-except blocks
4. **Support Async**: Provide both sync and async method wrapping
5. **Document Attributes**: Comment on what attributes are captured
6. **Test Thoroughly**: Write unit tests for your instrumentor

## Examples

See the `examples/` directory for usage examples of each instrumentor.

### agentops/instrumentation/providers/openai/instrumentor.py

```python
"""OpenAI API Instrumentation for AgentOps

This module provides comprehensive instrumentation for the OpenAI API, including:
- Chat completions (streaming and non-streaming)
- Regular completions
- Embeddings
- Image generation
- Assistants API (create, runs, messages)
- Responses API (Agents SDK)

The instrumentation supports both sync and async methods, metrics collection,
and distributed tracing.
"""

from typing import Dict, Any
from wrapt import wrap_function_wrapper
