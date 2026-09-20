---
id: "71bfd5c8-ba32-52eb-9df6-e536db3c233c"
name: "Virtual WAN Branch Connection Routing Consistency Enforcement"
description: "Validates and enforces that all branch connections (Point-to-site, Site-to-site, ExpressRoute) are consistently associated to the Default route table and propagate routes to the same set of route tables, ensuring uniform prefix learning and reachability across all branches."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "branch_connections"
  - "routing_policy"
  - "configuration_validation"
  - "consistency_enforcement"
triggers:
  - "configuring branch connections in Virtual WAN"
  - "validating routing consistency across multiple branch types"
---

# Virtual WAN Branch Connection Routing Consistency Enforcement

Validates and enforces that all branch connections (Point-to-site, Site-to-site, ExpressRoute) are consistently associated to the Default route table and propagate routes to the same set of route tables, ensuring uniform prefix learning and reachability across all branches.

## Prompt

Verify and enforce the following configuration constraints:
1. All branch connections must be associated to the Default route table.
2. All branch connections must propagate their routes to the same set of route tables.
3. Document the route table association and propagation configuration for each branch connection type.
4. Confirm consistency across all branches before deployment.

## Objective

enforce_consistent_branch_routing_configuration
## Applicable Signals

- configuring branch connections in Virtual WAN
- validating routing consistency across multiple branch types
- adding or modifying Point-to-site, Site-to-site, or ExpressRoute connections
- pre-deployment routing audit

## Contraindications

- hub is isolated or branch connections are intentionally segmented into different route tables
- asymmetric routing is explicitly required by design
- branches are intentionally isolated from each other

## Intervention Moves

- Identify all branch connections in the Virtual WAN hub
- Verify each branch connection is associated to the Default route table
- Confirm all branch connections propagate routes to the same set of route tables
- Document route table association and propagation settings for each branch connection
- Validate consistency across all branch connection types
- Remediate any non-compliant branch connections to match standard configuration

## Workflow Steps

- {'step': 1, 'action': 'Identify all branch connections', 'detail': 'List all Point-to-site, Site-to-site, and ExpressRoute connections in the Virtual WAN hub.'}
- {'step': 2, 'action': 'Verify Default route table association', 'detail': 'Confirm each branch connection is associated to the Default route table.'}
- {'step': 3, 'action': 'Verify route propagation configuration', 'detail': 'Confirm all branch connections propagate routes to the same set of route tables.'}
- {'step': 4, 'action': 'Document configuration state', 'detail': 'Record the route table association and propagation settings for each branch connection.'}
- {'step': 5, 'action': 'Validate consistency', 'detail': 'Ensure no branch connection deviates from the standard configuration.'}
- {'step': 6, 'action': 'Remediate deviations', 'detail': 'Update any non-compliant branch connections to match the standard configuration.'}

## Constraints

- All branch connection types (Point-to-site, Site-to-site, ExpressRoute) must use the same route table association.
- Route propagation configuration must be identical across all branches.
- Changes to one branch connection's route table association require corresponding updates to all other branches.

## Cautions

- Inconsistent route table associations will result in some branches being unable to reach others.
- Partial propagation configuration can cause routing failures and connectivity loss.
- Verify configuration before committing changes to production Virtual WAN instances.

## Output Contract

- All branch connections verified as associated to the Default route table; route propagation configuration confirmed consistent across all branches. Output includes: (1) list of all branch connections with their route table associations, (2) confirmation of propagation configuration consistency, (3) any remediation actions taken.

## Triggers

- configuring branch connections in Virtual WAN
- validating routing consistency across multiple branch types
