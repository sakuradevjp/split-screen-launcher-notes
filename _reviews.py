# -*- coding: utf-8 -*-
"""Curated user testimonials from Google Play reviews.

Each entry has:
  - id            stable slug
  - reviewer      display name (rounded for privacy: "Nurudeen E.")
  - device        device model (or None when unknown)
  - android       Android version label (e.g. "Android 14") — shown in
                  the card header next to the reviewer and device
  - rating        integer 1–5
  - date          ISO date "YYYY-MM-DD"; per-locale formatting happens
                  in _build.py
  - original_lang language code of original_text (matches hreflang slugs
                  used in _strings.LOCALES, plus "az" for Azerbaijani)
  - original_text the user's words, verbatim
  - translations  dict mapping hreflang → AI-translated text

The build only renders, per page, up to three versions of each review:
  1. original  2. English (if original isn't English & page isn't original)
  3. page's language  (deduped).
"""

from datetime import date as _date

# Language name in its own language (autoglottonym), used as the small
# label above each quote variant. Keys must match original_lang values
# and hreflang codes in _strings.LOCALES.
LANG_NAMES = {
    "en":    "English",
    "ja":    "日本語",
    "ko":    "한국어",
    "zh-CN": "简体中文",
    "zh-TW": "繁體中文",
    "es":    "Español",
    "pt-BR": "Português",
    "fr":    "Français",
    "de":    "Deutsch",
    "it":    "Italiano",
    "ru":    "Русский",
    "ar":    "العربية",
    "hi":    "हिन्दी",
    "th":    "ไทย",
    "vi":    "Tiếng Việt",
    "az":    "Azərbaycanca",
    "nl":    "Nederlands",
}


