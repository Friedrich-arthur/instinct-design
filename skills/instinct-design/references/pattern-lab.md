# A small lab for useful product borrowing

These are authored, synthetic design exercises. They are not Instinct screenshots or observed customer results. Try one task in your actual product before adopting a pattern broadly.

## Exercise 1: A result that is only partly complete

**Given facts.** A video is exported. Upload failed. The draft is saved. No deadline is provided.

**Weak message.** "Workflow complete. The publishing connector returned an error."

**Proposed message.** "The video is exported, but the post is not published. Your draft is saved. Retry the upload when you're ready."

The primary view carries the real state and retry action. Upload diagnostics and the saved file belong in a named detail view. Retrying needs an actual duplicate-prevention check if the first result is uncertain.

**Try it.**

```text
Use $instinct-design on this task result.
Rewrite the user-facing message and specify what belongs in the detail view.
Keep preparation, external effects, and verified completion distinct.
Facts: [paste the actual known states].
```

**Check.** Show only the opening to a reader. Can they tell what is done and what is still pending? Do not claim the proposed retry flow exists until implemented.

## Exercise 2: A disconnection receipt

**Given facts.** Future calendar access is revoked. Previously indexed events remain. A restaurant reservation has already been made. No deletion or cancellation has been executed.

**Weak message.** "Calendar disconnected. Everything is cleared."

**Proposed first view.** "Calendar access is disconnected. Saved events remain, and the existing restaurant reservation is unchanged."

Show separate controls for deleting retained events, managing pending tasks, and opening the reservation's cancellation options when available. Name each operation's scope and result. Keep confirmed deletion distinct from a request to delete.

**Try it.**

```text
Use $instinct-design to design our account-disconnection flow.
Return a first view, expanded retained-data view, and recovery states.
State what stops, what remains, and which committed effects still exist.
Our real data and task states: [paste the known facts].
```

**Check.** A user who presses disconnect must not infer that stored data or external effects disappeared. Verify the separate operations in the real implementation. This pattern is inspired by the [published policy distinction](https://instinct.com/privacy-policy); it is our design proposal.

## Exercise 3: Choose when to interrupt

**Given facts.** The product can record a task update, batch it into a digest, or notify the user. A useful notification needs a current consequence the user can affect.

| Event | Matters now | User can act | Waiting has a consequence | Proposed behavior |
| --- | --- | --- | --- | --- |
| Background comparison is ready, no urgency | No | Yes | No | Task view or digest |
| An available slot will expire and the user can select it | Yes | Yes | Yes | Interrupt with the real expiry and action |
| A harmless internal connector changes | No | No | No | Technical history |
| An urgent event has already ended and cannot be changed | Yes | No | No | Explain in the relevant view, avoid a misleading action alert |

These judgments depend on the user's actual context. The last row may still require a requested status message, but it does not justify pretending a preventive action remains.

**Try it.**

```text
Use $instinct-design to review these notifications.
For each event, choose interruption, digest, task view, or no message.
Explain the consequence and useful action. Do not invent a deadline.
Events and user preferences: [paste the actual context].
```

**Check.** Test all three conditions, then test a meaningful loss with no explicit deadline. This is an authored design rule, not an inferred Instinct implementation.
