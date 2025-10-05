# Tinish belgilari haqida

Quyidagi qoidalar Unicode yordamida matn terishda tinish belgilaridan toʻgʻri foydalanishga qaratilgan.

## Qoʻshtirnoqlar

Ingliz tilida raqamli muhitda standart klaviaturadagi " (qoʻsh) va ' (yakka) qoʻshtirnoqlardan foydalanish odatiy hol. Oʻzbek tilida esa, imlo qoidalari boshqacha boʻlib, matbuot va rasmiy hujjatlarda quyidagi qoʻshtirnoqlardan foydalaniladi.

**Lotin oʻzbek yozuvi:** Lotin alifbosidagi oʻzbek tilida “...” (inglizcha “dubl-sferik” qoʻshtirnoqlar) asosiy (tashqi) qoʻshtirnoqlar hisoblanadi. Matn ichida, yaʼni qoʻshtirnoqlar ichida boshqa bir soʻz yoki gap qoʻshtirnoqqa olinadigan boʻlsa, ‘...’ (yakka) qoʻshtirnoqlardan foydalaniladi.

- **Misol:** U shunday dedi: “Unga ‘salom’ deganimni ayting”.

#### Kiritish usullari
Tashqi: “...”
- **HTML kodlari:** `&ldquo;` va `&rdquo;`
- **Unicode kodlari:** `&#8220;` va `&#8221;`

Ichki: ‘...’
- **HTML kodlari:** `&lsquo;` va `&rsquo;`
- **Unicode kodlari:** `&#8216;` va `&#8217;`

---

**Kirill oʻzbek yozuvi:** Kirill alifbosidagi oʻzbek tilida asosiy (tashqi) qoʻshtirnoqlar sifatida «...» (fransuzcha yoki “dubl-shevron”) qoʻshtirnoqlaridan foydalaniladi. Agar ularning ichida qoʻshtirnoqlar kerak boʻlsa, „...“ (nemischa “dubl-sferik”) qoʻshtirnoqlari ishlatiladi.

- **Misol:** У шундай деди: «Унга „салом“ деганимни айтинг».

#### Kiritish usullari

Tashqi: «...»
- **HTML kodlari:** `&laquo;` va `&raquo;`
- **Unicode kodlari:** `&#171;` va `&#187;`

Ichki: „...“
- **HTML kodlari:** yoʻq
- **Unicode kodlari:** `&#8222;` va `&#8220;`

## Tire belgilari

**Qisqa tire** (En dash, –): Bu belgi asosan oraliqni, masofani yoki chegarani koʻrsatish uchun sonlar oʻrtasida ishlatiladi.

- **Misol:** 2020–2025 yillar, 12:00–14:00, Toshkent–Samarqand.

**HTML kodi:** `&ndash;` \
**Unicode kodi:** `&#8211;`

---

**Uzun tire** (Em dash, —): Bu belgi fikrni, izohni yoki maʼnoni ajratib koʻrsatish uchun ishlatiladi. Gap ichida undan oldin va keyin boʻsh joy qoldirilmaydi.

- **Misol:** Mening hayotim — bu kurash. Buni unga aytdim — lekin u eshitmadi.

**HTML kodi:** `&mdash;` \
**Unicode kodi:** `&#8212;`

## Koʻrinmas boʻshliq (Non-breaking space)

Bu belgi satr uzilishining oldini olish uchun ishlatiladi. U, masalan, son bilan birlik ajralib qolmasligini taʼminlaydi.

Qoidalar:

- Raqam va oʻlchov birligi oʻrtasida: 150 km/soat, 20 soat.

- Raqam va valyuta belgisi oʻrtasida: 20 $.

- Qisqartmalar bilan bogʻliq soʻzlarda, masalan, F. I. O..

**HTML kodi:** `&nbsp;` \
**Unicode kodi:** `&#160;`

