#!/usr/bin/env python3
"""Offline bundle integrity checks. Passing is not a security certification."""
import argparse
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKIP = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}
TEXT = {".md", ".html", ".json", ".svg", ".xml", ".yaml", ".yml", ".js", ".css", ".py"}
RISKS = {
    "private local path": r"(?i)(?:[A-Z]:[\\/]+(?:Users|workspace)\b|/(?:Users|home)/[^/\s]+/|/mnt/[a-z]/(?:Users|workspace)/|notion-file-block:/{2}|file:/{2})",
    "credential token": r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)",
    "credential assignment": r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"'](?!<|example|placeholder)[A-Za-z0-9_+/=-]{16,}[\"']",
}


def reject_constant(value):
    raise ValueError(f"non-finite JSON number: {value}")


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links, self.anchors, self.ld, self.script = [], set(), [], None
        self.canonical = ""
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.anchors.update(attrs[k] for k in (("id", "name") if tag == "a" else ("id",)) if attrs.get(k))
        self.links.extend((self.getpos()[0], attrs[k] or "") for k in ("href", "src") if k in attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href", "")
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self.script = [self.getpos()[0], ""]

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        if self.script is not None:
            self.script[1] += data

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.ld.append(self.script)
            self.script = None


def markdown(source):
    lines, fence = [], ""
    for line in source.splitlines():
        mark = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if mark and (not fence or mark[1][0] == fence[0] and len(mark[1]) >= len(fence)):
            fence = "" if fence else mark[1]
            lines.append("")
        else:
            lines.append("" if fence else line)
    clean, anchors, counts = re.sub(r"(`+).*?\1", "", "\n".join(lines)), set(), {}
    for i, line in enumerate(lines):
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        title = heading[1] if heading else lines[i - 1] if i and re.fullmatch(r"\s{0,3}(?:=+|-+)\s*", line) else ""
        if title:
            title = re.sub(r"!?\[([^]]+)\]\([^)]*\)|<[^>]*>", lambda m: m[1] or "", title)
            slug = re.sub(r"[^\w\- ]", "", html.unescape(title).lower()).replace(" ", "-")
            n = counts.get(slug, 0)
            anchors.add(slug + (f"-{n}" if n else ""))
            counts[slug] = n + 1
    refs = {m[1].strip().casefold(): m[2] for m in re.finditer(r"^\s{0,3}\[([^]]+)\]:\s*(<[^>]+>|\S+)", clean, re.M)}
    links = []
    pattern = r"!?\[([^]\n]+)\](?:\(\s*(<[^>]+>|(?:[^()\s]|\([^()]*\))+)(?:\s+[^)]+)?\s*\)|\[([^]\n]*)\])?"
    for m in re.finditer(pattern, clean):
        target = m[2] or refs.get((m[3] or m[1]).strip().casefold())
        if target:
            links.append((clean.count("\n", 0, m.start()) + 1, target.strip("<>")))
    page = Page(clean)
    return links + page.links, anchors | page.anchors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    root = parser.parse_args().root.resolve()
    errors, texts, pages, anchors = [], {}, {}, {}

    def fail(path, line, message):
        errors.append(f"{path.relative_to(root).as_posix()}:{line}: {message}")

    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    files = []
    for folder, dirs, names in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP]
        files.extend(Path(folder) / name for name in names)
    for path in sorted(files):
        if not path.resolve().is_relative_to(root):
            fail(path, 1, "file resolves outside bundle")
            continue
        raw = path.read_bytes()
        try:
            if b"\0" in raw:
                if path.suffix.lower() in TEXT:
                    fail(path, raw[:raw.index(b"\0")].count(b"\n") + 1, "NUL byte in text")
                continue
            source = raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            if path.suffix.lower() in TEXT:
                fail(path, 1, "text is not valid UTF-8")
            continue
        texts[path] = source
        for label, pattern in RISKS.items():
            for match in re.finditer(pattern, source):
                fail(path, source.count("\n", 0, match.start()) + 1, f"possible {label}")
        suffix = path.suffix.lower()
        try:
            if suffix == ".json":
                json.loads(source, parse_constant=reject_constant)
            elif suffix in {".svg", ".xml"}:
                tree = ET.fromstring(source)
                anchors[path] = {node.attrib["id"] for node in tree.iter() if "id" in node.attrib}
            elif suffix == ".html":
                pages[path] = Page(source)
                anchors[path] = pages[path].anchors
                for line, block in pages[path].ld:
                    try:
                        json.loads(block, parse_constant=reject_constant)
                    except ValueError as exc:
                        fail(path, line + getattr(exc, "lineno", 1) - 1, f"invalid JSON-LD: {exc}")
            elif suffix == ".md":
                anchors[path] = markdown(source)[1]
        except (ValueError, ET.ParseError) as exc:
            line = getattr(exc, "lineno", None) or getattr(exc, "position", (1,))[0]
            fail(path, line, f"invalid {suffix[1:].upper()}: {exc}")
    site = urlsplit("")
    if root / "docs" / "sitemap.xml" not in texts:
        fail(root / "docs" / "sitemap.xml", 1, "missing sitemap")
    if root / "docs" / "index.html" in pages:
        try:
            site = urlsplit(pages[root / "docs" / "index.html"].canonical)
        except ValueError as exc:
            fail(root / "docs" / "index.html", 1, f"invalid canonical URL: {exc}")
    checked = 0

    def check(path, line, link, sitemap=False):
        nonlocal checked
        try:
            url = urlsplit(html.unescape(link))
        except ValueError as exc:
            fail(path, line, f"invalid URL: {exc}")
            return
        owned = bool(site.netloc and url.netloc.lower() == site.netloc.lower() and url.path.startswith(site.path))
        if (url.scheme or url.netloc) and not owned:
            if sitemap:
                fail(path, line, "sitemap target is outside the canonical site")
            return
        checked += 1
        name = unquote(url.path)
        if owned or path.suffix == ".html" and name.startswith("/"):
            name = name[len(site.path):] if site.path and name.startswith(site.path) else name.lstrip("/")
            target = root / "docs" / name
        else:
            target = root / name.lstrip("/") if name.startswith("/") else path.parent / name if name else path
        target = target.resolve()
        if target.is_dir():
            target = next((target / f for f in ("index.html", "index.md", "README.md") if (target / f).is_file()), target)
        if not target.is_relative_to(root) or not target.is_file():
            fail(path, line, f"missing or escaping local target: {link}")
        elif sitemap and target.suffix != ".html":
            fail(path, line, f"sitemap target is not HTML: {link}")
        elif url.fragment and target in anchors and unquote(url.fragment) not in anchors[target]:
            fail(path, line, f"missing anchor: {link}")

    for path, source in texts.items():
        links = pages[path].links if path in pages else markdown(source)[0] if path.suffix == ".md" else []
        for line, link in links:
            check(path, line, link)
        if path.name == "sitemap.xml":
            try:
                offset = 0
                for node in ET.fromstring(source).iter():
                    value = node.text.strip() if node.tag.endswith("}loc") and node.text else node.get("href")
                    if value:
                        found = source.find(value, offset)
                        offset = found + len(value)
                        check(path, source[:max(found, 0)].count("\n") + 1, value, sitemap=True)
            except ET.ParseError:
                pass
    core = root / "skills" / "instinct-design" / "SKILL.md"
    body = texts.get(core, "")
    front = re.match(r"\A---\s*\n(.*?)\n---(?:\r?\n|$)", body, re.S)
    fields = front[1] if front else ""

    def scalar(source, key, indent=""):
        match = re.search(rf"(?m)^{indent}{key}:[ \t]*(.*)$", source)
        value = match[1].strip() if match else ""
        if value.startswith(("\"", "'")):
            return value[1:-1].strip() if len(value) > 1 and value[-1] == value[0] else ""
        return value.split(" #", 1)[0].strip() if value and value[0] not in "#|>" and value not in {"null", "~", "true", "false"} else ""

    metadata = re.search(r"(?m)^metadata:[ \t]*\r?\n((?:[ \t]+.*\n?)*)", fields + "\n")
    values = {"name": scalar(fields, "name") == "instinct-design", "description": bool(scalar(fields, "description")), "metadata.version": bool(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][\w.-]+)?", scalar(metadata[1] if metadata else "", "version", "  ")))}
    for label, valid in values.items():
        if not valid:
            fail(core, 1, f"missing or invalid core {label}")
    agent = core.parent / "agents" / "openai.yaml"
    config = texts.get(agent, "")
    interface = re.search(r"(?m)^interface:[ \t]*\r?\n((?:[ \t]+.*\n?)*)", config + "\n")
    if not interface:
        fail(agent, 1, "missing agents interface")
    for key in ("display_name", "short_description", "default_prompt"):
        if not scalar(interface[1] if interface else "", key, "  "):
            fail(agent, 1, f"missing or empty agents interface.{key}")
    print(json.dumps({"root": str(root), "text_files_checked": len(texts), "local_links_checked": checked, "json_ld_blocks": sum(len(p.ld) for p in pages.values()), "errors": errors, "passed": not errors}, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
