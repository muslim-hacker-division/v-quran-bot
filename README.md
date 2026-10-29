# V-Quran Bot 2026 Edition

Bot Telegram yang menghadirkan ayat-ayat Al-Qur'an secara interaktif dengan tema pilihan yang relevan untuk kebutuhan harian: kabar gembira, azab, nasehat, ketenangan, sabar, dan doa.

Selamat datang di repositori `v-quran-bot` — sebuah proyek Python sederhana yang menggabungkan `python-telegram-bot`, `requests`, dan API Al-Quran Cloud untuk membangun pengalaman membaca ayat yang lebih hidup di Telegram.

## ✨ Fitur utama

- Bot Telegram interaktif berbasis inline keyboard
- Kategori ayat yang mudah dipilih:
  - Kabar Gembira
  - Peringatan Azab
  - Nasehat Akhlak
  - Ketenangan Hati
  - Sabar & Ujian
  - Doa Pilihan
- Mengambil teks Arab dan terjemahan Indonesia dari API Al-Quran Cloud
- Data ayat dikelola dalam format JSON untuk kemudahan update dan ekspansi
- Siap di-deploy di platform seperti Render

## 🧠 Struktur proyek

```text
v-quran-bot/
├── app.py                 # entry point bot Telegram
├── data/
│   └── ayat.json          # database ayat per kategori
├── Procfile               # konfigurasi proses untuk deployment
├── render.yaml            # konfigurasi Render
├── requirements.txt       # dependensi Python
├── README.md              # dokumentasi proyek
└── .gitignore             # file yang diabaikan Git
```

## 📦 Teknologi yang dipakai

- Python 3
- python-telegram-bot
- requests
- JSON untuk database lokal
- Al-Quran Cloud API untuk mengambil ayat dan terjemahan

## 🚀 Cara menjalankan lokal

1. Clone repositori:

```bash
git clone https://github.com/muslim-hacker-division/v-quran-bot.git
cd v-quran-bot
```

2. Buat virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# atau
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Siapkan token Telegram:

```bash
export TELEGRAM_TOKEN="TOKEN_ANDA_DISINI"
```

5. Jalankan bot:

```bash
python app.py
```

## 🗂️ Format data ayat

File `data/ayat.json` berisi pasangan surah dan nomor ayat dalam format berikut:

```json
{
  "kabar_gembira": [[2, 25], [3, 133]],
  "azab": [[7, 40], [22, 19]],
  "nasehat": [[31, 13], [49, 10]],
  "ketenangan": [[13, 28], [2, 186]],
  "sabar": [[2, 153], [3, 200]],
  "doa": [[2, 201], [20, 25]]
}
```

Setiap item berisi:
- nomor surah
- nomor ayat

Bot akan memilih ayat acak dari kategori tertentu, lalu mengambil teks Arab dan terjemahan Indonesia dari API Al-Quran Cloud.

## 🌍 Deployment ke Render

Repo ini sudah dilengkapi dengan file `render.yaml` dan `Procfile` untuk deploy ke Render.

Konfigurasi yang dipakai:

```yaml
services:
  - type: worker
    name: v-quran-bot
    runtime: python
    region: singapore
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
```

Pastikan variabel environment berikut tersedia di dashboard Render:

```bash
TELEGRAM_TOKEN=your_token_here
```

## 🧪 Contoh alur bot

1. User mengirim `/start`
2. Bot menampilkan keyboard kategori ayat
3. User memilih kategori
4. Bot mengambil ayat acak dari data JSON
5. Bot menampilkan:
   - teks Arab
   - terjemahan Indonesia
   - nama surah dan nomor ayat

## 📌 Catatan pengembangan

Proyek ini dibuat dengan prinsip sederhana dan mudah dikembangkan:

- kumpulan ayat terstruktur dalam JSON
- logika bot tetap terpisah dengan data
- proses deploy cepat dan ringan
- mudah ditambahkan kategori baru atau data ayat baru

## 🛠️ Kontribusi

Kontribusi sangat terbuka. Anda dapat:

- menambah data ayat pada `data/ayat.json`
- menambahkan kategori baru
- memperbaiki tampilan pesan bot
- memperbarui desain pengalaman pengguna

## 📜 Lisensi

Proyek ini dibuat untuk kebutuhan edukasi dan pengembangan komunitas. Gunakan dengan bijak dan tetap menghormati sumber serta konten Al-Qur'an.

## 🚀 Status proyek

Status: Aktif untuk pengembangan dan deployment dasar

Terima kasih telah menggunakan dan mengembangkan `v-quran-bot`.

---

"Bersama ayat-ayat yang menenangkan, jadikan setiap hari lebih tenang, lebih sadar, dan lebih dekat pada kebaikan."
