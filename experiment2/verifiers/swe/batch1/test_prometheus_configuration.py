"""
Task-aligned verifier for 'prometheus-configuration'.

Independent checks:
- exact YAML structure required by the task
- Prometheus-native config parser
- Prometheus-native relabel engine
- repository-native Go tests

Agent-authored config/config_test.go is not used as the sole oracle.
"""

from pathlib import Path
import subprocess
import tempfile
import textwrap

import pytest
import yaml


REPO_DIR = Path("/workspace/prometheus")
CONFIG_FILE = (
    REPO_DIR
    / "documentation"
    / "examples"
    / "multi-job-prometheus.yml"
)
CONFIG_TEST = REPO_DIR / "config" / "config_test.go"


def run(cmd, *, cwd=REPO_DIR, timeout=600):
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


@pytest.fixture(scope="module")
def parsed_config():
    assert CONFIG_FILE.is_file(), (
        "documentation/examples/multi-job-prometheus.yml is missing"
    )

    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert isinstance(data, dict), "YAML root must be a mapping"
    return data


def jobs_by_name(config):
    jobs = config.get("scrape_configs")
    assert isinstance(jobs, list), "scrape_configs must be a list"

    result = {}
    for job in jobs:
        assert isinstance(job, dict), f"Invalid scrape job: {job!r}"
        name = job.get("job_name")
        assert isinstance(name, str) and name, (
            f"Scrape job missing job_name: {job!r}"
        )
        assert name not in result, f"Duplicate job_name: {name}"
        result[name] = job

    return jobs, result


def all_static_targets(job):
    targets = []
    for group in job.get("static_configs", []):
        targets.extend(group.get("targets", []))
    return targets


