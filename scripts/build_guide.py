import argparse
import json
import re
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

root = Path(__file__).resolve().parents[1]
source = root / 'skills/instinct-design/references/instinct-teardown.zh-CN.md'
target = root / 'docs/zh/guide/index.html'
template = root / 'docs/templates/guide.html.template'
parser = argparse.ArgumentParser(description='Build the Chinese guide from its Skill reference.')
parser.add_argument('--check', action='store_true', help='Fail if the published article is stale.')
args = parser.parse_args()
text = source.read_text(encoding='utf-8')
text = re.sub(r'\]\((pattern-lab\.md|sources\.md|instinct-teardown\.md)([^)]*)\)',
              r'](https://github.com/Friedrich-arthur/instinct-design/blob/main/skills/instinct-design/references/\1\2)', text)
renderer = markdown.Markdown(extensions=['toc', 'fenced_code'],
                            extension_configs={'toc': {'slugify': slugify_unicode, 'toc_depth': '2-2'}})
body = renderer.convert(text)
url = 'https://friedrich-arthur.github.io/instinct-design/zh/guide/'
schema = {
    '@context': 'https://schema.org', '@type': 'Article',
    'headline': '从 Instinct 借鉴产品设计的八个思路',
    'description': '独立 REA 产品拆解，包含证据边界、迁移条件、反例与练习。',
    'inLanguage': 'zh-CN', 'url': url, 'mainEntityOfPage': url,
    'datePublished': '2026-10-13', 'dateModified': '2026-10-13',
    'author': {'@type': 'Person', 'name': 'Friedrich-arthur', 'url': 'https://github.com/Friedrich-arthur'},
    'license': 'https://github.com/Friedrich-arthur/instinct-design/blob/main/LICENSE',
    'image': 'https://friedrich-arthur.github.io/instinct-design/share-card.png',
}
html = template.read_text(encoding='utf-8').replace('{{body}}', body).replace('{{toc}}', renderer.toc)
html = html.replace('{{schema}}', json.dumps(schema, ensure_ascii=False, indent=2))
if args.check:
    if not target.exists() or target.read_text(encoding='utf-8') != html:
        raise SystemExit('Chinese article is stale. Run python scripts/build_guide.py.')
    print('Chinese article matches its canonical Skill reference.')
else:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8', newline='\n')
    print('Built docs/zh/guide/index.html.')
