# -*- coding: utf-8 -*-
"""Upload _play_listings.json contents to Play Console (all 15 locales).

Mirror of _fetch_from_play.py: opens an edit, pushes listings.update() for
each locale present in _play_listings.json, then commits the edit. Existing
fields not present in the JSON (e.g. video URL) are preserved.

Usage: python _upload_to_play.py
"""
import io
import json
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).parent
KEY_PATH = ROOT.parent / "notikeep-secrets" / "play-publisher.json"
IN_PATH = ROOT / "_play_listings.json"

PACKAGE_NAME = "com.ryodev.splitscreen"
SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]


def main():
    if not KEY_PATH.exists():
        print(f"ERROR: credential not found at {KEY_PATH}")
        sys.exit(1)
    if not IN_PATH.exists():
        print(f"ERROR: input not found at {IN_PATH}")
        sys.exit(1)

    listings_local = json.loads(IN_PATH.read_text(encoding="utf-8"))
    print(f"loaded {len(listings_local)} locales from {IN_PATH.name}")

    creds = service_account.Credentials.from_service_account_file(
        str(KEY_PATH), scopes=SCOPES
    )
    service = build("androidpublisher", "v3", credentials=creds, cache_discovery=False)

    edits = service.edits()
    edit = edits.insert(packageName=PACKAGE_NAME, body={}).execute()
    edit_id = edit["id"]
    print(f"opened edit {edit_id}")

    committed = False
    try:
        for lang, info in listings_local.items():
            body = {
                "language": lang,
                "title": info.get("title", ""),
                "shortDescription": info.get("shortDescription", ""),
                "fullDescription": info.get("fullDescription", ""),
            }
            video = info.get("video", "")
            if video:
                body["video"] = video
            edits.listings().update(
                packageName=PACKAGE_NAME,
                editId=edit_id,
                language=lang,
                body=body,
            ).execute()
            print(f"  pushed {lang} ({len(body['fullDescription'])} chars)")

        edits.commit(packageName=PACKAGE_NAME, editId=edit_id).execute()
        committed = True
        print(f"committed edit {edit_id}")
    finally:
        if not committed:
            try:
                edits.delete(packageName=PACKAGE_NAME, editId=edit_id).execute()
                print(f"abandoned edit {edit_id}")
            except Exception as e:
                print(f"warn: failed to abandon edit: {e}")


if __name__ == "__main__":
    main()
