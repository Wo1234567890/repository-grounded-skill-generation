# StreamExecutionEnvironment Setup Evidence

- family: 未分类技能
- skill_id: b4c9fc6a-1f05-51ad-b9af-555a91583de9
- support_count: 3

## Evidence 1

- support_id: bc9b7295-5d4c-5ac1-828a-d74af15c02b9
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 14821:17779
- confidence: 0.85
- quote: All Flink Scala APIs are deprecated and will be removed in a future Flink version. You can still build your application in Scala, but you should move to the Java version of either the DataStream and/or Table API.

See FLIP-265 Deprecate and remove Scala API support

Java

We will now give an overview of each of those steps, please refer to the
respective sections for more details. Note that all core classes of the Java
DataStream API can be found in

org.apache.flink.streaming.api

.

The `StreamExecutionEnvironment` is the basis for all Flink programs. You can
obtain one using these static methods on `StreamExecutionEnvironment`:

```
getExecutionEnvironment();

createLocalEnvironment();

createRemoteEnvironment(String host, int port, String... jarFiles);

```

For specifying data sources the execution environment has several methods to
read from files using various methods: you can just read them line by line, as
CSV files, or using any of the other provided sources. To just read a text file
as a sequence of lines, you can use:

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

DataStream<String> text = env.readTextFile("file:///path/to/file");

```

This will give you a DataStream on which you can then apply transformations to create new
derived DataStreams.

You apply transformations by calling methods on DataStream with a
transformation functions. For example, a map transformation looks like this:

```
DataStream<String> input = ...;

DataStream<Integer> parsed = input.map(new MapFunction<String, Integer>() {
    @Override
    public Integer map(String value) {
        return Integer.parseInt(value);
    }
});

```

This will create a new DataStream by converting every String in the original
collection to an Integer.

Once you have a DataStream containing your final results, you can write it to
an outside system by creating a sink. These are just some example methods for
creating a sink:

```
writeAsText(String path);

print();

```

Scala

We will now give an overview of each of those steps, please refer to the
respective sections for more details. Note that all core classes of the Scala
DataStream API can be found in

org.apache.flink.streaming.api.scala

.

The `StreamExecutionEnvironment` is the basis for all Flink programs. You can
obtain one using these static methods on `StreamExecutionEnvironment`:

## Evidence 2

- support_id: df8b4b25-ae76-5b5b-b16d-5c3c8e1299e8
- relation_type: support
- document: spring-boot3-migration.md
- doc_id: 8a0719aa-8715-5b31-81e8-b6b7665dcece
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/spring-boot3-migration.md
- section: Spring Boot 3.0 Migration Guide
- span: 19428:22592
- confidence: 0.85
- quote: @Override
  public KeyValues getHighCardinalityKeyValues(ServerRequestObservationContext context) {
    return KeyValues.of(httpUrl(context));
  }

protected KeyValue method(ServerRequestObservationContext context) {
    // You should reuse as much as possible the corresponding ObservationDocumentation for key names
    return KeyValue.of(ServerHttpObservationDocumentation.LowCardinalityKeyNames.METHOD, context.getCarrier().getMethod());
  }

//...
}
```

In both cases, you can contribute those as beans to the application context and they will be picked up by the auto-configuration, effectively replacing the default ones.

```
@Configuration
public class CustomMvcObservationConfiguration {

@Bean
  public ExtendedServerRequestObservationConvention extendedServerRequestObservationConvention() {
    return new ExtendedServerRequestObservationConvention();
  }

}
```

You can also similar goals using a custom `ObservationFilter` - adding or removing key values for an observation.
Filters do not replace the default convention and are used as a post-processing component.

```
public class ServerRequestObservationFilter implements ObservationFilter {

Auto-configuration of Micrometer’s JvmInfoMetrics
Micrometer’s `JvmInfoMetrics` is now auto-configured. Any manually configured `JvmInfoMetrics` bean definition can be removed.

See issue #30381 for details.

Data Access Changes
The following changes should be reviewed if your application is working with data.

Please review the Spring Data release notes for important changes in Spring Data repository interfaces.

Changes to Data properties
The `spring.data` prefix has been reserved for Spring Data and any properties under the prefix imply that Spring Data is required on the classpath.

Cassandra Properties
Configuration Properties for Cassandra have moved from `spring.data.cassandra.` to `spring.cassandra.`.

## Evidence 3

- support_id: 65f8ffab-c017-5826-8cbc-8a30218fe921
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: First class Developer Experience
- span: 1930:2249
- confidence: 0.70
- quote: @workflow
def my_workflow(data):
    # Workflow implementation
    return result
```

```python
# Nest decorators for proper span hierarchy
from agentops.sdk.decorators import session, agent, operation

@agent
class MyAgent:
    @operation
    def nested_operation(self, message):
        return f"Processed: {message}"
