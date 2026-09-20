---
id: "dc38a859-38f1-55bc-9391-873c4f853157"
name: "Validate Azure Firewall Multi-Region Route Table Alignment"
description: "Enforce that all spoke virtual networks in a multi-region Azure Firewall deployment within a single virtual hub are associated to the same route table. This prevents partial bypass of firewall inspection and ensures consistent security posture across all traffic flows."
version: "0.1.0"
tags:
  - "azure_firewall"
  - "virtual_wan"
  - "multi_region"
  - "route_table"
  - "security_constraint"
triggers:
  - "deploying Azure Firewall across multiple regions"
  - "configuring spoke virtual network associations in a virtual hub"
examples:
  - input: "Virtual hub with Azure Firewall deployed; three spoke VNets (VNet-A, VNet-B, VNet-C) with VNet-A and VNet-B associated to route table 'RT-Firewall' and VNet-C associated to 'RT-Direct'"
    output: "Configuration rejected; VNet-C must be reassociated to 'RT-Firewall' to ensure all traffic routes through the firewall"
    notes: "Partial bypass creates a security gap"
  - input: "Virtual hub with Azure Firewall; all three spoke VNets (VNet-A, VNet-B, VNet-C) associated to route table 'RT-Firewall'"
    output: "Configuration validated; all VNets route through firewall inspection"
    notes: "Consistent security posture confirmed"
---

# Validate Azure Firewall Multi-Region Route Table Alignment

Enforce that all spoke virtual networks in a multi-region Azure Firewall deployment within a single virtual hub are associated to the same route table. This prevents partial bypass of firewall inspection and ensures consistent security posture across all traffic flows.

## Prompt

When deploying Azure Firewall across multiple regions in a Virtual WAN hub, verify that all spoke virtual networks are associated to the same route table. Do not allow a subset of VNets to bypass the firewall while others route through it in the same hub. Confirm the association before finalizing the configuration.

## Objective

enforce_firewall_inspection_consistency
## Applicable Signals

- Azure Firewall deployed across multiple regions
- Spoke virtual networks being associated to route tables in a virtual hub
- Configuration review before firewall activation

## Contraindications

- Firewall is not deployed in the hub
- Single-region hub deployment
- Intentional traffic segmentation requiring some VNets to bypass firewall inspection

## Intervention Moves

- Identify all spoke virtual networks in the virtual hub and list all VNets connected to the hub
- Verify the route table association for each spoke VNet and confirm all VNets are associated to the same route table
- If associations differ, reassociate all VNets to a single route table
- Validate firewall inspection path for sample traffic flows to confirm traffic from all VNets routes through the firewall

## Workflow Steps

- {'step': 1, 'action': 'Identify all spoke virtual networks in the virtual hub', 'check': 'List all VNets connected to the hub'}
- {'step': 2, 'action': 'Verify the route table association for each spoke VNet', 'check': 'Confirm all VNets are associated to the same route table'}
- {'step': 3, 'action': 'If associations differ, reassociate all VNets to a single route table', 'check': 'No VNet is left with a different route table association'}
- {'step': 4, 'action': 'Validate firewall inspection path for sample traffic flows', 'check': 'Traffic from all VNets routes through the firewall'}

## Constraints

- All spoke VNets in the same hub must use the same route table
- Partial firewall bypass within a single hub is not supported
- This constraint applies only within a single virtual hub; different hubs may have different configurations

## Cautions

- Verify route table association before traffic flows begin
- Changing route table associations after deployment may cause traffic disruption
- Audit spoke VNet associations regularly to detect configuration drift

## Output Contract

- All spoke virtual networks in the hub are confirmed associated to the same route table
- Firewall inspection path is verified for all traffic flows
- Configuration is locked to prevent partial bypass

## Example Therapist Responses

### Example 1

- Client/Input: Virtual hub with Azure Firewall deployed; three spoke VNets (VNet-A, VNet-B, VNet-C) with VNet-A and VNet-B associated to route table 'RT-Firewall' and VNet-C associated to 'RT-Direct'
- Therapist/Output: Configuration rejected; VNet-C must be reassociated to 'RT-Firewall' to ensure all traffic routes through the firewall
- Notes: Partial bypass creates a security gap

### Example 2

- Client/Input: Virtual hub with Azure Firewall; all three spoke VNets (VNet-A, VNet-B, VNet-C) associated to route table 'RT-Firewall'
- Therapist/Output: Configuration validated; all VNets route through firewall inspection
- Notes: Consistent security posture confirmed

## Triggers

- deploying Azure Firewall across multiple regions
- configuring spoke virtual network associations in a virtual hub

## Examples

### Example 1

Input:

  Virtual hub with Azure Firewall deployed; three spoke VNets (VNet-A, VNet-B, VNet-C) with VNet-A and VNet-B associated to route table 'RT-Firewall' and VNet-C associated to 'RT-Direct'

Output:

  Configuration rejected; VNet-C must be reassociated to 'RT-Firewall' to ensure all traffic routes through the firewall

Notes:

  Partial bypass creates a security gap

### Example 2

Input:

  Virtual hub with Azure Firewall; all three spoke VNets (VNet-A, VNet-B, VNet-C) associated to route table 'RT-Firewall'

Output:

  Configuration validated; all VNets route through firewall inspection

Notes:

  Consistent security posture confirmed
