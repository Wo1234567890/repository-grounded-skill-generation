---
id: "25472116-53ae-5f48-b184-2fe552106ba6"
name: "Configure virtual hub connection routing"
description: "Set up routing configuration for a virtual network connection to a virtual hub, including association and propagation to route tables. Establishes the routing behavior when creating or reconfiguring a hub virtual network connection."
version: "0.1.0"
tags:
  - "azure"
  - "virtual-wan"
  - "routing"
  - "hub-connection"
  - "route-table"
  - "network-configuration"
triggers:
  - "creating a new virtual network connection to a virtual hub"
  - "reconfiguring routing behavior for an existing hub virtual network connection"
  - "need to define route table association and propagation for a connection"
---

# Configure virtual hub connection routing

Set up routing configuration for a virtual network connection to a virtual hub, including association and propagation to route tables. Establishes the routing behavior when creating or reconfiguring a hub virtual network connection.

## Prompt

When setting up a virtual network connection to a virtual hub, configure its routing by specifying which route table the connection should associate with and propagate to. By default, all connections associate and propagate to the Default route table. Customize this during connection setup if non-default routing behavior is required.

## Objective

establish and configure routing for hub connections
## Applicable Signals

- connection setup workflow initiated
- virtual network connection resource being created or modified
- routing configuration step reached during connection provisioning

## Contraindications

- troubleshooting existing route propagation issues unrelated to connection setup
- modifying route table policies independently of connection creation
- adjusting routes after connection is already established and stable

## Workflow Steps

- {'step': 1, 'action': 'Identify connection type', 'detail': 'Determine which connection type is being configured: VPN connection, ExpressRoute connection, P2S configuration connection, or Hub virtual network connection.'}
- {'step': 2, 'action': 'Select route table association', 'detail': 'Choose the route table to which the connection will associate. Default is the Default route table; specify a custom route table if non-default routing is required.'}
- {'step': 3, 'action': 'Configure propagation', 'detail': 'Set the propagation behavior to the selected route table. By default, all connections propagate to the Default route table.'}
- {'step': 4, 'action': 'Apply routing configuration', 'detail': 'Complete the connection setup with the routing configuration applied.'}
- {'step': 5, 'action': 'Verify association and propagation', 'detail': 'Confirm that the connection is associated and propagating to the intended route table.'}

## Constraints

- routing configuration must be set during or immediately after connection creation for optimal application
- connection must be a valid Resource Manager resource type (VPN, ExpressRoute, P2S, or Hub virtual network connection)

## Output Contract

- Virtual network connection resource created or updated with routing configuration applied
- Connection is associated and propagating to the specified route table (Default or custom)
- Routing behavior is active and ready for traffic flow

## Triggers

- creating a new virtual network connection to a virtual hub
- reconfiguring routing behavior for an existing hub virtual network connection
- need to define route table association and propagation for a connection
