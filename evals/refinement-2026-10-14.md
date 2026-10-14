# v0.5.0 refinement checks

Date: 2026-10-14. The candidate adds accepted-decision continuity, relevant content-range checks, a brief task-specific visual reason, and a narrower rule for non-interface documents. This record describes bounded internal checks. It is not an uplift, activation-rate, customer-adoption, or runtime-performance result.

## Fresh task artifacts

Three separate agents received the candidate Skill snapshot and the task below. They inherited the configured session model. They did not receive the case criteria, example outputs, peer comparison, or previous evaluation reports. The follow-up deliberately received the actual first artifact and the project reviewer's feedback. This was not a comparison across models or an A/B run.

The delivered text is retained without editorial changes. Publication line endings are normalized to LF with one terminal newline.

| Task | Supplied job and facts | Actual artifact |
| --- | --- | --- |
| Expert supplier comparison | Improve a dense seven-column table for procurement experts. A: $9, MOQ 500, 25 days, $700 freight, today. B: $8.6, MOQ 600, 20 days, unknown freight because parsing failed, yesterday. C: $9.2, MOQ 400, 23 days, $650 freight, today. Preserve existing rows, source file, keyboard use and return from the detail panel. No purchase or email is authorized. The old headline incorrectly says all synchronization succeeded and procurement can proceed. | [Unedited screen and recovery specification](artifacts/expert-table-2026-10-14.md) |
| Non-interface import rules | Rewrite a product-rule document. Parsing and preview do not write business records. Missing mandatory columns reject the batch. Explicit confirmation is needed to submit valid rows. Submission is one transaction; failure rolls back this batch. CSV retention follows an unspecified existing policy. No automatic retry or submission. Return rules and acceptance conditions, not UI or code. | [Unedited rule revision](artifacts/import-rules-2026-10-14.md) |
| Follow-up on the same table | The project reviewer read the first specification and observed that acceptance conditions omit zero suppliers, one supplier, and long names. Add only the missing content-range behavior. Preserve accepted density, keyboard continuity, facts and authorization. Actual maximum count and longest name are unknown; label any example ranges. | [Unedited bounded follow-up](artifacts/expert-followup-2026-10-14.md) |

The first artifact keeps seven columns and distinguishes known fields, failed freight parsing, and unconfirmed comparability. Its proposed arithmetic is explicitly conditional and is not a procurement recommendation. The rule revision separates preview from committed business data and marks retention duration as unknown. The follow-up adds content-boundary acceptance behavior without restyling the product. Read the raw artifacts to assess the detail and any proposed capability expansion.

The feedback is an actual internal document-review observation, not a report from an external customer. All three outputs are specifications. No supplier flow, CSV transaction, saved state, procurement, email, or customer task was executed. Snapshot hashes confirm that the supplied instruction files match the final candidate. Agent reports of reference loading were not independently audited from tool transcripts; no loading-frequency or token figure is claimed.

The [case registry](cases.json) now contains nine prompts. The four added categories are implementation, expert-table continuity, feedback iteration and non-interface rules. Registry coverage does not mean all nine were newly run. The historical implementation trial remains [separately documented](product-optimization-2026-10-13.md).

## Structure and static safety

The Codex minimal frontmatter validator accepted the final candidate. The Chinese article matches its canonical reference. The package checker checks local links, anchors, structured data and private-path patterns; it is not a behavior validator.

The installed Skill security auditor returned PASS with no findings on 14 scanned files, including 11 Markdown files and no scripts. Its [sanitized actual JSON result](artifacts/static-security-2026-10-14.json) preserves the verdict and scope. This static pattern check does not certify safe agent execution, authorization, data handling, integrations or supply-chain security.

Legacy meta scorers were actually run on v0.4.0 and failed their format/length rules. The revision did not add filler, fixed chapters or an unused script directory to satisfy those rules. The SkillOpt and Sleep engines were not run. See the [method ledger](../docs/skill-refinement.md).

## Public interface checks

The bilingual site was exercised in installed Edge at 1440, 390 and 320 pixels. The checks cover overflow, both actual clipboard contents, keyboard activation of the request, nearby success/failure feedback, eight attention-condition combinations and refresh reset, native disclosure with JavaScript disabled, metadata, and no unexpected external requests or script errors. Clipboard denial preserves the text and supplies a manual-copy instruction for both controls. Windows clipboard CRLF was normalized to LF only in the multiline readback assertion; no other characters were ignored.

The actual 1200 × 630 share PNG was exported from the edited SVG source and inspected. Both now promise a concrete improvement to the user's product. The launch kit is prepared copy, not published social content. Feedback links reach the existing issue-form chooser; the new source field is optional. No account, analytics, cookie, local-storage persistence, or external effect was added.

These checks cover the local product interface. Publication readback is recorded separately in the release. Screenshots and keyboard checks do not establish full accessibility compliance, discovery ranking, AI citation, directory acceptance or adoption. Runtime performance was not benchmarked.
