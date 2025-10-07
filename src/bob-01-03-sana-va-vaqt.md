# Sana va vaqt formatlari

Ushbu boʻlimda Oʻzbekistonda sana va vaqtni formatlash boʻyicha standartlar haqida maʼlumotlar berilgan.

## Sana

Oʻzbekistonda sana formatlari uchun quyidagi qoidalar amal qiladi:

- **Kalendar/Era:** Grigorian kalendaridan foydalaniladi.

- **Haftaning birinchi kuni:** Dushanba hisoblanadi.

- **Yilning birinchi haftasi:** Yanvar oyining birinchi kunini oʻz ichiga olgan hafta yilning birinchi haftasi deb belgilanadi.

### Standart sana formatlari

- **Qisqa sana formati:** dd.MM.yyyy.

    - **Misol:** 17.03.2011.

- **Uzun sana formati:** yyyy-yil d-MMMM.

    - **Misol:** 2011-yil 3-mart.

#### Format kodlaridagi belgilar

- `d` — kunni ifodalaydi: `d` (bosh nolsiz raqam), `dd` (bosh nol bilan raqam), `ddd` (qisqa kun nomi), `dddd` (toʻliq kun nomi).

- `M` — oyni ifodalaydi: `M` (bosh nolsiz raqam), `MM` (bosh nol bilan raqam), `MMM` (qisqa oy nomi), `MMMM` (toʻliq oy nomi).

- `y` — yilni ifodalaydi: `yy` (ikki xonali raqam) va `yyyy` (toʻrt xonali raqam).


### Hafta kunlari

| Kun (toʻliq shakli) | Qisqartma |
| - | - |
| Dushanba | Du |
| Seshanba | Se |
| Chorshanba | Ch |
| Payshanba | Pa |
| Juma | Ju |
| Shanba | Sh |
| Yakshanba | Ya |

### Oy nomlari

| Oy (toʻliq shakli) | Qisqartma |
| - | - |
| Yanvar | Yan. |
| Fevral | Fev. |
| Mart | Mar. |
| Aprel | Apr. |
| May | May |
| Iyun | Iyn. |
| Iyul | Iyl. |
| Avgust | Avg. |
| Sentyabr | Sen. |
| Oktyabr | Okt. |
| Noyabr | Noy. |
| Dekabr | Dek. |

### Hafta kuni va oy nomlari

- Hafta kun nomlari kalendarda va alohida ishlatilganda bosh harf bilan yoziladi. Agar ular gapning oʻrtasida kelsa, ular bosh harf bilan yozilmaydi.

- Oy nomlari ham kalendarda va alohida ishlatilganda bosh harf bilan yoziladi. Agar ular gapning oʻrtasida kelsa, ular bosh harf bilan yozilmaydi.

### Qoʻshimcha qoidalar

- Sana oraliqlar **en dash** bilan yoziladi.

    - **Misol:** 13 yanvar - 15 yanvar.

## Vaqt

- **24 soatlik format:** Ha.

- **Vaqt zonasi:** UZT UTC+05:00.

- **Yozgi vaqtga oʻtish (daylight saving time):**  qoʻllanilmaydi.

- **Standart vaqt formati:** `HH:mm:ss`.

    - **Misol:** 09:25:43; 15:10:31; 23:45:19.

- **Vaqt ajratuvchi:** Ikki nuqta (`:`).

    - **Misol:** 22:34:05.

- **Soatlar uchun bosh nol belgisi:** Ha.

    - **Misol:** 07:30:45.

- **Qisqa vaqt formati:** `HH:mm`.

    - **Misol:** 09:25; 15:10; 23:45.

- **Sana va vaqt formati:** `dd.MM.yyyy HH:mm:ss`

    - **Misol:** 20.04.2015 16:30:00.

## ISO 8601 standarti

ISO 8601 — xalqaro standart boʻlib, sana va vaqt maʼlumotlarini yozishning universal usulini belgilaydi. Ushbu standartdan foydalanish maʼlumotlarni almashishda va tizimlararo aloqada (masalan, API, veb-serverlar va maʼlumotlar bazalari) chalkashliklarning oldini oladi.

Uning asosiy formati  `YYYY-MM-DD` dir.

### Nima uchun foydalanish kerak?

**Aniq va tushunarli:** Baʼzi mamlakatlarda sana `MM/DD/YYYY` (oy/kun/yil) formatida, baʼzilarida esa `DD/MM/YYYY` (kun/oy/yil) formatida yoziladi. Bu holat tushunmovchiliklarga sabab boʻlishi mumkin. `ISO 8601` esa har doim yil-oy-kun tartibida boʻlgani uchun global miqyosda bir xil tushuniladi.

**Saralash oson:** Maʼlumotlar bazalarida sanalarni alifbo tartibida saralash (alphabetical sorting) orqali toʻgʻri xronologik tartibga keltirish imkonini beradi. Boshqa formatlarda bu ish bermaydi.

#### Misol:

- **Standard format:** `2025-10-07`

- **Vaqt bilan birga:** `2025-10-07T14:55:17` (Bu yerda `T` belgisi vaqtni sanadan ajratadi)

### Qachon foydalanish kerak?

Foydalanuvchi interfeysida asosan mahalliy format (`dd.MM.yyyy`) ishlatilishi kerak boʻlsa-da, tizimlararo maʼlumotlar almashinuvi, log fayllari, API chaqiriqlari va konfiguratsiya fayllarida doimo `ISO 8601` formatidan foydalanish tavsiya etiladi.