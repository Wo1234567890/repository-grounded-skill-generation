---
id: "64580c55-a909-50e6-9941-3d7b9fd28644"
name: "Create interning Map for non-primitive keys"
description: "Instantiate a Map that interns non-primitive keys (e.g., dates, objects) for consistent identity-based lookup and memory efficiency. Use when standard Map equality is insufficient for complex key types."
version: "0.1.0"
tags:
  - "data-structure"
  - "interning"
  - "non-primitive-keys"
  - "map"
  - "initialization"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Keys are non-primitive types (dates, objects, custom types)"
  - "Identity-based equality is required for key comparison"
  - "Memory efficiency and consistent key interning matter"
---

# Create interning Map for non-primitive keys

Instantiate a Map that interns non-primitive keys (e.g., dates, objects) for consistent identity-based lookup and memory efficiency. Use when standard Map equality is insufficient for complex key types.

## Prompt

Instantiate a new InternMap to store and retrieve values using non-primitive keys with identity-based equality. InternMap automatically interns keys, ensuring consistent lookup behavior for dates, objects, and other non-primitive types.

## Objective

Create interning Map for non-primitive key identity
## Applicable Signals

- Working with Date objects as map keys
- Using complex objects or custom types as keys
- Need for stable key identity across multiple references

## Contraindications

- Keys are primitives (strings, numbers, booleans)
- Standard Map equality is sufficient for use case
- Interning overhead is unacceptable for performance constraints

## Workflow Steps

- {'step': 1, 'action': 'Instantiate new InternMap', 'detail': 'Call new InternMap() to create an empty interning map instance'}
- {'step': 2, 'action': 'Store key-value pairs', 'detail': 'Use .set(key, value) with non-primitive keys; InternMap automatically interns keys'}
- {'step': 3, 'action': 'Retrieve values', 'detail': 'Use .get(key) with the same or equivalent non-primitive key; interning ensures consistent lookup'}

## Constraints

- InternMap requires explicit instantiation before use
- Key interning is automatic; caller does not manage interning lifecycle

## Cautions

- InternMap trades memory for consistent identity-based lookup
- Not suitable for high-frequency key creation with primitives

## Output Contract

- InternMap instance ready to store and retrieve values by interned non-primitive keys. Caller receives a fully initialized Map-like object with identity-based key equality.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Keys are non-primitive types (dates, objects, custom types)
- Identity-based equality is required for key comparison
- Memory efficiency and consistent key interning matter
