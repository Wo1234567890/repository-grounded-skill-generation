"""
Task-aligned verifier for 'analyze-ci'.

The task requires:
- scripts/analyze_ci_failures.py
- sample_pytest_output.log
- CLI: --input / --output
- parsing pytest failure logs
- extracting failed test names
- identifying error type
- generating stack trace summary
- JSON output fields:
    failed_tests
    error_type
    stack_summary

Functional correctness is tested using verifier-owned input rather than
the agent-authored sample log.
"""

from pathlib import Path
import json
import subprocess
import tempfile

import pytest


REPO_DIR = Path("/workspace/sentry")
SCRIPT = REPO_DIR / "scripts" / "analyze_ci_failures.py"
SAMPLE_LOG = REPO_DIR / "sample_pytest_output.log"


def run(cmd, *, cwd=REPO_DIR, timeout=120):
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


@pytest.fixture(scope="module")
def independent_result():
    """
    Execute the agent implementation against verifier-owned pytest output.
    """
    pytest_log = r"""
============================= test session starts ==============================
platform linux -- Python 3.11.0, pytest-8.0.0
collected 2 items

tests/test_math.py .F                                                   [100%]

=================================== FAILURES ===================================
________________________________ test_addition _________________________________

    def test_addition():
>       assert 2 + 2 == 5
E       AssertionError: expected 5 but got 4
E       assert (2 + 2) == 5

tests/test_math.py:8: AssertionError
=========================== short test summary info ============================
FAILED tests/test_math.py::test_addition - AssertionError: expected 5 but got 4
========================= 1 failed, 1 passed in 0.05s =========================
""".strip()

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        input_path = td / "independent_pytest.log"
        output_path = td / "report.json"

        input_path.write_text(
            pytest_log,
            encoding="utf-8",
        )

        result = run(
            [
                "python",
                str(SCRIPT),
                "--input",
                str(input_path),
                "--output",
                str(output_path),
            ]
        )

        output_exists = output_path.is_file()

        data = None
        json_error = None

        if output_exists:
            try:
                data = json.loads(
                    output_path.read_text(encoding="utf-8")
                )
            except Exception as exc:
                json_error = str(exc)

        return {
            "result": result,
            "output_exists": output_exists,
            "data": data,
            "json_error": json_error,
        }


class TestAnalyzeCiTaskAligned:

    # --------------------------------------------------------------
    # Required artifacts
    # --------------------------------------------------------------

    def test_required_files_exist(self):
        assert SCRIPT.is_file(), (
            "scripts/analyze_ci_failures.py is missing"
        )

        assert SAMPLE_LOG.is_file(), (
            "sample_pytest_output.log is missing"
        )

    def test_script_compiles(self):
        result = run(
            [
                "python",
                "-m",
                "py_compile",
                "scripts/analyze_ci_failures.py",
            ],
            timeout=30,
        )

        assert result.returncode == 0, (
            f"Python syntax error:\n{result.stderr}"
        )

    # --------------------------------------------------------------
    # Agent-authored sample file requirement
    # --------------------------------------------------------------

    def test_sample_log_matches_task_requirements(self):
        content = SAMPLE_LOG.read_text(
            encoding="utf-8",
            errors="replace",
        )

        assert "FAILED" in content, (
            "sample_pytest_output.log must contain a FAILED marker"
        )

        assert "AssertionError" in content, (
            "sample_pytest_output.log must contain AssertionError"
        )

        # Task explicitly asks for traceback-style pytest output.
        traceback_evidence = (
            "FAILURES" in content
            or "Traceback" in content
            or ">" in content
        )

        assert traceback_evidence, (
            "sample_pytest_output.log does not contain traceback-style output"
        )

    # --------------------------------------------------------------
    # CLI contract
    # --------------------------------------------------------------

    def test_cli_help_exposes_required_arguments(self):
        result = run(
            [
                "python",
                str(SCRIPT),
                "--help",
            ],
            timeout=30,
        )

        assert result.returncode == 0, (
            f"--help failed:\n{result.stderr}"
        )

        assert "--input" in result.stdout, (
            "--input argument is missing"
        )

        assert "--output" in result.stdout, (
            "--output argument is missing"
        )

    # --------------------------------------------------------------
    # Independent functional verification
    # --------------------------------------------------------------

    def test_independent_input_executes_successfully(
        self,
        independent_result,
    ):
        result = independent_result["result"]

        assert result.returncode == 0, (
            f"Analyzer failed on verifier-owned pytest log.\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

        assert independent_result["output_exists"], (
            "Analyzer did not create the requested JSON output"
        )

    def test_independent_output_schema(
        self,
        independent_result,
    ):
        assert independent_result["json_error"] is None, (
            "Generated report is not valid JSON: "
            + str(independent_result["json_error"])
        )

        data = independent_result["data"]

        assert isinstance(data, dict), (
            "JSON report root must be an object"
        )

        for field in [
            "failed_tests",
            "error_type",
            "stack_summary",
        ]:
            assert field in data, (
                f"Required output field missing: {field}"
            )

        assert isinstance(data["failed_tests"], list), (
            "failed_tests must be a list"
        )

    def test_independent_failure_is_actually_extracted(
        self,
        independent_result,
    ):
        data = independent_result["data"]

        failed_tests = [
            str(x)
            for x in data["failed_tests"]
        ]

        assert any(
            "test_addition" in x
            for x in failed_tests
        ), (
            "Analyzer did not extract the failed test "
            "'test_addition' from verifier-owned input. "
            f"Got: {failed_tests}"
        )

        assert "AssertionError" in str(data["error_type"]), (
            "Analyzer did not identify AssertionError. "
            f"Got: {data['error_type']!r}"
        )

        stack_summary = data["stack_summary"]

        assert isinstance(stack_summary, str), (
            "stack_summary must be a string"
        )

        assert stack_summary.strip(), (
            "stack_summary must contain a stack trace summary"
        )
