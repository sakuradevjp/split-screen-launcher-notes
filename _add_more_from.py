# -*- coding: utf-8 -*-
"""One-shot: insert 'More from sakuradev' cross-promo block before <footer>
in each /store/<locale>/index.html. Idempotent — skips files that already
contain the marker.
"""
from pathlib import Path

ROOT = Path(__file__).parent / "store"

# (locale-dir, dir, more_from_label, notikeep_blurb, all_apps_label, all_apps_blurb)
LOCALES = [
    ("ja",    "ltr", "sakuradev のその他のアプリ",     "Android の通知をすべて保存 — 写真も含めて",            "sakuradev の全アプリ",              "Windows と Android のインディーアプリ"),
    ("ko",    "ltr", "sakuradev의 다른 앱",           "모든 Android 알림 저장 — 사진 포함",                    "sakuradev의 모든 앱",               "Windows 및 Android용 인디 앱"),
    ("zh-CN", "ltr", "sakuradev 的更多应用",          "保存每条 Android 通知 — 包括图片",                      "sakuradev 的所有应用",              "面向 Windows 和 Android 的独立应用"),
    ("zh-TW", "ltr", "sakuradev 的更多應用",          "儲存每則 Android 通知 — 包含圖片",                      "sakuradev 的所有應用",              "適用於 Windows 與 Android 的獨立應用"),
    ("es",    "ltr", "Más de sakuradev",              "Guarda cada notificación de Android — incluidas las fotos", "Todas las apps de sakuradev",   "Apps indie para Windows y Android"),
    ("pt-BR", "ltr", "Mais de sakuradev",             "Salve cada notificação do Android — fotos incluídas",   "Todos os apps de sakuradev",        "Apps indie para Windows e Android"),
    ("fr",    "ltr", "Plus de sakuradev",             "Enregistrez chaque notification Android — photos incluses", "Toutes les apps de sakuradev",  "Apps indé pour Windows et Android"),
    ("de",    "ltr", "Mehr von sakuradev",            "Jede Android-Benachrichtigung speichern — inkl. Fotos", "Alle Apps von sakuradev",           "Indie-Apps für Windows & Android"),
    ("it",    "ltr", "Altro da sakuradev",            "Salva ogni notifica Android — foto incluse",            "Tutte le app di sakuradev",         "App indie per Windows e Android"),
    ("ru",    "ltr", "Ещё от sakuradev",              "Сохраняйте каждое уведомление Android — включая фото",  "Все приложения sakuradev",          "Инди-приложения для Windows и Android"),
    ("ar",    "rtl", "المزيد من sakuradev",           "احفظ كل إشعار في Android — بما في ذلك الصور",            "جميع تطبيقات sakuradev",            "تطبيقات مستقلة لنظامي Windows و Android"),
    ("hi",    "ltr", "sakuradev से और",                "हर Android सूचना सहेजें — फ़ोटो सहित",                      "sakuradev के सभी ऐप",                "Windows और Android के लिए इंडी ऐप"),
    ("th",    "ltr", "เพิ่มเติมจาก sakuradev",          "บันทึกการแจ้งเตือน Android ทุกรายการ — รวมถึงรูปภาพ",        "แอปทั้งหมดของ sakuradev",            "แอปอินดี้สำหรับ Windows และ Android"),
    ("vi",    "ltr", "Thêm từ sakuradev",             "Lưu mọi thông báo Android — bao gồm cả ảnh",            "Tất cả ứng dụng của sakuradev",     "Ứng dụng indie cho Windows & Android"),
]

MARKER = 'aria-label="More from sakuradev"'

BLOCK_TEMPLATE = """<section style="max-width:760px;margin:1rem auto 2rem;padding:2rem 16px 0;border-top:1px solid var(--border,#e6e6ee)" aria-label="More from sakuradev">
  <p style="font-size:.95rem;text-align:center;margin:0 0 1.25rem;color:var(--text-muted,#4a4a5e);letter-spacing:.08em;text-transform:uppercase;font-weight:600">{more_from}</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:.75rem;max-width:640px;margin:0 auto">
    <a href="https://sakuradevjp.github.io/notikeep-notes/" style="display:flex;align-items:center;gap:.85rem;background:var(--card,#f7f7fb);border:1px solid var(--border,#e6e6ee);border-radius:12px;padding:.9rem 1.1rem;text-decoration:none;color:inherit">
      <img src="https://sakuradevjp.github.io/notikeep.svg" alt="" width="32" height="32" style="flex-shrink:0;border-radius:6px;display:block;background:#fff">
      <span style="line-height:1.4"><strong style="display:block;color:var(--text,#1a1a2e);font-size:.98rem">NotiKeep</strong><span style="color:var(--text-muted,#4a4a5e);font-size:.86rem">{notikeep_blurb}</span></span>
    </a>
    <a href="https://sakuradevjp.github.io/" style="display:flex;align-items:center;gap:.85rem;background:var(--card,#f7f7fb);border:1px solid var(--border,#e6e6ee);border-radius:12px;padding:.9rem 1.1rem;text-decoration:none;color:inherit">
      <img src="https://sakuradevjp.github.io/avatar.png" alt="" width="32" height="32" style="flex-shrink:0;border-radius:6px;display:block;background:#fff">
      <span style="line-height:1.4"><strong style="display:block;color:var(--text,#1a1a2e);font-size:.98rem">{all_apps}</strong><span style="color:var(--text-muted,#4a4a5e);font-size:.86rem">{all_apps_blurb}</span></span>
    </a>
  </div>
</section>

"""

INSERT_BEFORE = "<footer>"

def main():
    for slug, _direction, more_from, notikeep_blurb, all_apps, all_apps_blurb in LOCALES:
        path = ROOT / slug / "index.html"
        if not path.exists():
            print(f"SKIP missing: {path}")
            continue
        html = path.read_text(encoding="utf-8")
        if MARKER in html:
            print(f"SKIP already has marker: {path}")
            continue
        block = BLOCK_TEMPLATE.format(
            more_from=more_from,
            notikeep_blurb=notikeep_blurb,
            all_apps=all_apps,
            all_apps_blurb=all_apps_blurb,
        )
        new_html = html.replace(INSERT_BEFORE, block + INSERT_BEFORE, 1)
        if new_html == html:
            print(f"FAIL no <footer> found: {path}")
            continue
        path.write_text(new_html, encoding="utf-8")
        print(f"OK {path}")

if __name__ == "__main__":
    main()
