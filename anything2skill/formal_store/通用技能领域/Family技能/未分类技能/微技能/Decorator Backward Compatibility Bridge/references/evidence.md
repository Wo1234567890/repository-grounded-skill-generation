# Decorator Backward Compatibility Bridge Evidence

- family: 未分类技能
- skill_id: 12c14332-2c45-5fb7-bce9-f6acd3f1a926
- support_count: 1

## Evidence 1

- support_id: efc0de74-817b-5b89-a7cc-7eed0c766ae0
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 59239:60867
- confidence: 0.80
- quote: from agentops.helpers.deprecation import deprecated
from agentops.sdk.decorators.factory import create_entity_decorator
from agentops.semconv.span_kinds import SpanKind

# Create decorators for specific entity types using the factory
agent = create_entity_decorator(SpanKind.AGENT)
task = create_entity_decorator(SpanKind.TASK)
operation_decorator = create_entity_decorator(SpanKind.OPERATION)
workflow = create_entity_decorator(SpanKind.WORKFLOW)
trace = create_entity_decorator(SpanKind.SESSION)
tool = create_entity_decorator(SpanKind.TOOL)
operation = task
guardrail = create_entity_decorator(SpanKind.GUARDRAIL)
track_endpoint = create_entity_decorator(SpanKind.HTTP)

# For backward compatibility: @session decorator calls @trace decorator
def session(*args, **kwargs):  # noqa: F811
    """@deprecated Use @agentops.trace instead. Wraps the @trace decorator for backward compatibility."""
    # If called as @session or @session(...)
    if not args or not callable(args[0]):  # called with kwargs like @session(name=...)
        return trace(*args, **kwargs)
    else:  # called as @session directly on a function
        return trace(args[0], **kwargs)  # args[0] is the wrapped function

# Apply deprecation decorator to session function
session = deprecated("Use @trace decorator instead.")(session)

# Note: The original `operation = task` was potentially problematic if `operation` was meant to be distinct.
# Using operation_decorator for clarity if a distinct OPERATION kind decorator is needed.
# For now, keeping the alias as it was, assuming it was intentional for `operation` to be `task`.
operation = task
