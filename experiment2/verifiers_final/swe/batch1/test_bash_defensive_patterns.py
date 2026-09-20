
import os
import subprocess


REPO_DIR = "/workspace/shellcheck"

SAFE = os.path.join(REPO_DIR, "test", "safe_backup.sh")
UTILS = os.path.join(REPO_DIR, "test", "common_utils.sh")


def read(path):
    assert os.path.isfile(path), f"Required file missing: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_required_scripts_exist():
    assert os.path.isfile(SAFE), "test/safe_backup.sh missing"
    assert os.path.isfile(UTILS), "test/common_utils.sh missing"


def test_safe_backup_defensive_settings():
    source = read(SAFE)

    assert "set -euo pipefail" in source, (
        "safe_backup.sh must use set -euo pipefail"
    )

    assert "trap " in source, (
        "safe_backup.sh must define a cleanup/error trap"
    )

    assert "EXIT" in source or "ERR" in source, (
        "trap must handle EXIT or ERR"
    )

    assert any(x in source for x in [
        "-d ",
        "test -d",
        "[ -d",
        "[[ -d",
    ]), "safe_backup.sh must validate directory input"


def test_common_utils_features():
    source = read(UTILS).lower()

    for name in ["info", "warn", "error"]:
        assert name in source, (
            f"common_utils.sh missing {name} logging support"
        )

    assert (
        "getopts" in source
        or "case " in source
        or "while " in source
    ), "common_utils.sh missing argument parsing template"


def test_required_scripts_are_valid_bash():
    for path in [SAFE, UTILS]:
        result = subprocess.run(
            ["bash", "-n", path],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, (
            f"Bash syntax error in {path}:\n{result.stderr}"
        )


def test_required_scripts_pass_shellcheck():
    result = subprocess.run(
        [
            "shellcheck",
            "--severity=warning",
            "test/safe_backup.sh",
            "test/common_utils.sh",
        ],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
        timeout=120,
    )

    assert result.returncode == 0, (
        f"shellcheck failed:\n{result.stdout}\n{result.stderr}"
    )
