# Interaction design

Keep the user's task visible while the system does complex work. A minimal screen still needs discoverable actions, meaningful status, and a way to recover.

## Design three levels

| Level | Content | Typical form |
| --- | --- | --- |
| Primary | Outcome or current state, decisive limitation, next action | Message, task row, or result card |
| Expanded | Rationale, evidence, alternatives, and useful edits | Disclosure, side panel, table, or document |
| Advanced | Execution details, technical controls, and history | Task details or settings |

This is a starting structure. Keep the existing interface when it fits. A dense professional workspace may need more information in its primary view. Don't hide what the user needs for the current decision merely to satisfy the three levels.

Preserve context when expanding. Keep the user's edits and selection. Make the expanded state navigable with a keyboard. Support a clear close or back action. Match labels across the primary view, detail view, and action result.

## Make states meaningful

Name the state using its effect on the user. "Finding available times" can be useful. A stream of internal tool names usually is not.

For a consequential task, design the relevant states:

- Preparing or running, with useful progress if available.
- Waiting for a specific user decision or external response.
- Completed with verified evidence.
- Partially completed, with the remaining work visible.
- Failed, with preserved work and a recovery action.
- Cancelled, with the status of any effects already committed.

Avoid pretending that every task needs every state. Don't invent timing estimates. If the user can cancel, explain what cancellation stops and what has already happened.

## Keep consent and continuity together

Carry existing authorization forward for the same scope. Don't ask repeatedly because the system changed tools. Before a new commitment, present what changes, who is affected, and any material cost or risk. Finish the authorized preparation first.

A confirmation must be specific enough to understand without opening logs. "Send this invitation to Alex for Tuesday at 10:00?" names the effect. A generic "Continue?" does not.

Request access for the job that needs it. Explain the use, and allow refusal without implying consent. If the product supports revocation, distinguish disconnecting an account from deleting cached data and derived memory. Show which operation completed and which data remains. Do not promise deletion or continued access that the implementation cannot provide.

If the design includes persistence, specify what survives reload and restart, how the user sees the saved state, and how conflicting changes are handled. Don't imply that an HTML prototype or a written state model implements persistence.

## Design interruption

Notify when the information matters, the user can act, and waiting has a consequence. Put the deadline and consequence in the primary message. Batch other events into a digest or task history. Let users control quiet hours and relevant notification preferences when the product supports them.

Reduce repeated notices for the same unresolved event. Escalation needs a changed consequence or deadline. These are product recommendations, not permission to message the user's contacts.
