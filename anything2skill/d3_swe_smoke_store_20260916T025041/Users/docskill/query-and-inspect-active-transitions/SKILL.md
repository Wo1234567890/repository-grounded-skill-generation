---
id: "3cdfd0da-3a26-5492-b2b3-8e60ee48ddb4"
name: "Query and Inspect Active Transitions"
description: "Retrieve metadata and state information about active or completed transitions, including selection references, element counts, and active transition handles. This is a read-only inspection skill that does not modify transition behavior."
version: "0.1.0"
tags:
  - "d3"
  - "transition"
  - "inspection"
  - "state_query"
  - "read_only"
  - "animation"
triggers:
  - "Need to check if a transition is currently active on a node"
  - "Need to retrieve the selection associated with a transition"
  - "Need to count the number of elements affected by a transition"
  - "Need to access the first element in a transition"
  - "Need to verify if a transition is empty"
examples:
  - input: "node = document.querySelector('#my-element'); activeTransition = d3.active(node)"
    output: "activeTransition is a transition object if one is active on the node, or undefined if none"
    notes: "Use to check if a specific element has an active transition before scheduling a new one"
  - input: "transition.selection()"
    output: "Returns the selection object that was used to create this transition"
    notes: "Useful for chaining inspection with further selection operations"
  - input: "transition.size()"
    output: "Returns an integer representing the number of elements in the transition"
    notes: "Use to verify that the transition affects the expected number of elements"
---

# Query and Inspect Active Transitions

Retrieve metadata and state information about active or completed transitions, including selection references, element counts, and active transition handles. This is a read-only inspection skill that does not modify transition behavior.

## Prompt

Use this skill to inspect the current state of a transition without side effects. Call d3.active() to get the active transition for a node, transition.selection() to retrieve the underlying selection, transition.nodes() to get all affected elements, transition.node() for the first element, transition.size() for element count, or transition.empty() to check if the transition has no elements.

## Objective

Inspect or retrieve transition state and associated DOM elements
## Applicable Signals

- Transition object is available
- DOM node reference is available
- State query is required before modification

## Contraindications

- Do not use when modifying transition behavior (use transition scheduling or tweening skills instead)
- Do not use when scheduling new transitions (use transition.transition() or selection.transition() instead)
- Do not use if no inspection is needed

## Workflow Steps

- {'step': 1, 'action': 'Obtain transition reference or DOM node', 'detail': 'Have either an active transition object or a DOM node to query'}
- {'step': 2, 'action': 'Select appropriate inspection method', 'detail': 'Choose d3.active() for node-based lookup, or transition.selection/nodes/node/size/empty() for transition-based inspection'}
- {'step': 3, 'action': 'Execute query', 'detail': 'Call the selected method with appropriate arguments'}
- {'step': 4, 'action': 'Consume metadata', 'detail': 'Use returned selection, node array, count, or boolean state for downstream logic'}

## Constraints

- All operations are read-only and produce no side effects
- d3.active() requires a valid DOM node reference
- transition.selection(), transition.nodes(), transition.node(), transition.size(), and transition.empty() require a valid transition object

## Cautions

- transition.node() returns the first non-null element; may return null if no elements are selected
- transition.empty() returns true only if the transition has zero elements; does not indicate completion status

## Output Contract

- Returns one of: (1) a transition object (d3.active), (2) a selection object (transition.selection), (3) an array of DOM elements (transition.nodes), (4) a single DOM element or null (transition.node), (5) an integer count (transition.size), or (6) a boolean (transition.empty). All outputs are read-only snapshots with no side effects.

## Example Therapist Responses

### Example 1

- Client/Input: node = document.querySelector('#my-element'); activeTransition = d3.active(node)
- Therapist/Output: activeTransition is a transition object if one is active on the node, or undefined if none
- Notes: Use to check if a specific element has an active transition before scheduling a new one

### Example 2

- Client/Input: transition.selection()
- Therapist/Output: Returns the selection object that was used to create this transition
- Notes: Useful for chaining inspection with further selection operations

### Example 3

- Client/Input: transition.size()
- Therapist/Output: Returns an integer representing the number of elements in the transition
- Notes: Use to verify that the transition affects the expected number of elements

## Triggers

- Need to check if a transition is currently active on a node
- Need to retrieve the selection associated with a transition
- Need to count the number of elements affected by a transition
- Need to access the first element in a transition
- Need to verify if a transition is empty

## Examples

### Example 1

Input:

  node = document.querySelector('#my-element'); activeTransition = d3.active(node)

Output:

  activeTransition is a transition object if one is active on the node, or undefined if none

Notes:

  Use to check if a specific element has an active transition before scheduling a new one

### Example 2

Input:

  transition.selection()

Output:

  Returns the selection object that was used to create this transition

Notes:

  Useful for chaining inspection with further selection operations

### Example 3

Input:

  transition.size()

Output:

  Returns an integer representing the number of elements in the transition

Notes:

  Use to verify that the transition affects the expected number of elements
