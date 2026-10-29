# V-Quran Bot 2026

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge)
![Data](https://img.shields.io/badge/Data-JSON-FFB703?style=for-the-badge)

</div>

<p align="center">
  <b>Bot Telegram interaktif untuk membagikan ayat Al-Qur'an dalam tema yang relevan dengan kehidupan sehari-hari.</b>
</p>

## Overview

V-Quran Bot adalah bot Telegram sederhana yang menyediakan ayat-ayat pilihan berdasarkan kategori seperti:

- Kabar Gembira
- Peringatan Azab
- Nasehat Akhlak
- Ketenangan Hati
- Sabar & Ujian
- Doa Pilihan

Bot ini mengambil teks Arab dan terjemahan Indonesia dari API Al-Quran Cloud dan menampilkannya secara ringkas ke pengguna melalui Telegram.

## Why this project?

Proyek ini dibuat untuk:

- membagikan ayat yang relevan dengan situasi harian
- mempermudah akses ke ayat secara interaktif di Telegram
- menjadi contoh proyek Python yang ringan, mudah dipelajari, dan mudah dikembangkan
- menyediakan basis data ayat yang mudah diupdate melalui `data/ayat.json`

## Features

- Inline keyboard interaktif di Telegram
- Pilihan kategori ayat yang jelas dan mudah diakses
- Teks Arab dari sumber resmi Al-Quran Cloud
- Terjemahan Indonesia yang ditampilkan bersama ayat
- Data ayat dikelola dalam format JSON
- Siap deploy di Render, Railway, atau platform Python lainnya
- Struktur kode sederhana untuk modifikasi dan ekspansi

## Project structure

```text
v-quran-bot/
├── app.py                 # Lokasi utama logika bot Telegram
├── data/
│   └── ayat.json          # Database ayat per kategori
├── Procfile               # Command proses deployment
├── render.yaml            # Konfigurasi Render
├── requirements.txt       # Dependensi Python
├── README.md              # Dokumentasi proyek
├── .gitignore             # File yang diabaikan Git
└── LICENSE                # (opsional jika nanti ditambahkan)
```

## Screenshots

> Screenshot preview akan ditambahkan di sini saat project sudah memiliki tampilan visual yang lebih matang.

### Bot preview mockup

```text
[ /start ]

✨ SELAMAT DATANG ✨
Database Al-Qur'an terhubung via folder /data.
Pilih kategori amunisi di bawah ini:

[✨ Kabar Gembira]   [🔥 Peringatan Azab]
[🌿 Nasehat Akhlak]  [🤍 Ketenangan Hati]
[💪 Sabar & Ujian]   [🤲 Doa Pilihan]
```

```text
✨ KABAR GEMBIRA ✨
[teks arab ayat]

Artinya:
[terjemahan Indonesia]

📍 (QS. Al-Baqarah ayat 25)
```

## Tech stack

- Python 3
- python-telegram-bot
- requests
- JSON
- Al-Quran Cloud API

## Local setup

### 1) Clone repository

```bash
git clone https://github.com/muslim-hacker-division/v-quran-bot.git
cd v-quran-bot
```

### 2) Create virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Set Telegram token

```bash
export TELEGRAM_TOKEN="YOUR_TELEGRAM_TOKEN"
```

Windows PowerShell:

```powershell
$env:TELEGRAM_TOKEN="YOUR_TELEGRAM_TOKEN"
```

### 5) Run the bot

```bash
python app.py
```

## Data format

File `data/ayat.json` berisi daftar surah dan nomor ayat berdasarkan kategori.

```json
{
  "kabar_gembira": [[2, 25], [3, 133], [9, 21]],
  "azab": [[7, 40], [22, 19], [40, 70]],
  "nasehat": [[31, 13], [49, 10], [17, 23]],
  "ketenangan": [[13, 28], [2, 186], [94, 5]],
  "sabar": [[2, 153], [2, 155], [3, 200]],
  "doa": [[2, 201], [3, 8], [20, 25]]
}
```

Setiap item adalah pasangan:

- [surah, ayat]

Contoh:

- `[2, 25]` = Surah Al-Baqarah ayat 25

## Deployment

Repo ini sudah dilengkapi dengan `render.yaml` dan `Procfile` untuk deployment ke Render.

### Render configuration

```yaml
services:
  - type: worker
    name: v-quran-bot
    runtime: python
    region: singapore
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
```

Pastikan variabel environment di Render sudah diisi:

```bash
TELEGRAM_TOKEN=your_token_here
```

## Bot flow

1. User mengirim `/start`
2. Bot menampilkan keyboard kategori
3. User memilih kategori ayat
4. Bot mengambil ayat acak dari `data/ayat.json`
5. Bot menampilkan:
   - teks Arab
   - terjemahan Indonesia
   - nama surah dan nomor ayat

## Contribution

Kontribusi sangat terbuka. Anda bisa:

- menambah data ayat baru pada `data/ayat.json`
- menambahkan kategori baru
- memperbaiki pesan bot
- meningkatkan pengalaman user interface
- menambahkan fitur notifikasi atau schedule ayat harian

## Notes

Proyek ini dibuat untuk kebutuhan pembelajaran, pengembangan, dan nilai edukatif. Gunakan dengan bijak dan tetap menghormati konteks keagamaan serta sumber referensi yang digunakan.

## Status

Status: Active development / ready for deployment

---

<p align="center">
  <b>"Semoga setiap ayat yang dibagikan menjadi sumber keberkahan, ketenangan, dan refleksi hati."</b>
</p>
