---
id: "7ec5c4cf-2eb0-5ecb-af47-744d6e016140"
name: "Virtual Network Connection Next Hop IP Constraint Validation"
description: "Validates next hop IP configurations on virtual network connections to prevent conflicting routes. Enforces that multiple next hop IPs targeting the same network virtual appliance cannot coexist if any route uses a public IP address or 0.0.0.0/0 (internet) as next hop."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "routing"
  - "next_hop"
  - "network_appliance"
  - "constraint"
triggers:
  - "configuring multiple next hop IPs on a virtual network connection"
  - "adding internet-facing or public IP routes"
---

# Virtual Network Connection Next Hop IP Constraint Validation

Validates next hop IP configurations on virtual network connections to prevent conflicting routes. Enforces that multiple next hop IPs targeting the same network virtual appliance cannot coexist if any route uses a public IP address or 0.0.0.0/0 (internet) as next hop.

## Prompt

When configuring multiple next hop IP addresses on a single virtual network connection, verify that if any route specifies a public IP address or 0.0.0.0/0 (internet) as next hop, no other routes can target the same network virtual appliance with different next hop IPs. Reject or consolidate conflicting configurations before deployment.

## Objective

prevent_conflicting_next_hop_configurations
## Applicable Signals

- configuring multiple next hop IPs on a virtual network connection
- adding internet-facing routes (0.0.0.0/0)
- adding public IP address routes
- targeting same network virtual appliance with multiple next hops

## Contraindications

- single next hop IP is sufficient for the connection
- no public IP or 0.0.0.0/0 routes are planned
- different virtual appliances are targets for different routes

## Intervention Moves

- reject configuration with conflicting next hop IPs
- consolidate routes targeting same appliance
- remove or modify public IP or 0.0.0.0/0 routes

## Workflow Steps

- {'step': 1, 'action': 'Identify all next hop IPs configured on the virtual network connection'}
- {'step': 2, 'action': 'Check if any next hop IP is a public IP address or 0.0.0.0/0 (internet)'}
- {'step': 3, 'action': 'If public IP or 0.0.0.0/0 is present, verify that all other next hops target different network virtual appliances'}
- {'step': 4, 'action': 'If multiple next hops target the same appliance and a public IP or 0.0.0.0/0 route exists, reject configuration or consolidate routes'}
- {'step': 5, 'action': 'Document the validated configuration and appliance mappings'}

## Constraints

- Multiple unique next hop IPs to the same network virtual appliance are prohibited if any route uses public IP or 0.0.0.0/0
- This constraint applies only to the same virtual appliance target; different appliances may have different next hops

## Cautions

- Verify appliance identity before consolidating routes; misidentification can cause traffic loss
- Public IP and 0.0.0.0/0 routes have special precedence; review routing priority before consolidation

## Output Contract

- Next hop configuration validated and either approved for deployment or rejected with specific conflict details. Conflicting public IP or internet routes identified and consolidated or removed.

## Triggers

- configuring multiple next hop IPs on a virtual network connection
- adding internet-facing or public IP routes
