---
name: instinct-design
description: Design or review AI products with outcome-first messages, familiar interactions, progressive disclosure, calm visual hierarchy, predictable actions, and user control. Use for AI assistant UX, agent task flows, product screens, notifications, or product design specs. Supports existing interfaces and design systems.
license: MIT
metadata:
  version: "0.1.0"
---

# Instinct design

Make the user understand the outcome, the consequence, and the next useful action before exposing how the system works. This is an independent method inspired by public Instinct material. It is not an official Instinct guide.

## Start with the user's job

Use the brief and existing product artifacts. Identify who needs to get what done, what they already know, and the action the current design asks of them. Preserve the product's language, established design system, and authorized scope. Ask only when a missing fact materially changes the result. Otherwise state a reasonable assumption and produce the requested artifact.

Write in the language requested for the current task. If no output language is specified, use that task's language.

For a copy edit, return usable copy. For a screen or flow, produce a concrete layout or interaction spec. For a review, lead with the highest-impact defect and its fix. Add detail only when it helps that task.

## Rules that change the design

1. **Outcome first.** Open with what happened, what is recommended, or what needs attention. Name any limitation that changes the user's decision next to that statement. Never turn a plan, draft, pending request, or unverified tool result into a completed action.
2. **Plain language.** Use the user's objects and verbs. Say "Your export is ready" rather than describing orchestration, reasoning, or tool calls. Preserve technical detail when the user needs it to decide or act.
3. **A quiet front.** Make the main job and its next action obvious. Put rationale, evidence, alternatives, and advanced controls behind clearly named disclosures. Keep critical cost, risk, uncertainty, consent, and failures visible.
4. **Depth on demand.** Reveal useful detail in place, with an obvious way back. Give substantial comparisons or editable results their own artifact when a message cannot carry them well. Don't convert every workflow into chat.
5. **Predictable capability.** Describe meaningful task states and their consequences. Separate preparation from external effects. Reuse existing authorization for the same scope, and request a decision only at a real boundary.
6. **Earn attention.** Interrupt for information that matters now, permits useful action, and has a consequence if the user waits. Name a deadline when one is known. Batch other updates. A changed internal state alone does not justify notifying the user.
7. **Calm craft.** Use hierarchy, spacing, readable type, consistent controls, and restrained motion to clarify the task. Retain discoverability, accessibility, and recovery when reducing visual clutter.

## Load the needed depth

Read only the reference needed for the current task. Do not load this whole table by default.

| Task | Reference |
| --- | --- |
| Product positioning, value, or tradeoffs | [Product philosophy](references/product-philosophy.md) |
| Assistant replies, status, errors, or notifications | [Message design](references/message-design.md) |
| Screens, task flows, disclosure, or authorization | [Interaction design](references/interaction-design.md) |
| Visual hierarchy, typography, color, or motion | [Visual craft](references/visual-craft.md) |
| Auditing a spec or an implementation | [Review](references/review.md) |
| Checking attribution or interpreting Instinct claims | [Sources and boundaries](references/sources.md) |

## Finish on the requested artifact

Show the proposed result first. Explain the consequential design choice briefly. For a spec, define the primary view, the expanded view, and the relevant failure or recovery state. For an implementation, inspect the actual experience and report what was verified. A written spec does not prove that memory, permissions, automation, persistence, or task execution works.

Check that a user who reads only the opening still knows the real state and the next action. Stop when the requested work and proportionate checks are complete.
