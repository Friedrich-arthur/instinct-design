# Improve an import flow, then iterate on feedback

This is an authored, synthetic example. The screen, results, and illustrative feedback are not observed customer behavior. It demonstrates the product-optimization deliverable.

## Input artifact and job

A financial operator reviews imported transactions before submission. The existing table supports keyboard selection and filtering. Its status bar says “Import complete,” while a side log says the supplier column is unmapped. Thirty-seven records are unmatched, five need threshold review, and zero rows have been submitted.

The user asks to improve the screen with this design philosophy. They need a design proposal, not a replacement application or an Instinct essay.

## Proposed first change

Replace the misleading status with “Import paused: map the supplier column to continue. Current unmatched records: 37; threshold reviews: 5. Submitted: 0.” In Chinese, use “导入已暂停：请配置供应商列后继续。当前37条未匹配，5条需阈值复核；0条已提交。”

Keep the transaction table and its comparison fields visible. Make “Map supplier column” the primary action. Open a side panel with actual source headers and sample values; do not infer the mapping without evidence. Put diagnostics in “Import details.” Preserve selection and edits when closing the panel, and state the requirements for resuming without duplicate rows.

This applies outcome-first language and depth on demand. It keeps decisive missing information visible and retains expert task efficiency. Completion and persistence remain implementation requirements until exercised.

## Check the first change

Ask a target reader to identify what is done, what is blocked, and the next action from the status bar. In the actual implementation, map a column, close and reopen the panel, and resume the same import. Check the selected row, saved edits, current counts, and duplicate prevention. Report which behavior was actually exercised.

## A narrower next iteration

Suppose later permitted feedback says the mapping panel works, but returning to the table resets the user's filter. That feedback would justify repairing return continuity and checking it on the same task. It would not justify replacing the table with chat or adding another global notification.

Keep the clearer status and the comparison fields. Repair the filter reset, then replay “filter, select, map, return.” Record whether the state survives. If that report never arrives, do not invent it or claim the second change is necessary.

## Copy the request for your product

```text
Use $instinct-design to improve this product task.
User and desired result: [actual context].
Current screen, flow, spec, or code: [artifact].
Known problem or feedback: [observed fact; mark a hypothesis if unverified].
Deliverable: [copy, layout, flow, spec, or implementation].
Keep the working interface and essential constraints.
Return the concrete improvement, its before/after consequence, and a check.
```
