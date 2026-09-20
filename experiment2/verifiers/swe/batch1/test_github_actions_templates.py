
import json
import os
import subprocess

import yaml


REPO_DIR = "/workspace/starter-workflows"

WORKFLOW = os.path.join(
    REPO_DIR,
    "ci",
    "python-pytest.yml",
)

PROPERTIES = os.path.join(
    REPO_DIR,
    "ci",
    "properties",
    "python-pytest.properties.json",
)


def test_required_files_exist():
    assert os.path.isfile(WORKFLOW), (
        "ci/python-pytest.yml missing"
    )
    assert os.path.isfile(PROPERTIES), (
        "ci/properties/python-pytest.properties.json missing"
    )


def test_properties_exact_required_fields():
    with open(PROPERTIES, "r", encoding="utf-8") as f:
        props = json.load(f)

    assert props.get("name") == "Python pytest"
    assert "pytest" in props.get("description", "").lower()
    assert props.get("iconName") == "python"

    categories = props.get("categories", [])
    assert "Python" in categories
    assert "CI" in categories


def load_workflow():
    with open(WORKFLOW, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.BaseLoader)


def test_required_triggers_and_matrix():
    doc = load_workflow()

    triggers = doc.get("on", {})
    assert "push" in triggers
    assert "pull_request" in triggers

    jobs = doc.get("jobs", {})
    assert jobs

    combined = json.dumps(doc)

    for version in ["3.9", "3.10", "3.11", "3.12"]:
        assert version in combined, (
            f"Python {version} missing from matrix"
        )

    assert "ubuntu-latest" in combined


def test_required_ci_steps():
    with open(WORKFLOW, "r", encoding="utf-8") as f:
        source = f.read()

    assert "actions/checkout" in source
    assert "actions/setup-python" in source

    assert (
        "cache: pip" in source
        or "actions/cache" in source
    ), "pip dependency caching missing"

    assert "requirements.txt" in source
    assert "pytest" in source
    assert "coverage" in source


def test_actionlint_acceptance():
    result = subprocess.run(
        ["actionlint", "ci/python-pytest.yml"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
        timeout=120,
    )

    assert result.returncode == 0, (
        f"actionlint failed:\n{result.stdout}\n{result.stderr}"
    )
