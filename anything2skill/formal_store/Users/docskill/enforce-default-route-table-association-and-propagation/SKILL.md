---
id: "3775efec-3285-5ad9-a47b-b5d31692bb7b"
name: "Enforce Default Route Table Association and Propagation"
description: "Validate and enforce automatic association and propagation of new connections (VPN, ExpressRoute, P2S, Hub virtual network) to the Default route table at initialization, unless explicitly overridden by user configuration. Prevents orphaned or misconfigured routing by ensuring all connections have a valid route table assignment."
version: "0.1.0"
tags:
  - "routing"
  - "virtual_hub"
  - "connection_management"
  - "default_behavior"
  - "guardrail"
triggers:
  - "Creating a new connection and no custom route table association has been specified"
---

# Enforce Default Route Table Association and Propagation

Validate and enforce automatic association and propagation of new connections (VPN, ExpressRoute, P2S, Hub virtual network) to the Default route table at initialization, unless explicitly overridden by user configuration. Prevents orphaned or misconfigured routing by ensuring all connections have a valid route table assignment.

## Prompt

When a new connection (VPN, ExpressRoute, P2S, or Hub virtual network) is created without an explicit route table assignment, confirm that it automatically associates and propagates to the Default route table. Do not allow connections to remain unassociated or to skip propagation unless the user has explicitly selected a non-default route table.

## Objective

Ensure routing consistency by enforcing default route table behavior for new connections
## Applicable Signals

- New VPN connection created
- New ExpressRoute connection created
- New P2S configuration connection created
- New Hub virtual network connection created
- Connection setup initiated without explicit route table selection

## Contraindications

- User has explicitly selected a non-default route table
- Custom routing policies are being managed for this connection
- Connection is part of a multi-table routing strategy

## Intervention Moves

- Verify connection resource has Default route table association set
- Confirm propagation flag is enabled for Default route table
- Log or alert if connection lacks route table assignment

## Workflow Steps

- Detect connection creation event for VPN, ExpressRoute, P2S, or Hub virtual network
- Check if user has explicitly specified a route table assignment
- If no explicit assignment, verify Default route table association is set
- Verify propagation flag is enabled for Default route table
- Validate routing configuration and confirm no orphaned connections exist

## Constraints

- Rule applies only at connection initialization or when no prior route table assignment exists
- Does not override user-specified route table selections
- Applies to all four connection types: VPN, ExpressRoute, P2S, and Hub virtual network

## Cautions

- Ensure user intent is captured before enforcing default behavior; explicit non-default selections must be honored
- Monitor for connections that bypass this rule through API or automation

## Output Contract

- Connection is confirmed associated and propagated to Default route table; routing configuration is validated and no orphaned or unrouted connections exist.

## Triggers

- Creating a new connection and no custom route table association has been specified