class TestPrometheusConfigurationTaskAligned:

    # --------------------------------------------------------------
    # Required artifacts
    # --------------------------------------------------------------

    def test_required_files_exist(self):
        assert CONFIG_FILE.is_file(), (
            "multi-job-prometheus.yml is missing"
        )
        assert CONFIG_TEST.is_file(), (
            "config/config_test.go is missing"
        )

    def test_config_test_go_was_modified(self):
        """
        Task explicitly requires adding parsing unit tests to config_test.go.
        """
        result = run(
            [
                "git",
                "diff",
                "--name-only",
                "HEAD",
                "--",
                "config/config_test.go",
            ],
            timeout=30,
        )

        assert result.returncode == 0, result.stderr
        assert "config/config_test.go" in result.stdout.splitlines(), (
            "Task requires adding tests to config/config_test.go, "
            "but it was not modified"
        )

    # --------------------------------------------------------------
    # Exact task-required YAML structure
    # --------------------------------------------------------------

    def test_exact_three_required_jobs(self, parsed_config):
        jobs, by_name = jobs_by_name(parsed_config)

        assert len(jobs) == 3, (
            f"Expected exactly 3 scrape jobs, got {len(jobs)}"
        )

        assert set(by_name) == {
            "prometheus",
            "node-exporter",
            "kubernetes-pods",
        }, (
            "Expected exactly prometheus, node-exporter, "
            f"and kubernetes-pods; got {sorted(by_name)}"
        )

    def test_prometheus_self_monitoring_target(self, parsed_config):
        _, by_name = jobs_by_name(parsed_config)

        targets = all_static_targets(by_name["prometheus"])

        assert targets == ["localhost:9090"], (
            "prometheus job must target exactly localhost:9090; "
            f"got {targets}"
        )

    def test_node_exporter_targets(self, parsed_config):
        _, by_name = jobs_by_name(parsed_config)

        targets = all_static_targets(by_name["node-exporter"])

        assert set(targets) == {
            "node1:9100",
            "node2:9100",
        }, (
            "node-exporter must target node1:9100 and node2:9100; "
            f"got {targets}"
        )

        assert len(targets) == 2, (
            f"Expected exactly 2 node-exporter targets, got {targets}"
        )

    def test_node_exporter_relabel_rule(self, parsed_config):
        _, by_name = jobs_by_name(parsed_config)

        rules = by_name["node-exporter"].get("relabel_configs", [])

        assert isinstance(rules, list) and rules, (
            "node-exporter must define relabel_configs"
        )

        matching = [
            r for r in rules
            if r.get("source_labels") == ["__address__"]
            and r.get("target_label") == "instance"
        ]

        assert matching, (
            "Missing node-exporter relabel rule mapping "
            "__address__ to instance"
        )

        rule = matching[0]

        assert rule.get("regex") == r"([^:]+):\d+", (
            "Expected regex '([^:]+):\\d+'; "
            f"got {rule.get('regex')!r}"
        )

        assert rule.get("replacement") == "${1}", (
            "Expected replacement '${1}'; "
            f"got {rule.get('replacement')!r}"
        )

        # Prometheus defaults an omitted action to "replace".
        assert rule.get("action", "replace") == "replace", (
            "Node relabel rule must use replace semantics"
        )

    def test_kubernetes_metric_filter_rule(self, parsed_config):
        _, by_name = jobs_by_name(parsed_config)

        rules = by_name["kubernetes-pods"].get(
            "metric_relabel_configs",
            [],
        )

        assert isinstance(rules, list) and rules, (
            "kubernetes-pods must define metric_relabel_configs"
        )

        matching = [
            r for r in rules
            if r.get("source_labels") == ["__name__"]
            and r.get("regex") == "go_.*"
            and r.get("action") == "drop"
        ]

        assert matching, (
            "Missing metric relabel rule that drops go_.* metrics "
            "using __name__"
        )

    # --------------------------------------------------------------
    # Prometheus-native independent validation
    # --------------------------------------------------------------

    def test_prometheus_native_parser_and_relabel_behavior(self):
        """
        Use Prometheus's own config parser and relabel implementation rather
        than reimplementing their semantics in the verifier.
        """

        helper = r'''
package main

import (
    "fmt"
    "io"
    "log/slog"
    "os"

    promconfig "github.com/prometheus/prometheus/config"
    "github.com/prometheus/prometheus/model/labels"
    "github.com/prometheus/prometheus/model/relabel"
)

func fail(format string, args ...any) {
    fmt.Fprintf(os.Stderr, format+"\n", args...)
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        fail("usage: verifier <config>")
    }

    logger := slog.New(
        slog.NewTextHandler(io.Discard, nil),
    )

    cfg, err := promconfig.LoadFile(
        os.Args[1],
        false,
        logger,
    )
    if err != nil {
        fail("Prometheus config parser rejected file: %v", err)
    }

    if len(cfg.ScrapeConfigs) != 3 {
        fail(
            "expected exactly 3 scrape configs, got %d",
            len(cfg.ScrapeConfigs),
        )
    }

    jobs := map[string]*promconfig.ScrapeConfig{}
    for _, sc := range cfg.ScrapeConfigs {
        jobs[sc.JobName] = sc
    }

    node, ok := jobs["node-exporter"]
    if !ok {
        fail("node-exporter job not found")
    }

    // Verify target relabel transformation using Prometheus itself.
    lb := labels.NewBuilder(
        labels.FromStrings(
            "__address__", "node1:9100",
        ),
    )

    if !relabel.ProcessBuilder(
        lb,
        node.RelabelConfigs...,
    ) {
        fail("node1:9100 was unexpectedly dropped")
    }

    transformed := lb.Labels()

    if got := transformed.Get("instance"); got != "node1" {
        fail(
            "expected instance=node1 after relabeling, got %q",
            got,
        )
    }

    kube, ok := jobs["kubernetes-pods"]
    if !ok {
        fail("kubernetes-pods job not found")
    }

    // go_* metric must be dropped.
    goMetric := labels.NewBuilder(
        labels.FromStrings(
            "__name__", "go_gc_duration_seconds",
        ),
    )

    if relabel.ProcessBuilder(
        goMetric,
        kube.MetricRelabelConfigs...,
    ) {
        fail("go_* metric was not dropped")
    }

    // A non-go metric must remain.
    otherMetric := labels.NewBuilder(
        labels.FromStrings(
            "__name__", "http_requests_total",
        ),
    )

    if !relabel.ProcessBuilder(
        otherMetric,
        kube.MetricRelabelConfigs...,
    ) {
        fail("non-go metric was unexpectedly dropped")
    }

    fmt.Println("PROMETHEUS_NATIVE_VALIDATION_OK")
}
'''

        with tempfile.TemporaryDirectory() as td:
            helper_path = Path(td) / "verify_prometheus_config.go"
            helper_path.write_text(
                textwrap.dedent(helper),
                encoding="utf-8",
            )

            result = run(
                [
                    "go",
                    "run",
                    str(helper_path),
                    str(CONFIG_FILE),
                ],
                timeout=600,
            )

        assert result.returncode == 0, (
            "Prometheus-native validation failed.\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

        assert "PROMETHEUS_NATIVE_VALIDATION_OK" in result.stdout

    # --------------------------------------------------------------
    # Repository-native test suite
    # --------------------------------------------------------------

    def test_go_config_tests_pass(self):
        result = run(
            [
                "go",
                "test",
                "./config/...",
                "-count=1",
            ],
            timeout=600,
        )

        assert result.returncode == 0, (
            "go test ./config/... failed.\n"
            f"stdout:\n{result.stdout[-3000:]}\n"
            f"stderr:\n{result.stderr[-2000:]}"
        )
