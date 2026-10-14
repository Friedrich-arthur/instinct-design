# Instinct design

Improve your own product with Instinct-inspired design philosophy. Bring a screen, flow, spec, or code; get a concrete change and a way to check it.

Independent and unaffiliated. Outcome-first language, a focused primary view, depth on demand, predictable actions, and calm craft guide the improvements. Product research stays available when you need the source.

[Try the patterns](https://friedrich-arthur.github.io/instinct-design/) · [中文说明](README.zh-CN.md) · [Instinct teardown](skills/instinct-design/references/instinct-teardown.md) · [Pattern lab](skills/instinct-design/references/pattern-lab.md)

> **Before:** "Workflow complete! The publishing connector returned an error. See logs."
>
> **After:** "The video is exported, but the post is not published. Your draft is saved. Retry the upload when you're ready."

![An original diagram comparing a cluttered assistant screen with a result-first screen](assets/before-after.svg)

## Install

```sh
npx skills add Friedrich-arthur/instinct-design --skill instinct-design
```

Choose your agent and installation scope in the CLI. The folder uses the [Agent Skills format](https://agentskills.io/specification). For manual installation, copy the entire `skills/instinct-design` folder into your agent's supported skill directory. Copying only `SKILL.md` loses the references.

## Use

```text
Use $instinct-design to improve this product.
Inspect the attached screen, flow, spec, or code and find the friction that most affects the user's job.
Apply the relevant design principles and deliver the concrete change.
Keep the existing design system, expert needs, and critical constraints.
Show the before/after difference and how to verify it. Implement if requested and authorized.
```

For another iteration, provide the previous artifact and actual feedback or failure. The Skill checks the same user task and changes what the new evidence justifies. A one-line copy request still gets one usable line. It follows your task's language and preserves authorization, costs, uncertainty, and failure states.

Start with the material you already have:

- **Fix a page.** “Use $instinct-design on this page. Find the obstacle that most affects [user task] and deliver the smallest useful change.”
- **Improve a flow.** “Use $instinct-design on this flow. Make the result, next action, and failure recovery clear. Preserve the existing design system.”
- **Iterate from feedback.** “Use $instinct-design with this previous artifact and actual feedback. Keep accepted decisions, fix the failing moment, and check the same task.”

## What it adds

- Messages start with the actual outcome, its consequence, and the next useful action.
- The primary view stays focused. Evidence, alternatives, and advanced controls remain discoverable.
- Actions have predictable states, visible boundaries, and recovery paths.
- Visual hierarchy and restraint clarify the user's job.

The core is short. Ten references cover product optimization, the English and Chinese Instinct teardown, pattern lab, philosophy, messages, interaction, visual craft, review, and source boundaries. The agent reads only the relevant depth for the task.

## Optimize one actual task

The [optimization guide](skills/instinct-design/references/product-optimization.md) connects an observed obstacle to a design principle, a concrete change, and a check on the same task. It preserves working behavior and useful expert density. The default output is your improved artifact; an Instinct research essay appears only when relevant or requested.

[A worked product iteration](examples/04-product-iteration.md) shows how misleading import status becomes a clearer primary view and recovery, then how actual feedback would guide a narrower second change.

## Learn one useful pattern

The [teardown](skills/instinct-design/references/instinct-teardown.md) applies an evidence-led Reverse Engineer Anything approach to public product materials. Each pattern includes its evidence, mechanism hypothesis, transferable design, boundary, and check. It does not claim access to Instinct's implementation.

Try the [pattern lab](skills/instinct-design/references/pattern-lab.md) on a partly completed task, an account-disconnection receipt, or notification choices. Pick one real product problem and produce an artifact you can assess.

The [Chinese field guide](https://friedrich-arthur.github.io/instinct-design/zh/guide/) includes a borrowing worksheet and an expert-table counterexample. Its source ships inside the installed Skill.

## See the changes

| Example | Design change |
| --- | --- |
| [Assistant message](examples/01-assistant-message.md) | Put the recommendation and unresolved freight cost first |
| [Result screen](examples/02-result-screen.md) | Separate the main decision from source messages and reply editing |
| [Failure and attention](examples/03-failure-and-attention.md) | Keep partial success honest and notify only when the consequence warrants it |

These are synthetic examples. They do not document customer results or actual Instinct responses.

## Validation and contributions

The repository includes [regression prompts](evals/cases.json), including authorized continuation, expert density, feedback iteration, and non-interface documents. Read [validation scope](evals/README.md) before interpreting any result. A formatted Skill is not evidence of better user outcomes.

To report a failure, [share a sanitized task, actual output, and consequence](https://github.com/Friedrich-arthur/instinct-design/issues/new/choose). To contribute, submit the smallest rule or example that addresses an observable defect. Do not include private customer data, transcripts, credentials, or product screenshots you cannot publish.

Maintainers can rerun the integrity and article checks in the [contribution guide](CONTRIBUTING.md).

The [peer comparison and refinement record](docs/skill-refinement.md) explains the methods used, the choices adopted, and what was not measured.

The [growth plan](docs/growth-plan.md) links six executable tickets. The [launch kit](docs/launch-kit.md) provides channel-specific lessons and directory listing text. Publication, indexing, real adoption, and Stars are tracked separately.

## Attribution

This is an independent, unaffiliated design method inspired by [Instinct's public product introduction](https://instinct.com/) and interview notes. Outcome-first communication, plain language, and progressive disclosure are the author's synthesis. Visual defaults are original recommendations, not Instinct's official design system. See [sources and boundaries](skills/instinct-design/references/sources.md).

The Skill guides your agent's product improvements, including authorized code changes. It supplies instructions rather than account integrations or an autonomous assistant service. Actual execution and permissions depend on the host environment.

MIT license for the original material in this repository. Third-party brands and linked material retain their own rights.
