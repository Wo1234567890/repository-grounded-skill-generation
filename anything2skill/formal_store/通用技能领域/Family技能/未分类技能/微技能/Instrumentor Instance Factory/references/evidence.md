# Instrumentor Instance Factory Evidence

- family: 未分类技能
- skill_id: 291617a0-293a-55d3-b5bb-fc9486e4bf69
- support_count: 1

## Evidence 1

- support_id: 3fba5b17-c98d-58db-a736-54c434d836da
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 103886:105194
- confidence: 0.80
- quote: @property
    def module(self) -> ModuleType:
        """Get the instrumentor module."""
        return importlib.import_module(self.module_name)

@property
    def should_activate(self) -> bool:
        """Check if the package is available and meets version requirements."""
        try:
            # Special case for stdlib modules (like concurrent.futures)
            if self.package_name == "python":
                import sys

python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
                return Version(python_version) >= parse(self.min_version)

# Use explicit package_name if provided, otherwise derive from module_name
            if self.package_name:
                provider_name = self.package_name
            else:
                provider_name = self.module_name.split(".")[-1]

# Use common version utility
            module_version = get_library_version(provider_name)
            return module_version != "unknown" and Version(module_version) >= parse(self.min_version)
        except Exception:
            return False

def get_instance(self) -> BaseInstrumentor:
        """Create and return a new instance of the instrumentor."""
        return getattr(self.module, self.class_name)()
