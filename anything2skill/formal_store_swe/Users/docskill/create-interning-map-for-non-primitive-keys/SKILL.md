---
id: "64580c55-a909-50e6-9941-3d7b9fd28644"
name: "Create interning Map for non-primitive keys"
description: "Instantiate a Map that interns non-primitive keys (e.g., dates, objects) for consistent identity-based lookup and memory efficiency. Use when standard Map equality is insufficient for complex key types."
version: "0.1.0"
tags:
  - "data_structure"
  - "interning"
  - "non_primitive_keys"
  - "identity_equality"
  - "memory_efficiency"
triggers:
  - "Keys are non-primitive types (dates, objects, custom types)"
  - "Standard Map equality is insufficient for key comparison"
  - "Identity-based key lookup is required"
---

# Create interning Map for non-primitive keys

Instantiate a Map that interns non-primitive keys (e.g., dates, objects) for consistent identity-based lookup and memory efficiency. Use when standard Map equality is insufficient for complex key types.

## Prompt

Instantiate a new InternMap to store and retrieve values using non-primitive keys. InternMap interns keys for identity-based equality, enabling reliable lookup of complex objects like dates or custom types without relying on value equality.

## Objective

Create interning Map for non-primitive key identity
## Applicable Signals

- Working with Date objects as keys
- Using custom objects or class instances as keys
- Need for consistent key identity across operations

## Contraindications

- Keys are primitives (strings, numbers, booleans)
- Standard Map equality is sufficient
- Interning overhead is unacceptable for performance constraints

## Workflow Steps

- {'step': 1, 'action': 'Instantiate new InternMap', 'detail': 'Call new InternMap() to create an empty interning Map instance'}
- {'step': 2, 'action': 'Populate with non-primitive keys', 'detail': 'Use .set(key, value) to store entries where keys are non-primitive objects'}
- {'step': 3, 'action': 'Retrieve values by interned key identity', 'detail': 'Use .get(key) to retrieve values; lookup uses interned key identity'}

## Constraints

- InternMap must be instantiated before use
- Keys must be objects or non-primitive values
- Memory overhead from interning should be acceptable for use case

## Cautions

- InternMap has higher memory overhead than standard Map due to interning
- Suitable only when identity-based equality is required

## Output Contract

- InternMap instance ready to store and retrieve values by interned non-primitive keys; supports standard Map operations (set, get, has, delete) with identity-based key equality.

## Triggers

- Keys are non-primitive types (dates, objects, custom types)
- Standard Map equality is insufficient for key comparison
- Identity-based key lookup is required
