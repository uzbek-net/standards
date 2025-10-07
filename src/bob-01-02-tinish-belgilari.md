# Tinish belgilari haqida

Quyidagi qoidalar Unicode yordamida matn terishda tinish belgilaridan toʻgʻri foydalanishga qaratilgan.

## Qoʻshtirnoqlar

Ingliz tilida raqamli muhitda standart klaviaturadagi " (qoʻshtirnoq) va ' (yakka tirnoq) belgilaridan foydalanish odatiy hol. Oʻzbek tilida esa, imlo qoidalari boshqacha boʻlib, matbuot va rasmiy hujjatlarda quyidagi qoʻshtirnoqlardan foydalaniladi.

**Lotin oʻzbek yozuvi:** Lotin alifbosidagi oʻzbek tilida “...” (inglizcha “dubl-sferik” qoʻshtirnoqlar) asosiy (tashqi) qoʻshtirnoqlar hisoblanadi. Matn ichida, yaʼni qoʻshtirnoqlar ichida boshqa bir soʻz yoki gap qoʻshtirnoqqa olinadigan boʻlsa, ‘...’ (yakka) qoʻshtirnoqlardan foydalaniladi.

- **Misol:** U shunday dedi: “Unga ‘salom’ deganimni ayting”.

#### Kiritish usullari
Tashqi: “...”
- **HTML kodlari:** `&ldquo;` (ochish) va `&rdquo;` (yopish)
- **Unicode kodlari:** `&#8220;` (ochish) va `&#8221;` (yopish)
- **Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0147` (ochish) yoki `0148` (yopish) tering.
- **macOS**ʼda kiritish uchun `Option + [` (ochish) yoki `Option + Shift + [` (yopish) tugmalarini bosing.

Ichki: ‘...’
- **HTML kodlari:** `&lsquo;` (ochish) va `&rsquo;` (yopish)
- **Unicode kodlari:** `&#8216;` (ochish) va `&#8217;` (yopish)
- **Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0145` (ochish) yoki `0146` (yopish) tering.
- **macOS**ʼda kiritish uchun `Option + ]` (ochish) yoki `Option + Shift + ]` (yopish) tugmalarini bosing.

---

**Kirill oʻzbek yozuvi:** Kirill alifbosidagi oʻzbek tilida asosiy (tashqi) qoʻshtirnoqlar sifatida «...» (fransuzcha yoki “dubl-shevron”) qoʻshtirnoqlaridan foydalaniladi. Agar ularning ichida qoʻshtirnoqlar kerak boʻlsa, „...“ (nemischa “dubl-sferik”) qoʻshtirnoqlari ishlatiladi.

- **Misol:** У шундай деди: «Унга „салом“ деганимни айтинг».

#### Kiritish usullari

Tashqi: «...»
- **HTML kodlari:** `&laquo;` (ochish) va `&raquo;` (yopish)
- **Unicode kodlari:** `&#171;` (ochish) va `&#187;` (yopish)
- **Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0171` (ochish) yoki `0187` (yopish) tering.

Ichki: „...“
- **HTML kodlari:** yoʻq
- **Unicode kodlari:** `&#8222;` (ochish) va `&#8220;` (yopish)

## Tire belgilari

**Qisqa tire** (En dash, –): Bu belgi asosan oraliqni, masofani yoki chegarani koʻrsatish uchun sonlar oʻrtasida ishlatiladi.

- **Misol:** 2020–2025 yillar, 12:00–14:00, Toshkent–Samarqand.

**HTML kodi:** `&ndash;` \
**Unicode kodi:** `&#8211;`

**Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0150` ni tering. **macOS**ʼda kiritish uchun `Option + - (defis)` tugmalarini bosing.

---

**Uzun tire** (Em dash, —): Bu belgi fikrni, izohni yoki maʼnoni ajratib koʻrsatish uchun ishlatiladi. Gap ichida undan oldin va keyin boʻsh joy qoldirilmaydi.

- **Misol:** Mening hayotim — bu kurash. Buni unga aytdim — lekin u eshitmadi.

**HTML kodi:** `&mdash;` \
**Unicode kodi:** `&#8212;`

**Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0151` ni tering. **macOS**ʼda kiritish uchun `Option + Shift + - (defis)` tugmalarini bosing.

## Uzilmas boʻshliq (Non-breaking space)

Bu belgi satr uzilishining oldini olish uchun ishlatiladi. U, masalan, son bilan birlik ajralib qolmasligini taʼminlaydi.

Qoidalar:

- Raqam va oʻlchov birligi oʻrtasida: 150 km/soat, 20 soat.

- Raqam va valyuta belgisi oʻrtasida: 20 $.

- Qisqartmalar bilan bogʻliq soʻzlarda, masalan, F. I. O..

**HTML kodi:** `&nbsp;` \
**Unicode kodi:** `&#160;`

**Windows**ʼda kiritish uchun `Alt` tugmasini bosib turgan holda, raqamlar klaviaturasida `0160` ni tering. **macOS**ʼda kiritish uchun `Option + Space` tugmalarini bosing.

