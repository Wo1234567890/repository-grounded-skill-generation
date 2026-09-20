---
id: "178a5caa-cb2a-53ca-af41-94d900f83d6d"
name: "Client Configuration Update"
description: "Apply runtime configuration changes to an initialized client. Modify client behavior after instantiation without reinitializing."
version: "0.1.0"
tags:
  - "configuration"
  - "runtime"
  - "client"
  - "parameter_update"
triggers:
  - "Client is initialized and ready"
  - "Configuration parameters need adjustment after instantiation"
---

# Client Configuration Update

Apply runtime configuration changes to an initialized client. Modify client behavior after instantiation without reinitializing.

## Prompt

Call this skill when the client is already initialized and you need to adjust configuration parameters at runtime. Pass configuration key-value pairs as kwargs. The skill delegates to the client's config.configure() method to apply changes.

## Objective

Update client configuration parameters at runtime
## Applicable Signals

- Client initialization complete
- Runtime parameter change required

## Contraindications

- Client is not yet initialized; use constructor parameters instead
- Initial setup phase; defer to initialization configuration

## Workflow Steps

- Verify client is initialized
- Collect configuration parameters as kwargs
- Delegate to client.config.configure(**kwargs)
- Confirm configuration update completion

## Constraints

- Client must be in initialized state (_initialized=True)
- Configuration changes apply only to the current session

## Cautions

- Configuration changes do not restart or reinitialize the client
- Some parameters may require client restart to take full effect

## Output Contract

- Client config object updated with new parameter values; changes take effect immediately for subsequent operations

## Triggers

- Client is initialized and ready
- Configuration parameters need adjustment after instantiation
