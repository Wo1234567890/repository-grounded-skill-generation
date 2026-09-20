---
id: "a4d38a5f-6811-52c8-9fec-f31a7053c890"
name: "Brush Configuration and Filtering"
description: "Configure brush behavior including extent boundaries, input event filtering, touch support detection, key modifiers, and handle sizing. Use this skill to customize brush interaction parameters before or during brush use."
version: "0.1.0"
tags:
  - "d3"
  - "brush"
  - "configuration"
  - "interaction"
  - "setup"
  - "filtering"
triggers:
  - "Brush extent, input filtering, touch behavior, or handle appearance must be customized before or during brush use"
---

# Brush Configuration and Filtering

Configure brush behavior including extent boundaries, input event filtering, touch support detection, key modifiers, and handle sizing. Use this skill to customize brush interaction parameters before or during brush use.

## Prompt

Apply brush configuration methods to set extent boundaries, control which input events initiate brushing, enable touch support detection, configure key modifiers, and adjust handle size. Each configuration method modifies the brush instance and affects subsequent user interactions.

## Objective

Customize brush interaction parameters and constraints
## Applicable Signals

- Brush extent, input filtering, touch behavior, or handle appearance must be customized
- Custom constraints or filtering needed before brush use
- Brush interaction parameters require modification during setup phase

## Contraindications

- Default brush behavior is sufficient
- No custom constraints or filtering needed
- Brush is already active and user interaction is in progress

## Intervention Moves

- Set brush extent using brush.extent()
- Control input events with brush.filter()
- Enable or disable touch support with brush.touchable()
- Configure key modifiers with brush.keyModifiers()
- Adjust handle size with brush.handleSize()

## Workflow Steps

- Obtain or create a brush instance (d3.brush, d3.brushX, or d3.brushY)
- Define the brushable region extent if custom boundaries are required
- Configure input event filtering to control which events initiate brushing
- Set touch support detection behavior if touch interaction is needed
- Enable or disable key modifiers for modifier-key-based interaction
- Set handle size to control visual appearance of brush handles
- Apply the configured brush to a selection

## Constraints

- Configuration must be applied before or during brush setup, not after user interaction begins
- Extent boundaries must be valid numeric ranges
- Filter function must return a boolean indicating whether an event should initiate brushing
- Touch support detector must be a function that returns a boolean

## Cautions

- Changing configuration during active brushing may cause unexpected behavior
- Filter functions are called for every input event; keep them performant
- Handle size affects visual feedback; very small or very large values may confuse users

## Output Contract

- Brush configuration applied; subsequent brush interactions respect extent, filter, touch support, key modifier, and handle size settings. Configuration persists until explicitly changed.

## Triggers

- Brush extent, input filtering, touch behavior, or handle appearance must be customized before or during brush use
