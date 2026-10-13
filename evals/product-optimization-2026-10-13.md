# Product optimization forward task

Date: 2026-10-13. An independent fresh agent received a local copy of the actual published v0.3.0 Chinese homepage and a draft v0.4.0 Skill. The task was to improve the page for this product-centered positioning. No intended wording, assessment criteria, previous outputs, or suspected defect was supplied.

## Task supplied

```text
我们已有一个开源产品设计Skill的网站。现在希望访客理解：它帮助用户借鉴其中设计哲学优化自己的产品，并可以根据反馈继续迭代。请用这个Skill优化现有中文首页的介绍与使用示例，让访客知道带来什么输入、得到什么具体产物、怎样继续下一轮。直接修改现有HTML，保留安装、通知练习、来源与既有页面布局。不要建新应用。检查改动是否完成目标，说明已检查与尚未验证的内容。
```

The provided workspace contained the real homepage, its unchanged CSS and JavaScript, the Skill snapshot, room instructions, and the task. It intentionally did not contain the whole site, user accounts, visitor metrics, or customer records. The agent inherited the same configured model and reasoning settings as root. This is independent same-model work, not cross-model testing or a with/without comparison.

## Actual artifacts and finding

The agent changed the HTML. It made inputs and delivered artifacts explicit, rewrote the existing examples around inputs and checks, added an implementation prompt and an illustrative feedback prompt, and clarified the hosting agent's authorized code changes. It did not stop at an Instinct essay or recommendations alone.

The [actual patch](artifacts/product-homepage.patch) preserves its changes against v0.3.0 as a zero-context unified diff. The [actual delivery note](artifacts/product-homepage-result.md) preserves its reported checks and limitations. Only newline encoding is normalized. Root read the changed file and independently confirmed that the installation command, IDs, interaction hooks, CSS, and JavaScript remained unchanged. The Skill supplied to the task was a draft; a later qualifier keeps small copy edits from loading the full optimization reference.

The page's second-iteration prompt contains illustrative feedback. No visitor actually supplied that example. A future-feedback prompt is not evidence of repeat use. The task result also correctly noticed that the partial workspace lacked the linked guide and did not infer that the live guide was unavailable.

The candidate performed static checks and reported that browser rendering, clipboard, narrow layouts, and actual visitor understanding remained unverified. Its patch is preserved as task evidence, not published as the canonical website. Root's own product edits were reviewed separately.

## Final package and product checks

An independent reviewer inspected the revised core, default prompt, optimization reference, worked example, and public entry points. Two consistency issues were fixed: the synthetic bilingual example no longer adds an unsupported subset relation, and the homepage FAQ now explains authorized product-code changes separately from account services.

Root exercised the canonical English and Chinese pages in Edge at 1440, 390, and 320 pixels, plus no-JavaScript reading. Copying the actual installation command, all eight attention combinations, refresh reset, keyboard focus, language alternates, and structured data passed. Visual inspection found an awkward Chinese headline wrap at 320 pixels; root shortened it and confirmed the revised headline fits two lines at that width. These are actual artifact checks, not customer outcome measurements.

Package checks and article-generation checks remain available through [the contribution guide](../CONTRIBUTING.md). This one forward task establishes an observed concrete optimization behavior. It does not establish stable agent reliability, better visitor comprehension, conversion, actual customer feedback, or repeat adoption. No target-specific tool-transcript audit is claimed.
