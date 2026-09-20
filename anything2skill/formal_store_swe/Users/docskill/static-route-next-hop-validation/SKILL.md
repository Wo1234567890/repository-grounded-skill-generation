---
id: "47108649-c88e-5616-84b8-b5ad982c8c4b"
name: "Static Route Next Hop Validation"
description: "Validate that hub router IPs are not used as next hop addresses in static route configurations to prevent routing loops and outages in Virtual WAN."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "static_routing"
  - "safety_constraint"
  - "next_hop_validation"
  - "routing_loop_prevention"
triggers:
  - "Defining static routes in Virtual WAN connections"
  - "Configuring next hop addresses for spoke virtual networks"
---

# Static Route Next Hop Validation

Validate that hub router IPs are not used as next hop addresses in static route configurations to prevent routing loops and outages in Virtual WAN.

## Prompt

When defining static routes in Virtual WAN, verify that hub router IPs are NOT used as next hop addresses in the route configuration.

## Objective

Prevent routing loops by excluding hub router IPs from static route next hop definitions
## Applicable Signals

- Static route creation or modification initiated
- Next hop IP address specified in route configuration

## Contraindications

- Using dynamic routing only (no static routes defined)
- Hub router IPs intentionally required as next hops in other systems outside Virtual WAN

## Intervention Moves

- Review next hop IP addresses in static route definitions
- Confirm no hub router IPs are present in next hop list
- Block deployment if hub router IPs detected in next hop configuration

## Workflow Steps

- {'step': 1, 'action': 'Review next hop IP addresses in static route definitions', 'check': 'Confirm no hub router IPs are present in next hop list'}
- {'step': 2, 'action': 'Document validation results', 'check': 'Record approval or remediation actions before deployment'}

## Constraints

- Hub router IPs must never be used as next hop addresses in static routes
- Validation must occur before route deployment

## Cautions

- Violating this constraint creates routing loops and potential outages

## Output Contract

- Static route next hop configuration validated
- Hub router IPs confirmed excluded from next hop definitions
- Validation report generated with approval or remediation actions

## Triggers

- Defining static routes in Virtual WAN connections
- Configuring next hop addresses for spoke virtual networks
