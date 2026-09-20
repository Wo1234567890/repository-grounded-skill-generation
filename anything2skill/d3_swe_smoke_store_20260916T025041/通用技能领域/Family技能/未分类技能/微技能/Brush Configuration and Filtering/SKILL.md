---
id: "5e835d05-d9d6-56c4-89a4-20c1a728f50e"
name: "Brush Configuration and Filtering"
description: "Configure brush behavior including extent boundaries, input event filtering, touch support detection, key modifiers, and handle sizing. Apply these settings before or during brush interaction to customize how the brush responds to user input and what region is brushable."
version: "0.1.0"
tags:
  - "d3"
  - "brush"
  - "configuration"
  - "interaction"
  - "filtering"
  - "setup"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Brush extent, input filtering, touch behavior, or handle appearance must be customized"
  - "Before attaching brush to a selection, to pre-configure constraints"
  - "During active brush session, to modify interaction rules dynamically"
---

# Brush Configuration and Filtering

Configure brush behavior including extent boundaries, input event filtering, touch support detection, key modifiers, and handle sizing. Apply these settings before or during brush interaction to customize how the brush responds to user input and what region is brushable.

## Prompt

Use this skill to set up brush constraints and interaction parameters. Call brush.extent() to define the brushable region, brush.filter() to control which input events trigger brushing, brush.touchable() to enable or disable touch support, brush.keyModifiers() to control keyboard interaction, and brush.handleSize() to adjust handle appearance. Apply these configurations to a brush instance before attaching it to a selection or after creation to modify behavior mid-session.

## Objective

Customize brush interaction parameters and constraints
## Applicable Signals

- brush instance created and ready for configuration
- requirement to limit brushable region to specific bounds
- need to filter specific input events (mouse, touch, keyboard)
- touch device support must be enabled or disabled
- handle size or appearance customization needed

## Contraindications

- Default brush behavior is sufficient; no custom constraints or filtering needed
- Brush has not yet been created or instantiated
- Configuration is not supported by the brush implementation

## Workflow Steps

- {'step': 1, 'action': 'Define brushable extent', 'detail': 'Call brush.extent([[x0, y0], [x1, y1]]) to constrain the region where brushing is allowed'}
- {'step': 2, 'action': 'Set input event filter', 'detail': 'Call brush.filter(function) to control which input events (mouse, touch, keyboard) initiate or continue brushing'}
- {'step': 3, 'action': 'Configure touch support', 'detail': 'Call brush.touchable(boolean or detector function) to enable or disable touch input detection'}
- {'step': 4, 'action': 'Enable key modifiers', 'detail': 'Call brush.keyModifiers(boolean) to allow or disallow keyboard modifier keys (Shift, Ctrl, Alt, Meta) to affect brush behavior'}
- {'step': 5, 'action': 'Adjust handle size', 'detail': 'Call brush.handleSize(pixels) to set the visual size of brush handles for easier interaction'}

## Constraints

- Configuration must be applied to a valid brush instance
- Extent boundaries must be valid numeric ranges or null
- Filter function must return boolean to accept or reject events
- Touch and key modifier settings must be boolean or detector functions

## Cautions

- Changing configuration during active brushing may interrupt user interaction
- Filter functions should be lightweight to avoid performance degradation
- Extent changes do not automatically clear existing brush selection

## Output Contract

- Brush configuration applied; subsequent brush interactions respect extent, filter, touch, key modifier, and handle size settings. Configuration persists until explicitly changed or brush is recreated.

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Brush extent, input filtering, touch behavior, or handle appearance must be customized
- Before attaching brush to a selection, to pre-configure constraints
- During active brush session, to modify interaction rules dynamically
