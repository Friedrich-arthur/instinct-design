# Instinct design

Design AI products that put the result first and reveal useful depth when the user needs it.

[中文说明](README.zh-CN.md) · [Skill](skills/instinct-design/SKILL.md) · [Design document 中文](docs/design.zh-CN.md)

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

The core is short. Five focused references cover philosophy, messages, interaction, visual craft, and review. A separate source note records attribution and evidence limits. The agent reads the relevant depth for the task.

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

## Attribution

This is an independent, unaffiliated design method inspired by [Instinct's public product introduction](https://instinct.com/) and interview notes. Outcome-first communication, plain language, and progressive disclosure are the author's synthesis. Visual defaults are original recommendations, not Instinct's official design system. See [sources and boundaries](skills/instinct-design/references/sources.md).

The Skill designs and reviews experiences. It does not install an assistant, connect personal accounts, or implement autonomous actions.

MIT license for the original material in this repository. Third-party brands and linked material retain their own rights.
