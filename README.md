# Instinct design

Borrow practical product ideas from Instinct, then design clearer AI assistant messages, interfaces, permissions, and recovery.

Independent and unaffiliated. Eight evidence-backed patterns, three synthetic practice tasks, and a short Skill that reveals depth when you need it.

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
Use $instinct-design to improve this AI assistant screen.
Keep the user's task and existing design system.
Show a concrete first view, expanded details, and failure recovery.
```

You can also ask it to rewrite a notification, design an agent task flow, or review a product spec. It follows the language of your request. It preserves existing authorization and keeps cost, risk, uncertainty, and failures visible.

## What it adds

- Messages start with the actual outcome, its consequence, and the next useful action.
- The primary view stays focused. Evidence, alternatives, and advanced controls remain discoverable.
- Actions have predictable states, visible boundaries, and recovery paths.
- Visual hierarchy and restraint clarify the user's job.

The core is short. Nine references cover the English and Chinese Instinct teardown, pattern lab, philosophy, messages, interaction, visual craft, review, and source boundaries. The agent reads only the relevant depth for the task.

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

The repository includes [five evaluation prompts](evals/cases.json), including authorized continuation and the risk of hiding payment behind minimalism. Read [validation scope](evals/README.md) before interpreting any result. A formatted Skill is not evidence of better user outcomes.

To report a failure, open an issue with a sanitized task, the observed output, and the consequence. To contribute, submit the smallest rule or example that addresses an observable defect. Do not include private customer data, transcripts, credentials, or product screenshots you cannot publish.

Maintainers can rerun the integrity and article checks in the [contribution guide](CONTRIBUTING.md).

The [growth plan](docs/growth-plan.md) links six executable tickets. The [launch kit](docs/launch-kit.md) provides channel-specific lessons and directory listing text. Publication, indexing, real adoption, and Stars are tracked separately.

## Attribution

This is an independent, unaffiliated design method inspired by [Instinct's public product introduction](https://instinct.com/) and interview notes. Outcome-first communication, plain language, and progressive disclosure are the author's synthesis. Visual defaults are original recommendations, not Instinct's official design system. See [sources and boundaries](skills/instinct-design/references/sources.md).

The Skill designs and reviews experiences. It does not install an assistant, connect personal accounts, or implement autonomous actions.

MIT license for the original material in this repository. Third-party brands and linked material retain their own rights.
