# Why the product-optimization method changed

The v0.5.0 revision keeps one job: improve the user's product and check the same task. It adds continuity between iterations, task-specific design reasons, clearer first requests, and a narrower document rule. Research stays optional.

## Five peers informed the choices

On 2026-10-13, the comparison read each maintainer's public source at the fixed commit below. Anthropic publishes its own Skills. The other projects are first-hand maintainer sources, not platform endorsements. Source review establishes what the instructions define, not which Skill works best.

| Peer and fixed source | License read | What informed this revision | What stays out |
| --- | --- | --- | --- |
| [Anthropic frontend-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/SKILL.md), `dbd4588f9e1033efb41dad4bef2f7947c8993d44` | [Apache-2.0 for this Skill](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt) | Explain how the main design choice serves this brief. | A new visual identity for every local fix. Licenses for other Skills in the repository do not apply here. |
| [Impeccable](https://github.com/pbakaus/impeccable/blob/245ad82def45831dc56a21b683c7a1ff530b06cc/.agents/skills/impeccable/SKILL.md), `245ad82def45831dc56a21b683c7a1ff530b06cc` | [Apache-2.0](https://github.com/pbakaus/impeccable/blob/245ad82def45831dc56a21b683c7a1ff530b06cc/LICENSE) and [NOTICE](https://github.com/pbakaus/impeccable/blob/245ad82def45831dc56a21b683c7a1ff530b06cc/NOTICE.md) | Preserve accepted product decisions. Distinguish operating, reading, and persuasion tasks. | Its 24 commands, launcher, hooks, live service, and initialization interview. |
| [Taste Skill v2](https://github.com/Leonxlnx/taste-skill/blob/c924fad1a79c7d70a04bcc8c415b593e9928ad8a/skills/taste-skill/SKILL.md), `c924fad1a79c7d70a04bcc8c415b593e9928ad8a` | [MIT](https://github.com/Leonxlnx/taste-skill/blob/c924fad1a79c7d70a04bcc8c415b593e9928ad8a/LICENSE) | Read the existing product before a scoped change, as its [redesign Skill](https://github.com/Leonxlnx/taste-skill/blob/c924fad1a79c7d70a04bcc8c415b593e9928ad8a/skills/redesign-skill/SKILL.md) defines. | Universal bans on fonts or gradients, minimum image and motion counts, and fixed critique rounds. v2 itself targets public websites rather than app screens. |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7246805992a42b7bba37d4cac83b01416f0c6c44/.claude/skills/ui-ux-pro-max/SKILL.md), `7246805992a42b7bba37d4cac83b01416f0c6c44` | [MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7246805992a42b7bba37d4cac83b01416f0c6c44/LICENSE) | Read existing design decisions before changing them. Use only relevant task depth. | A style database, numeric taste controls, or resource counts as quality evidence. |
| [Interface Design](https://github.com/Dammyjay93/interface-design/blob/2f9be3206855bcb2d1d0af262c8bae25cba6658d/.claude/skills/interface-design/SKILL.md), `2f9be3206855bcb2d1d0af262c8bae25cba6658d` | [MIT](https://github.com/Dammyjay93/interface-design/blob/2f9be3206855bcb2d1d0af262c8bae25cba6658d/LICENSE) | Keep useful expert density and check drift against accepted decisions. | Mandatory domain inventories, signature tests, or repeated approval to save an authorized decision. |

The revision uses original instructions and commentary. It does not copy third-party Skill text, scripts, or assets. The comparison did not install or run these five peers.

## The changes stay small

- Read the previous artifact and existing design notes. Keep accepted tasks, constraints, and working behavior. Reopen only decisions that new evidence affects.
- Inspect real content, important states, controls, and expert information before proposing a change. A familiar dense table can be the right primary view.
- Explain one important visual or structural choice through the user's action. Extra motion or a new brand direction needs a task reason.
- Offer three natural-language entry points: fix a page, improve a flow, or iterate from actual feedback. No new command system is required.
- Limit primary and expanded views to interface specifications where they help. Revise another document in its useful existing structure.

## Meta tools contributed methods and checks

The quality review used the installed instructions below. Reading a method is separate from running its engine.

| Method | Actual use | Engine boundary |
| --- | --- | --- |
| `skill-creator` | Review concrete outputs, relevant references, routing boundaries, and coverage. Run the Codex minimal frontmatter validator. | The validator accepted the v0.4.0 package. No CLI description-optimization loop or measured trigger rate. |
| `skill-tester` | Inspect and run its local structure validator and quality scorer on v0.4.0. Preserve the failures. | Structure scored 16.7/100 and quality 38.7/100 because its legacy layout and length rules differ. No padding to satisfy them. No script tester for an instruction-only installed Skill. |
| `skill-optimizer` | Separate task cases from candidate selection. Define success through artifacts and preserve failures. | No `gbrain skillopt` run, selection-set score, median-of-three gate, or automatic optimization receipt. |
| `skillopt-sleep` | Use the bounded cycle of actual failure, targeted change, and a check under the original conditions. | No sleep engine, history harvest, scheduled replay, global configuration change, or memory evolution. |
| `skill-security-auditor` | Run the installed static scanner on the final instruction folder; retain its actual result. | Pattern matching only. No runtime or supply-chain certification. |
| `copywriting` | Align the share image and prepared channel summaries with the concrete product-improvement promise. | No invented customer quotes, conversion numbers, or social publication. |
| `page-cro` | Reduce the steps from installation to a usable request and from use to the existing feedback form. | No traffic-based A/B experiment or predicted uplift. |
| `content-strategy` | Lead with a transferable design lesson and use actual task feedback to choose future content. | No invented search volume, interview results, or mandatory content calendar. |
| `ai-seo` | Inspect visible definitions, metadata, source attribution and technical discovery; check current official guidance. | No ranking, AI citation, or search-console result. Search crawling and training are separate decisions. |

The legacy security score was 100 because the installed Skill has no scripts. That empty-set result is not a safety assessment. The v0.4.0 reference inventory found 11 readable instruction files and 21 existing local file references. Word and line counts were not model-token measurements.

## Evidence has a version and a limit

Read [validation scope](../evals/README.md) for the historical paired and implementation trials. The [v0.5.0 refinement checks](../evals/refinement-2026-10-14.md) are the release-specific place for raw behavioral artifacts and static safety results. Follow each result's actual status and scope.

This comparison alone does not establish successful behavior, safe execution, reliable routing, runtime performance, customer adoption, or repeat use. Static safety checks inspect instructions and files. The host still controls tools, permissions, accounts, and persistence.
