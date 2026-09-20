# TicToc Concurrency Control Protocol Evidence

- family: 未分类技能
- skill_id: cdd22de9-5de9-5117-acad-5df117ce2e82
- support_count: 2

## Evidence 1

- support_id: 577f2eb1-db4f-59fb-9d43-c1f973208a6d
- relation_type: support
- document: tictoc-paper.txt
- doc_id: 9fdf1d6f-b6bf-5ce1-8417-e6bbcc7c565c
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/tictoc-paper.txt
- section: 5.4               Lower Isolation Levels                                                       6.1     Workloads
- span: 73748:75997
- confidence: 0.85
- quote: 1636
                                                                                          DL_DETECT         HEKATON          NO_WAIT                      SILO             TICTOC

2.0                                                                               0.8

Throughput (Million txn/s)
                                                              1.5                                                                               0.6

Abort Rate
                                                              1.0                                                                               0.4

0.5                                                                               0.2

5.0                                                                               0.8

Throughput (Million txn/s)
                                                              4.0
                                                                                                                                                0.6

## Evidence 2

- support_id: 81e2edcf-448e-58ce-a1aa-858a257c2634
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 114112:115163
- confidence: 0.85
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
