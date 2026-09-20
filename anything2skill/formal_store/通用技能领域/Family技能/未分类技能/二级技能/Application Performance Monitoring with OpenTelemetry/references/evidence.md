# Application Performance Monitoring with OpenTelemetry Evidence

- family: 未分类技能
- skill_id: 62dc23d5-43a2-5633-9c5a-97701033acac
- support_count: 4

## Evidence 1

- support_id: 697033ee-fa78-5771-9675-f2d993238471
- relation_type: support
- document: nextjs14-optimization.md
- doc_id: 348ef37d-8f72-5077-a811-da520815fca2
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/nextjs14-optimization.md
- section: Analytics and Monitoring
- span: 2809:4615
- confidence: 0.80
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

- support_id: bc224f73-fd14-5922-b14f-81d1900e3c4b
- relation_type: support
- document: trl-grpo-017.md
- doc_id: 1b1cfe5e-1be5-5bc1-9b07-6e37f39e1ae1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/trl-grpo-017.md
- section: GRPO Trainer
- span: 15086:16263
- confidence: 0.85
- quote: GRPO at scale: train a 70B+ Model on multiple nodes
When training large models like Qwen2.5-72B, you need several key optimizations to make the training efficient and scalable across multiple GPUs and nodes. These include:

- DeepSpeed ZeRO Stage 3: ZeRO leverages data parallelism to distribute model states (weights, gradients, optimizer states) across multiple GPUs and CPUs, reducing memory and compute requirements on each device. Since large models cannot fit on a single GPU, using ZeRO Stage 3 is required for training such model. For more details, see DeepSpeed Integration. 
- Accelerate: Accelerate is a library that simplifies distributed training across multiple GPUs and nodes. It provides a simple API to launch distributed training and handles the complexities of distributed training, such as data parallelism, gradient accumulation, and distributed data loading. For more details, see Distributing Training. 
- vLLM: See the previous section on how to use vLLM to speed up generation.

Below is an example SLURM script to train a 70B model with GRPO on multiple nodes. This script trains a model on 4 nodes and uses the 5th node for vLLM-powered generation.

## Evidence 3

- support_id: 7b712ea5-9338-5c62-8b33-12881d864a09
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

## Evidence 4

- support_id: 5de145d5-feb6-56a1-bfe9-9fe3f1707628
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 31577:32383
- confidence: 0.75
- quote: return event

def init(
    api_key: Optional[str] = None,
    endpoint: Optional[str] = None,
    app_url: Optional[str] = None,
    max_wait_time: Optional[int] = None,
    max_queue_size: Optional[int] = None,
    tags: Optional[List[str]] = None,
    default_tags: Optional[List[str]] = None,
    trace_name: Optional[str] = None,
    instrument_llm_calls: Optional[bool] = None,
    auto_start_session: Optional[bool] = None,
    auto_init: Optional[bool] = None,
    skip_auto_end_session: Optional[bool] = None,
    env_data_opt_out: Optional[bool] = None,
    log_level: Optional[Union[str, int]] = None,
    fail_safe: Optional[bool] = None,
    log_session_replay_url: Optional[bool] = None,
    exporter_endpoint: Optional[str] = None,
    **kwargs,
):
    """
    Initializes the AgentOps SDK.
