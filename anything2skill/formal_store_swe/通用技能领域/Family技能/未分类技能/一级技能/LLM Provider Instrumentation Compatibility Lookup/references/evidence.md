# LLM Provider Instrumentation Compatibility Lookup Evidence

- family: 未分类技能
- skill_id: b563919d-c70f-5b34-a5f8-aff7efb13aa9
- support_count: 1

## Evidence 1

- support_id: ebb0c580-0af7-58b2-b592-9e9cd240b3b8
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 106343:111779
- confidence: 0.88
- quote: def instrument_all():
    """Start monitoring and instrumenting packages if not already started."""
    # Check if active_instrumentors is empty, as a proxy for not started.
    if not _active_instrumentors:
        builtins.__import__ = _import_monitor
        global _instrumenting_packages, _has_agentic_library

# If an agentic library is already instrumented, don't instrument anything else
        if _has_agentic_library:
            return

for name in list(sys.modules.keys()):
            # Stop if an agentic library gets instrumented during the loop
            if _has_agentic_library:
                break

module = sys.modules.get(name)
            if not isinstance(module, ModuleType):
                continue

if (
                package_to_check
                and package_to_check not in _instrumenting_packages
                and not _is_package_instrumented(package_to_check)
            ):
                target_module_obj = sys.modules.get(package_to_check)

return active_libs

```

### agentops/instrumentation/README.md

# AgentOps Instrumentation

This package provides OpenTelemetry instrumentation for various LLM providers and related services.

## Available Instrumentors

- **OpenAI** (`v0.27.0+` and `v1.0.0+`)
- **Anthropic** (`v0.7.0+`)
- **Google GenAI** (`v0.1.0+`)
- **IBM WatsonX AI** (`v0.1.0+`)
- **CrewAI** (`v0.56.0+`)
- **AG2/AutoGen** (`v0.3.2+`)
- **Google ADK** (`v0.1.0+`)
- **Agno** (`v0.0.1+`)
- **Mem0** (`v0.1.0+`)
- **smolagents** (`v0.1.0+`)

## Common Module Usage

The `agentops.instrumentation.common` module provides shared utilities for creating instrumentations:

### Base Instrumentor

Use `CommonInstrumentor` for creating new instrumentations:

```python
from agentops.instrumentation.common import CommonInstrumentor, InstrumentorConfig, WrapConfig

### Attribute Handlers

Create attribute handlers to extract data from method calls:

```python
from agentops.instrumentation.common import AttributeMap

def my_attribute_handler(args=None, kwargs=None, return_value=None) -> AttributeMap:
    attributes = {}

if kwargs and "model" in kwargs:
        attributes["llm.request.model"] = kwargs["model"]

if return_value and hasattr(return_value, "usage"):
        attributes["llm.usage.total_tokens"] = return_value.usage.total_tokens

return attributes
```

### Span Management
