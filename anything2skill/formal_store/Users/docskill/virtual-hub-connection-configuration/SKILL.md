---
id: "6638f7f5-52cf-5aea-a353-2abbe66acf3d"
name: "Virtual Hub Connection Configuration"
description: "Establish and configure routing settings for one of four connection types (VPN, ExpressRoute, P2S, or hub virtual network) to a virtual hub, with default association and propagation to the Default route table."
version: "0.1.0"
tags:
  - "network_connection"
  - "routing_configuration"
  - "virtual_hub"
  - "connection_setup"
triggers:
  - "User initiates setup of a new VPN connection to a virtual hub VPN gateway"
  - "User initiates setup of a new ExpressRoute connection to a virtual hub ExpressRoute gateway"
  - "User initiates setup of a new P2S (Point-to-site) User VPN configuration to a virtual hub User VPN gateway"
  - "User initiates setup of a new hub virtual network connection to connect virtual networks to a virtual hub"
---

# Virtual Hub Connection Configuration

Establish and configure routing settings for one of four connection types (VPN, ExpressRoute, P2S, or hub virtual network) to a virtual hub, with default association and propagation to the Default route table.

## Prompt

Create a new connection resource (VPN, ExpressRoute, P2S, or hub virtual network) to a virtual hub. Configure its routing settings during setup. By default, the connection will associate and propagate to the Default route table. Verify that the connection resource is created as a Resource Manager resource with routing configuration applied.

## Objective

Configure a new connection resource with correct routing defaults
## Applicable Signals

- Connection type selected (VPN, ExpressRoute, P2S, or hub virtual network)
- Virtual hub target identified
- Routing configuration required during connection setup

## Contraindications

- Do not use when modifying existing route table policies
- Do not use when troubleshooting routing propagation issues
- Do not use when managing inter-hub routing
- Do not use for post-creation connection modifications

## Workflow Steps

- {'step': 1, 'action': 'Select connection type', 'detail': 'Choose one of: VPN connection, ExpressRoute connection, P2S configuration connection, or hub virtual network connection'}
- {'step': 2, 'action': 'Identify target virtual hub and gateway', 'detail': 'Specify the virtual hub and corresponding gateway (VPN gateway, ExpressRoute gateway, User VPN gateway, or hub)'}
- {'step': 3, 'action': 'Configure routing settings', 'detail': 'Set up routing configuration for the connection during setup phase'}
- {'step': 4, 'action': 'Create connection resource', 'detail': 'Create the Resource Manager resource with routing configuration applied'}
- {'step': 5, 'action': 'Verify default associations', 'detail': 'Confirm that the connection automatically associates and propagates to the Default route table'}

## Constraints

- Connection must be created as a Resource Manager resource
- Routing configuration must be set up during connection initialization
- Default route table association and propagation apply automatically

## Output Contract

- Connection resource created and registered as a Resource Manager resource with routing configuration applied
- Connection associated and propagated to Default route table
- Connection ready for traffic routing

## Triggers

- User initiates setup of a new VPN connection to a virtual hub VPN gateway
- User initiates setup of a new ExpressRoute connection to a virtual hub ExpressRoute gateway
- User initiates setup of a new P2S (Point-to-site) User VPN configuration to a virtual hub User VPN gateway
- User initiates setup of a new hub virtual network connection to connect virtual networks to a virtual hub
