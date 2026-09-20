"""
Test for 'grafana-dashboards' skill — Grafana Dashboard Provisioning
Validates that the Agent created JSON dashboards with proper panel definitions
and a provisioning YAML for Grafana.
"""

import os
import json
import pytest
import yaml  # Imported at the top for consistency


class TestGrafanaDashboards:
    """Verify Grafana dashboard provisioning setup."""

    REPO_DIR = "/workspace/grafana"

    # [!] Change: extracted constant path to match the requirements doc
    JSON_PATH = ("devenv", "dev-dashboards", "infra", "service_metrics.json")
    YAML_PATH = ("devenv", "provisioning", "dashboards", "infra.yaml")

    # ------------------------------------------------------------------
    # L1: file existence
    # ------------------------------------------------------------------

    def test_dashboard_json_exists(self):
        """service_metrics.json must exist."""
        fpath = os.path.join(self.REPO_DIR, *self.JSON_PATH)
        assert os.path.isfile(fpath), f"{self.JSON_PATH[-1]} not found"

    def test_provisioning_yaml_exists(self):
        """infra.yaml must exist."""
        fpath = os.path.join(self.REPO_DIR, *self.YAML_PATH)
        assert os.path.isfile(fpath), f"{self.YAML_PATH[-1]} not found"

    # ------------------------------------------------------------------
    # L2: dashboard JSON validation
    # ------------------------------------------------------------------

    def _load_dashboard(self):
        fpath = os.path.join(self.REPO_DIR, *self.JSON_PATH)
        with open(fpath, "r") as f:
            return json.load(f)

    def test_dashboard_is_valid_json(self):
        """service_metrics.json must be valid JSON."""
        dash = self._load_dashboard()
        assert isinstance(dash, dict), "Dashboard root must be an object"

    def test_dashboard_has_title(self):
        """Dashboard must have a title."""
        dash = self._load_dashboard()
        assert "title" in dash, "Dashboard 'title' field missing"
        assert len(dash["title"]) > 0, "Dashboard title is empty"

    def test_dashboard_has_panels(self):
        """Dashboard must have at least 4 panels."""
        dash = self._load_dashboard()
        panels = dash.get("panels", [])
        assert len(panels) >= 4, f"Need >= 4 panels, got {len(panels)}"

    def test_panels_have_required_fields(self):
        """Each panel must have id, type, title, and targets or similar."""
        dash = self._load_dashboard()
        for panel in dash.get("panels", []):
            assert "type" in panel, f"Panel missing 'type': {panel.get('title', '?')}"
            assert (
                "title" in panel or "id" in panel
            ), "Panel missing both 'title' and 'id'"

    def test_has_graph_or_timeseries_panel(self):
        """At least one panel must be graph or timeseries type."""
        dash = self._load_dashboard()
        types = {p.get("type") for p in dash.get("panels", [])}
        graph_types = {"graph", "timeseries", "stat", "gauge", "barchart"}
        assert types & graph_types, f"No graph-like panel found; types: {types}"

    def test_dashboard_has_datasource(self):
        """Dashboard should reference a data source."""
        dash = self._load_dashboard()
        content = json.dumps(dash)
        assert "datasource" in content.lower(), "No datasource reference found"

    def test_has_prometheus_queries(self):
        """Dashboard panels should have Prometheus queries (expr)."""
        dash = self._load_dashboard()
        content = json.dumps(dash)
        query_markers = ["expr", "promQL", "rate(", "sum(", "histogram_quantile"]
        found = any(m in content for m in query_markers)
        assert found, "No Prometheus query expressions found in panels"

    def test_provisioning_yaml_valid(self):
        """infra.yaml must be valid YAML with providers."""
        fpath = os.path.join(self.REPO_DIR, *self.YAML_PATH)
        with open(fpath, "r") as f:
            config = yaml.safe_load(f)
        assert isinstance(config, dict), "Provisioning must be a mapping"

    def test_provisioning_references_path(self):
        """Provisioning config must reference dashboard folder path."""
        fpath = os.path.join(self.REPO_DIR, *self.YAML_PATH)
        with open(fpath, "r") as f:
            content = f.read()
        assert (
            "path" in content or "folder" in content
        ), "Provisioning config missing path/folder reference"

    def test_templating_variables(self):
        """Dashboard should have templating variables."""
        dash = self._load_dashboard()
        templating = dash.get("templating", {})
        var_list = templating.get("list", [])
        assert len(var_list) >= 1, "Dashboard should have at least 1 template variable"


# TASK_ALIGNED_GRAFANA_CHECKS

def test_prometheus_datasource_config():
    path = os.path.join(
        TestGrafanaDashboards.REPO_DIR,
        "devenv",
        "provisioning",
        "datasources",
        "prometheus.yaml",
    )

    assert os.path.isfile(path), (
        "prometheus.yaml datasource config missing"
    )

    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    text = str(config)

    assert "Prometheus" in text or "prometheus" in text
    assert "http://localhost:9090" in text
    assert "proxy" in text.lower()


def test_dashboard_exact_task_features():
    dash = TestGrafanaDashboards()._load_dashboard()

    assert dash.get("uid"), "Dashboard uid missing"

    panel_types = {
        str(p.get("type", "")).lower()
        for p in dash.get("panels", [])
    }

    assert panel_types & {"graph", "timeseries"}, (
        "Request-rate graph/timeseries panel missing"
    )
    assert "stat" in panel_types, "Stat panel missing"
    assert "table" in panel_types, "Table panel missing"

    assert (
        "histogram" in panel_types
        or "heatmap" in panel_types
    ), "Latency histogram/heatmap panel missing"

    variables = {
        v.get("name")
        for v in dash.get("templating", {}).get("list", [])
    }

    assert "namespace" in variables, "$namespace variable missing"
    assert "service" in variables, "$service variable missing"

    time_cfg = dash.get("time", {})
    assert time_cfg.get("from") in {"now-1h", "now-60m"}, (
        "Default dashboard range must be last 1 hour"
    )


def test_dashboard_provisioning_exact_values():
    path = os.path.join(
        TestGrafanaDashboards.REPO_DIR,
        *TestGrafanaDashboards.YAML_PATH,
    )

    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    text = str(config)

    assert "devenv/dev-dashboards/infra" in text
    assert "disableDeletion" in text
    assert "updateIntervalSeconds" in text
    assert "10" in text
