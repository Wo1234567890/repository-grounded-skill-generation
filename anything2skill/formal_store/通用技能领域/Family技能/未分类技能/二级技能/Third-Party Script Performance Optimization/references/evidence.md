# Third-Party Script Performance Optimization Evidence

- family: 未分类技能
- skill_id: f79dec56-8f91-5eaa-80bc-6d8f686412df
- support_count: 3

## Evidence 1

- support_id: 3d83a95a-b697-5dbd-a9e5-3199feddb96d
- relation_type: support
- document: nextjs14-optimization.md
- doc_id: 348ef37d-8f72-5077-a811-da520815fca2
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/nextjs14-optimization.md
- section: Analytics and Monitoring
- span: 2809:4615
- confidence: 0.85
- quote: - [Images](/docs/14/app/building-your-application/optimizing/images)
  - Optimize your images with the built-in `next/image` component.
- [Fonts](/docs/14/app/building-your-application/optimizing/fonts)
  - Optimize your application's web fonts with the built-in `next/font` loaders.
- [Scripts](/docs/14/app/building-your-application/optimizing/scripts)
  - Optimize 3rd party scripts with the built-in Script component.
- [Metadata](/docs/14/app/building-your-application/optimizing/metadata)
  - Use the Metadata API to define metadata in any layout or page.
- [Static Assets](/docs/14/app/building-your-application/optimizing/static-assets)
  - Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here.
- [Bundle Analyzer](/docs/14/app/building-your-application/optimizing/bundle-analyzer)
  - Analyze the size of your JavaScript bundles using the @next/bundle-analyzer plugin.
- [Lazy Loading](/docs/14/app/building-your-application/optimizing/lazy-loading)
  - Lazy load imported libraries and React Components to improve your application's loading performance.
- [Analytics](/docs/14/app/building-your-application/optimizing/analytics)
  - Measure and track page performance using Next.js Speed Insights
- [Instrumentation](/docs/14/app/building-your-application/optimizing/instrumentation)
  - Learn how to use instrumentation to run code at server startup in your Next.js app
- [OpenTelemetry](/docs/14/app/building-your-application/optimizing/open-telemetry)
  - Learn how to instrument your Next.js app with OpenTelemetry.
- [Third Party Libraries](/docs/14/app/building-your-application/optimizing/third-party-libraries)
  - Optimize the performance of third-party libraries in your application with the `@next/third-parties` package.

---

## Evidence 2

- support_id: b481d0b2-7f84-5475-a20a-b596950373dc
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 40960:43311
- confidence: 0.90
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

## Evidence 3

- support_id: 1b546292-b9cc-59e4-a598-45cb867862f0
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 22522:22788
- confidence: 0.75
- quote: ### Running Tests

1. **Run All Tests**:
   ```bash
   tox
   ```

2. **Run Specific Test File**:
   ```bash
   pytest tests/llms/test_anthropic.py -v
   ```

3. **Run with Coverage**:
   ```bash
   coverage run -m pytest
   coverage report
   ```

### Writing Tests
