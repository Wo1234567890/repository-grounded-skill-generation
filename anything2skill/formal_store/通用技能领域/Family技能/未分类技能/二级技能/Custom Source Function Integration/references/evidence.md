# Custom Source Function Integration Evidence

- family: 未分类技能
- skill_id: 87f86160-f44f-511c-82f8-58083943120b
- support_count: 1

## Evidence 1

- support_id: 5b7c0831-629d-5a43-889f-e3cbb07d2bf0
- relation_type: support
- document: flink-118-datastream.md
- doc_id: 8a36b10a-4e32-5b2b-bc38-0c56680e2cda
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/flink-118-datastream.md
- section: DataStream API▾
- span: 25932:31012
- confidence: 0.72
- quote: If the `watchType` is set to `FileProcessingMode.PROCESS_CONTINUOUSLY`, when a file is modified, its contents are re-processed entirely. This can break the “exactly-once” semantics, as appending data at the end of a file will lead to all its contents being re-processed.

-

Socket-based:

- `socketTextStream` - Reads from a socket. Elements can be separated by a delimiter.

Collection-based:

-

`fromCollection(Collection)` - Creates a data stream from the Java Java.util.Collection. All elements
in the collection must be of the same type.

-

`fromCollection(Iterator, Class)` - Creates a data stream from an iterator. The class specifies the
data type of the elements returned by the iterator.

-

`fromElements(T ...)` - Creates a data stream from the given sequence of objects. All objects must be
of the same type.

-

`fromParallelCollection(SplittableIterator, Class)` - Creates a data stream from an iterator, in
parallel. The class specifies the data type of the elements returned by the iterator.

-

`generateSequence(from, to)` - Generates the sequence of numbers in the given interval, in
parallel.

Custom:

- `addSource` - Attach a new source function. For example, to read from Apache Kafka you can use
`addSource(new FlinkKafkaConsumer<>(...))`. See connectors for more details.

Scala

There are several predefined stream sources accessible from the `StreamExecutionEnvironment`:

File-based:

-

`readTextFile(path)` - Reads text files, i.e. files that respect the `TextInputFormat` specification, line-by-line and returns them as Strings.

-

`readFile(fileInputFormat, path)` - Reads (once) files as dictated by the specified file input format.

-

IMPLEMENTATION:

IMPORTANT NOTES:

-

If the `watchType` is set to `FileProcessingMode.PROCESS_CONTINUOUSLY`, when a file is modified, its contents are re-processed entirely. This can break the “exactly-once” semantics, as appending data at the end of a file will lead to all its contents being re-processed.

-

Socket-based:

- `socketTextStream` - Reads from a socket. Elements can be separated by a delimiter.

Collection-based:

-

`fromCollection(Seq)` - Creates a data stream from the Java Java.util.Collection. All elements
in the collection must be of the same type.

-

`fromCollection(Iterator)` - Creates a data stream from an iterator. The class specifies the
data type of the elements returned by the iterator.
