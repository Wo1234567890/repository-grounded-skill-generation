---
id: "27ac5968-5d6f-5ef7-b50d-ee2aceca1e10"
name: "Static Route Next Hop Validation"
description: "Validates that static route next hop IP addresses do not match hub router IPs in Virtual WAN configurations. Prevents routing loops and misconfigurations by rejecting routes that use hub router IPs as next hop addresses."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "static_routing"
  - "configuration_validation"
  - "next_hop_validation"
  - "routing_safety"
triggers:
  - "defining static routes in Virtual WAN"
  - "configuring next hop addresses"
examples:
  - input: "Static route definition: destination 10.2.0.0/16, next hop 10.0.0.1 (hub router IP)"
    output: "Configuration rejected. Hub router IP 10.0.0.1 cannot be used as next hop. Specify spoke virtual appliance IP instead."
    notes: "Prevents routing loop and misconfiguration."
---

# Static Route Next Hop Validation

Validates that static route next hop IP addresses do not match hub router IPs in Virtual WAN configurations. Prevents routing loops and misconfigurations by rejecting routes that use hub router IPs as next hop addresses.

## Prompt

When defining static routes in Virtual WAN, validate that next hop IP addresses do not match hub router IPs. Reject any static route configuration where the next hop is identified as a hub router IP and suggest alternative next hop addresses (e.g., spoke virtual appliance IPs).

## Objective

prevent_hub_router_ip_next_hop_misconfigurations
## Applicable Signals

- static route definition initiated
- next hop IP address specified

## Contraindications

- dynamic routing only (no static routes defined)
- hub router IPs are intentionally required as next hop (architectural exception)

## Intervention Moves

- Reject static route if hub router IP detected in next hop field
- Suggest alternative next hop (e.g., spoke virtual appliance IP)
- Provide validation checklist confirming next hop is not hub router IP

## Workflow Steps

- Capture next hop IP address from static route definition
- Identify hub router IPs in the Virtual WAN configuration
- Compare next hop IP against hub router IP list
- If match found, reject configuration with violation reason
- If no match, approve next hop selection

## Constraints

- hub router IPs must never be used as next hop in static routes
- validation must occur before route activation

## Cautions

- violation of this constraint causes routing loops and potential outages
- hub router IP validation must be performed on all next hop addresses in the route definition

## Output Contract

- Route next hop configuration validated. If hub router IP is detected in next hop field, configuration is rejected with specific violation reason and alternative next hop suggestion provided. If validation passes, route is approved for deployment with hub router IP absence confirmed.

## Example Therapist Responses

### Example 1

- Client/Input: Static route definition: destination 10.2.0.0/16, next hop 10.0.0.1 (hub router IP)
- Therapist/Output: Configuration rejected. Hub router IP 10.0.0.1 cannot be used as next hop. Specify spoke virtual appliance IP instead.
- Notes: Prevents routing loop and misconfiguration.

## Triggers

- defining static routes in Virtual WAN
- configuring next hop addresses

## Examples

### Example 1

Input:

  Static route definition: destination 10.2.0.0/16, next hop 10.0.0.1 (hub router IP)

Output:

  Configuration rejected. Hub router IP 10.0.0.1 cannot be used as next hop. Specify spoke virtual appliance IP instead.

Notes:

  Prevents routing loop and misconfiguration.
