---
id: "4e80b7c9-5aec-5df6-b91d-b68518669178"
name: "Identify Offending AS in Route Leak"
description: "Determine which AS announced a route in violation of intended policies by tracing the announcement path and comparing against expected peer/transit relationships."
version: "0.1.0"
tags:
  - "route_leak"
  - "bgp_security"
  - "incident_diagnosis"
  - "as_identification"
  - "path_analysis"
triggers:
  - "A route announcement has been detected outside its intended scope and the source AS must be identified"
examples:
  - input: "BGP update: AS_PATH=[65001, 65002, 65003], prefix=192.0.2.0/24. AS 65002 is a transit provider of AS 65001. AS 65003 is a lateral peer of AS 65002."
    output: "Offending AS: 65002. Violation: leaked transit-provider prefix (192.0.2.0/24 from customer 65001) to lateral peer 65003. Type: Type 3 leak."
    notes: "AS 65002 announced a route learned from its customer (65001) to a peer (65003), violating peer-to-peer boundary."
  - input: "BGP update: AS_PATH=[65010, 65020, 65030], prefix=10.0.0.0/8. AS 65020 is a lateral peer of AS 65010. AS 65030 is the transit provider of AS 65020."
    output: "Offending AS: 65020. Violation: leaked peer prefix (10.0.0.0/8 from peer 65010) to transit provider 65030. Type: Type 4 leak."
    notes: "AS 65020 announced a route learned from a peer (65010) to its own transit provider (65030), violating customer-to-provider boundary."
---

# Identify Offending AS in Route Leak

Determine which AS announced a route in violation of intended policies by tracing the announcement path and comparing against expected peer/transit relationships.

## Prompt

To identify the offending AS in a route leak incident:
1. Obtain the route announcement path (AS_PATH) from BGP data or routing logs.
2. Identify the originating AS and all intermediate ASes that propagated the route.
3. Cross-reference each AS's documented relationships (transit provider, lateral peer, customer) against the route's origin and destination.
4. Locate the AS that announced the route to a peer or provider in violation of its policy (e.g., leaking a transit-provider prefix to a lateral peer, or a peer prefix to its own transit provider).
5. Document the offending AS, the leaked prefix, the relationship type that was violated, and the incident type (Type 3, Type 4, Type 6, etc.).

## Objective

pinpoint_offending_as
## Applicable Signals

- Route announcement detected outside intended scope
- BGP path trace shows unexpected AS propagation
- Prefix appears in peer or transit provider's routing table unexpectedly
- Monitoring alert indicates route leak candidate

## Contraindications

- Route announcement is policy-compliant
- AS relationship graph is incomplete or unreliable
- BGP data or path information is unavailable or corrupted
- Offending AS cannot be uniquely determined due to ambiguous topology

## Intervention Moves

- Extract AS_PATH from BGP update or routing log
- Map each AS in path to its relationship type (transit provider, lateral peer, customer)
- Compare announced prefix origin against expected customer cone
- Identify first AS that violated policy boundary
- Classify leak type based on relationship violation

## Constraints

- Requires accurate AS relationship data (peer, transit, customer mappings)
- Requires complete or near-complete BGP path information
- Analysis assumes standard BGP propagation rules

## Cautions

- AS relationships may change over time; use relationship data contemporaneous with the incident
- Multiple ASes in the path may have violated policy; focus on the first AS that crossed the boundary
- Some leaks may involve route filtering failures rather than intentional announcements

## Output Contract

- Offending AS identified and documented with: (1) AS number, (2) leaked prefix, (3) relationship type violated (transit-to-peer, peer-to-transit, internal-prefix leak), (4) incident type classification (Type 1–6), (5) evidence (AS_PATH, timestamp, source).

## Example Executions

### Example 1

- Input: BGP update: AS_PATH=[65001, 65002, 65003], prefix=192.0.2.0/24. AS 65002 is a transit provider of AS 65001. AS 65003 is a lateral peer of AS 65002.
- Output: Offending AS: 65002. Violation: leaked transit-provider prefix (192.0.2.0/24 from customer 65001) to lateral peer 65003. Type: Type 3 leak.
- Notes: AS 65002 announced a route learned from its customer (65001) to a peer (65003), violating peer-to-peer boundary.

### Example 2

- Input: BGP update: AS_PATH=[65010, 65020, 65030], prefix=10.0.0.0/8. AS 65020 is a lateral peer of AS 65010. AS 65030 is the transit provider of AS 65020.
- Output: Offending AS: 65020. Violation: leaked peer prefix (10.0.0.0/8 from peer 65010) to transit provider 65030. Type: Type 4 leak.
- Notes: AS 65020 announced a route learned from a peer (65010) to its own transit provider (65030), violating customer-to-provider boundary.

## Triggers

- A route announcement has been detected outside its intended scope and the source AS must be identified

## Examples

### Example 1

Input:

  BGP update: AS_PATH=[65001, 65002, 65003], prefix=192.0.2.0/24. AS 65002 is a transit provider of AS 65001. AS 65003 is a lateral peer of AS 65002.

Output:

  Offending AS: 65002. Violation: leaked transit-provider prefix (192.0.2.0/24 from customer 65001) to lateral peer 65003. Type: Type 3 leak.

Notes:

  AS 65002 announced a route learned from its customer (65001) to a peer (65003), violating peer-to-peer boundary.

### Example 2

Input:

  BGP update: AS_PATH=[65010, 65020, 65030], prefix=10.0.0.0/8. AS 65020 is a lateral peer of AS 65010. AS 65030 is the transit provider of AS 65020.

Output:

  Offending AS: 65020. Violation: leaked peer prefix (10.0.0.0/8 from peer 65010) to transit provider 65030. Type: Type 4 leak.

Notes:

  AS 65020 announced a route learned from a peer (65010) to its own transit provider (65030), violating customer-to-provider boundary.
