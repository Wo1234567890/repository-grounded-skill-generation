---
id: "db0c89b8-5508-5da5-9421-4117ee2bb58c"
name: "Future Completion Callback Registration"
description: "Attach a callback function to be invoked when a future completes or is cancelled. Callbacks are executed in the order added and always run in the thread that registered them. Enables non-blocking notification and post-processing when an asynchronous task finishes."
version: "0.1.0"
tags:
  - "concurrent.futures"
  - "future"
  - "callback"
  - "async"
  - "completion_notification"
  - "non-blocking"
triggers:
  - "Caller wants to perform cleanup, logging, or chained operations after a task completes without blocking the main thread"
  - "Need to handle multiple futures reactively"
  - "Post-processing is required upon task completion or cancellation"
---

# Future Completion Callback Registration

Attach a callback function to be invoked when a future completes or is cancelled. Callbacks are executed in the order added and always run in the thread that registered them. Enables non-blocking notification and post-processing when an asynchronous task finishes.

## Prompt

Use add_done_callback(fn) to register a callable that will be invoked with the future as its only argument when the future is cancelled or finishes running. Callbacks are called in registration order and always execute in the thread that added them. If the future has already completed or been cancelled, fn will be called immediately.

## Objective

Enable non-blocking notification and post-processing when an asynchronous task finishes
## Applicable Signals

- Future object is available
- Asynchronous task execution is in progress
- Non-blocking completion notification is desired

## Contraindications

- Callback must run in a specific thread other than the registering thread
- Callback raises BaseException subclasses (behavior is undefined)
- Synchronous result retrieval is required before proceeding

## Intervention Moves

- Define callback function that accepts future as sole argument
- Call add_done_callback(fn) on the future object
- Callback executes automatically upon future completion or cancellation

## Constraints

- Callback receives future as its only argument
- Callbacks are always executed in the thread that registered them
- Callbacks are called in the order they were added
- Exceptions in callbacks are logged and ignored; BaseException subclasses have undefined behavior

## Cautions

- If callback raises an Exception subclass, it will be logged and ignored
- If callback raises a BaseException subclass, behavior is undefined
- Callback executes immediately if future is already completed or cancelled at registration time

## Output Contract

- Callback is registered and will be invoked with the future as its sole argument upon completion or cancellation; exceptions in the callback are logged and ignored.

## Triggers

- Caller wants to perform cleanup, logging, or chained operations after a task completes without blocking the main thread
- Need to handle multiple futures reactively
- Post-processing is required upon task completion or cancellation
