# Iterative Stream Loop Construction Evidence

- family: 未分类技能
- skill_id: 568447d8-71c4-552c-b75e-25889b5a1fdf
- support_count: 2

## Evidence 1

- support_id: 246bf5c0-01bb-5fea-969e-c94112e6efd8
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 34183:38548
- confidence: 0.88
- quote: `writeUsingOutputFormat()` / `FileOutputFormat` - Method and base class for custom file outputs. Supports
custom object-to-bytes conversion.

-

`writeToSocket` - Writes elements to a socket according to a `SerializationSchema`

-

`addSink` - Invokes a custom sink function. Flink comes bundled with connectors to other systems (such as
Apache Kafka) that are implemented as sink functions.

For reliable, exactly-once delivery of a stream into a file system, use the `FileSink`.
Also, custom implementations through the `.addSink(...)` method can participate in Flink’s checkpointing
for exactly-once semantics.

Back to top

## 
 Iterations
 #

Java

```
IterativeStream<Integer> iteration = input.iterate();

```

Then, we specify the logic that will be executed inside the loop using a series of transformations (here
a simple `map` transformation)

```
DataStream<Integer> iterationBody = iteration.map(/* this is executed many times */);

```

```
iteration.closeWith(iterationBody.filter(/* one part of the stream */));
DataStream<Integer> output = iterationBody.filter(/* some other part of the stream */);

```

For example, here is program that continuously subtracts 1 from a series of integers until they reach zero:

```
DataStream<Long> someIntegers = env.generateSequence(0, 1000);

IterativeStream<Long> iteration = someIntegers.iterate();

DataStream<Long> minusOne = iteration.map(new MapFunction<Long, Long>() {
  @Override
  public Long map(Long value) throws Exception {
    return value - 1 ;
  }
});

DataStream<Long> stillGreaterThanZero = minusOne.filter(new FilterFunction<Long>() {
  @Override
  public boolean filter(Long value) throws Exception {
    return (value > 0);
  }
});

iteration.closeWith(stillGreaterThanZero);

DataStream<Long> lessThanZero = minusOne.filter(new FilterFunction<Long>() {
  @Override
  public boolean filter(Long value) throws Exception {
    return (value <= 0);
  }
});

```

Scala

```
val iteratedStream = someDataStream.iterate(
  iteration => {
    val iterationBody = iteration.map(/* this is executed many times */)
    (iterationBody.filter(/* one part of the stream */), iterationBody.filter(/* some other part of the stream */))
})

```

For example, here is program that continuously subtracts 1 from a series of integers until they reach zero:

```
val someIntegers: DataStream[Long] = env.generateSequence(0, 1000)

## Evidence 2

- support_id: ed3535f1-83d9-5c18-8f7c-cd72353796b9
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 69905:70474
- confidence: 0.75
- quote: # Example usage:
# search_result = web_search("AgentOps features")
# calculation = calculator("2 + 2")
```

### Grouping with Traces (`@trace` or manual)
Create custom traces to group a sequence of operations or define logical units of work. You can use the `@trace` decorator or manage traces manually for more complex scenarios.
If `auto_start_session=False` in `agentops.init()`, you must use `@trace` or `agentops.start_trace()` for any data to be recorded.

```python
from agentops.sdk.decorators import trace
# Assuming MyAgent and web_search are defined as above
