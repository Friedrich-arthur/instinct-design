# Validation scope

The first version was checked on 2026-10-13 using the actual files and small, qualitative agent trials. These checks establish package integrity and observed behavior. They do not establish customer adoption or an improvement percentage. The sections below identify the version and setup of each run.

## Package checks

The latest [v0.5.0 refinement checks](refinement-2026-10-14.md) include fresh expert-table and non-interface artifacts, a separate follow-up from actual internal review, and the static safety result. The historical runs below retain their original versions and limits.

- The Codex skill-creator validator accepted the Skill's frontmatter and structure.
- The Skills CLI discovered exactly one local Skill, named `instinct-design`.
- Local references, UTF-8 text, JSON cases, and SVG syntax were checked. Public files were reviewed for private paths and credentials.
- An independent reviewer inspected the public method for attribution, usability, state consistency, disclosure, authorization, and implementation claims.

The illustration is a static, original design diagram. It was rendered to PNG and visually inspected for legible text, spacing, and content. Browser preview attempts did not complete. The illustration has no interactive behavior.

## Behavior smoke trials

Two agents with fresh context received the same five task prompts. One used the Skill and its relevant references, and one used no Skill. Each agent handled its five tasks in a single batch. The agents inherited the same configured model; this was not a comparison across different models. The agents did not read the case criteria or example outputs.

| Case | Observed with the Skill | Baseline observation |
| --- | --- | --- |
| Partial completion | Kept exported, saved, and not published distinct | Also preserved those facts |
| Screen disclosure | Kept unknown freight and unauthorized purchase visible, and specified expanded evidence | Also preserved these boundaries |
| Authorized continuation | Continued the existing scope without approving an internal connector change | Also avoided redundant approval |
| Expert depth | Preserved zero committed rows and missing mapping evidence | Also avoided inventing the mapping |
| Minimalism boundary | Kept $120, non-refundability, and the external reservation visible | Also kept these consequences visible |

The comparison did not demonstrate a reliable advantage over the baseline. The with-Skill batch produced more detailed state and recovery specifications, which may help a product spec and may be excessive for a smaller request. Review the artifact requested by the user before expanding detail.

The mixed-language with-Skill batch answered English prompts in Chinese. The core was clarified to follow the current task's requested language. A separate, fresh-context English supplier-comparison task then produced an English specification and preserved the freight and authorization boundaries. Batch context and one run per condition limit the comparison; the cases should be rerun as separate tasks when testing broader reliability.

## Reuse the cases

Run each prompt in [cases.json](cases.json) as a separate task with minimal input and no expected answer. Repeat the same prompt without the Skill or with the prior version. Preserve the raw outputs outside the installed Skill folder, then inspect them against the behavioral criteria.

Record the actual artifact, relevant loaded references, the model and context setup when available, and any failure. Add a new case when a real defect justifies it. Do not turn wording matches into proof of a good experience.

Live email sending, buying, import execution, payment, account deletion, persistence, accessibility compliance, and runtime performance were not exercised. They are design requirements in these outputs, not implemented capabilities of this Skill.

## v0.2.0 product borrowing and public entry point

The updated Skill adds an evidence-backed Instinct teardown and a pattern lab. A fresh agent used the Skill on a minimal email-disconnection screen with retained indexed messages, two unsent drafts, and a previously sent newsletter. Its actual artifact kept those states distinct, defined relevant detail and recovery views, and did not invent Instinct's runtime or assume that unsent drafts were queued jobs. This is a bounded qualitative trial, not proof of superiority over the baseline.

The bilingual static landing pages were exercised using bundled Playwright and an installed Edge browser. English and Chinese views were checked at 1440 and 390 pixels, including copying the real installation command, all eight attention-condition combinations, keyboard access, refresh reset, and content without JavaScript. An independent check covered 320 pixels and clipboard denial. The exercise intentionally has no persistent state and resets on refresh. No third-party script, analytics, cookie, or account action is part of the page.

Review found an undersized example-disclosure target; it was enlarged to 44 pixels before the final check. Metadata, language alternates, and structured data were inspected separately from search indexing. Page publication does not establish search ranking, AI citation, directory listing, audience traffic, or useful adoption.

## Separate paired tasks and v0.3.0 maintenance

[Raw paired artifacts](paired-2026-10-13.md) preserve three briefs and all six outputs. Every task ran in a separate fresh context. The Skill condition received v0.2.1; baseline rooms received the same brief without it. A separate reviewer assessed anonymous pairs on one scale. The reviewer preferred the Skill travel artifact slightly and had no clear preference for expert-table or one-sentence tasks. Root agrees with the limited findings. This run does not demonstrate a reliable improvement or actual user benefit. The provided reference files do not establish which files each agent read; no independent tool-transcript audit is claimed.

Both expert-table outputs rejected forcing a dense reconciliation workflow into chat, and both short-copy outputs preserved the partial failure in one sentence. These are useful observed boundaries. They do not turn the Skill into a necessary condition for good design.

The v0.3.0 package adds a full Chinese reference and a static article generated from it. The paired run did not use this new reference. The article and package need separate structural, browser, and editorial checks. Maintainers can rerun the [public check commands](../CONTRIBUTING.md); package checks do not score prose or prove that agents obey it.

## v0.4.0 product optimization as the default job

The default task now applies the philosophy to the user's product, delivers concrete changes, checks the same job, and iterates from actual feedback. Instinct research is optional depth. [The fresh forward task](product-optimization-2026-10-13.md) preserves an actual change to a copy of this project's published homepage, the input, the patch, and the delivery note. It is one observed implementation task, not a superiority comparison or a customer adoption report.

Independent review and browser checks identified and resolved an unsupported bilingual count relationship, a stale capability FAQ, and an awkward narrow-screen headline wrap. The record distinguishes the candidate's static checks from root's final website checks and hypothetical feedback from actual use.
