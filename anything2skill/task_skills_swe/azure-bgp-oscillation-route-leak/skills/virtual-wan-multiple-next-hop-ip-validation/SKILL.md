---
id: "b1496473-6df6-5357-bf99-b0a73ae109f1"
name: "Virtual WAN Multiple Next Hop IP Validation"
description: "Validate that multiple next hop IP addresses on a single VNet connection do not include a public IP or 0.0.0.0/0 route pointing to the same network virtual appliance, as this configuration is unsupported and will cause routing failures."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "routing"
  - "next_hop"
  - "network_appliance"
  - "configuration_validation"
triggers:
  - "Configuring multiple next hop IP addresses on VNet connections"
  - "Defining routes to network virtual appliances in spokes"
---

# Virtual WAN Multiple Next Hop IP Validation

Validate that multiple next hop IP addresses on a single VNet connection do not include a public IP or 0.0.0.0/0 route pointing to the same network virtual appliance, as this configuration is unsupported and will cause routing failures.

## Prompt

When configuring multiple next hop IPs on a VNet connection:
1. Identify all routes targeting the same network virtual appliance in the spoke.
2. Check if any route uses a public IP address or 0.0.0.0/0 as the next hop.
3. If yes, reject the configuration or separate routes to different appliances.
4. Confirm all next hop IPs for the same appliance use private, non-default routes only.

## Objective

Prevent unsupported multiple next hop configurations that could cause routing failures
## Applicable Signals

- Configuring multiple next hop IP addresses on a single VNet connection
- Defining routes to network virtual appliances in spoke virtual networks
- Adding or modifying next hop IPs for the same appliance target

## Contraindications

- Single next hop configurations (no validation needed)
- Routes to different network virtual appliances (separate validation per appliance)
- Non-appliance next hop targets

## Intervention Moves

- Validate next hop IP list against appliance target
- Check for public IP or 0.0.0.0/0 in multi-hop configuration
- Reject or flag unsupported combinations before deployment

## Workflow Steps

- Identify all routes targeting the same network virtual appliance
- Enumerate next hop IP addresses for that appliance target
- Check for presence of public IP addresses in the next hop list
- Check for presence of 0.0.0.0/0 in the next hop list
- If public IP or 0.0.0.0/0 found with other next hops to same appliance, flag as unsupported
- If all next hops are private IPs and no 0.0.0.0/0 to same appliance, confirm as supported

## Constraints

- Multiple next hop IPs to the same appliance must all be private IP addresses
- 0.0.0.0/0 (internet route) cannot coexist with other next hops to the same appliance
- Public IP addresses cannot be used as next hop when multiple routes target the same appliance

## Cautions

- This constraint applies only to multiple next hop IPs on the same VNet connection targeting the same appliance
- Single next hop configurations or routes to different appliances are not subject to this restriction

## Output Contract

- Configuration validation result: either (1) next hop configuration confirmed as supported (all IPs private, no 0.0.0.0/0 to same appliance), or (2) unsupported configuration identified with specific constraint violation details

## Triggers

- Configuring multiple next hop IP addresses on VNet connections
- Defining routes to network virtual appliances in spokes
