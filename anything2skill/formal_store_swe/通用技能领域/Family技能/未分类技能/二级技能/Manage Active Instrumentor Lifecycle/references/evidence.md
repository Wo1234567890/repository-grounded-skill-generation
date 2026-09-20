# Manage Active Instrumentor Lifecycle Evidence

- family: 未分类技能
- skill_id: 0d976330-bcf0-57fd-96db-19a0cfb1e9a5
- support_count: 1

## Evidence 1

- support_id: ab1c12db-de96-5822-88c4-85e802bb8efa
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 85278:93443
- confidence: 0.75
- quote: from opentelemetry.instrumentation.instrumentor import BaseInstrumentor  # type: ignore

from agentops.logging import logger
from agentops.sdk.core import tracer
from agentops.instrumentation.common import get_library_version

# Define the structure for instrumentor configurations
class InstrumentorConfig(TypedDict):
    module_name: str
    class_name: str
    min_version: str
    package_name: NotRequired[str]  # Optional: actual pip package name if different from module

# Combine all target packages for monitoring
TARGET_PACKAGES = set(PROVIDERS.keys()) | set(AGENTIC_LIBRARIES.keys())

# Create a single instance of the manager
# _manager = InstrumentationManager() # Removed

# Module-level state variables
_active_instrumentors: list[BaseInstrumentor] = []
_original_builtins_import = builtins.__import__  # Store original import
_instrumenting_packages: Set[str] = set()
_has_agentic_library: bool = False

module_path = os.path.normcase(os.path.realpath(os.path.abspath(module_obj.__file__)))

# Priority 1: Check if it's in any site-packages directory.
    site_packages_dirs = site.getsitepackages()
    if isinstance(site_packages_dirs, str):
        site_packages_dirs = [site_packages_dirs]

if hasattr(site, "USER_SITE") and site.USER_SITE and os.path.exists(site.USER_SITE):
        site_packages_dirs.append(site.USER_SITE)

normalized_site_packages_dirs = [
        os.path.normcase(os.path.realpath(p)) for p in site_packages_dirs if p and os.path.exists(p)
    ]

for sp_dir in normalized_site_packages_dirs:
        if module_path.startswith(sp_dir):
            logger.debug(
                f"_is_installed_package: Module '{package_name_key}' is a library, instrumenting '{package_name_key}'."
            )
            return True

# Priority 2: If not in site-packages, it's highly likely a local module or not an SDK we target.
    logger.debug(f"_is_installed_package: Module '{package_name_key}' is a local module, skipping instrumentation.")
    return False

return False

def _should_instrument_package(package_name: str) -> bool:
    """
    Determine if a package should be instrumented based on current state.
    Handles special cases for agentic libraries and providers.
    """
    global _has_agentic_library
