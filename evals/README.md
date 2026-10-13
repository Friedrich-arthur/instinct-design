# Validation scope

The first version was checked on 2026-10-13 using the actual files and small, qualitative agent trials. These checks establish package integrity and observed instruction-following. They do not establish customer adoption or an improvement percentage.

## Package checks

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
