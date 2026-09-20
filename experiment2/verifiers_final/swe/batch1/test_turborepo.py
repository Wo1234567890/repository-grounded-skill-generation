"""
Test for 'turborepo' skill — Turborepo Monorepo Configuration
Validates that the Agent set up a Turborepo monorepo with workspaces,
shared packages, and proper turbo.json pipeline config.
"""

import os
import json
import subprocess
import pytest


class TestTurborepo:
    """Verify Turborepo monorepo setup."""

    REPO_DIR = "/workspace/turbo"

    # ------------------------------------------------------------------
    # L1: file existence
    # ------------------------------------------------------------------

    def test_turbo_json_exists(self):
        """turbo.json must exist at project root or examples dir."""
        paths = [
            os.path.join(self.REPO_DIR, "turbo.json"),
            os.path.join(self.REPO_DIR, "examples", "turbo.json"),
        ]
        found = any(os.path.isfile(p) for p in paths)
        if not found:
            # Search recursively
            for root, dirs, files in os.walk(self.REPO_DIR):
                if "turbo.json" in files and "node_modules" not in root:
                    found = True
                    break
        assert found, "turbo.json not found"

    def test_package_json_workspaces(self):
        """Root package.json must define workspaces."""
        found = False
        for root, dirs, files in os.walk(self.REPO_DIR):
            if "package.json" in files and "node_modules" not in root:
                fpath = os.path.join(root, "package.json")
                with open(fpath, "r") as f:
                    pkg = json.load(f)
                if "workspaces" in pkg:
                    found = True
                    break
        assert found, "No package.json with workspaces found"

    def test_apps_directory_exists(self):
        """apps/ or packages/ directory must exist."""
        found = False
        for root, dirs, files in os.walk(self.REPO_DIR):
            if "apps" in dirs or "packages" in dirs:
                found = True
                break
        assert found, "Neither apps/ nor packages/ directory found"

    # ------------------------------------------------------------------
    # L2: configuration validation
    # ------------------------------------------------------------------

    def _find_turbo_json(self):
        for root, dirs, files in os.walk(self.REPO_DIR):
            if "turbo.json" in files and "node_modules" not in root:
                return os.path.join(root, "turbo.json")
        return None

    def test_turbo_json_valid(self):
        """turbo.json must be valid JSON."""
        fpath = self._find_turbo_json()
        assert fpath, "turbo.json not found"
        with open(fpath, "r") as f:
            config = json.load(f)
        assert isinstance(config, dict), "turbo.json must be a JSON object"

    def test_turbo_has_pipeline_or_tasks(self):
        """turbo.json must define pipeline or tasks."""
        fpath = self._find_turbo_json()
        assert fpath, "turbo.json not found"
        with open(fpath, "r") as f:
            config = json.load(f)
        has_pipeline = "pipeline" in config or "tasks" in config
        assert has_pipeline, "turbo.json missing pipeline/tasks"

    def test_build_task_defined(self):
        """turbo.json must define a build task."""
        fpath = self._find_turbo_json()
        assert fpath, "turbo.json not found"
        with open(fpath, "r") as f:
            config = json.load(f)
        tasks = config.get("pipeline", config.get("tasks", {}))
        assert (
            "build" in tasks
        ), f"build task not in pipeline; tasks: {list(tasks.keys())}"

    def test_build_task_has_deps(self):
        """Build task should declare dependencies."""
        fpath = self._find_turbo_json()
        assert fpath, "turbo.json not found"
        with open(fpath, "r") as f:
            config = json.load(f)
        tasks = config.get("pipeline", config.get("tasks", {}))
        build = tasks.get("build", {})
        has_deps = "dependsOn" in build or "inputs" in build or "outputs" in build
        assert has_deps, "Build task missing dependsOn/inputs/outputs"

    def test_shared_package_exists(self):
        """At least one shared package in packages/ must exist."""
        found = False
        for root, dirs, files in os.walk(self.REPO_DIR):
            if "packages" in root.split(os.sep) and "package.json" in files:
                found = True
                break
        assert found, "No shared package found in packages/"

    def test_at_least_two_workspaces(self):
        """Must have at least 2 workspace packages."""
        count = 0
        for root, dirs, files in os.walk(self.REPO_DIR):
            if "package.json" in files and "node_modules" not in root:
                # Exclude root
                if root != self.REPO_DIR:
                    count += 1
        assert count >= 2, f"Only {count} workspace packages found, need >= 2"

    def test_lint_task_defined(self):
        """turbo.json should define a lint task."""
        fpath = self._find_turbo_json()
        assert fpath, "turbo.json not found"
        with open(fpath, "r") as f:
            config = json.load(f)
        tasks = config.get("pipeline", config.get("tasks", {}))
        assert "lint" in tasks or "check" in tasks, "No lint/check task in pipeline"


# TASK_ALIGNED_TURBOREPO_CHECKS

def test_exact_cache_demo_structure():
    root = os.path.join(
        TestTurborepo.REPO_DIR,
        "examples",
        "cache-demo",
    )

    required = [
        "package.json",
        "turbo.json",
        "benchmark.sh",
        "packages/core/package.json",
        "packages/core/src/index.ts",
        "packages/utils/package.json",
        "packages/utils/src/index.ts",
        "packages/app/package.json",
        "packages/app/src/index.ts",
    ]

    for rel in required:
        assert os.path.isfile(os.path.join(root, rel)), (
            f"Missing examples/cache-demo/{rel}"
        )


def test_exact_cache_demo_turbo_config():
    path = os.path.join(
        TestTurborepo.REPO_DIR,
        "examples",
        "cache-demo",
        "turbo.json",
    )

    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)

    tasks = config.get("tasks", config.get("pipeline", {}))

    for name in ["build", "lint", "test"]:
        assert name in tasks, f"turbo.json missing {name} task"

    build = tasks["build"]

    assert "outputs" in build
    assert "inputs" in build
    assert "dependsOn" in build
    assert "^build" in build["dependsOn"]


def test_cache_demo_benchmark_acceptance():
    root = os.path.join(
        TestTurborepo.REPO_DIR,
        "examples",
        "cache-demo",
    )

    result = subprocess.run(
        ["bash", "benchmark.sh"],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=300,
    )

    assert result.returncode == 0, (
        f"benchmark.sh failed:\n"
        f"{result.stdout[-3000:]}\n"
        f"{result.stderr[-2000:]}"
    )

    output = (result.stdout + result.stderr).lower()

    assert (
        "full turbo" in output
        or "cache hit" in output
        or "cached" in output
    ), (
        "Second build did not report a Turborepo cache hit"
    )
