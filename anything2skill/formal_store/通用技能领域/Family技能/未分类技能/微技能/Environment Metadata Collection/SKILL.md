---
id: "ef672d65-9bb8-50e3-aab8-4f4f8f8d139a"
name: "Environment Metadata Collection"
description: "Automatically capture and log runtime environment details (OS type/version, Python version, anonymized hostname, SDK version) at agent startup for debugging and reproducibility."
version: "0.1.0"
tags:
  - "environment"
  - "metadata"
  - "logging"
  - "debugging"
  - "initialization"
  - "reproducibility"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Agent startup or initialization"
  - "Session initialization"
  - "Debugging environment-related issues"
---

# Environment Metadata Collection

Automatically capture and log runtime environment details (OS type/version, Python version, anonymized hostname, SDK version) at agent startup for debugging and reproducibility.

## Prompt

Collect the following environment metadata at agent startup or session initialization: operating system type and version, Python version in use, hostname (anonymized), and SDK version. Log this metadata so it is available in the monitoring dashboard for later inspection.

## Objective

collect_environment_metadata
## Applicable Signals

- Agent process begins
- Monitoring session starts
- Environment troubleshooting requested

## Contraindications

- User has explicitly disabled telemetry collection
- Privacy-sensitive deployment where hostname or OS must not be logged
- Compliance requirements prohibit automatic environment capture

## Workflow Steps

- Detect operating system type and version
- Retrieve Python version in use
- Capture hostname and anonymize it
- Retrieve SDK version
- Log all four metadata fields to persistent storage
- Confirm metadata is available in dashboard

## Constraints

- Hostname must be anonymized before logging
- Collection must occur before agent execution begins
- Metadata must be persisted for dashboard access

## Output Contract

- Environment metadata record containing OS type/version, Python version, anonymized hostname, and SDK version is logged and accessible in the monitoring dashboard

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Agent startup or initialization
- Session initialization
- Debugging environment-related issues
