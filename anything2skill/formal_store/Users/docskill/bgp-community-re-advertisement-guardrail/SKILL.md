---
id: "2208eb6f-b182-511d-a905-80aa738b6de5"
name: "BGP Community Re-advertisement Guardrail"
description: "Prevents re-advertisement of routes with removed Azure BGP communities back into Virtual WAN. Blocks or confirms absence of routes with modified BGP community attributes before re-advertisement to prevent routing issues and outages."
version: "0.1.0"
tags:
  - "virtual_wan"
  - "static_routing"
  - "bgp_communities"
  - "configuration_validation"
  - "routing_safety"
triggers:
  - "managing BGP community attributes"
  - "planning route re-advertisement to Virtual WAN"
examples:
  - input: "Route with Azure BGP communities removed; operator attempts to re-advertise into Virtual WAN"
    output: "Re-advertisement blocked. Routes with removed BGP communities cannot be re-advertised into Virtual WAN. Confirm BGP community restoration or remove route from re-advertisement list."
    notes: "Prevents outage caused by BGP community mismatch."
---

# BGP Community Re-advertisement Guardrail

Prevents re-advertisement of routes with removed Azure BGP communities back into Virtual WAN. Blocks or confirms absence of routes with modified BGP community attributes before re-advertisement to prevent routing issues and outages.

## Prompt

When managing BGP community attributes in Virtual WAN routes, validate that routes with removed Azure BGP communities are not re-advertised back into Virtual WAN. Block re-advertisement or require explicit override with justification if BGP communities have been removed from VNet or UDR routes.

## Objective

prevent_bgp_community_mismatch_outages
## Applicable Signals

- BGP community attributes modified or removed
- route re-advertisement to Virtual WAN planned

## Contraindications

- BGP communities are not modified or removed
- dynamic routing only (no static routes defined)

## Intervention Moves

- Warn if route with removed BGP communities is marked for re-advertisement
- Block re-advertisement or require explicit override with justification
- Provide validation checklist confirming BGP community status is known and re-advertisement intent is explicit

## Workflow Steps

- Identify routes with modified or removed BGP community attributes
- Check if these routes are marked for re-advertisement into Virtual WAN
- If re-advertisement is planned, block and warn operator
- Request explicit confirmation of BGP community restoration or removal from re-advertisement list
- Document override justification if operator proceeds

## Constraints

- routes with removed Azure BGP communities must not be re-advertised into Virtual WAN
- validation must occur before route activation

## Cautions

- violation of this constraint causes routing issues and potential outages
- BGP community removal is irreversible; confirm intent before removal

## Output Contract

- BGP community re-advertisement status validated. If routes with removed BGP communities are marked for re-advertisement, re-advertisement is blocked with specific violation reason. Operator must either restore BGP communities or remove route from re-advertisement list. If validation passes, re-advertisement is approved with BGP community status confirmed.

## Example Therapist Responses

### Example 1

- Client/Input: Route with Azure BGP communities removed; operator attempts to re-advertise into Virtual WAN
- Therapist/Output: Re-advertisement blocked. Routes with removed BGP communities cannot be re-advertised into Virtual WAN. Confirm BGP community restoration or remove route from re-advertisement list.
- Notes: Prevents outage caused by BGP community mismatch.

## Triggers

- managing BGP community attributes
- planning route re-advertisement to Virtual WAN

## Examples

### Example 1

Input:

  Route with Azure BGP communities removed; operator attempts to re-advertise into Virtual WAN

Output:

  Re-advertisement blocked. Routes with removed BGP communities cannot be re-advertised into Virtual WAN. Confirm BGP community restoration or remove route from re-advertisement list.

Notes:

  Prevents outage caused by BGP community mismatch.