REVIEWS = [
    {
        "id": "dipesh_2026_05_30",
        "reviewer": "Dipesh N.",
        "device": None,  # Android CarPlay AI Box (not a Play-listed device)
        "android": None,  # Play Console returned no androidOsVersion
        "rating": 5,
        "date": _date(2026, 5, 30),
        "original_lang": "en",
        "original_text": (
            "I just purchased this app after trying out a few other apps "
            "(that did not work). I sure am glad I got it. I run this app "
            "in my BYD Sealion 7 android car play AI box and it works as "
            "promised. No complex handling. Plain and simple pairing of "
            "any apps. I normally run maps with Spotify and when my wife "
            "is in the passenger seat, I run maps with Netflix (for her). "
            "Kudos to you for creating this wonderful app. Keep updating. "
            "Thanks"
        ),
        "translations": {
            "ja": (
                "他のアプリをいくつか試して(どれも動かなかった)からこのアプリを購入しました。"
                "買って本当によかった。BYD Sealion 7 の Android CarPlay AI Box で"
                "動かしてるんですが、書かれた通りに動きます。複雑な操作は一切なし、"
                "どんなアプリでもシンプルにペアにできる。普段は地図と Spotify、"
                "助手席に妻が乗っているときは地図と Netflix (妻用)。"
                "素晴らしいアプリを作ってくれてありがとう。これからもアップデート続けてください。"
            ),
            "ko": (
                "다른 앱을 몇 개 시도해 본 뒤(전부 작동하지 않았어요) 이 앱을 구입했어요. "
                "사길 정말 잘했다 싶습니다. 제 BYD Sealion 7의 Android CarPlay AI Box에서 "
                "돌리는데, 약속한 대로 작동합니다. 복잡한 조작은 없고, 어떤 앱이든 "
                "그냥 간단하게 페어로 묶을 수 있어요. 평소엔 지도 + Spotify, 조수석에 "
                "아내가 있을 때는 지도 + Netflix(아내용)로 씁니다. 멋진 앱을 만들어 "
                "주셔서 감사합니다. 계속 업데이트 부탁드려요. 고맙습니다."
            ),
            "zh-CN": (
                "试了几个别的 app 都不行，然后买了这个。买对了。我在 BYD 海狮 07 的 "
                "Android CarPlay AI Box 上跑这个 app，效果跟介绍的一样。完全没有复杂的"
                "操作，任何应用都能简单地配对。我平时用地图 + Spotify，老婆坐副驾时就用"
                "地图 + Netflix（给她看）。感谢你们做出这么棒的 app。请继续更新。谢谢。"
            ),
            "zh-TW": (
                "試了幾個別的 app 都不行，然後買了這個。買對了。我在 BYD Sealion 7 的 "
                "Android CarPlay AI Box 上跑這個 app，效果跟介紹的一樣。完全沒有複雜的"
                "操作，任何應用都能簡單地配對。我平常用地圖 + Spotify，老婆坐副駕時就用"
                "地圖 + Netflix（給她看）。感謝你們做出這麼棒的 app。請繼續更新。謝謝。"
            ),
            "es": (
                "Después de probar otras apps (que no funcionaron) compré esta. Y qué "
                "bien hice. La uso en el AI Box de Android CarPlay de mi BYD Sealion 7 "
                "y funciona como prometen. Sin nada complicado, simplemente puedes "
                "emparejar cualquier app. Yo suelo poner mapas con Spotify, y cuando "
                "mi esposa va de copiloto, mapas con Netflix (para ella). Mil gracias "
                "por crear esta gran app. Sigan actualizando. Gracias."
            ),
            "pt-BR": (
                "Depois de testar outros apps (que não funcionaram), comprei este. E "
                "que bom que comprei. Rodo ele no AI Box do Android CarPlay do meu BYD "
                "Sealion 7 e funciona como prometido. Nada complicado, é só emparelhar "
                "qualquer app, de forma simples. Geralmente uso mapas com Spotify, e "
                "quando minha esposa está no banco do passageiro, mapas com Netflix "
                "(pra ela). Parabéns por criar esse app maravilhoso. Continuem "
                "atualizando. Obrigado."
            ),
            "fr": (
                "Après avoir essayé d'autres applis (qui ne marchaient pas), j'ai "
                "acheté celle-ci. Je suis bien content de l'avoir prise. Je l'utilise "
                "sur l'AI Box Android CarPlay de ma BYD Sealion 7 et elle fonctionne "
                "comme promis. Aucune manipulation compliquée, on jumelle simplement "
                "n'importe quelles applis. D'habitude j'utilise cartes + Spotify, et "
                "quand ma femme est sur le siège passager, cartes + Netflix (pour "
                "elle). Bravo pour cette super appli. Continuez à la mettre à jour. "
                "Merci."
            ),
            "de": (
                "Nach ein paar anderen Apps (die nicht funktionierten) habe ich diese "
                "gekauft. Und das war eine gute Entscheidung. Ich nutze sie auf der "
                "Android-CarPlay-AI-Box in meinem BYD Sealion 7 und sie funktioniert "
                "genau wie versprochen. Keine komplizierte Bedienung, einfach "
                "beliebige Apps koppeln. Normalerweise nutze ich Karten + Spotify, "
                "und wenn meine Frau auf dem Beifahrersitz sitzt, Karten + Netflix "
                "(für sie). Vielen Dank für diese großartige App. Bitte weiter "
                "updaten. Danke."
            ),
            "it": (
                "Dopo aver provato altre app (che non funzionavano) ho comprato "
                "questa. Sono davvero contento di averlo fatto. La uso sull'AI Box "
                "Android CarPlay della mia BYD Sealion 7 e funziona come promesso. "
                "Nessuna gestione complicata, basta abbinare qualunque app. Di solito "
                "uso mappe + Spotify, e quando mia moglie è sul sedile passeggero, "
                "mappe + Netflix (per lei). Complimenti per questa fantastica app. "
                "Continuate ad aggiornarla. Grazie."
            ),
            "ru": (
                "После того как попробовал ещё пару приложений (которые не заработали), "
                "купил это. И очень рад, что купил. Использую его на Android CarPlay "
                "AI Box в моей BYD Sealion 7, и оно работает как обещано. Никаких "
                "сложных настроек, просто пара любых приложений. Обычно у меня карты "
                "+ Spotify, а когда жена на пассажирском сиденье — карты + Netflix "
                "(для неё). Огромное спасибо за такое прекрасное приложение. "
                "Продолжайте обновлять. Спасибо."
            ),
            "ar": (
                "بعد أن جرّبت بضع تطبيقات أخرى (لم تعمل) اشتريت هذا التطبيق. وأنا "
                "سعيد جدًا أنني فعلت. أشغّله على جهاز Android CarPlay AI Box في "
                "سيارتي BYD Sealion 7 ويعمل كما هو موعود. لا توجد إعدادات معقدة، "
                "فقط إقران بسيط لأي تطبيقات. عادةً أشغّل الخرائط مع Spotify، وعندما "
                "تكون زوجتي في مقعد الراكب، الخرائط مع Netflix (لها). شكرًا لكم "
                "على هذا التطبيق الرائع. واصلوا التحديثات. شكرًا."
            ),
            "hi": (
                "कुछ और apps आज़माने के बाद (जो काम नहीं किए), मैंने यह app खरीदा। और सच "
                "में, खरीदा अच्छा किया। मैं इसे अपनी BYD Sealion 7 के Android CarPlay "
                "AI Box में चलाता हूँ — जैसा बताया गया था, वैसा ही चलता है। कोई पेचीदा "
                "सेटिंग नहीं, बस किसी भी app को आसानी से pair कर लो। आम तौर पर मैं "
                "Maps + Spotify, और जब पत्नी पैसेंजर सीट पर हो तो Maps + Netflix "
                "(उनके लिए)। इतना बढ़िया app बनाने के लिए शुक्रिया। updates जारी रखें। "
                "धन्यवाद।"
            ),
            "th": (
                "หลังจากที่ลองแอปอื่นไม่กี่ตัว (ใช้ไม่ได้) ผมก็ซื้อแอปนี้ ดีใจมากที่ซื้อ "
                "ผมใช้บน Android CarPlay AI Box ใน BYD Sealion 7 ของผม ทำงานตามที่บอกไว้เป๊ะ "
                "ไม่มีอะไรซับซ้อน แค่จับคู่แอปไหนก็ได้ง่ายๆ ปกติผมใช้แผนที่ + Spotify "
                "และเมื่อภรรยานั่งข้างจะใช้แผนที่ + Netflix (สำหรับเธอ) ขอบคุณที่ทำแอป"
                "ดีๆ แบบนี้ อัปเดตต่อไปนะครับ ขอบคุณครับ"
            ),
            "vi": (
                "Sau khi thử vài app khác (đều không chạy được), mình đã mua app này. "
                "Mua xong thấy đúng đắn lắm. Mình chạy trên AI Box Android CarPlay "
                "của xe BYD Sealion 7, và app chạy đúng như quảng cáo. Không thao "
                "tác phức tạp gì cả, cứ thế ghép cặp bất kỳ app nào. Bình thường "
                "mình dùng Maps + Spotify, còn khi vợ ngồi ghế phụ thì Maps + Netflix "
                "(cho vợ). Cảm ơn rất nhiều vì đã làm ra app tuyệt vời này. Mong "
                "tiếp tục cập nhật. Cảm ơn."
            ),
        },
    },

    {
        "id": "nurudeen_2026_04_03",
        "reviewer": "Nurudeen E.",
        "device": "Redmi 12C",
        "android": "Android 14",
        "rating": 5,
        "date": _date(2026, 4, 3),
        "original_lang": "en",
        "original_text": (
            "This is the best app in its category. I just tested several "
            "similar apps and they all require you sacrifice your soul and "
            "they don't even work reliably. Then I stumbled upon this and "
            "it just works. No questions asked, no unnecessary permissions "
            "request and it works completely offline. Big thank you to the "
            "developers. For anyone finding it difficult to make it work "
            "with whatsapp, just make the whatsapp app be at the bottom. "
            "I find that to work for me."
        ),
        "translations": {
            "ja": (
                "同カテゴリで最高のアプリ。似たアプリをいくつか試したけど、"
                "どれも魂を売れと言わんばかりで、しかもまともに動かない。"
                "そこで偶然見つけたのがこれ。とにかく、ちゃんと動く。"
                "質問もなし、不要な権限要求もなし、完全オフラインで動作する。"
                "開発者に心からの感謝を。WhatsAppと組み合わせがうまくいかない人は、"
                "WhatsAppを下に置くといい。私はそれでうまくいった。"
            ),
            "ko": (
                "같은 카테고리에서 최고의 앱. 비슷한 앱 몇 개를 시험해 봤는데, "
                "다들 영혼을 팔라는 수준이고 안정적으로 작동하지도 않았다. "
                "그러다 우연히 이걸 발견했는데, 그냥 잘 된다. 묻는 것도 없고, "
                "불필요한 권한 요청도 없고, 완전히 오프라인으로 작동한다. "
                "개발자분께 진심으로 감사. WhatsApp과 조합이 잘 안 되는 분은 "
                "WhatsApp을 아래쪽에 놓아 보세요. 저는 그렇게 해서 잘 됐습니다."
            ),
            "zh-CN": (
                "这是同类应用里最好的一个。我刚试了几个类似的应用，每一个都要让你"
                "出卖灵魂，而且还不稳定。后来偶然发现了这款，它就是能用。不问东问西，"
                "不要求多余权限，完全离线也能工作。非常感谢开发者。如果 WhatsApp "
                "总是用不顺，把 WhatsApp 放到下面试试。我就是这样搞定的。"
            ),
            "zh-TW": (
                "這是同類應用裡最好的一個。我剛試了幾個類似的應用，每一個都要你"
                "出賣靈魂，而且還不穩定。後來偶然發現了這款，它就是能用。不問東問西，"
                "不要求多餘權限，完全離線也能運作。非常感謝開發者。如果 WhatsApp "
                "總是用不順，把 WhatsApp 放到下面試試。我就是這樣搞定的。"
            ),
            "es": (
                "Es la mejor app de su categoría. Probé varias parecidas y todas "
                "te piden venderles el alma, y ni siquiera funcionan bien. Después "
                "di con esta y simplemente funciona. Sin preguntas, sin permisos "
                "innecesarios, totalmente offline. Mil gracias a los desarrolladores. "
                "Si te cuesta hacerlo funcionar con WhatsApp, pon la app de WhatsApp "
                "abajo. A mí me funcionó."
            ),
            "pt-BR": (
                "É o melhor app da categoria. Testei vários parecidos e todos pediam "
                "você vender a alma, e nem funcionavam direito. Aí encontrei esse e "
                "simplesmente funciona. Sem perguntas, sem permissões desnecessárias, "
                "totalmente offline. Muito obrigado aos desenvolvedores. Se estiver "
                "difícil fazer funcionar com o WhatsApp, deixa o WhatsApp embaixo. "
                "Comigo deu certo assim."
            ),
            "fr": (
                "C'est la meilleure appli de sa catégorie. J'ai testé plusieurs apps "
                "similaires, elles te demandent toutes de vendre ton âme, et en plus "
                "elles marchent mal. Puis je suis tombé sur celle-ci et ça marche, "
                "point. Pas de questions, pas de permissions inutiles, totalement "
                "hors ligne. Un grand merci aux développeurs. Si tu galères à la "
                "faire marcher avec WhatsApp, mets WhatsApp en bas. Chez moi ça a "
                "fonctionné."
            ),
            "de": (
                "Die beste App in dieser Kategorie. Ich habe gerade mehrere ähnliche "
                "Apps getestet — alle wollen, dass man seine Seele verkauft, und "
                "laufen trotzdem nicht zuverlässig. Dann bin ich über diese "
                "gestolpert, und sie funktioniert einfach. Keine Fragen, keine "
                "unnötigen Berechtigungen, komplett offline. Großes Dankeschön an "
                "die Entwickler. Wenn es mit WhatsApp schwierig wird: WhatsApp "
                "einfach unten platzieren. Bei mir hat das geholfen."
            ),
            "it": (
                "È la migliore app nella sua categoria. Ne ho appena provate diverse "
                "simili — tutte ti chiedono di vendere l'anima e in più non funzionano "
                "nemmeno bene. Poi mi sono imbattuto in questa e semplicemente "
                "funziona. Nessuna domanda, nessun permesso superfluo, completamente "
                "offline. Un grande grazie agli sviluppatori. Se fai fatica a farla "
                "funzionare con WhatsApp, metti WhatsApp in basso. A me ha funzionato "
                "così."
            ),
            "ru": (
                "Лучшее приложение в своей категории. Только что попробовал несколько "
                "похожих — все требуют продать душу и при этом нормально не работают. "
                "А потом наткнулся на это, и оно просто работает. Без вопросов, без "
                "лишних разрешений, полностью офлайн. Большое спасибо разработчикам. "
                "Если не получается подружить с WhatsApp, поставьте WhatsApp вниз — "
                "у меня сработало."
            ),
            "ar": (
                "هذا أفضل تطبيق في فئته. جرّبت للتو عدة تطبيقات مشابهة، وكلها تطلب "
                "منك أن تبيع روحك، ومع ذلك لا تعمل بشكل موثوق. ثم صادفت هذا التطبيق، "
                "وهو ببساطة يعمل. بدون أسئلة، بدون أذونات زائدة، ويعمل تمامًا دون "
                "اتصال. ألف شكر للمطوّرين. لمن يجد صعوبة في تشغيله مع واتساب: ضع "
                "واتساب في الأسفل. هذا ما نجح معي."
            ),
            "hi": (
                "अपनी श्रेणी में यह सबसे अच्छा ऐप है। मैंने अभी कई ऐसे ही ऐप आज़माए — "
                "सब आपकी आत्मा बेचने को कहते हैं, और फिर भी ठीक से काम नहीं करते। "
                "फिर मुझे यह मिला और यह बस काम करता है। न कोई सवाल, न ज़रूरत से ज़्यादा "
                "अनुमतियाँ, पूरी तरह ऑफ़लाइन। डेवलपर्स का बहुत-बहुत धन्यवाद। अगर "
                "WhatsApp के साथ चलाने में दिक्कत हो, तो WhatsApp को सबसे नीचे रखें — "
                "मेरे लिए तो यही काम कर गया।"
            ),
            "th": (
                "เป็นแอปที่ดีที่สุดในประเภทนี้ ผมเพิ่งลองหลายแอปที่คล้ายกัน "
                "ทุกตัวเหมือนต้องขายวิญญาณ แถมยังทำงานไม่เสถียร "
                "แล้วก็มาเจอตัวนี้ มันก็แค่ใช้งานได้ ไม่ถามอะไรเยอะ "
                "ไม่ขอสิทธิ์เกินจำเป็น ทำงานออฟไลน์ได้ทั้งหมด ขอบคุณนักพัฒนามากครับ "
                "ถ้าใครใช้กับ WhatsApp ไม่ลง ลองย้าย WhatsApp ไปไว้ด้านล่าง "
                "ของผมแบบนั้นใช้ได้"
            ),
            "vi": (
                "Đây là ứng dụng tốt nhất trong cùng loại. Mình vừa thử vài app "
                "tương tự — cái nào cũng đòi bạn bán linh hồn, mà còn chạy không "
                "ổn định. Rồi mình tình cờ thấy app này — nó cứ thế chạy. Không "
                "hỏi han gì, không xin quyền linh tinh, hoạt động hoàn toàn offline. "
                "Cảm ơn nhà phát triển rất nhiều. Ai khó dùng cùng WhatsApp thì "
                "đặt WhatsApp ở dưới — mình làm vậy là chạy."
            ),
        },
    },

    {
        "id": "vanitha_2026_03_04",
        "reviewer": "Vanitha Y.",
        "device": "Redmi A3 Pro",
        "android": "Android 16 Beta",
        "rating": 5,
        "date": _date(2026, 3, 4),
        "original_lang": "en",
        "original_text": (
            "No any ads, Best experience. My Redmi 14C doesn't have this "
            "split screen option so this app is a blessing for me. Highly "
            "recommended."
        ),
        "translations": {
            "ja": (
                "広告ゼロ、最高の体験。私の Redmi 14C には分割画面の機能がないので、"
                "このアプリは本当に救世主です。強くおすすめします。"
            ),
            "ko": (
                "광고가 하나도 없고, 최고의 경험. 제 Redmi 14C에는 화면 분할 기능이 "
                "없는데, 이 앱은 정말 구원자예요. 강력 추천합니다."
            ),
            "zh-CN": (
                "完全没有广告，体验超棒。我的 Redmi 14C 没有分屏功能，这个 app "
                "对我来说就是救星。强烈推荐。"
            ),
            "zh-TW": (
                "完全沒有廣告，體驗超棒。我的 Redmi 14C 沒有分割畫面功能，這個 app "
                "對我來說就是救星。強烈推薦。"
            ),
            "es": (
                "Sin anuncios, la mejor experiencia. Mi Redmi 14C no tiene la "
                "opción de pantalla dividida, así que esta app es una bendición "
                "para mí. Muy recomendada."
            ),
            "pt-BR": (
                "Sem nenhum anúncio, a melhor experiência. Meu Redmi 14C não tem "
                "a opção de tela dividida, então esse app é uma benção pra mim. "
                "Super recomendo."
            ),
            "fr": (
                "Aucune pub, la meilleure expérience. Mon Redmi 14C n'a pas "
                "l'option d'écran partagé, donc cette appli est une bénédiction "
                "pour moi. Vivement recommandée."
            ),
            "de": (
                "Keine Werbung, beste Erfahrung. Mein Redmi 14C hat keine "
                "Split-Screen-Option, also ist diese App ein Segen für mich. "
                "Klare Empfehlung."
            ),
            "it": (
                "Nessuna pubblicità, la migliore esperienza. Il mio Redmi 14C "
                "non ha l'opzione schermo diviso, quindi questa app è una manna "
                "dal cielo. Consigliatissima."
            ),
            "ru": (
                "Совсем без рекламы, лучший опыт. На моём Redmi 14C нет опции "
                "разделённого экрана, поэтому это приложение — настоящее спасение. "
                "Очень рекомендую."
            ),
            "ar": (
                "بدون إعلانات على الإطلاق، تجربة رائعة. هاتفي Redmi 14C لا يحتوي "
                "على خاصية تقسيم الشاشة، فهذا التطبيق نعمة بالنسبة لي. أوصي به بشدة."
            ),
            "hi": (
                "कोई विज्ञापन नहीं, सबसे बढ़िया अनुभव। मेरे Redmi 14C में split "
                "screen का विकल्प नहीं है, इसलिए यह ऐप मेरे लिए वरदान है। ज़ोरदार "
                "सिफारिश।"
            ),
            "th": (
                "ไม่มีโฆษณาเลย ประสบการณ์ดีที่สุด Redmi 14C ของฉันไม่มีฟีเจอร์ "
                "แบ่งหน้าจอ แอปนี้เลยเป็นพรสำหรับฉัน แนะนำสุดๆ"
            ),
            "vi": (
                "Không một quảng cáo, trải nghiệm tuyệt nhất. Redmi 14C của mình "
                "không có chức năng chia màn hình nên app này như cứu tinh. "
                "Cực kỳ khuyến nghị."
            ),
        },
    },

    {
        "id": "pramila_2026_05_20",
        "reviewer": "Pramila M.",
        "device": "Redmi 10 Prime",
        "android": "Android 11",
        "rating": 5,
        "date": _date(2026, 5, 20),
        "original_lang": "en",
        "original_text": (
            "Wow, actually great, cuz it has no ads and it's very simple "
            "to use, nice UI."
        ),
        "translations": {
            "ja": (
                "うわ、これ普通にすごい。広告がないし、使い方もすごくシンプル、"
                "UIもいい。"
            ),
            "ko": (
                "와, 진짜 좋다. 광고도 없고 쓰기도 아주 간단하고, UI도 깔끔하다."
            ),
            "zh-CN": (
                "哇，真的不错，因为没有广告，用起来很简单，UI 也好看。"
            ),
            "zh-TW": (
                "哇，真的不錯，因為沒有廣告，用起來很簡單，UI 也好看。"
            ),
            "es": (
                "Vaya, la verdad que genial: no tiene anuncios, es muy fácil "
                "de usar y la interfaz está muy bien."
            ),
            "pt-BR": (
                "Nossa, muito bom mesmo — não tem anúncios, é super fácil de "
                "usar e a interface é ótima."
            ),
            "fr": (
                "Waouh, vraiment top : aucune pub, très simple à utiliser, "
                "et une belle interface."
            ),
            "de": (
                "Wow, echt klasse — keine Werbung, super einfach zu bedienen "
                "und eine schöne Oberfläche."
            ),
            "it": (
                "Wow, davvero ottima: niente pubblicità, facilissima da usare "
                "e una bella interfaccia."
            ),
            "ru": (
                "Ого, реально здорово — никакой рекламы, очень просто "
                "пользоваться, и интерфейс приятный."
            ),
            "ar": (
                "واو، رائع فعلًا — بدون إعلانات، وسهل الاستخدام جدًا، "
                "وواجهة جميلة."
            ),
            "hi": (
                "वाह, सच में बढ़िया — कोई विज्ञापन नहीं, इस्तेमाल करना बहुत "
                "आसान, और UI भी अच्छा।"
            ),
            "th": (
                "ว้าว ดีจริง ๆ ไม่มีโฆษณา ใช้งานง่ายมาก แล้ว UI ก็สวย"
            ),
            "vi": (
                "Ồ, thật sự tuyệt — không có quảng cáo, dùng rất đơn giản, "
                "giao diện đẹp."
            ),
        },
    },

    {
        "id": "carlos_2026_04_19",
        "reviewer": "Carlos C.",
        "device": None,  # Play Console returned "-"
        "android": "Android 13",
        "rating": 5,
        "date": _date(2026, 4, 19),
        "original_lang": "en",
        "original_text": (
            "great productivity tool, what I do is to pair time sink apps with "
            "good for me apps; think vlc + anki"
        ),
        "translations": {
            "ja": (
                "素晴らしい生産性ツール。私のやり方は、時間を吸われがちなアプリと、"
                "自分のためになるアプリを組み合わせること。例えば VLC と Anki みたいに。"
            ),
            "ko": (
                "훌륭한 생산성 도구. 제 활용법은 시간을 잡아먹는 앱과 저에게 도움이 "
                "되는 앱을 짝으로 묶는 것. 예를 들어 VLC + Anki 같은 식."
            ),
            "zh-CN": (
                "很棒的生产力工具。我的用法是把会让人沉迷的应用和对自己有益的应用"
                "搭配起来，比如 VLC + Anki。"
            ),
            "zh-TW": (
                "很棒的生產力工具。我的用法是把會讓人沉迷的應用和對自己有益的應用"
                "搭配起來，比如 VLC + Anki。"
            ),
            "es": (
                "Genial herramienta de productividad. Lo que hago es emparejar apps "
                "tragatiempos con apps que me convienen — por ejemplo, VLC + Anki."
            ),
            "pt-BR": (
                "Ótima ferramenta de produtividade. O que eu faço é juntar apps que "
                "devoram tempo com apps que me fazem bem — tipo VLC + Anki."
            ),
            "fr": (
                "Excellent outil de productivité. Ce que je fais, c'est associer "
                "une appli chronophage avec une appli utile — genre VLC + Anki."
            ),
            "de": (
                "Großartiges Produktivitäts-Tool. Mein Trick: eine Zeitfresser-App "
                "mit einer App koppeln, die mir guttut — z. B. VLC + Anki."
            ),
            "it": (
                "Ottimo strumento di produttività. Quello che faccio è abbinare app "
                "che fanno perdere tempo con app utili — tipo VLC + Anki."
            ),
            "ru": (
                "Отличный инструмент для продуктивности. Я обычно пары собираю так: "
                "одно «пожирающее время» приложение + одно полезное — например, "
                "VLC + Anki."
            ),
            "ar": (
                "أداة إنتاجية رائعة. ما أفعله هو إقران التطبيقات الملتهمة للوقت "
                "بتطبيقات مفيدة لي — مثل VLC مع Anki."
            ),
            "hi": (
                "ज़बरदस्त productivity tool। मैं वक़्त खा जाने वाले ऐप को ऐसे ऐप के "
                "साथ जोड़ता हूँ जो मेरे लिए अच्छे हैं — जैसे VLC + Anki।"
            ),
            "th": (
                "เครื่องมือเพิ่ม productivity ที่เยี่ยมมาก สิ่งที่ผมทำคือ "
                "จับคู่แอปที่กินเวลา กับแอปที่เป็นประโยชน์ต่อตัวเอง — เช่น VLC + Anki"
            ),
            "vi": (
                "Công cụ tăng năng suất tuyệt vời. Cách mình dùng là ghép một app "
                "tốn thời gian với một app có ích cho mình — kiểu VLC + Anki."
            ),
        },
    },

    {
        "id": "kazu_2026_05_16",
        "reviewer": "Kazu",
        "device": "moto g24 power",
        "android": "Android 14",
        "rating": 5,
        "date": _date(2026, 5, 16),
        "original_lang": "pt-BR",
        "original_text": "o melhor e grátis pode instalar e top",
        "translations": {
            "en":    "The best — and it's free. Install it. Top notch.",
            "ja":    "最高で、しかも無料。入れとくべし。神アプリ。",
            "ko":    "최고. 게다가 무료. 그냥 깔아라. 갑이다.",
            "zh-CN": "最好的，而且免费。装就完事了。绝了。",
            "zh-TW": "最棒的，而且免費。裝下去就對了。神級。",
            "es":    "Lo mejor — y gratis. Instálala. De primera.",
            "fr":    "La meilleure — et gratuite. Installe. Au top.",
            "de":    "Die beste — und gratis. Einfach installieren. Top.",
            "it":    "La migliore — e gratis. Installala. Da urlo.",
            "ru":    "Лучшее — и бесплатно. Ставь. Огонь.",
            "ar":    "الأفضل — ومجاني. ثبّته. ممتاز.",
            "hi":    "बेस्ट है — और मुफ़्त भी। बस install कर लो। टॉप।",
            "th":    "เจ๋งสุด แถมฟรี ลงเลย ของแท้",
            "vi":    "Đỉnh nhất — mà còn free. Cài đi. Top thiệt.",
        },
    },

    {
        "id": "fariz_2026_04_18",
        "reviewer": "Fariz H.",
        "device": "POCO M3",
        "android": "Android 12",
        "rating": 5,
        "date": _date(2026, 4, 18),
        "original_lang": "az",
        "original_text": "çox gözəl",
        "translations": {
            "en":    "Very nice.",
            "ja":    "とても素敵。",
            "ko":    "아주 좋다.",
            "zh-CN": "非常棒。",
            "zh-TW": "非常棒。",
            "es":    "Muy bonito.",
            "pt-BR": "Muito bom.",
            "fr":    "Très joli.",
            "de":    "Sehr schön.",
            "it":    "Molto bello.",
            "ru":    "Очень здорово.",
            "ar":    "جميل جدًا.",
            "hi":    "बहुत बढ़िया।",
            "th":    "เยี่ยมมาก",
            "vi":    "Rất tuyệt.",
        },
    },

    {
        "id": "musse_2026_05_26",
        "reviewer": "Musse G.",
        "device": "Galaxy A11",
        "android": "Android 10",
        "rating": 5,
        "date": _date(2026, 5, 26),
        "original_lang": "en",
        "original_text": "perfect",
        "translations": {
            "ja":    "完璧。",
            "ko":    "완벽.",
            "zh-CN": "完美。",
            "zh-TW": "完美。",
            "es":    "Perfecta.",
            "pt-BR": "Perfeita.",
            "fr":    "Parfaite.",
            "de":    "Perfekt.",
            "it":    "Perfetta.",
            "ru":    "Идеально.",
            "ar":    "ممتاز.",
            "hi":    "एकदम परफेक्ट।",
            "th":    "สมบูรณ์แบบ",
            "vi":    "Hoàn hảo.",
        },
    },

    {
        "id": "sam_2026_05_17",
        "reviewer": "Sam G.",
        "device": "Vivo Y200 Pro 5G",
        "android": "Android 15",
        "rating": 5,
        "date": _date(2026, 5, 17),
        "original_lang": "nl",
        "original_text": "op",
        "translations": {
            "en":    "OP (overpowered).",
            "ja":    "やばい。",
            "ko":    "최강.",
            "zh-CN": "无敌。",
            "zh-TW": "無敵。",
            "es":    "Brutal.",
            "pt-BR": "Demais.",
            "fr":    "Une tuerie.",
            "de":    "Krass.",
            "it":    "Una bomba.",
            "ru":    "Имба.",
            "ar":    "خرافي.",
            "hi":    "ज़बरदस्त।",
            "th":    "เทพมาก",
            "vi":    "Bá đạo.",
        },
    },
]
