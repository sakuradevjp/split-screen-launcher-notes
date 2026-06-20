# -*- coding: utf-8 -*-
"""Per-locale UI strings for the Split Screen Launcher store landing pages.

Body text (title / shortDescription / fullDescription) comes from the Play
Store listings via _play_listings.json — see _fetch_from_play.py.

Only the small UI bits live here (CTA button labels, "Read the dev notes"
link text, final CTA tagline). Keep these short.
"""

# Maps Play Store locale → web URL slug + hreflang code + display name.
# Order here is the order languages appear in the language switcher.
LOCALES = [
    # (play_locale, slug, hreflang, display_name, dir, play_hl)
    ("en-US",  "",       "en",     "English",          "ltr", "en"),
    ("ja-JP",  "ja",     "ja",     "日本語",            "ltr", "ja"),
    ("ko-KR",  "ko",     "ko",     "한국어",            "ltr", "ko"),
    ("zh-CN",  "zh-CN",  "zh-CN",  "简体中文",          "ltr", "zh-CN"),
    ("zh-TW",  "zh-TW",  "zh-TW",  "繁體中文",          "ltr", "zh-TW"),
    ("es-419", "es",     "es",     "Español",          "ltr", "es"),
    ("pt-BR",  "pt-BR",  "pt-BR",  "Português (BR)",   "ltr", "pt-BR"),
    ("fr-FR",  "fr",     "fr",     "Français",         "ltr", "fr"),
    ("de-DE",  "de",     "de",     "Deutsch",          "ltr", "de"),
    ("it-IT",  "it",     "it",     "Italiano",         "ltr", "it"),
    ("ru-RU",  "ru",     "ru",     "Русский",          "ltr", "ru"),
    ("ar",     "ar",     "ar",     "العربية",            "rtl", "ar"),
    ("hi-IN",  "hi",     "hi",     "हिन्दी",              "ltr", "hi"),
    ("th",     "th",     "th",     "ไทย",               "ltr", "th"),
    ("vi",     "vi",     "vi",     "Tiếng Việt",        "ltr", "vi"),
]

