---
name: bgp-oscillation-route-leak-analysis
description: Analyze routing topology and relationship data for preference cycles and valley-free BGP route leaks, then evaluate candidate mitigations by their structural effect.
---

# BGP Oscillation and Route-Leak Analysis

## When to Use

Use this skill for offline analysis of BGP/Virtual-WAN topology files that describe advertised routes, hub preferences, relationship weights, and candidate mitigations.

## Workflow

1. **Normalize every input into one topology model.** Keep AS/hub identifiers, advertised routes, preference edges, and relationship types separate. Do not infer a relationship from a label if an explicit local-preference/relationship file is available.
2. **Detect oscillation as a preference-cycle problem.** Build a directed graph from the effective routing preferences and find cycles among the hubs/ASes involved in choosing paths. Report the concrete cycle and affected ASes.
3. **Check valley-free export behavior separately.** A route leak is not the same condition as an oscillation. Track where a route was learned from and where it is re-advertised; flag exports that violate the relationship policy represented in the inputs.
4. **Keep detection evidence explicit.** For each leak, record leaker, source AS, destination AS, and the source/destination relationship types used in the decision.
5. **Evaluate solutions by simulation of their stated effect.** For each candidate, ask two independent questions: does it break every relevant preference cycle, and does it stop the offending cross-hub advertisement? A timer change or unrelated filter should not be credited merely because it sounds like a routing fix.
6. **Do not couple the two verdicts.** A solution can resolve oscillation only, route leak only, both, or neither.
7. **Validate the JSON schema before writing.** Preserve booleans, cycle arrays, leak records, and one result object per candidate solution.

## Trajectory-Derived Caution

The no-skill runs initially missed a cycle and then revised their topology reasoning, yet all received zero reward. Avoid hard-coding a visually obvious two-node cycle or judging solutions from their text. Build the graph and relationship checks from the actual input data and re-evaluate after each candidate transformation.

## Common Failure Modes

- Equating any mutual peering with oscillation without checking effective preferences.
- Detecting a route leak without using relationship types.
- Treating keepalive/hold timers as automatically changing path preference.
- Marking a mitigation successful without applying its structural effect to the model.
