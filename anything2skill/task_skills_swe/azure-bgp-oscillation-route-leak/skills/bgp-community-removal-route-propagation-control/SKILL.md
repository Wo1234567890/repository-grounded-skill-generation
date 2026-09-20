---
id: "e2a8910f-9b71-581b-ba7f-be1622820f4a"
name: "BGP Community Removal Route Propagation Control"
description: "Prevent re-advertisement of routes with removed Azure BGP communities back into Virtual WAN to avoid routing issues and outages."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "bgp_communities"
  - "route_propagation"
  - "safety_constraint"
  - "outage_prevention"
triggers:
  - "Managing BGP community attributes on routes"
  - "Configuring route propagation settings"
---

# BGP Community Removal Route Propagation Control

Prevent re-advertisement of routes with removed Azure BGP communities back into Virtual WAN to avoid routing issues and outages.

## Prompt

When managing BGP community attributes on routes: Confirm that routes with removed Azure BGP communities are NOT re-advertised back into Virtual WAN.

## Objective

Prevent routing issues by controlling propagation of routes with removed BGP communities
## Applicable Signals

- BGP community removal or modification detected
- Route propagation configuration initiated

## Contraindications

- Using dynamic routing only (no static routes defined)

## Intervention Moves

- Audit BGP community attributes on routes being configured
- Identify routes with removed Azure BGP communities
- Verify re-advertisement settings
- Block propagation if removed BGP communities detected

## Workflow Steps

- {'step': 1, 'action': 'Audit BGP community attributes on routes being configured', 'check': 'Identify any routes with removed Azure BGP communities'}
- {'step': 2, 'action': 'Verify re-advertisement settings', 'check': 'Ensure routes with removed BGP communities are not propagated back into Virtual WAN'}
- {'step': 3, 'action': 'Document validation results', 'check': 'Record approval or remediation actions before deployment'}

## Constraints

- Routes with removed Azure BGP communities must not be re-advertised into Virtual WAN
- Validation must occur before route deployment

## Cautions

- BGP community removal without proper handling can cause route propagation failures and outages

## Output Contract

- BGP community handling validated and confirmed compliant
- Routes with removed communities confirmed excluded from re-advertisement
- Validation report generated with approval or remediation actions

## Triggers

- Managing BGP community attributes on routes
- Configuring route propagation settings
