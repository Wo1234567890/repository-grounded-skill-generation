# Package Import Interception and Instrumentation Evidence

- family: 未分类技能
- skill_id: 2142ee5d-6d0f-5077-9736-8fbf5a8844d3
- support_count: 1

## Evidence 1

- support_id: 8102f808-2597-515b-b40a-12e3d6095276
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 95270:103880
- confidence: 0.85
- quote: def _perform_instrumentation(package_name: str):
    """Helper function to perform instrumentation for a given package."""
    global _instrumenting_packages, _active_instrumentors, _has_agentic_library
    if not _should_instrument_package(package_name):
        return

config = PROVIDERS.get(package_name) or AGENTIC_LIBRARIES.get(package_name)
    loader = InstrumentorLoader(**config)

# Store the package key this instrumentor is for, to aid _is_package_instrumented
        instrumentor_instance._agentops_instrumented_package_key = package_name

# Special case: If mem0 is instrumented, also instrument concurrent.futures
        if package_name == "mem0" and is_newly_added:
            try:
                # Check if concurrent.futures module is available

# Create and instrument concurrent.futures
                concurrent_loader = InstrumentorLoader(**concurrent_config)
                concurrent_instrumentor = instrument_one(concurrent_loader)

def _import_monitor(name: str, globals_dict=None, locals_dict=None, fromlist=(), level=0):
    """
    Monitor imports and instrument packages as they are imported.
    This replaces the built-in import function to intercept package imports.
    """
    global _instrumenting_packages, _has_agentic_library

# If an agentic library is already instrumented, skip all further instrumentation
    if _has_agentic_library:
        return _original_builtins_import(name, globals_dict, locals_dict, fromlist, level)

# First, do the actual import
    module = _original_builtins_import(name, globals_dict, locals_dict, fromlist, level)

# Check for exact matches first (handles package.module like google.adk)
    packages_to_check = set()

# Check full name if item forms part of a target package name
            full_item_name_candidate = f"{name}.{item}"

# Instrument all matching packages
    for package_to_check in packages_to_check:
        if package_to_check not in _instrumenting_packages and not _is_package_instrumented(package_to_check):
            target_module_obj = sys.modules.get(package_to_check)

return module

@dataclass
class InstrumentorLoader:
    """
    Represents a dynamically-loadable instrumentor.
    Handles version checking and instantiation of instrumentors.
    """

module_name: str
    class_name: str
    min_version: str
    package_name: Optional[str] = None  # Optional: actual pip package name
