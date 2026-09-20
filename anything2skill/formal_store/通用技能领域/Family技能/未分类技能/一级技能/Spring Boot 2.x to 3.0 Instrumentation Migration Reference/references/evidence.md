# Spring Boot 2.x to 3.0 Instrumentation Migration Reference Evidence

- family: 未分类技能
- skill_id: d68ed7cc-0e6f-59e0-be4b-23d284fc1279
- support_count: 2

## Evidence 1

- support_id: 12418ed4-483e-54fa-8bb0-cce4a4b09fd2
- relation_type: support
- document: spring-boot3-migration.md
- doc_id: 8a0719aa-8715-5b31-81e8-b6b7665dcece
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/spring-boot3-migration.md
- section: Spring Boot 3.0 Migration Guide
- span: 16238:19424
- confidence: 0.88
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

- support_id: 1f06c328-0798-58f2-bd7d-9582b821b15f
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 14477:15268
- confidence: 0.80
- quote: Llama Stack
AgentOps provides support for Llama Stack Python Client(>=0.0.53), allowing you to monitor your Agentic applications.

- [AgentOps integration example 1](https://github.com/AgentOps-AI/agentops/pull/530/files/65a5ab4fdcf310326f191d4b870d4f553591e3ea#diff-fdddf65549f3714f8f007ce7dfd1cde720329fe54155d54389dd50fbd81813cb)
- [AgentOps integration example 2](https://github.com/AgentOps-AI/agentops/pull/530/files/65a5ab4fdcf310326f191d4b870d4f553591e3ea#diff-6688ff4fb7ab1ce7b1cc9b8362ca27264a3060c16737fb1d850305787a6e3699)
- [Official Llama Stack Python Client](https://github.com/meta-llama/llama-stack-client-python)

SwarmZero AI
Track and analyze SwarmZero agents with full observability. Set an `AGENTOPS_API_KEY` in your environment and initialize AgentOps to get started.
