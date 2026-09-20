---
id: "b29e3738-05f8-52f9-a327-b879906b46b0"
name: "Collect Agent Runtime Environment Metadata"
description: "Automatically gather and log basic system and SDK information (OS type/version, Python version, anonymized hostname, SDK version) from the agent execution environment for debugging and diagnostics."
version: "0.1.0"
tags:
  - "environment"
  - "diagnostics"
  - "metadata"
  - "initialization"
  - "observability"
triggers:
  - "Agent process starts or when debugging environment-related issues; invoked automatically during SDK initialization"
---

# Collect Agent Runtime Environment Metadata

Automatically gather and log basic system and SDK information (OS type/version, Python version, anonymized hostname, SDK version) from the agent execution environment for debugging and diagnostics.

## Prompt

Collect the following environment metadata at agent initialization: operating system type and version, Python version, anonymized hostname, and SDK version. Store the result in a structured metadata record for logging and dashboard display.

## Objective

capture_environment_state
## Applicable Signals

- Agent process startup
- SDK initialization begins
- Debugging environment-related issues requested

## Contraindications

- User has explicitly disabled telemetry or environment collection
- Running in restricted security contexts that prohibit system introspection

## Workflow Steps

- {'step': 1, 'action': 'Detect operating system type and version'}
- {'step': 2, 'action': 'Retrieve Python version in use'}
- {'step': 3, 'action': 'Obtain hostname and anonymize if necessary'}
- {'step': 4, 'action': 'Retrieve SDK version'}
- {'step': 5, 'action': 'Assemble metadata into structured record'}
- {'step': 6, 'action': 'Log metadata and make available for dashboard display'}

## Constraints

- Hostname must be anonymized before logging
- Collection must not block agent initialization
- Must respect user telemetry preferences

## Output Contract

- Structured metadata record containing: OS type, OS version, Python version, anonymized hostname, and SDK version; record is logged and available for downstream dashboard views and debugging workflows.

## Triggers

- Agent process starts or when debugging environment-related issues; invoked automatically during SDK initialization
