---
id: "8ab7d9c6-0610-506d-b327-c9d8908c0519"
name: "Event listener management"
description: "Add, remove, or manage event listeners on DOM selections using selection.on(). Use when you need to attach or detach event handlers to interactive elements."
version: "0.1.0"
tags:
  - "dom"
  - "event"
  - "interaction"
  - "selection"
  - "d3"
  - "未分类技能"
  - "profile:default::未分类技能"
triggers:
  - "Interactive element requires event response"
  - "User interaction must trigger a callback"
---

# Event listener management

Add, remove, or manage event listeners on DOM selections using selection.on(). Use when you need to attach or detach event handlers to interactive elements.

## Prompt

Use selection.on(type, listener) to add an event listener or selection.on(type, null) to remove it. The listener callback receives the event object and the datum associated with the element.

## Objective

Attach or detach event handlers to DOM selections
## Applicable Signals

- Interactive element requires event response
- User interaction must trigger a callback
- Native DOM event binding is needed

## Contraindications

- Event is synthetic or programmatically dispatched; use selection.dispatch instead
- Custom event dispatch is required

## Constraints

- Listener must be a function or null
- Event type must be a valid DOM event name

## Output Contract

- Event listener is registered or removed
- Subsequent user interaction triggers the callback

## Files

- `references/evidence.md`
- `references/evidence_manifest.json`

## Triggers

- Interactive element requires event response
- User interaction must trigger a callback
