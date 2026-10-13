# Contribute a useful design correction

Start with an observable design failure. Include a sanitized task, actual output, consequence, and the smallest proposed correction. State whether you permit publication of the supplied material. A generated artifact, an installation, and a real user's successful task are different evidence.

## Keep the source in one place

The installed method lives in `skills/instinct-design`. Keep shared rules in `SKILL.md` and conditional depth in its references. Preserve the user's language, existing interface, and authorized scope.

The English and Chinese teardown cover the same eight patterns. Use the same evidence boundaries when changing either. Put source updates in `references/sources.md`. Do not infer runtime behavior or internal architecture from a page or interview chapter.

The Chinese article comes from `references/instinct-teardown.zh-CN.md`. Change that source, then regenerate the article. The generator consumes repository-authored Markdown; it is not a sanitizer for untrusted uploads.

## Run the package checks

Use Python 3.10 or later. The integrity checker uses only the standard library. Article generation uses the pinned development dependency.

```sh
python -m pip install -r requirements-dev.txt
python scripts/build_guide.py
python scripts/build_guide.py --check
python scripts/check_bundle.py
```

The integrity check detects broken local references, malformed structured files, and selected private-path or credential patterns. It does not certify security, accessibility, real runtime behavior, or writing quality. Check any changed page in a browser, including a narrow layout, keyboard access, navigation, and relevant failure behavior.

## Check changes on a real task

For changes that affect decisions, run one relevant prompt in a fresh task with the Skill. Use the same prompt without it when assessing an advantage. Preserve the actual artifact, setup, and failures. [Validation scope](evals/README.md) records current findings and limitations.

Do not supply an expected answer to the executing agent. Have an independent reviewer inspect state honesty, artifact usefulness, evidence, applicability, and reader load. Prefer a narrow correction over adding a new rule for every example. Small wording edits need proportionate checks.

## Share material you can publish

Use original diagrams and examples or content you have permission to share. Remove customer data, credentials, private paths, full transcripts, and personal records. Claim actual tests and outcomes only. Directory acceptance, search indexing, AI citation, voluntary adoption, and Stars each require separate evidence.
