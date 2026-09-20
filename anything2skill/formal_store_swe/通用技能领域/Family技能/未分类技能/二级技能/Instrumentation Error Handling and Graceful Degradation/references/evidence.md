# Instrumentation Error Handling and Graceful Degradation Evidence

- family: 未分类技能
- skill_id: e1c33881-5c6b-5405-8b21-a771ac02a898
- support_count: 1

## Evidence 1

- support_id: a661caba-dc9e-598f-a3e4-d730223abefc
- relation_type: constraint
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 114112:115163
- confidence: 0.80
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
