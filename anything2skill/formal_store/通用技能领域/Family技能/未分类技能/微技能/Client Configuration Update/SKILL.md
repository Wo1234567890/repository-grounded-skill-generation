---
id: "87a0e63f-7be5-58b3-b072-f851cfc732ac"
name: "Client Configuration Update"
description: "Apply configuration parameter changes to an initialized client instance by delegating to the internal config object. Use this micro-skill when the client is already running and you need to modify settings without reinitializing."
version: "0.1.0"
tags:
  - "configuration"
  - "runtime"
  - "client"
  - "parameter_update"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Client is already initialized and in running state"
  - "Caller needs to modify one or more configuration settings at runtime"
---

# Client Configuration Update

Apply configuration parameter changes to an initialized client instance by delegating to the internal config object. Use this micro-skill when the client is already running and you need to modify settings without reinitializing.

## Prompt

Call this skill after client initialization. Pass configuration parameters as keyword arguments (kwargs). The skill updates the client's config object in-place and returns None. Do not use this to set initial configuration; use initialization parameters instead.

## Objective

Apply configuration changes to running client instance
## Applicable Signals

- client._initialized == True
- configuration change request received during active session

## Contraindications

- Client has not yet been initialized
- Caller should use initialization parameters instead of this skill for pre-initialization setup

## Workflow Steps

- Verify client is initialized
- Accept configuration kwargs from caller
- Delegate to self.config.configure(**kwargs)
- Return None (no return value)

## Constraints

- Client must be in initialized state before calling configure()
- Configuration changes are applied in-place to the running instance

## Cautions

- This skill modifies the running client state; ensure configuration changes are safe for the current execution context
- No validation or rollback is performed; caller is responsible for providing valid configuration parameters

## Output Contract

- Client config object is updated with provided kwargs; method returns None. Caller should verify configuration change took effect by inspecting client.config state if needed.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Client is already initialized and in running state
- Caller needs to modify one or more configuration settings at runtime
