# Raqamlar

Bu boʻlimda raqamlarni Oʻzbek tilida qanday yozish, ajratish va ulardan
qanday foydalanish boʻyicha qoidalar keltirilgan.

### Oʻlchov birliklari va SI tizimi

Oʻzbekiston Respublikasi Vazirlar Mahkamasining 2018-yil 10-yanvardagi
[“Oʻzbekiston Respublikasida oʻlcham birliklarini qoʻllash
toʻgʻrisida”gi](https://lex.uz/docs/3499851) qaroriga binoan, barcha
texnik, ilmiy va ommaviy nashrlarda (shu jumladan, dasturiy taʼminot
interfeyslarida) xalqaro birliklar tizimi (SI) qoʻllanilishi shart.

Mahalliylashtirishda oʻlchov birliklarini oʻzbekcha qisqartmalar bilan
(masalan, kg oʻrniga кg yoki m oʻrniga м) yozish xato hisoblanadi. Barcha
qisqartmalar xalqaro standart (lotin harflari) asosida yozilishi kerak.

#### 1. Asosiy oʻlchov birliklari jadvali

Dastur interfeysini mahalliylashtirishda quyidagi xalqaro belgilardan
foydalaning:

| Oʻlchov nomi  | Xalqaro belgisi | Misol (Toʻgʻri) | Xato yozilishi       |
| ------------- | --------------- | --------------- | -------------------- |
| Metr          | m               | 10 m            | 10 metr, 10 m.       |
| Kilogramm     | kg              | 5 kg            | 5 kg., 5 кg          |
| Sekund        | s               | 30 s            | 30 sek, 30 s.        |
| Soat          | h               | 2 h             | 2 soat, 2 s, 2 soat. |
| Minut         | min             | 15 min          | 15 daqiqa, 15 m.     |
| Sutka (kun)   | d               | 1 d             | 1 kun, 1 sutka       |
| Litr          | l yoki L        | 1.5 L           | 1.5 l.               |
| Gektar        | ha              | 10 ha           | 10 gek, 10 ga        |
| Tonna         | t               | 3 t             | 3 tn                 |
| Kilovatt-soat | kW·h            | 250 kW·h        | 250 kVt/s            |

#### 2. Yozish qoidalari

- **Lotin harflarida yozish:** Matn kirill alifbosida boʻlsa ham, oʻlchov
  birliklarining qisqartmalari lotin harflarida (masalan, **m**, **kg**,
  **s**) yozilishi shart.

- **Boʻshliq qoldirish:** Raqam va oʻlchov birligi orasida har doim
  **uzilmas boʻshliq** (non-breaking space, \&nbsp;) qoʻyilishi kerak.
  - **Toʻgʻri:** 10&nbsp;kg
  - **Xato:** 10kg

- **Nuqta qoʻymaslik:** Oʻlchov birliklarining qisqartmalaridan soʻng
  nuqta qoʻyilmaydi (agar u gapning oxirida kelmagan boʻlsagina).
  - **Toʻgʻri:** "Fayl hajmi 15&nbsp;MB ga teng."
  - **Xato:** "Fayl hajmi 15&nbsp;MB. ga teng."

- **Katta-kichik harflar:** Birlik belgilarida harflarning registri
  (katta-kichikligi) muhim ahamiyatga ega. Masalan, millivatt (mW) va megavatt
  (MW) bir-biridan farq qiladi.

#### 3. Toʻliq va qisqartirilgan shakllarning qoʻllanilishi

Oʻlchov birliklarini interfeysda qanday yozish matnning joylashuvi va
kontekstiga bogʻliq:

- **Qisqartirilgan shakllar (Xalqaro):** Agar oʻlchov birligi raqamdan keyin
  qisqartma shaklda kelish kerak boʻlsa, faqat xalqaro lotin belgilaridan
  foydalaniladi.
  - **Misol:** **5&nbsp;kg**, **10&nbsp;m**, **2&nbsp;h**.

- **Toʻliq yozilgan shakllar (Oʻzbekcha):** Agar oʻlchov birligi gap
  ichida yoki interfeys elementida toʻliq soʻz bilan yozilsa, u oʻzbek
  tili imlosiga koʻra mahalliylashtiriladi.
  - **Misol:** "Ogʻirligi 5&nbsp;**kilogramm**dan kam boʻlmasligi kerak."
  - **Misol:** "Kutish vaqti: 2&nbsp;**soat**."

### Koʻplik shakllari (Plurals)

Dasturiy taʼminotni mahalliylashtirishda (masalan, Gettext yoki ICU formatlari
bilan ishlashda) ingliz tilida koʻpincha ikki xil shakl — **one** (birlik)
va **other** (koʻplik) ishlatiladi. Oʻzbek tilida esa sonlardan keyin
keladigan otlar har doim birlik shaklda qoʻllaniladi.

Agar otning miqdori sonlar (raqamlar) bilan ifodalansa, otga -lar koʻplik
qoʻshimchasi qoʻshilmaydi.

| Miqdor | Inglizcha (Plural) | Oʻzbekcha (Toʻgʻri) | Oʻzbekcha (Xato) |
| ------ | ------------------ | ------------------- | ---------------- |
| 1      | 1 book             | 1 ta kitob          | 1 ta kitob       |
| 5      | 5 books            | 5 ta kitob          | 5 ta kitoblar    |
| 0      | 0 files            | 0 ta fayl           | 0 ta fayllar     |

##### CLDR va Gettext qoidalari

Xalqaro mahalliylashtirish standartlarida (Unicode CLDR) oʻzbek tili uchun
koʻplik qoidasi "one" toifasiga kiradi. Bu degani, oʻzbek tili uchun n =
1 va n != 1 holatlari uchun tarjima bir xil boʻladi.

##### "ta" hisob soʻzining ishlatilishi

Raqam va otdan iborat birikmalarda raqamdan keyin "ta" hisob soʻzini ishlatish
tavsiya etiladi. Bu interfeysning tabiiyroq koʻrinishini taʼminlaydi.

- **Toʻgʻri:** 3 ta bildirishnoma, 10 ta xabar.
- **Qabul qilinadi (lekin tavsiya etilmaydi):** 3 bildirishnoma, 10 xabar.

##### Istisnolar: "-lar" qoʻshimchasi qachon ishlatiladi?

Koʻplik qoʻshimchasi faqat sonlar qatnashmagan, umumiy koʻplikni anglatuvchi
holatlarda ishlatiladi:

- Sozlamalar (Settings)
- Foydalanuvchilar (Users)
- Xabarlar (Messages)

Biroq, bu soʻzlar oldidan raqam kelsa, qoʻshimcha darhol tushib qoladi:

- 5 ta foydalanuvchi (5 users).

### Kasr va minglik ajratgichlar

Oʻzbek tilida raqamlarni yozishda oʻnlik (kasr) ajratgich va minglik
ajratgichlar ishlatiladi.

- **Oʻnlik ajratgich:** Vergul (`,`) ishlatiladi.
  - **Misollar:**
    - 15,45 soniya qoldi
    - 250,55 soʻm toʻlash kerak

- **Minglik ajratgich:** Uzilmas boʻsh joy (non-breaking space) ishlatiladi.
  - **Misol:** 14 400

#### Istisnolar

Ayrim hollarda nuqta (`.`) ajratgich sifatida ishlatilishi mumkin, ayniqsa
versiya raqamlarida.

- **Misol:** Python 3.12.

### Pul birliklari

Pul birliklarini yozishda raqam bilan soʻm yoki tiyin soʻzi orasida uzilmas
boʻsh joy (non-breaking space) ishlatiladi.

- **Misol:** 1 256 700,00 soʻm.

### Telefon raqamlari

Oʻzbekistonda telefon raqamlarini yozishda turli formatlardan foydalaniladi.

- **Xalqaro format:** `+998 (90) 123-45-67`. Bunda **998** mamlakat kodi,
  **90** uyali aloqa kodi va qolgan raqamlar.

- **Mahalliy format:** `(71) 123-45-67`. Bunda **71** shahar kodi.
