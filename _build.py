# -*- coding: utf-8 -*-
"""Build per-locale store landing pages from _play_listings.json.

Layout produced:
  store/index.html         — English (en-US)
  store/ja/index.html      — Japanese
  store/zh-CN/index.html   — and so on for all 13 Play locales

Inputs:
  _template.html         — page template with {{PLACEHOLDERS}}
  _play_listings.json    — fetched by _fetch_from_play.py
  _strings.py            — locale list + small UI strings (CTA labels)

Also writes store/sitemap.xml.

Usage:
  python _fetch_from_play.py    # refresh listings cache
  python _build.py              # generate pages
"""
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).parent
STORE_ROOT = ROOT / "store"
TEMPLATE = (ROOT / "_template.html").read_text(encoding="utf-8")
PLAY_DATA = json.loads((ROOT / "_play_listings.json").read_text(encoding="utf-8"))

from _strings import LOCALES, UI

BASE_URL = "https://sakuradevjp.github.io/split-screen-launcher-notes"


def store_url(slug: str) -> str:
    return f"{BASE_URL}/store/" if slug == "" else f"{BASE_URL}/store/{slug}/"


def notes_url(slug: str) -> str:
    """URL of the dev-notes article for this locale (existing pages)."""
    return f"{BASE_URL}/" if slug == "" else f"{BASE_URL}/{slug}/"


def html_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


# Bullet markers seen in localized Play descriptions.
BULLET_RE = re.compile(r"^[\*\-•・·]\s*")

import unicodedata


def _is_bullet(line: str) -> bool:
    return bool(BULLET_RE.match(line.strip()))


def _strip_bullet(line: str) -> str:
    return BULLET_RE.sub("", line.strip())


def _looks_like_heading(first_line: str, has_following_content: bool) -> bool:
    """Heuristic: a leading line is a section heading when it's short,
    has body content following it, and ends without trailing punctuation
    (colon excepted). Works across en / ja / zh / ar / hi / th / etc.
    because Play Store section labels ("Common Uses", "主な機能",
    "استخدامات شائعة") are label-style with no trailing punctuation,
    while prose lines end in `.` `。` `।` `،` `、` etc."""
    if not has_following_content:
        return False
    s = first_line.strip()
    if not s or len(s) > 80:
        return False
    last = s[-1]
    if last in (":", "："):
        return True
    # Any other punctuation (Unicode category starts with "P") → prose.
    return not unicodedata.category(last).startswith("P")


def fulldesc_to_html(full_desc: str) -> str:
    """Convert Play Store fullDescription text → semantic HTML.

    Rules:
    - Blank line ⇒ block separator.
    - A block whose every non-empty line starts with a bullet marker
      becomes a <ul>. The very first such block (the "* maintained /
      * no ads" pair) gets a `lead-bullets` callout class.
    - A block where SOME lines are bullets and others aren't: the
      first non-bullet line (if it leads the block) is treated as a
      section heading <h2>; the remainder is parsed bullet-by-bullet,
      with indented continuation lines folded into the previous bullet.
    - A block with NO bullets is a single <p> (with <br> for line breaks).
      Even if the first line is short, we don't promote it to <h2>:
      Play descriptions reliably pair section headings with bulleted
      content underneath, so a no-bullet block is prose.
    """
    # Keep original raw lines (with leading whitespace) so we can detect
    # indented bullet continuations like "  EN, JA, KO, ..." under a
    # bullet point.
    raw_blocks = re.split(r"\n\s*\n", full_desc.strip("\n"))
    out_parts = []

    for i, block in enumerate(raw_blocks):
        raw_lines = [ln for ln in block.split("\n") if ln.strip()]
        if not raw_lines:
            continue

        bullet_flags = [_is_bullet(ln) for ln in raw_lines]
        any_bullet = any(bullet_flags)
        all_bullet = all(bullet_flags)

        if all_bullet:
            items = [html_escape(_strip_bullet(ln)) for ln in raw_lines]
            li_html = "\n".join(f"      <li>{x}</li>" for x in items)
            cls = ' class="lead-bullets"' if i == 0 else ""
            out_parts.append(f"    <ul{cls}>\n{li_html}\n    </ul>")
            continue

        if not any_bullet:
            # No-bullet block: still might lead with a section heading
            # ("Common Uses\n<5 use case lines>") that just happens to use
            # plain newlines instead of bullets. Promote the first line to
            # <h2> only if it looks like a label, not a sentence.
            if _looks_like_heading(raw_lines[0], has_following_content=len(raw_lines) > 1):
                heading = html_escape(raw_lines[0].strip())
                out_parts.append(f"    <h2>{heading}</h2>")
                rest_text = "<br>".join(html_escape(ln.strip()) for ln in raw_lines[1:])
                out_parts.append(f"    <p>{rest_text}</p>")
            else:
                text = "<br>".join(html_escape(ln.strip()) for ln in raw_lines)
                out_parts.append(f"    <p>{text}</p>")
            continue

        # Mixed block: first non-bullet line at the top is a section heading.
        idx = 0
        if not bullet_flags[0] and _looks_like_heading(
            raw_lines[0], has_following_content=len(raw_lines) > 1
        ):
            heading = html_escape(raw_lines[0].strip())
            out_parts.append(f"    <h2>{heading}</h2>")
            idx = 1

        # Walk the rest, folding indented non-bullet lines into the previous bullet.
        buf_bullets = []   # list[str] — pending bullet item texts
        buf_para = []      # list[str] — pending paragraph lines

        def flush_bullets():
            if buf_bullets:
                li_html = "\n".join(f"      <li>{html_escape(b)}</li>" for b in buf_bullets)
                out_parts.append(f"    <ul>\n{li_html}\n    </ul>")
                buf_bullets.clear()

        def flush_para():
            if buf_para:
                text = "<br>".join(html_escape(p) for p in buf_para)
                out_parts.append(f"    <p>{text}</p>")
                buf_para.clear()

        for ln in raw_lines[idx:]:
            if _is_bullet(ln):
                flush_para()
                buf_bullets.append(_strip_bullet(ln))
            elif ln.startswith((" ", "\t")) and buf_bullets:
                # Indented continuation of the previous bullet.
                buf_bullets[-1] += " " + ln.strip()
            else:
                flush_bullets()
                buf_para.append(ln.strip())
        flush_bullets()
        flush_para()

    return "\n".join(out_parts)


