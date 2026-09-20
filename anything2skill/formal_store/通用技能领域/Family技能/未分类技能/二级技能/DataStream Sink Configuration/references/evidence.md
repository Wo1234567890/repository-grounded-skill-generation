# DataStream Sink Configuration Evidence

- family: 未分类技能
- skill_id: f2084a63-0d37-52bb-ba37-663e4a2cf660
- support_count: 2

## Evidence 1

- support_id: 3f3852ca-a2dc-5eae-820b-73b3078c9fa1
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 31020:34179
- confidence: 0.85
- quote: `fromElements(elements: _*)` - Creates a data stream from the given sequence of objects. All objects must be
of the same type.

-

`fromParallelCollection(SplittableIterator)` - Creates a data stream from an iterator, in
parallel. The class specifies the data type of the elements returned by the iterator.

-

`generateSequence(from, to)` - Generates the sequence of numbers in the given interval, in
parallel.

Custom:

- `addSource` - Attach a new source function. For example, to read from Apache Kafka you can use
`addSource(new FlinkKafkaConsumer<>(...))`. See connectors for more details.

Back to top

## 
 DataStream Transformations
 #

Please see operators for an overview of the available stream transformations.

Back to top

## 
 Data Sinks
 #

Java

Data sinks consume DataStreams and forward them to files, sockets, external systems, or print them.
Flink comes with a variety of built-in output formats that are encapsulated behind operations on the
DataStreams:

-

`writeAsText()` / `TextOutputFormat` - Writes elements line-wise as Strings. The Strings are
obtained by calling the toString() method of each element.

-

`writeAsCsv(...)` / `CsvOutputFormat` - Writes tuples as comma-separated value files. Row and field
delimiters are configurable. The value for each field comes from the toString() method of the objects.

-

-

`writeUsingOutputFormat()` / `FileOutputFormat` - Method and base class for custom file outputs. Supports
custom object-to-bytes conversion.

-

`writeToSocket` - Writes elements to a socket according to a `SerializationSchema`

-

`addSink` - Invokes a custom sink function. Flink comes bundled with connectors to other systems (such as
Apache Kafka) that are implemented as sink functions.

Scala

Data sinks consume DataStreams and forward them to files, sockets, external systems, or print them.
Flink comes with a variety of built-in output formats that are encapsulated behind operations on the
DataStreams:

-

`writeAsText()` / `TextOutputFormat` - Writes elements line-wise as Strings. The Strings are
obtained by calling the toString() method of each element.

-

`writeAsCsv(...)` / `CsvOutputFormat` - Writes tuples as comma-separated value files. Row and field
delimiters are configurable. The value for each field comes from the toString() method of the objects.

-

-

## Evidence 2

- support_id: 631d2f2f-7709-58c2-8aee-ed7dddf028db
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 77728:78229
- confidence: 0.75
- quote: AgentOps automatically tracks LLM API calls from supported providers, collecting valuable information like:

- **Model**: The specific model used (e.g., "gpt-4", "claude-3-opus")
- **Provider**: The LLM provider (e.g., "OpenAI", "Anthropic")
- **Prompt Tokens**: Number of tokens in the input
- **Completion Tokens**: Number of tokens in the output
- **Cost**: The estimated cost of the interaction
- **Messages**: The prompt and completion content

```python
import agentops
from openai import OpenAI
