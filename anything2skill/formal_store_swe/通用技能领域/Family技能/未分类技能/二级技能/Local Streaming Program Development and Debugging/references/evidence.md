# Local Streaming Program Development and Debugging Evidence

- family: 未分类技能
- skill_id: 1e4849ca-a605-5714-9f0e-b6174e4ffece
- support_count: 2

## Evidence 1

- support_id: 09e3d480-7492-554f-b326-ec19bcac4cc5
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 40960:43311
- confidence: 0.92
- quote: Before running a streaming program in a distributed cluster, it is a good
idea to make sure that the implemented algorithm works as desired. Hence, implementing data analysis
programs is usually an incremental process of checking results, debugging, and improving.

Flink provides features to significantly ease the development process of data analysis
programs by supporting local debugging from within an IDE, injection of test data, and collection of
result data. This section give some hints how to ease the development of Flink programs.

### 
 Local Execution Environment
 #

A `LocalStreamEnvironment` starts a Flink system within the same JVM process it was created in. If you
start the LocalEnvironment from an IDE, you can set breakpoints in your code and easily debug your
program.

A LocalEnvironment is created and used as follows:

Java

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.createLocalEnvironment();

DataStream<String> lines = env.addSource(/* some source */);
// build your program

env.execute();

```

Scala

```
val env = StreamExecutionEnvironment.createLocalEnvironment()

val lines = env.addSource(/* some source */)
// build your program

env.execute()

```

### 
 Collection Data Sources
 #

Flink provides special data sources which are backed
by Java collections to ease testing. Once a program has been tested, the sources and sinks can be
easily replaced by sources and sinks that read from / write to external systems.

Collection data sources can be used as follows:

Java

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.createLocalEnvironment();

// Create a DataStream from a list of elements
DataStream<Integer> myInts = env.fromElements(1, 2, 3, 4, 5);

// Create a DataStream from any Java collection
List<Tuple2<String, Integer>> data = ...
DataStream<Tuple2<String, Integer>> myTuples = env.fromCollection(data);

// Create a DataStream from an Iterator
Iterator<Long> longIt = ...;
DataStream<Long> myLongs = env.fromCollection(longIt, Long.class);

```

Scala

```
val env = StreamExecutionEnvironment.createLocalEnvironment()

// Create a DataStream from a list of elements
val myInts = env.fromElements(1, 2, 3, 4, 5)

// Create a DataStream from any Collection
val data: Seq[(String, Int)] = ...
val myTuples = env.fromCollection(data)

## Evidence 2

- support_id: 27410ef0-307f-50fe-881a-dd0cf0d0a7ec
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 63497:63947
- confidence: 0.75
- quote: [Give us a star](https://github.com/AgentOps-AI/agentops) to bookmark on GitHub, save for later )

With just two lines of code, you can free yourself from the chains of the terminal and, instead, visualize your agents' behavior
in your AgentOps Dashboard. After setting up AgentOps, each execution of your program is recorded as a session and the above
data is automatically recorded for you.

The examples below were captured with two lines of code.