# Small UI strings keyed by hreflang code.
UI = {
    "en":    {"CTA_GET": "Get it on Google Play", "CTA_NOTES": "Developer notes",   "FINAL_CTA_LEAD": "Free, no ads. Try it on Google Play.",
              "REVIEWS_HEADING": "What users say", "REVIEWS_SOURCE": "via Google Play", "VIDEO_HEADING": "See it in action"},
    "ja":    {"CTA_GET": "Google Play で入手",     "CTA_NOTES": "開発者ノート",        "FINAL_CTA_LEAD": "無料・広告なし。Google Play で試してみてください。",
              "REVIEWS_HEADING": "ユーザーの声",     "REVIEWS_SOURCE": "Google Play より", "VIDEO_HEADING": "デモを見る"},
    "ko":    {"CTA_GET": "Google Play에서 받기",    "CTA_NOTES": "개발자 노트",         "FINAL_CTA_LEAD": "무료, 광고 없음. Google Play에서 시도해 보세요.",
              "REVIEWS_HEADING": "사용자 리뷰",      "REVIEWS_SOURCE": "Google Play에서", "VIDEO_HEADING": "데모 영상"},
    "zh-TW": {"CTA_GET": "在 Google Play 取得",   "CTA_NOTES": "開發者筆記",          "FINAL_CTA_LEAD": "免費,無廣告。在 Google Play 試試看。",
              "REVIEWS_HEADING": "使用者評論",      "REVIEWS_SOURCE": "來自 Google Play", "VIDEO_HEADING": "觀看示範影片"},
    "zh-CN": {"CTA_GET": "在 Google Play 获取",   "CTA_NOTES": "开发者笔记",          "FINAL_CTA_LEAD": "免费,无广告。在 Google Play 试试看。",
              "REVIEWS_HEADING": "用户评价",        "REVIEWS_SOURCE": "来自 Google Play", "VIDEO_HEADING": "观看演示视频"},
    "es":    {"CTA_GET": "Obtener en Google Play","CTA_NOTES": "Notas del desarrollador","FINAL_CTA_LEAD": "Gratis, sin anuncios. Pruébalo en Google Play.",
              "REVIEWS_HEADING": "Lo que dicen los usuarios", "REVIEWS_SOURCE": "vía Google Play", "VIDEO_HEADING": "Míralo en acción"},
    "pt-BR": {"CTA_GET": "Baixar no Google Play", "CTA_NOTES": "Notas do desenvolvedor","FINAL_CTA_LEAD": "Grátis, sem anúncios. Experimente no Google Play.",
              "REVIEWS_HEADING": "O que os usuários dizem", "REVIEWS_SOURCE": "via Google Play", "VIDEO_HEADING": "Veja em ação"},
    "fr":    {"CTA_GET": "Obtenir sur Google Play","CTA_NOTES": "Notes du développeur","FINAL_CTA_LEAD": "Gratuit, sans publicité. Essayez sur Google Play.",
              "REVIEWS_HEADING": "Ce que disent les utilisateurs", "REVIEWS_SOURCE": "via Google Play", "VIDEO_HEADING": "Voir la démo"},
    "de":    {"CTA_GET": "Auf Google Play laden", "CTA_NOTES": "Entwickler-Notizen",  "FINAL_CTA_LEAD": "Kostenlos, ohne Werbung. Auf Google Play ausprobieren.",
              "REVIEWS_HEADING": "Was Nutzer sagen", "REVIEWS_SOURCE": "via Google Play", "VIDEO_HEADING": "Im Einsatz sehen"},
    "it":    {"CTA_GET": "Scarica su Google Play","CTA_NOTES": "Note dello sviluppatore","FINAL_CTA_LEAD": "Gratis, senza pubblicità. Provalo su Google Play.",
              "REVIEWS_HEADING": "Cosa dicono gli utenti", "REVIEWS_SOURCE": "via Google Play", "VIDEO_HEADING": "Guardalo in azione"},
    "ru":    {"CTA_GET": "Установить из Google Play","CTA_NOTES": "Заметки разработчика","FINAL_CTA_LEAD": "Бесплатно, без рекламы. Попробуйте в Google Play.",
              "REVIEWS_HEADING": "Отзывы пользователей", "REVIEWS_SOURCE": "из Google Play", "VIDEO_HEADING": "Смотрите в действии"},
    "ar":    {"CTA_GET": "احصل عليه من Google Play","CTA_NOTES": "ملاحظات المطور",     "FINAL_CTA_LEAD": "مجاني وبدون إعلانات. جرّبه على Google Play.",
              "REVIEWS_HEADING": "آراء المستخدمين", "REVIEWS_SOURCE": "من Google Play", "VIDEO_HEADING": "شاهده أثناء العمل"},
    "hi":    {"CTA_GET": "Google Play से प्राप्त करें","CTA_NOTES": "डेवलपर नोट्स",       "FINAL_CTA_LEAD": "मुफ़्त, कोई विज्ञापन नहीं। Google Play पर आज़माएं।",
              "REVIEWS_HEADING": "उपयोगकर्ता क्या कहते हैं", "REVIEWS_SOURCE": "Google Play से", "VIDEO_HEADING": "डेमो देखें"},
    "th":    {"CTA_GET": "ดาวน์โหลดบน Google Play","CTA_NOTES": "บันทึกของนักพัฒนา",   "FINAL_CTA_LEAD": "ฟรี ไม่มีโฆษณา ลองใช้บน Google Play",
              "REVIEWS_HEADING": "เสียงจากผู้ใช้", "REVIEWS_SOURCE": "จาก Google Play", "VIDEO_HEADING": "ดูการสาธิต"},
    "vi":    {"CTA_GET": "Tải trên Google Play",  "CTA_NOTES": "Ghi chú nhà phát triển","FINAL_CTA_LEAD": "Miễn phí, không quảng cáo. Hãy thử trên Google Play.",
              "REVIEWS_HEADING": "Người dùng nói gì", "REVIEWS_SOURCE": "qua Google Play", "VIDEO_HEADING": "Xem video demo"},
}
