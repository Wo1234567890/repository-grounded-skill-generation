# Package Instrumentation Eligibility Check Evidence

- family: 未分类技能
- skill_id: e63667bd-2d54-5e5c-afa1-a566d7cccf56
- support_count: 1

## Evidence 1

- support_id: 5107090a-7b8d-56cc-8820-1b4d93b36dbc
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 93449:95267
- confidence: 0.75
- quote: # If already instrumented by AgentOps (using our refined check), skip.
    if _is_package_instrumented(package_name):
        logger.debug(f"_should_instrument_package: '{package_name}' already instrumented by AgentOps. Skipping.")
        return False

is_target_agentic = package_name in AGENTIC_LIBRARIES
    is_target_provider = package_name in PROVIDERS

if not is_target_agentic and not is_target_provider:
        logger.debug(
            f"_should_instrument_package: '{package_name}' is not a targeted provider or agentic library. Skipping."
        )
        return False

logger.debug(
        f"_should_instrument_package: Defaulting to False for '{package_name}' (state: _has_agentic_library={_has_agentic_library})"
    )
    return False
