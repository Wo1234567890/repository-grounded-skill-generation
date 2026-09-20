---
id: "f8ce413d-fe72-5b08-926a-66e6d344b93e"
name: "Virtual Hub Router Configuration"
description: "Configure and manage BGP-based routing between multiple gateways (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall) within a virtual hub to enable transit connectivity across virtual networks."
version: "0.1.0"
tags:
  - "network_routing"
  - "virtual_hub"
  - "bgp"
  - "gateway_management"
  - "azure_virtual_wan"
  - "transit_connectivity"
triggers:
  - "Deploying a virtual hub with multiple gateway types"
  - "Requiring inter-gateway routing and virtual network transit connectivity"
  - "Configuring Standard Virtual WAN SKU with BGP-based routing"
---

# Virtual Hub Router Configuration

Configure and manage BGP-based routing between multiple gateways (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall) within a virtual hub to enable transit connectivity across virtual networks.

## Prompt

Set up a virtual hub router to manage routing between multiple gateway types using BGP. Ensure all connected gateways are configured to advertise routes and that transit connectivity is established between virtual networks connected to the hub. Verify that the router supports the required aggregate throughput (up to 50 Gbps for Standard Virtual WAN).

## Objective

establish_multi_gateway_routing
## Applicable Signals

- Multiple gateways present in virtual hub (VPN, ExpressRoute, Point-to-site, Firewall)
- Need for transit connectivity between virtual networks
- Standard Virtual WAN customer tier active

## Contraindications

- Non-Standard Virtual WAN SKUs
- Managing individual gateway configurations outside hub context
- Scenarios requiring static routing only without BGP

## Workflow Steps

- Verify virtual hub is deployed and Standard Virtual WAN SKU is active
- Confirm all required gateways (Site-to-site VPN, ExpressRoute, Point-to-site, Azure Firewall) are connected to the hub
- Enable BGP on each gateway and configure BGP peering with the hub router
- Verify route advertisement from all gateways via BGP
- Test transit connectivity between virtual networks connected to the hub
- Monitor router throughput and performance against 50 Gbps aggregate limit

## Constraints

- Applicable only to Standard Virtual WAN customers
- Maximum aggregate throughput: 50 Gbps
- Requires BGP capability on all connected gateways

## Cautions

- Ensure BGP configuration is consistent across all gateways to avoid routing loops
- Monitor aggregate throughput to prevent exceeding 50 Gbps limit
- Verify route propagation before considering configuration complete

## Output Contract

- Virtual hub router operational with all connected gateways advertising routes via BGP and transit connectivity established between virtual networks. Router is ready to forward traffic between gateways and virtual networks.

## Triggers

- Deploying a virtual hub with multiple gateway types
- Requiring inter-gateway routing and virtual network transit connectivity
- Configuring Standard Virtual WAN SKU with BGP-based routing
