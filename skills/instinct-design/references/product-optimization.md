# Improve a product with the design philosophy

Start with the user's product and the task it needs to support. Apply the principles to remove a concrete obstacle. The Instinct teardown explains the inspiration when requested; it is not a prerequisite for every improvement.

## Establish the current task and evidence

Use the available screen, prototype, spec, repository, or user feedback. Identify the intended user, desired result, current action, and where the experience obscures or interrupts that job. Inspect the actual artifact when available. A brief can support a proposal; it cannot prove a runtime defect or actual user behavior.

Separate what the artifact shows from what you suspect. For example, a button labeled “Done” beside a failed upload is observable state inconsistency. “Users will abandon this page” remains a hypothesis without behavior evidence. Don't invent an analytics baseline, completion rate, or customer quote.

Preserve the established design system, working interactions, domain requirements, and authorization. Missing context should lead to a limited assumption or one consequential question, not a demand for a complete product brief.

## Select a change by its effect on the job

| Observable friction | Relevant principle | Concrete change | Check on the same task |
| --- | --- | --- | --- |
| The headline says complete while a required step failed | Outcome first, predictable capability | Separate confirmed result and unfinished step; attach the recovery action | Read the first view and predict what is actually complete |
| Logs and tool names dominate a result | Plain language, quiet front | Show the user's objects and next action; move useful diagnostics into named detail | Find the result and recovery without opening technical history |
| A user must unfold price or a decisive unknown | Quiet front, user control | Keep the decision-changing fact next to the action; move less relevant content | Predict cost and remaining uncertainty before acting |
| Closing a detail panel loses work or place | Depth on demand | Preserve the selected object, draft, and return focus when supported | Open, edit, close and return; verify the promised saved state |
| Every internal event triggers a notice | Earn attention | Keep routine updates discoverable; interrupt only for an actionable current consequence | Inspect a real update, its consequence, and the user's available action |
| A proposed minimalist design hides expert comparison fields | Calm craft, task fit | Keep the table and keyboard workflow; improve grouping and state language | Complete the same comparison without repeated expansion |

Use the applicable row as a decision aid, not a required report. Prefer the change that removes the most consequential obstacle with the least disruption. A cosmetic preference has less priority than a misleading result, lost work, or hidden commitment. Do not assign a numerical score unless the task provides a meaningful measurement.

## Produce the requested improvement

Give the revised message, layout, flow, patch, or edited spec first. Keep the explanation short and specific to the observed problem. For a substantial redesign, make the following clear where relevant.

- What changes in the primary view and what remains visible.
- What moves into a named expanded view and how the user returns.
- What happens on partial failure, missing information, or an uncertain result.
- Which behavior is implemented, specified, or still unknown.
- What the maintainer can inspect or rerun to verify the change.

If implementation is requested and authorized, change the actual product and exercise the affected flow. Do not stop at recommendations when you can make the requested change. A design-only request should yield a reviewable design rather than unrelated code or execution.

For a one-line copy edit, give the line. The surrounding method need not appear in the answer. For an expert screen, preserve useful density. For a new feature, fit it into the existing task rather than attaching a dashboard of every agent capability.

## Use evidence for the next iteration

Check the revised artifact against the original job and constraints. Choose content ranges that could change this task, such as zero, one, or many records, a long known label, or partial completion. Use actual data when available and label assumed ranges. A visual change needs the applicable narrow-layout and interaction check. A real saved-state change needs a real reload or restart. A text-only spec needs clear acceptance behavior, not a claim that persistence works.

Before another iteration, read the accepted decisions in the existing product spec or prior delivery. Preserve the user task, useful density, constraints, and verified behavior unless new evidence challenges them. For a substantial change that needs a handoff, record the accepted choice, its reason, what was checked, and the remaining question in the existing project document. Read it back after writing. Do not create a new memory system or an extra document for a small copy edit.

When feedback arrives, record the actual failing moment and revisit the relevant change. For example, if a reader still interprets “prepared” as “sent,” revise that state distinction and check it again. If the expanded source view loses the selected row, repair continuity rather than restyling the whole table.

Keep confirmed improvements and explain remaining uncertainty. If a measurement exists, compare the same task under comparable conditions and retain failures. A small agent trial is artifact evidence, not proof of customer benefit. Continue only within the requested scope or when new feedback gives a concrete reason.
