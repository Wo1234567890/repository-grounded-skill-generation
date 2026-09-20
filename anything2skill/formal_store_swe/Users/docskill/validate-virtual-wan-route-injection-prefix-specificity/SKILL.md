---
id: "163a4d6b-628f-57cd-b363-f19e095fdf47"
name: "Validate Virtual WAN Route Injection Prefix Specificity"
description: "Classify observed BGP route leak incidents into one of six documented types based on the relationship between offending AS, route origin, and announcement destination. Enables root cause determination and remediation planning by mapping incidents to established leak patterns."
version: "0.1.1"
tags:
  - "bgp"
  - "route_leak"
  - "incident_classification"
  - "network_security"
  - "taxonomy"
triggers:
  - "Planning route injection into spoke VNets"
  - "Designing routing policies for Virtual WAN"
  - "Troubleshooting route injection failures"
  - "Validating route prefix configuration before deployment"
examples:
  - input: "Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.0.0.0/8"
    output: "Valid. Prefix 10.0.0.0/8 is shorter (less specific) than 10.1.0.0/16. Route can be injected."
    notes: "Shorter prefix means fewer bits specified, allowing Virtual WAN to program the route."
  - input: "Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.1.0.0/24"
    output: "Invalid. Prefix 10.1.0.0/24 is more specific than 10.1.0.0/16. Route cannot be injected."
    notes: "More specific prefix (longer) falls within the VNet boundary and violates the constraint."
  - input: "Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.1.0.0/16"
    output: "Invalid. Prefix matches the VNet prefix exactly. Route cannot be injected."
    notes: "Equal specificity is not permitted; prefix must be strictly shorter."
---

# Validate Virtual WAN Route Injection Prefix Specificity

Classify observed BGP route leak incidents into one of six documented types based on the relationship between offending AS, route origin, and announcement destination. Enables root cause determination and remediation planning by mapping incidents to established leak patterns.

## Prompt

Given a reported BGP route leak incident, identify the offending AS (the AS announcing a route in violation of intended policies), the source of the route (transit provider, lateral peer, or internal), and the destination where it was announced. Match the incident pattern to one of the six documented route leak types to determine root cause and policy violation.

## Objective

categorize_route_leak_incident
## Applicable Signals

- Offending AS identity and its role (transit provider, peer, or customer)
- Route origin (transit provider, lateral peer, or internal prefix)
- Announcement destination (peer, transit provider, or customer cone)
- Whether the announced prefix matches the route origin or is more-specific

## Contraindications

- Incident involves intentional route manipulation or policy-compliant multi-path announcements
- Non-BGP routing protocols are involved
- Route announcement is authorized by explicit policy agreement

## Workflow Steps

- Identify the offending AS from incident report
- Determine route origin relationship (transit provider, lateral peer, or internal)
- Identify announcement destination (peer, transit provider, or customer cone)
- Match incident pattern to one of six documented route leak types
- Document policy violation and root cause pattern

## Constraints

- Classification requires clear identification of the offending AS
- Route origin and destination relationship must be determinable from incident data
- Taxonomy covers only documented route leak patterns; novel patterns may not fit existing types

## Cautions

- Type 3 and Type 4 leaks involve lateral peer relationships; verify peer status is non-transit
- Type 6 leaks involve internal prefixes or more-specific announcements; distinguish from legitimate aggregation
- Multiple leak types may occur in a single incident; classify the primary violation

## Output Contract

- Incident mapped to one of six route leak types with offending AS identified, policy violation described, and root cause pattern established for remediation planning.

## Triggers

- Planning route injection into spoke VNets
- Designing routing policies for Virtual WAN
- Troubleshooting route injection failures
- Validating route prefix configuration before deployment

## Examples

### Example 1

Input:

  Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.0.0.0/8

Output:

  Valid. Prefix 10.0.0.0/8 is shorter (less specific) than 10.1.0.0/16. Route can be injected.

Notes:

  Shorter prefix means fewer bits specified, allowing Virtual WAN to program the route.

### Example 2

Input:

  Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.1.0.0/24

Output:

  Invalid. Prefix 10.1.0.0/24 is more specific than 10.1.0.0/16. Route cannot be injected.

Notes:

  More specific prefix (longer) falls within the VNet boundary and violates the constraint.

### Example 3

Input:

  Spoke VNET1 prefix: 10.1.0.0/16. Proposed route to inject: 10.1.0.0/16

Output:

  Invalid. Prefix matches the VNet prefix exactly. Route cannot be injected.

Notes:

  Equal specificity is not permitted; prefix must be strictly shorter.
