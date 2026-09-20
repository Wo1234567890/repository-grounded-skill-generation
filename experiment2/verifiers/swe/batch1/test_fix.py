"""
Task-aligned verifier for 'fix'
Task: Fix ESLint Violations in TypeScript Codebase

Grounding:
- Agent modifications are restricted to src/**/*.ts.
- Test files must not be modified.
- package.json must provide lint and test scripts.
- npm run lint must exit 0.
- Existing tests must still pass.
- Agent changes must not introduce new ESLint warnings.

The original benchmark verifier is preserved separately.
"""

from collections import Counter
from pathlib import Path
import json
import subprocess

import pytest

from _dependency_utils import ensure_npm_dependencies


REPO_DIR = Path("/workspace/upgradle")


def run(cmd, *, input_text=None, timeout=300):
    return subprocess.run(
        cmd,
        cwd=REPO_DIR,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def git_changed_paths():
    """
    Capture agent-created/modified/deleted paths before dependency setup.
    Includes untracked files.
    """
    result = run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        timeout=30,
    )
    assert result.returncode == 0, result.stderr

    paths = []

    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue

        path = line[3:].strip()

        # Handle rename format: old -> new
        if " -> " in path:
            path = path.split(" -> ", 1)[1]

        paths.append(path)

    return sorted(set(paths))


# IMPORTANT:
# Capture agent modifications before npm dependency preparation can
# potentially touch environment-related files.
AGENT_CHANGED_PATHS = git_changed_paths()


@pytest.fixture(scope="module", autouse=True)
def ensure_dependencies():
    ensure_npm_dependencies(str(REPO_DIR))


@pytest.fixture(scope="module")
def package_json():
    path = REPO_DIR / "package.json"

    assert path.is_file(), "package.json is missing"

    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def lint_result():
    return run(["npm", "run", "lint"])


@pytest.fixture(scope="module")
def test_result():
    return run(["npm", "test"])


def eslint_messages_for_source(source, filename):
    """
    Lint supplied source text using the repository's own ESLint configuration.

    --stdin-filename makes ESLint apply the same configuration that would
    apply to the real repository file.
    """
    result = run(
        [
            "npx",
            "eslint",
            "--stdin",
            "--stdin-filename",
            filename,
            "--format",
            "json",
        ],
        input_text=source,
    )

    try:
        data = json.loads(result.stdout or "[]")
    except json.JSONDecodeError as exc:
        pytest.fail(
            f"Could not parse ESLint JSON for {filename}: {exc}\n"
            f"stdout:\n{result.stdout[-2000:]}\n"
            f"stderr:\n{result.stderr[-2000:]}"
        )

    messages = []

    for report in data:
        messages.extend(report.get("messages", []))

    return messages


def baseline_source(path):
    """
    Return path contents at repository HEAD.

    None means the file did not exist at HEAD (i.e. newly created by agent).
    """
    result = run(
        ["git", "show", f"HEAD:{path}"],
        timeout=30,
    )

    if result.returncode != 0:
        return None

    return result.stdout


def warning_signature(message):
    """
    Identify a warning independently of its line number.

    Line positions commonly change while fixing nearby code, so they are
    intentionally not part of the signature.
    """
    return (
        message.get("ruleId"),
        message.get("message"),
    )


class TestFixTaskAligned:
    # ------------------------------------------------------------------
    # Project / task scope
    # ------------------------------------------------------------------

    def test_src_directory_exists(self):
        assert (REPO_DIR / "src").is_dir(), "src/ directory is missing"

    def test_typescript_files_exist(self):
        files = list((REPO_DIR / "src").rglob("*.ts"))
        assert files, "No .ts files exist under src/"

    def test_package_has_required_scripts(self, package_json):
        scripts = package_json.get("scripts", {})

        assert "lint" in scripts, (
            "package.json must contain a lint script"
        )

        assert "test" in scripts, (
            "package.json must contain a test script"
        )

    def test_agent_changes_are_within_task_scope(self):
        """
        Task explicitly defines files to modify as src/**/*.ts.

        Therefore agent-created/modified/deleted repository files outside
        that scope are not accepted.
        """
        invalid = []

        for path in AGENT_CHANGED_PATHS:
            p = Path(path)

            allowed = (
                len(p.parts) >= 2
                and p.parts[0] == "src"
                and p.suffix == ".ts"
            )

            if not allowed:
                invalid.append(path)

        assert not invalid, (
            "Agent changed files outside the task scope src/**/*.ts: "
            + ", ".join(invalid)
        )

    # ------------------------------------------------------------------
    # Primary acceptance criterion: lint
    # ------------------------------------------------------------------

    def test_npm_run_lint_exits_zero(self, lint_result):
        assert lint_result.returncode == 0, (
            f"`npm run lint` failed with exit code "
            f"{lint_result.returncode}\n\n"
            f"stdout:\n{lint_result.stdout[-4000:]}\n\n"
            f"stderr:\n{lint_result.stderr[-4000:]}"
        )

    # ------------------------------------------------------------------
    # No new lint warnings
    # ------------------------------------------------------------------

    def test_no_new_eslint_warnings_introduced(self):
        """
        Compare warnings for every changed TypeScript source file against
        the same file at HEAD.

        This implements "No new lint warnings introduced" rather than the
        stricter and incorrect requirement "final warning count == 0".
        """
        new_warning_failures = []

        changed_ts = [
            p
            for p in AGENT_CHANGED_PATHS
            if p.startswith("src/") and p.endswith(".ts")
        ]

        for relpath in changed_ts:
            current_path = REPO_DIR / relpath

            # Deleted source file: there is no current warning to introduce.
            if not current_path.exists():
                continue

            current = current_path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            before = baseline_source(relpath)

            before_messages = (
                eslint_messages_for_source(before, relpath)
                if before is not None
                else []
            )

            after_messages = eslint_messages_for_source(
                current,
                relpath,
            )

            before_warnings = Counter(
                warning_signature(m)
                for m in before_messages
                if m.get("severity") == 1
            )

            after_warnings = Counter(
                warning_signature(m)
                for m in after_messages
                if m.get("severity") == 1
            )

            introduced = after_warnings - before_warnings

            if introduced:
                formatted = [
                    f"{rule or '<unknown rule>'}: {message} "
                    f"(+{count})"
                    for (rule, message), count in introduced.items()
                ]

                new_warning_failures.append(
                    f"{relpath}: " + "; ".join(formatted)
                )

        assert not new_warning_failures, (
            "New ESLint warning(s) were introduced:\n"
            + "\n".join(new_warning_failures)
        )

    # ------------------------------------------------------------------
    # Existing functionality
    # ------------------------------------------------------------------

    def test_existing_tests_still_pass(self, test_result):
        assert test_result.returncode == 0, (
            f"`npm test` failed with exit code "
            f"{test_result.returncode}\n\n"
            f"stdout:\n{test_result.stdout[-4000:]}\n\n"
            f"stderr:\n{test_result.stderr[-4000:]}"
        )
