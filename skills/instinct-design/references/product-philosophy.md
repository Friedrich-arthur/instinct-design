# Product philosophy

Design the product around a useful result the user can recognize. Judge a feature by the effort it removes from that job, the reliability of its result, and the control the user retains.

## What the user buys

Name the job in ordinary terms, such as arranging a meeting, comparing suppliers, or receiving a usable content package. Define completion with evidence, such as an accepted calendar invitation or a downloadable file. Producing text or executing a tool is only a step unless it satisfies the job.

Reuse a familiar entry point when it fits. Text, voice, email, a table, and an existing screen each serve different tasks. Familiarity reduces learning. Complex comparisons and precise editing often need a structured view.

## Capable work behind a legible experience

Separate these concerns in a product design:

| Concern | What the user sees | What the product must support |
| --- | --- | --- |
| Intent | A recognizable job and its constraints | Context relevant to that job |
| Preparation | A draft or recommendation labeled honestly | Research, comparison, or validation |
| Action | A clear commitment and consequence | Scoped authorization and execution |
| Verification | The real outcome and its evidence | Independent result checks where warranted |
| Recovery | What remains and how to continue | Retained work and a recoverable task state |

These are design responsibilities, not proof that an implementation has them. Don't expose agent topology or every execution step unless it helps the user diagnose or decide.

## Reliability and trust

Prefer a narrower promise that works consistently over a broader promise whose failure is hard to understand. When an action fails, fix the repeated failure mechanism, not only its wording. Design result checks separately from the action wherever silent failure would matter.

Use context without pretending to remember something that was not stored. A personalization spec must say which preferences are saved, where the user can inspect or correct them, and what happens when context is unavailable.

Protect the user's long-term interest when it conflicts with task completion. For example, an offer outside the user's price limit is not success merely because a purchase could be made. Explain the conflict and preserve useful prepared work.

## Resolve tradeoffs

- When simplicity hides a consequential fact, keep the fact visible and remove something else.
- When automation exceeds known permission, finish the preparation and present the exact pending action.
- When the user requests expert depth, provide it with a clear opening and navigable detail.
- When an existing workflow works well, improve its friction instead of imposing a new chat interface.

The message rules and visual defaults in this Skill are authored applications. Read [Sources and boundaries](sources.md) before attributing them to Instinct.
