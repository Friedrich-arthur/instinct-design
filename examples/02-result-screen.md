# A quiet screen with useful depth

Synthetic design example. A customer-feedback summary has been prepared, and its source messages are available. No customer has been contacted.

## Before

A dashboard shows the prompt, model selector, agent log, token use, every source message, sentiment chart, and suggested reply at the same visual weight. The primary action is labeled "Execute".

## After

The first view reads:

> Three customers report the same checkout error. Review the affected steps before replying.

The main action is "Review checkout errors". A visible note says "Reply drafts are prepared; none are sent."

Expand "View source messages" to inspect the evidence. Expand "Edit reply drafts" for the editable text and recipients. Technical execution details live in task history when they are needed for diagnosis.

If the user already authorized these exact replies, carry that authorization forward. If sending creates a new commitment, present the final text and recipients at that boundary. Keep the first view consistent with the actual send status.

## What changed

The screen centers the user's next decision. Expansion retains the selected customer. The visual hierarchy separates the result, action, and evidence without hiding external consequences.
