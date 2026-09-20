# StreamExecutionEnvironment Setup Evidence

- family: 未分类技能
- skill_id: cb55fb3e-7b22-513e-b682-5f6a4cb952b8
- support_count: 2

## Evidence 1

- support_id: 107a806d-d639-51c7-97fd-8ad35cf1744e
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 17782:20490
- confidence: 0.85
- quote: ```
getExecutionEnvironment()

createLocalEnvironment()

createRemoteEnvironment(host: String, port: Int, jarFiles: String*)

```

For specifying data sources the execution environment has several methods to
read from files using various methods: you can just read them line by line, as
CSV files, or using any of the other provided sources. To just read a text file
as a sequence of lines, you can use:

```
val env = StreamExecutionEnvironment.getExecutionEnvironment()

val text: DataStream[String] = env.readTextFile("file:///path/to/file")

```

This will give you a DataStream on which you can then apply transformations to
create new derived DataStreams.

You apply transformations by calling methods on DataStream with a
transformation functions. For example, a map transformation looks like this:

```
val input: DataSet[String] = ...

val mapped = input.map { x => x.toInt }

```

This will create a new DataStream by converting every String in the original
collection to an Integer.

Once you have a DataStream containing your final results, you can write it to
an outside system by creating a sink. These are just some example methods for
creating a sink:

```
writeAsText(path: String)

print()

```

Once you specified the complete program you need to trigger the program
execution by calling `execute()` on the `StreamExecutionEnvironment`.
Depending on the type of the `ExecutionEnvironment` the execution will be
triggered on your local machine or submit your program for execution on a
cluster.

The `execute()` method will wait for the job to finish and then return a
`JobExecutionResult`, this contains execution times and accumulator results.

```
final JobClient jobClient = env.executeAsync();

final JobExecutionResult jobExecutionResult = jobClient.getJobExecutionResult().get();

```

## Evidence 2

- support_id: 5a506233-18d9-58ef-ac36-7cb15564f491
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 20407:20724
- confidence: 0.85
- quote: Before starting work on a new feature:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/your-feature-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

3. **Set Up Pre-commit Hooks**:
   ```bash
   pre-commit install
   ```

## Development Environment
