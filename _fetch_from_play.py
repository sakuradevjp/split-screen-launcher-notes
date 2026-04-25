# -*- coding: utf-8 -*-
"""Fetch Play Store listings (all locales) for Split Screen Launcher.

Uses the Google Play Developer API (androidpublisher v3). Service-account
key lives outside the repo at ../notikeep-secrets/play-publisher.json
(same key has Play Console access to both NotiKeep and Split Screen
Launcher).

Output: writes _play_listings.json next to this script. The JSON has shape:
  { "en-US": {"title": "...", "shortDescription": "...", "fullDescription": "..."},
    "ja-JP": {...}, ... }

Usage: python _fetch_from_play.py
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
OUT_PATH = ROOT / "_play_listings.json"

PACKAGE_NAME = "com.ryodev.splitscreen"
SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]


def main():
    if not KEY_PATH.exists():
        print(f"ERROR: credential not found at {KEY_PATH}")
        sys.exit(1)

    creds = service_account.Credentials.from_service_account_file(
        str(KEY_PATH), scopes=SCOPES
    )
    service = build("androidpublisher", "v3", credentials=creds, cache_discovery=False)

    edits = service.edits()
    edit = edits.insert(packageName=PACKAGE_NAME, body={}).execute()
    edit_id = edit["id"]
    print(f"opened edit {edit_id}")

    try:
        resp = edits.listings().list(
            packageName=PACKAGE_NAME, editId=edit_id
        ).execute()
        listings = resp.get("listings", [])
        print(f"got {len(listings)} listings")

        out = {}
        for L in listings:
            lang = L.get("language")
            out[lang] = {
                "title": L.get("title", ""),
                "shortDescription": L.get("shortDescription", ""),
                "fullDescription": L.get("fullDescription", ""),
                "video": L.get("video", ""),
            }
            print(f"  {lang}: {len(out[lang]['fullDescription'])} chars")

        OUT_PATH.write_text(
            json.dumps(out, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"wrote {OUT_PATH.name} ({len(out)} locales)")
    finally:
        # Don't commit — just abandon the edit (read-only fetch)
        try:
            edits.delete(packageName=PACKAGE_NAME, editId=edit_id).execute()
            print(f"closed edit {edit_id}")
        except Exception as e:
            print(f"warn: failed to close edit: {e}")


if __name__ == "__main__":
    main()
