# Learn from Instinct without guessing its internals

The useful lesson is how a capable assistant makes its work understandable. Use the patterns below to design your own messages, task views, permissions, and recovery. Keep the evidence boundary attached to each pattern.

Reviewed 2026-10-13. This is independent product analysis. We inspected public pages and inherited interview notes. We did not use the private Instinct service, inspect its binaries, or establish its implementation. An official product claim describes a promise, not a verified runtime result.

## The REA approach, adapted to product design

[REA, Reverse Engineer Anything](https://github.com/morluto/rea), investigates behavior through relevant evidence and distinguishes observation, inference, and unknowns. Here the target is a public product experience rather than a binary. For each question, identify the available evidence, state a mechanism hypothesis, design a transferable version, and define a check that could refute it. REA tools are not required for this public-material analysis.

Use three evidence labels:

- **Public claim** means an inspected official page makes the statement.
- **Notes-based interpretation** means interview notes suggest the idea; the official chapter identifies the topic, but its complete transcript was not checked.
- **Design proposal** means this Skill's application or hypothesis. It is not attributed to Instinct's actual implementation.

## 1. A familiar entry point can reduce delegation friction

**Evidence.** The [official introduction](https://instinct.com/) describes text and calls as ways to contact the assistant. It also describes using a phone and computer. This is a public claim, not our service test.

**Mechanism hypothesis.** A recognizable channel lets users express a job without learning a feature catalog. The assistant then chooses how to prepare and execute it.

**Transfer.** Start with a place users already work, such as an inbox or an existing task view. Accept their goal and constraints there. Use a structured comparison or editor when the task demands it.

**Boundary and check.** Do not infer that Instinct has no apps, or that every product should use chat. Test whether a new user can start the main job without needing a feature tour, and whether a complex edit still remains precise.

## 2. Understandability is a product constraint

**Evidence.** The [official interview chapter guide](https://colossus.com/episode/instinct-the-personal-agent/) places product comprehension at 44:43 and judgment versus measurement at 48:15. The stronger claim that predictability should outweigh a capability catalog is a notes-based interpretation.

**Mechanism hypothesis.** Users can delegate when they can predict what a request will cause and how a failure will appear. More visible controls can make that prediction harder.

**Transfer.** Name an action by its consequence. Put the actual task state next to the result. Say which external step is pending. Retain a visible recovery path.

**Boundary and check.** Simplicity can hide essential constraints. Ask a reader to predict what the main action does, what remains unfinished, and whether it costs money. Compare that answer with the designed behavior.

## 3. A message preview is part of the interface

**Evidence.** Inherited notes associate the interview's comprehension discussion with putting useful information near the beginning of a message. The precise message layout and any percentage or character limit remain unverified.

**Mechanism hypothesis.** A user may read a notification preview and act before opening the detail. An early process narrative can displace the actual result or failure.

**Transfer.** Start with the outcome or pending state. Keep a decisive limitation beside it. Provide the next useful action if there is one. Put evidence and diagnostics after that opening.

**Boundary and check.** A short success headline must not conceal partial failure. Truncate your proposed message at the actual preview boundary. Can the reader still tell that the video is exported but not published? Use the [message exercise](pattern-lab.md#exercise-1-a-result-that-is-only-partly-complete).

## 4. Capability can expand without crowding the primary view

**Evidence.** The official interview's interface chapter starts at 1:08:32. Notes describe richer artifacts when needed. This supports a research question; it does not establish a specific screen or component implementation.

**Mechanism hypothesis.** The primary view carries the current decision. A deeper artifact carries comparison, evidence, or editing. Capability growth need not turn every task into a larger dashboard.

**Transfer.** Give the user a concise result card, a named evidence disclosure, and an editable artifact when necessary. Preserve the selected object and draft when the user moves between them.

**Boundary and check.** Do not put price, permission, failure, or decisive uncertainty behind the disclosure. Test whether a user can find a source and return to the same decision without losing edits.

## 5. Revoking access, deleting data, and undoing an action are different jobs

**Evidence.** The [official privacy policy](https://instinct.com/privacy-policy) states that disconnecting an integration does not automatically delete previously collected data and describes deleting indexed external data through the workspace. The [service terms](https://instinct.com/terms) discuss retained indexed data and external actions. These are inspected policy claims; we did not test the deletion controls.

**Mechanism hypothesis.** A user can reasonably expect that "disconnect" removes information and effects. A product needs separate, understandable controls for future access, retained information, and already committed actions.

**Transfer.** Present a receipt for each operation: future sync stopped, data that remains, pending tasks, and committed effects. Offer deletion or cancellation only when the product implements it. Confirm each result separately.

**Boundary and check.** Never say all data is deleted because a connection was removed. A completed external booking may still exist after revocation. Use the [permission exercise](pattern-lab.md#exercise-2-a-disconnection-receipt).

## 6. Proactivity needs a consequence, not a stream of updates

**Evidence.** The interview lists proactivity and mistakes at 1:03:59. The rule below is a design proposal informed by the notes, not a verified Instinct notification algorithm.

**Mechanism hypothesis.** Useful background work loses value when every internal event consumes attention. An interruption is justified by the user's opportunity to prevent a meaningful consequence.

**Transfer.** Ask whether the event matters now, the user can act, and waiting has a consequence. Interrupt when all three apply. Otherwise leave a task update or digest. State a real deadline when known.

**Boundary and check.** Do not manufacture urgency. Test harmless updates, urgent but unactionable news, and an actionable loss without a formal deadline. Use the [attention exercise](pattern-lab.md#exercise-3-choose-when-to-interrupt).

## 7. A goal includes limits and verification

**Evidence.** The official interview's goal discussion starts at 1:12:35. The official site promises assistance across everyday jobs. Neither source proves unlimited reliable autonomy.

**Mechanism hypothesis.** A string of completed tool calls can still miss the user's goal. Price limits, recipients, quality, and timing determine whether a result is acceptable.

**Transfer.** Define the desired outcome and constraints before choosing tools. Separate prepared, committed, verified, and uncertain states where they matter. Continue within existing authorization, and present the exact changed commitment at a new boundary.

**Boundary and check.** Finding a ticket above the budget is a useful lead, not a completed purchase. Check whether a failure preserves useful work and whether verification actually observes the intended result.

## 8. Taste needs observations from real use

**Evidence.** Official chapters cover judgment and measurement at 48:15 and brand naming at 1:16:27. The choice to treat visual calm as an aid to understanding is this Skill's proposal.

**Mechanism hypothesis.** Consistent hierarchy, language, and recovery can make the product feel coherent. A tidy screenshot alone cannot show whether users trust the task or find the details.

**Transfer.** Refine the core journey before adding decorative panels. Test the first view, expanded evidence, failure, and narrow layout. Ask actual users where the product surprised them.

**Boundary and check.** Do not invent Instinct's palette, fonts, motion, safety architecture, adoption, or outcomes. Keep author-chosen visual values distinct from observations. A real case needs the input, resulting artifact, user consequence, and permission to publish.

## Turn a borrowed idea into a useful design

For the selected pattern, return the user's concrete artifact, the supporting evidence and its limit, the proposed mechanism, the applicable conditions, a failure case, and a proportionate check. The artifact comes first. Do not write this full teardown for a one-line copy request.

The [pattern lab](pattern-lab.md) provides synthetic exercises you can try. [Sources and boundaries](sources.md) records the current evidence. New direct evidence can strengthen or change this analysis; keep the existing unknowns visible until then.
