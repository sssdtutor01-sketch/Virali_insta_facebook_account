# 🚩 पावरफुल बायोडाटा — पूरी गाइड (कमांड सहित)

एडवोकेट कप्तान सिंह कुशवाह | BJP जिला दतिया

इस गाइड से आप अपना बायोडाटा (PDF + इमेज) कभी भी दोबारा बना सकते हैं —
खासकर जब फोटो जोड़ें।

---

## ✅ रास्ता A — सबसे आसान (बिना कमांड, कोई भी कर सकता है)

1. रिपॉज़िटरी से ये फाइलें डाउनलोड करें (सब एक ही फोल्डर में रखें):
   - `parichay-patra-kaptan-singh.html`  (मुख्य फाइल)
   - `bjp-logo.png`  (कमल वॉटरमार्क)
   - `qr-instagram.png`, `qr-facebook.png`, `qr-twitter.png`  (QR कोड)
2. अपनी फोटो उसी फोल्डर में डालें (नाम नीचे "फोटो नियम" में हैं)।
3. `parichay-patra-kaptan-singh.html` को **Google Chrome** में खोलें।
4. **Ctrl + P** दबाएँ → **Destination = Save as PDF** → **Background graphics = ON** → Save।
5. 3 पेज का प्रोफेशनल PDF तैयार! ✅

> यह तरीका सबसे भरोसेमंद है — हिंदी एकदम साफ़ आती है।

---

## ⚙️ रास्ता B — कमांड से (सैंडबॉक्स/लिनक्स में, ऑटोमैटिक PDF+इमेज)

### चरण 1: हिंदी + इमोजी फ़ॉन्ट इंस्टॉल करें
```bash
mkdir -p ~/.fonts
curl -sL -o ~/.fonts/NotoSansDevanagari.ttf \
  "https://github.com/google/fonts/raw/main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwdth%2Cwght%5D.ttf"
curl -sL -o ~/.fonts/NotoColorEmoji.ttf \
  "https://github.com/google/fonts/raw/main/ofl/notocoloremoji/NotoColorEmoji-Regular.ttf"
fc-cache -f
```

### चरण 2: QR कोड बनाएँ (Python)
```bash
pip install "qrcode[pil]"
python3 gen_qr.py        # qr-instagram.png / qr-facebook.png / qr-twitter.png बनेंगे
```

### चरण 3: कमल (BJP) वॉटरमार्क बनाएँ
```bash
pip install pillow
python3 make_lotus.py     # bjp-logo.png बनेगा
```

### चरण 4: अपनी फोटो डालें
फोटो नियम (नीचे देखें) के अनुसार फ़ाइलों को उसी फोल्डर में रखें।

### चरण 5: Playwright (हेडलेस क्रोम) इंस्टॉल करें
```bash
npm init -y
npm i playwright
npx playwright install chromium
```

### चरण 6: PDF + इमेज बनाएँ
```bash
node render.js
```
आउटपुट:
- `Bio-Data-Kaptan-Singh.pdf`  — फाइनल PDF (जमा करने योग्य)
- `Bio-Data-Preview.png`       — पूरा 3-पेज इमेज
- `Bio-Data-Page1.png`         — सिर्फ पेज 1 (WhatsApp शेयर हेतु)

> फोटो/टेक्स्ट बदलने के बाद सिर्फ **चरण 6** दोबारा चलाएँ।

---

## 📸 फोटो नियम (फ़ाइल के नाम)

| कहाँ | फ़ाइल का नाम | किसके लिए |
|------|--------------|-----------|
| पेज 1 (ऊपर दाएँ) | `photo.jpg` | आपकी प्रोफाइल फोटो |
| पेज 2 (6 बॉक्स) | `photo1.jpg` … `photo6.jpg` | CM, नरोत्तम मिश्रा जी, विधायक/मंत्री, प्रचार, रैली, समाज सेवा |
| पेज 3 (5 बॉक्स) | `viral1.jpg` … `viral5.jpg` | वायरल रील/पोस्ट के स्क्रीनशॉट |

- सभी फोटो `.jpg` रखें, उसी फोल्डर में।
- फोटो अपने-आप बॉक्स में लग जाएगी (HTML एडिट नहीं करना)।
- कैप्शन में `[स्थान/वर्ष]` भर दें।

---

## 💪 बायोडाटा पावरफुल क्यों है (ताकत)

1. 🏆 **बूथ 156** — पूरे जिले में हार, पर आपके बूथ पर जीत/बढ़त (सबसे बड़ा हथियार)
2. 🚩 **अटूट निष्ठा** — 23 मार्च व 23 मई 2026, डॉ. नरोत्तम मिश्रा जी से जुड़ाव, "पार्टी हित सर्वोपरि"
3. 💼 **12 वर्ष** का संगठनात्मक अनुभव + RSS पृष्ठभूमि
4. 📱 **QR कोड** — वायरल रील/पोस्ट तुरंत स्कैन कर देखें (मॉडर्न इम्प्रेशन)
5. 🪷 **कमल वॉटरमार्क** + तिरंगा स्टाइलिंग — प्रोफेशनल लुक
6. 🎯 **विज़न सेक्शन** — सिर्फ पद नहीं, योजना दिखाता है

---

जय हिन्द • जय भाजपा 🚩
