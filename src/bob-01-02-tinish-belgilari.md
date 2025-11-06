# Tinish belgilari haqida

Quyidagi qoidalar Unicode yordamida matn terishda tinish belgilaridan toʻgʻri foydalanishga qaratilgan.

## Brend nomlari va oʻzlashgan atamalar

Bu qoida xalqaro tashkilotlar, savdo belgilari (brendlar) nomlari hamda oʻzbek tiliga oʻzlashtirilgan, ammo transliteratsiya qilinmagan barcha chet tili atamalari uchun amal qiladi.

### 1. Asl yozuvni saqlash qoidasi

Global kontekstda tanish boʻlgan yoki maxsus maʼnoni anglatuvchi xalqaro nomlar va ayrim oʻzlashgan atamalar original (ingliz, ispan, fransuz va h.k.) yozilishi boʻyicha qabul qilinadi.

- **Brendlar va Atoqli nomlar:** Windows, Xerox, SpaceX, Canon.

- **Oʻzlashgan Atamalar (Transliteratsiya qilinmagan):** Wi-Fi, HTTP, GitHub.

### 2. Qoʻshimchalar qoʻshish (tutuq belgisi orqali)

Agar asl lotin yozuvida saqlab qolingan bunday xorijiy nomlar yoki atamalarga oʻzbek tilidagi qoʻshimchalar (masalan, -dan, -ga, -ning, -ni, -da) qoʻshiladigan boʻlsa, qoʻshimchadan oldin tutuq belgisi (ʼ, `U02BC`) qoʻyilishi shart.

**Tutuq belgisi xizmati:** Bu belgi xorijiy oʻzakni oʻzbekcha qoʻshimchadan vizual ravishda ajratish va maʼnoni farqlash uchun xizmat qiladi.

| Asl soʻz | Qoʻshimcha bilan yozilishi |
| --- | --- |
| Windows | Windowsʼdan |
| Xerox | Xeroxʼga |
| Canon | Canonʼning |
| Wi-Fi | Wi-Fiʼda |
| GitHub | GitHubʼga |

### 3. Talaffuz shaklidan foydalanish (Ixtiyoriy)

Agar xalqaro nomning oʻzbek tilida anʼanaviy talaffuz shakli yoki muqobil (transliteratsiya qilingan) nomi keng qoʻllanilsa, bu nomlarga nisbatan ikki xil yozuvga ruxsat beriladi:

- **Asl shakli:** Qoʻshimchalar tutuq belgisi orqali qoʻshiladi.

- **Talaffuz (Transliteratsiya) shakli:** Qoʻshimchalar tutuq belgisidan foydalanmasdan, odatdagi oʻzbek imlo qoidalariga koʻra qoʻshiladi.

| Xalqaro Nom | Asl yozuvi | Talaffuz (Transliteratsiya) yozuvi |
| --- | --- | --- |
| UNICEF | UNICEFʼning | YUNISEFning |
| UNESCO | UNESCOʼga | YUNESKOga |

## Qoʻshtirnoqlar

Ingliz tilida raqamli muhitda standart klaviaturadagi " (qoʻshtirnoq) va ' (yakka tirnoq) belgilaridan foydalanish odatiy hol. Oʻzbek tilida esa, imlo qoidalari boshqacha boʻlib, matbuot va rasmiy hujjatlarda quyidagi qoʻshtirnoqlardan foydalaniladi.

**Lotin oʻzbek yozuvi:** Lotin alifbosidagi oʻzbek tilida “...” (inglizcha “dubl-sferik” qoʻshtirnoqlar) asosiy (tashqi) qoʻshtirnoqlar hisoblanadi. Matn ichida, yaʼni qoʻshtirnoqlar ichida boshqa bir soʻz yoki gap qoʻshtirnoqqa olinadigan boʻlsa, ‘...’ (yakka) qoʻshtirnoqlardan foydalaniladi.

- **Misol:** U shunday dedi: “Unga ‘salom’ deganimni ayting”.

---

**Kirill oʻzbek yozuvi:** Kirill alifbosidagi oʻzbek tilida asosiy (tashqi) qoʻshtirnoqlar sifatida «...» (fransuzcha yoki “dubl-shevron”) qoʻshtirnoqlaridan foydalaniladi. Agar ularning ichida qoʻshtirnoqlar kerak boʻlsa, „...“ (nemischa “dubl-sferik”) qoʻshtirnoqlari ishlatiladi.

- **Misol:** У шундай деди: «Унга „салом“ деганимни айтинг».

## Tire belgilari

**Qisqa tire** (En dash, –): Bu belgi asosan oraliqni, masofani yoki chegarani koʻrsatish uchun sonlar oʻrtasida ishlatiladi.

- **Misol:** 2020–2025 yillar, 12:00–14:00, Toshkent–Samarqand.

---

**Uzun tire** (Em dash, —): Bu belgi fikrni, izohni yoki maʼnoni ajratib koʻrsatish uchun ishlatiladi. Gap ichida undan oldin va keyin boʻsh joy qoldirilmaydi.

- **Misol:** Mening hayotim — bu kurash. Buni unga aytdim — lekin u eshitmadi.

## Uzilmas boʻshliq (Non-breaking space)

Bu belgi satr uzilishining oldini olish uchun ishlatiladi. U, masalan, son bilan birlik ajralib qolmasligini taʼminlaydi.

Qoidalar:

- Raqam va oʻlchov birligi oʻrtasida: 150 km/soat, 20 soat.

- Raqam va valyuta belgisi oʻrtasida: 20 $.

- Qisqartmalar bilan bogʻliq soʻzlarda, masalan, F. I. O..

## Kiritish usullari

| Belgi | HTML kod | Windows* | MacOS |
| --- | --- | --- | --- |
| Tutuq belgisi | `&#x02BC;` | | |
| “” (qoʻshtirnoqlar) | `&ldquo;`, `&rdquo;` | `Alt` + `0147`; `Alt` + `0148` | `Option` + `[`; `Option` + `Shift` + `[` |
| ‘’ (birtirnoqlar) | `&lsquo;`, `&rsquo;` | `Alt` + `0145`; `Alt` + `0146` | `Option` + `]`; `Option` + `Shift` + `]` |
| «» (Shevron) | `&laquo;`, `&raquo;` | `Alt` + `0171`; `Alt` + `0187` | |
| „“ (nemischa qoʻshtirnoqlar) | `&#8222;`, `&#8220;` | | |
| – (en dash) | `&ndash;` | `Alt` + `0150` | `Option` + `-` (defis) |
| — (em dash) | `&mdash;` | `Alt` + `0151` | `Option` + `Shift` + `-` (defis) |
| Uzilmas boʻshliq | `&nbsp;` | `Alt` + `0160` | `Option` + `Boʻshliq` |

* Windowsʼda kiritish uchun `Alt` tugmasini bosib turgan holda raqamlar klaviaturasida (numpad) raqamlarni kiriting.