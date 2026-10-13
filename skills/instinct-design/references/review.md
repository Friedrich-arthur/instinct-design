# Review a real product artifact

Start with the defect that most harms the user's job. Report its consequence, the evidence, and a specific fix. Review the dimensions relevant to the artifact rather than producing a ritual checklist.

| Dimension | Check |
| --- | --- |
| First impression | Can the user identify the outcome, current state, and next action? |
| Experience | Does expansion preserve context? Can the user discover details and recover from failure? |
| Interface | Are action labels, task states, messages, and component behavior consistent? |
| Persistence | If implemented, do saved drafts, permissions, and tasks survive the promised reload or restart? |
| Safety and control | Are costs, uncertainty, consent, recipients, and external effects visible before commitment? |
| Functional behavior | Does the main action produce the claimed result? Are partial results labeled honestly? |
| Performance | Does disclosure avoid unnecessary loading? Is latency observable without invented estimates? |
| Accessibility | Are controls operable, focus visible, reading order coherent, and critical states understandable? |

For a written spec, identify missing contracts and proposed checks. For a static prototype, test its navigation and presentation but label execution and persistence as unimplemented. For a live product, exercise the applicable real flow and inspect the result.

## Useful stress cases

- The user reads only the message preview.
- The main task fails after a draft is saved.
- A result contains both success and an unresolved external step.
- A new cost exceeds existing authorization.
- The user asks for expert detail.
- A keyboard user expands and closes details.
- A narrow screen shows a long localized label.

Keep critical issues visible even when the user asks for minimalism. Don't invent a score or improvement percentage without a defined measurement. Independent agent agreement is review evidence, not customer adoption or proof across different models.