def hreflang_block() -> str:
    lines = []
    for _, slug, hreflang, _, _, _ in LOCALES:
        lines.append(f'<link rel="alternate" hreflang="{hreflang}" href="{store_url(slug)}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{store_url("")}">')
    return "\n".join(lines)


def lang_switcher(current_slug: str) -> str:
    parts = []
    for _, slug, _, name, _, _ in LOCALES:
        if slug == current_slug:
            parts.append(f'<strong>{name}</strong>')
        else:
            parts.append(f'<a href="{store_url(slug)}">{name}</a>')
    return "\n    ".join(parts)


def asset_base(slug: str) -> str:
    """Path from store/{slug}/index.html → assets/."""
    if slug == "":
        # store/index.html → ../assets/
        return "../assets/"
    # store/<slug>/index.html → ../../assets/
    return "../../assets/"


_NOTES_URL_LINE = re.compile(
    r"^[^\n]*https?://sakuradevjp\.github\.io/split-screen-launcher-notes/[^\n]*$",
    re.M,
)


def _strip_notes_url(full: str) -> str:
    """Drop trailing 'More info: <notes URL>' line — redundant on the
    landing page itself, and the build otherwise renders it as a bare
    <p> with a raw URL."""
    return _NOTES_URL_LINE.sub("", full).rstrip("\n") + "\n"


def build_locale(play_locale, slug, hreflang, _name, direction, play_hl):
    if play_locale not in PLAY_DATA:
        print(f"  SKIP {play_locale}: missing in _play_listings.json")
        return None

    data = PLAY_DATA[play_locale]
    title = data.get("title", "Split Screen Launcher")
    short = data.get("shortDescription", "")
    full = _strip_notes_url(data.get("fullDescription", ""))

    body_html = fulldesc_to_html(full)
    ui = UI.get(hreflang, UI["en"])

    subs = {
        "LANG_ATTR": hreflang,
        "DIR_ATTR": ' dir="rtl"' if direction == "rtl" else "",
        "TITLE": html_escape(title),
        "SHORT_DESC": html_escape(short),
        "BODY_HTML": body_html,
        "CANONICAL_URL": store_url(slug),
        "HREFLANG_LINKS": hreflang_block(),
        "LANG_SWITCHER": lang_switcher(slug),
        "ASSET_BASE": asset_base(slug),
        "PLAY_HL": play_hl,
        "NOTES_LINK": notes_url(slug),
        "CTA_GET": html_escape(ui["CTA_GET"]),
        "CTA_NOTES": html_escape(ui["CTA_NOTES"]),
        "FINAL_CTA_LEAD": html_escape(ui["FINAL_CTA_LEAD"]),
    }

    out = TEMPLATE
    for k, v in subs.items():
        out = out.replace(f"{{{{{k}}}}}", v)

    leftover = re.findall(r"\{\{[A-Z0-9_]+\}\}", out)
    if leftover:
        print(f"  ! {hreflang}: unsubstituted placeholders: {set(leftover)}")

    if slug == "":
        target = STORE_ROOT / "index.html"
    else:
        target = STORE_ROOT / slug / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(out, encoding="utf-8")
    print(f"  wrote {target.relative_to(ROOT)} ({len(out)} chars, body {len(body_html)} chars)")
    return slug


def write_sitemap(slugs):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    for slug in slugs:
        priority = "1.0" if slug == "" else "0.8"
        lines.append("  <url>")
        lines.append(f"    <loc>{store_url(slug)}</loc>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        for _, sub, hl, _, _, _ in LOCALES:
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{store_url(sub)}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{store_url("")}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    sitemap_path = STORE_ROOT / "sitemap.xml"
    sitemap_path.parent.mkdir(parents=True, exist_ok=True)
    sitemap_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote store/sitemap.xml ({len(slugs)} URLs)")


def main():
    STORE_ROOT.mkdir(exist_ok=True)
    written = []
    for entry in LOCALES:
        slug = build_locale(*entry)
        if slug is not None:
            written.append(slug)
    write_sitemap(written)
    print(f"\nDone. {len(written)} locale pages written under store/.")


if __name__ == "__main__":
    main()
