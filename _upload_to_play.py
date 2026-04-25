# -*- coding: utf-8 -*-
"""Upload new locale store listings to Play Console via the Developer API.

Reads description_*.txt files from the app repo's `store/` directory,
parses them, and PATCHes the corresponding Play listing for each
locale. Then commits the edit.

By default, uploads ONLY locales not yet in _play_listings.json (i.e.
ko, zh-TW). Pass --all to overwrite all listings.

Source files expected at:
  ../split-screen-launcher/store/description_<code>.txt

Each file follows the format:
  【...title header...】
  Split Screen Launcher

  【...short description header...】
  <one line of ≤80 chars>

  【...full description header...】
  ...multi-line body...

  詳細: https://...   ← optional trailing URL line, stripped

Usage:
  python _upload_to_play.py            # upload missing locales only
  python _upload_to_play.py --dry-run  # parse + show what would upload
"""
import argparse
import io
import json
import re
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).parent
KEY_PATH = ROOT.parent / "notikeep-secrets" / "play-publisher.json"
APP_STORE_DIR = ROOT.parent / "split-screen-launcher" / "store"
LISTINGS_CACHE = ROOT / "_play_listings.json"

PACKAGE_NAME = "com.ryodev.splitscreen"
SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]

# (file_suffix, play_locale)
LOCALES_TO_UPLOAD = [
    ("ko",    "ko-KR"),
    ("zh-TW", "zh-TW"),
]


def parse_desc_file(path: Path):
    """Parse a 【header】+body Markdown-ish file → (title, short, full).

    The 【】 headers themselves are localized (e.g. 【앱 이름】 vs
    【應用程式名稱】). We don't try to read them; we just split on lines
    that look like '【...】' and take the body of section 1 (title),
    section 2 (short desc), section 3 (full desc).
    """
    text = path.read_text(encoding="utf-8").strip()
    bodies = re.split(r"^【[^】]+】\s*\n", text, flags=re.MULTILINE)
    bodies = [b.strip() for b in bodies if b.strip()]
    if len(bodies) < 3:
        raise ValueError(f"{path.name}: expected 3 sections, got {len(bodies)}")
    title = bodies[0].strip()
    short = bodies[1].strip()
    full = bodies[2].strip()
    # Strip trailing "詳細: https://..." style URL line if present.
    paragraphs = re.split(r"\n\s*\n", full)
    if paragraphs and "http" in paragraphs[-1] and len(paragraphs[-1]) < 200:
        paragraphs = paragraphs[:-1]
    full = "\n\n".join(paragraphs).strip()
    return title, short, full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="parse + display, no API calls")
    ap.add_argument("--all", action="store_true",
                    help="overwrite even existing listings")
    args = ap.parse_args()

    existing = {}
    if LISTINGS_CACHE.exists():
        existing = json.loads(LISTINGS_CACHE.read_text(encoding="utf-8"))

    plan = []
    for suffix, play_locale in LOCALES_TO_UPLOAD:
        src = APP_STORE_DIR / f"description_{suffix}.txt"
        if not src.exists():
            print(f"  SKIP {play_locale}: source file not found ({src})")
            continue
        if play_locale in existing and not args.all:
            print(f"  SKIP {play_locale}: already exists in Play Console (--all to overwrite)")
            continue
        try:
            title, short, full = parse_desc_file(src)
        except Exception as e:
            print(f"  ERROR {play_locale}: parse failed — {e}")
            continue
        plan.append((play_locale, title, short, full, src.name))

    if not plan:
        print("Nothing to upload.")
        return

    print(f"Plan: upload {len(plan)} locale(s)")
    for loc, t, s, f, fn in plan:
        print(f"\n--- {loc}  (from {fn}) ---")
        print(f"title:  {t!r}  (len={len(t)})")
        print(f"short:  {s!r}  (len={len(s)})")
        print(f"full:   ({len(f)} chars, {f.count(chr(10)) + 1} lines)")
        if len(s) > 80:
            print(f"  WARN: short description is {len(s)} chars (Play limit: 80)")
        if len(t) > 30:
            print(f"  WARN: title is {len(t)} chars (Play limit: 30)")
        if len(f) > 4000:
            print(f"  WARN: full description is {len(f)} chars (Play limit: 4000)")

    if args.dry_run:
        print("\n(dry run, no API calls)")
        return

    confirm = input("\nProceed with upload to Play Console? (yes/no) ").strip().lower()
    if confirm != "yes":
        print("Aborted.")
        return

    creds = service_account.Credentials.from_service_account_file(
        str(KEY_PATH), scopes=SCOPES
    )
    service = build("androidpublisher", "v3", credentials=creds, cache_discovery=False)
    edits = service.edits()
    edit = edits.insert(packageName=PACKAGE_NAME, body={}).execute()
    edit_id = edit["id"]
    print(f"opened edit {edit_id}")

    try:
        for loc, t, s, f, _ in plan:
            body = {
                "language": loc,
                "title": t,
                "shortDescription": s,
                "fullDescription": f,
            }
            edits.listings().update(
                packageName=PACKAGE_NAME,
                editId=edit_id,
                language=loc,
                body=body,
            ).execute()
            print(f"  uploaded {loc}")

        commit = edits.commit(packageName=PACKAGE_NAME, editId=edit_id).execute()
        print(f"committed edit {commit.get('id')}")
    except Exception:
        # On failure, abandon the edit so it doesn't linger.
        try:
            edits.delete(packageName=PACKAGE_NAME, editId=edit_id).execute()
            print(f"abandoned edit {edit_id} due to error")
        except Exception:
            pass
        raise


if __name__ == "__main__":
    main()
