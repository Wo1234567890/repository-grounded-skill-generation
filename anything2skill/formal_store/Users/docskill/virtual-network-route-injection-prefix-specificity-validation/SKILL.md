---
id: "531cf59a-b6b2-5f8b-ab8c-931e75377728"
name: "Virtual Network Route Injection Prefix Specificity Validation"
description: "Validates that a route prefix being injected into a spoke virtual network via Virtual WAN is shorter (less specific) than the target VNet's CIDR prefix. Prevents routing conflicts, subnet route collisions, and unintended inter-subnet traffic attraction within the same VNet."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "route_injection"
  - "prefix_validation"
  - "spoke_network"
  - "routing_safety"
triggers:
  - "route injection request into a spoke virtual network"
  - "validation of route prefix before programming into Virtual WAN"
examples:
  - input: "Route prefix: 10.0.0.0/8; Spoke VNet prefix: 10.1.0.0/16"
    output: "Validation passed. Route prefix /8 is shorter than VNet prefix /16. Injection safe."
    notes: "Route is less specific than VNet, no conflict with subnets."
  - input: "Route prefix: 10.1.0.0/24; Spoke VNet prefix: 10.1.0.0/16"
    output: "Validation failed. Route prefix /24 is longer (more specific) than VNet prefix /16. Injection rejected."
    notes: "Route matches a subnet within the VNet; would create routing conflict."
  - input: "Route prefix: 10.1.0.0/16; Spoke VNet prefix: 10.1.0.0/16"
    output: "Validation failed. Route prefix /16 matches VNet prefix /16. Injection rejected."
    notes: "Route is equally specific; cannot be injected by Virtual WAN."
---

# Virtual Network Route Injection Prefix Specificity Validation

Validates that a route prefix being injected into a spoke virtual network via Virtual WAN is shorter (less specific) than the target VNet's CIDR prefix. Prevents routing conflicts, subnet route collisions, and unintended inter-subnet traffic attraction within the same VNet.

## Prompt

Before injecting a route into a spoke virtual network via Virtual WAN, validate that the route prefix length is shorter (less specific) than the virtual network's CIDR prefix. If the route prefix matches or is longer (more specific) than the VNet prefix, reject the injection and return a clear error message. Example: if spoke VNET1 has prefix 10.1.0.0/16, Virtual WAN cannot inject routes matching 10.1.0.0/16 or any subnet like 10.1.0.0/24 or 10.1.1.0/24.

## Objective

prevent_route_injection_conflicts
## Applicable Signals

- route prefix length being configured
- target spoke virtual network CIDR prefix known
- route injection operation initiated

## Contraindications

- route prefix is equal to or longer (more specific) than VNet prefix
- no route injection is required
- target VNet prefix is unknown or unavailable
- static route definition without Virtual WAN programming

## Workflow Steps

- {'step': 1, 'action': 'Retrieve target spoke virtual network CIDR prefix (e.g., 10.1.0.0/16)'}
- {'step': 2, 'action': 'Retrieve route prefix to be injected (e.g., 10.0.0.0/8)'}
- {'step': 3, 'action': 'Compare prefix lengths: if route prefix length > VNet prefix length (shorter/less specific), proceed to step 5'}
- {'step': 4, 'action': 'If route prefix length <= VNet prefix length (equal or longer/more specific), reject injection and return error message with reason'}
- {'step': 5, 'action': 'Confirm route injection is safe; allow programming into Virtual WAN'}

## Constraints

- prefix comparison must be performed before any route injection
- validation applies only to Virtual WAN-programmed routes, not to routes already in the VNet
- this rule does not apply to routes propagated between hubs (dynamic routing only)

## Cautions

- Virtual WAN cannot attract traffic between two subnets in the same virtual network; this constraint prevents that scenario
- subnet routes within the VNet take precedence; injected routes must not conflict with them

## Output Contract

- Route prefix validated as shorter than target VNet prefix and injection confirmed safe, OR injection rejected with clear error message indicating prefix specificity violation and reason.

## Example Therapist Responses

### Example 1

- Client/Input: Route prefix: 10.0.0.0/8; Spoke VNet prefix: 10.1.0.0/16
- Therapist/Output: Validation passed. Route prefix /8 is shorter than VNet prefix /16. Injection safe.
- Notes: Route is less specific than VNet, no conflict with subnets.

### Example 2

- Client/Input: Route prefix: 10.1.0.0/24; Spoke VNet prefix: 10.1.0.0/16
- Therapist/Output: Validation failed. Route prefix /24 is longer (more specific) than VNet prefix /16. Injection rejected.
- Notes: Route matches a subnet within the VNet; would create routing conflict.

### Example 3

- Client/Input: Route prefix: 10.1.0.0/16; Spoke VNet prefix: 10.1.0.0/16
- Therapist/Output: Validation failed. Route prefix /16 matches VNet prefix /16. Injection rejected.
- Notes: Route is equally specific; cannot be injected by Virtual WAN.

## Triggers

- route injection request into a spoke virtual network
- validation of route prefix before programming into Virtual WAN

## Examples

### Example 1

Input:

  Route prefix: 10.0.0.0/8; Spoke VNet prefix: 10.1.0.0/16

Output:

  Validation passed. Route prefix /8 is shorter than VNet prefix /16. Injection safe.

Notes:

  Route is less specific than VNet, no conflict with subnets.

### Example 2

Input:

  Route prefix: 10.1.0.0/24; Spoke VNet prefix: 10.1.0.0/16

Output:

  Validation failed. Route prefix /24 is longer (more specific) than VNet prefix /16. Injection rejected.

Notes:

  Route matches a subnet within the VNet; would create routing conflict.

### Example 3

Input:

  Route prefix: 10.1.0.0/16; Spoke VNet prefix: 10.1.0.0/16

Output:

  Validation failed. Route prefix /16 matches VNet prefix /16. Injection rejected.

Notes:

  Route is equally specific; cannot be injected by Virtual WAN.
