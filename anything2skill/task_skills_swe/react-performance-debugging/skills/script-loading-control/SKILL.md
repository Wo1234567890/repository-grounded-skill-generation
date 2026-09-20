---
id: "c14710bc-1902-535b-adb8-982feefbd32e"
name: "Script Loading Control"
description: "Use the Performance Panel's live metrics view to observe cumulative layout shift (CLS) scores while interacting with a web page, identifying when and where shifts occur during user sessions."
version: "0.1.1"
tags:
  - "performance"
  - "layout_shift"
  - "devtools"
  - "real-time_monitoring"
  - "diagnosis"
triggers:
  - "integrating analytics scripts"
  - "integrating tracking or vendor scripts"
  - "need fine-grained control over script execution timing"
  - "want to prevent script loading from blocking page render"
---

# Script Loading Control

Use the Performance Panel's live metrics view to observe cumulative layout shift (CLS) scores while interacting with a web page, identifying when and where shifts occur during user sessions.

## Prompt

Open the Performance Panel in your browser DevTools. Navigate to the live metrics view. Interact with the web page (scroll, click, type) while observing the CLS score update in real-time. Note the timing and elements associated with each layout shift event.

## Objective

Real-time CLS observation
## Applicable Signals

- Page interaction triggers visible layout shifts
- CLS score increases during user actions
- Visual instability observed during development testing

## Contraindications

- Measuring CLS in production environments
- Analyzing historical field data
- When DevTools access is unavailable or disabled
- When real-time observation is not feasible

## Intervention Moves

- Open DevTools Performance Panel
- Activate live metrics view
- Interact with page elements (scroll, click, type)
- Observe CLS metric updates and shift events
- Record timing and associated elements

## Constraints

- Requires browser DevTools access
- Limited to single-session observation
- Does not capture field user data
- Dependent on browser and page state

## Cautions

- Live metrics reflect only current session; not representative of all users
- DevTools overhead may affect page performance
- Requires active interaction to observe shifts

## Output Contract

- Live CLS metric displayed in Performance Panel showing shift events and cumulative score during page interaction. Output includes timing of shifts and identification of elements causing layout changes.

## Triggers

- integrating analytics scripts
- integrating tracking or vendor scripts
- need fine-grained control over script execution timing
- want to prevent script loading from blocking page render
