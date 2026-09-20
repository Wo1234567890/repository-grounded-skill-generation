---
id: "d8ea0a6a-2ee7-5ade-872e-dde9abd80350"
name: "Assemble and Retrieve Tracing Client Instance"
description: "Construct a complete initialization parameter dictionary from user inputs and configuration, then retrieve or create a singleton client instance for tracing operations."
version: "0.1.0"
tags:
  - "initialization"
  - "client_factory"
  - "configuration"
  - "tracing"
  - "session_setup"
triggers:
  - "Starting a new tracing session"
  - "Resuming an existing tracing session"
  - "All configuration parameters (API key, endpoint, tags, queue settings) are available"
---

# Assemble and Retrieve Tracing Client Instance

Construct a complete initialization parameter dictionary from user inputs and configuration, then retrieve or create a singleton client instance for tracing operations.

## Prompt

Merge user-provided tags with default tags using set union to eliminate duplicates. Detect execution environment (Jupyter notebook vs. standard Python) to determine auto-start behavior. Assemble all initialization parameters into a single dictionary, then call get_client() to obtain or create the singleton client instance.

## Objective

Initialize and obtain a ready-to-use tracing client with merged configuration
## Applicable Signals

- user_provides_api_key
- user_provides_endpoint
- user_provides_tags_or_default_tags
- initialization_parameters_complete

## Contraindications

- Client is already initialized and active
- Configuration changes are not needed
- Tracing is disabled or skipped

## Workflow Steps

- {'step': 1, 'action': 'Merge tags and default_tags', 'detail': 'If both tags and default_tags are provided, combine them using set union to eliminate duplicates. If only one is provided, use that. If neither, set merged_tags to None.'}
- {'step': 2, 'action': 'Detect execution environment', 'detail': 'Attempt to call get_ipython().__class__.__name__ to check for Jupyter/ZMQInteractiveShell. If NameError is raised, assume standard Python environment. Set auto_start_session to False if Jupyter is detected, otherwise leave as provided.'}
- {'step': 3, 'action': 'Assemble initialization dictionary', 'detail': 'Create init_kwargs dictionary with all parameters: api_key, endpoint, app_url, max_wait_time, max_queue_size, default_tags (merged), trace_name, instrument_llm_calls, auto_start_session, auto_init, skip_auto_end_session, env_data_opt_out, log_level, fail_safe, log_session_replay_url, exporter_endpoint, plus any additional kwargs.'}
- {'step': 4, 'action': 'Retrieve or create client instance', 'detail': 'Call get_client() with the assembled init_kwargs to obtain the singleton client instance. This creates a new instance if none exists, or returns the existing one.'}

## Constraints

- API key must be provided or retrievable from environment
- Tags parameter and default_tags parameter are optional but may both be present
- Environment detection (Jupyter vs. standard) must complete before setting auto_start_session

## Cautions

- Tag merging uses set union; order is not preserved.
- Jupyter detection relies on exception handling; ensure NameError is the only expected exception.
- get_client() is a singleton factory; multiple calls with different parameters may not reinitialize an existing client.

## Output Contract

- A client instance (new or existing) with all initialization parameters applied, ready to accept trace events and manage session lifecycle.

## Triggers

- Starting a new tracing session
- Resuming an existing tracing session
- All configuration parameters (API key, endpoint, tags, queue settings) are available
