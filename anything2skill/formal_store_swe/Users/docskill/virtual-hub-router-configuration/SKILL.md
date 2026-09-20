---
id: "b920acd1-1335-567b-85dd-8959c9f3f8e7"
name: "Virtual Hub Router Configuration"
description: "Configure and manage BGP-based routing between multiple gateways (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall) within a virtual hub to enable transit connectivity across virtual networks."
version: "0.1.0"
tags:
  - "network_routing"
  - "bgp"
  - "virtual_wan"
  - "gateway_management"
  - "transit_connectivity"
triggers:
  - "Deploying a Standard Virtual WAN with multiple gateway types"
  - "Requirement for inter-gateway route exchange"
  - "Need to establish cross-VNet transit connectivity"
---

# Virtual Hub Router Configuration

Configure and manage BGP-based routing between multiple gateways (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall) within a virtual hub to enable transit connectivity across virtual networks.

## Prompt

Set up a virtual hub router to manage BGP-based routing between multiple gateway types. Ensure all connected gateways exchange routes via BGP and establish transit connectivity between virtual networks. Verify the router supports the aggregate throughput requirements (up to 50 Gbps).

## Objective

Set up multi-gateway routing with BGP protocol in a virtual hub
## Applicable Signals

- Multiple gateway types present (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall)
- Standard Virtual WAN SKU in use
- Transit routing between virtual networks required

## Contraindications

- Non-Standard Virtual WAN SKUs
- Single-gateway deployments without transit requirements
- Aggregate throughput requirements exceed 50 Gbps

## Workflow Steps

- {'step': 1, 'action': 'Verify Standard Virtual WAN deployment and SKU', 'detail': 'Confirm the virtual hub is part of a Standard Virtual WAN instance'}
- {'step': 2, 'action': 'Identify and inventory all connected gateways', 'detail': 'Document Site-to-site VPN, ExpressRoute, Point-to-site, and Azure Firewall gateways'}
- {'step': 3, 'action': 'Configure BGP routing on the virtual hub router', 'detail': 'Enable BGP protocol and set up routing policies between gateways'}
- {'step': 4, 'action': 'Establish route propagation between gateways', 'detail': 'Ensure all gateways exchange routes via BGP'}
- {'step': 5, 'action': 'Enable transit connectivity between virtual networks', 'detail': 'Configure virtual network connections to the hub for cross-VNet routing'}
- {'step': 6, 'action': 'Validate routing and throughput', 'detail': 'Test end-to-end connectivity and verify aggregate throughput is within limits'}

## Constraints

- Maximum aggregate throughput: 50 Gbps
- Requires Standard Virtual WAN tier
- BGP protocol must be supported by all connected gateways

## Cautions

- Verify all gateway types are compatible with BGP routing before configuration
- Monitor aggregate throughput to ensure it does not exceed 50 Gbps limit
- Test route propagation between all gateways after initial setup

## Output Contract

- Virtual hub router operational with all connected gateways exchanging routes via BGP and transit connectivity established between virtual networks. Routing tables populated and traffic flowing between gateways and virtual networks.

## Triggers

- Deploying a Standard Virtual WAN with multiple gateway types
- Requirement for inter-gateway route exchange
- Need to establish cross-VNet transit connectivity
