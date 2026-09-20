---
id: "be22c7cd-9d77-500b-bacb-15587249adef"
name: "Record Layout Shifts via Performance Observer"
description: "Capture and log Cumulative Layout Shift (CLS) events programmatically by pasting a Performance Observer script into the browser console. Provides a console-based alternative to DevTools Performance Panel for detecting, analyzing, and attributing layout shifts during page inter..."
version: "0.1.0"
tags:
  - "layout_shift"
  - "cls"
  - "performance_observer"
  - "console_script"
  - "web_vitals"
  - "performance_monitoring"
triggers:
  - "You need to capture layout shift data without relying on DevTools"
  - "Automating CLS detection in custom test scripts"
---

# Record Layout Shifts via Performance Observer

Capture and log Cumulative Layout Shift (CLS) events programmatically by pasting a Performance Observer script into the browser console. Provides a console-based alternative to DevTools Performance Panel for detecting, analyzing, and attributing layout shifts during page inter...

## Prompt

Use this skill when you need to programmatically capture layout shift data without relying on the DevTools Performance Panel. Paste a Performance Observer script into the browser console while browsing the target page. The observer will record layout shift events with timing and attribution details, outputting results to the console log. This approach is useful for automating CLS detection in custom test scripts or when DevTools is not available.

## Objective

Programmatic CLS event capture and analysis via console-based Performance Observer
## Applicable Signals

- Need to capture layout shift data without DevTools
- Automating CLS detection in custom test scripts
- Debugging layout shifts during page interaction
- Collecting CLS attribution information programmatically

## Contraindications

- DevTools Performance Panel is sufficient for one-off analysis
- Measuring CLS at scale in production (use RUM libraries instead)
- Real-time visual monitoring of layout shifts is the primary need

## Workflow Steps

- {'step': 1, 'action': 'Open the browser console on the target web page'}
- {'step': 2, 'action': 'Paste a Performance Observer script configured to observe layout-shift entries'}
- {'step': 3, 'action': 'Interact with the page or allow it to load fully'}
- {'step': 4, 'action': 'Review console output for recorded layout shift events with timing and attribution data'}

## Constraints

- Requires browser console access
- Script must be pasted into console while page is loaded or during interaction
- Output is limited to console log; not suitable for persistent data collection without additional logging infrastructure

## Cautions

- Console output may be cleared or lost if page reloads
- Performance Observer API support varies by browser; verify browser compatibility
- For production-scale CLS collection, use dedicated RUM providers or the web-vitals library instead

## Output Contract

- Console output or log containing recorded layout shift events, including timing information and attribution data for each shift. Output is available in the browser console and can be copied or exported for analysis.

## Triggers

- You need to capture layout shift data without relying on DevTools
- Automating CLS detection in custom test scripts
