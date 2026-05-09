import logging
import random
import requests
import json
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = "TELEGRAM_TOKEN"

# Baca Database dari folder data/
def load_data():
    with open('data/ayat.json', 'r') as f:
        return json.load(f)

database_ayat = load_data()

def ambil_ayat_api(kategori):
    try:
        surah, ayat = random.choice(database_ayat[kategori])
        url_arab = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayat}/quran-uthmani"
        res_arab = requests.get(url_arab, timeout=10).json()
        teks_arab = res_arab['data']['text']
        
        url_id = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayat}/id.indonesian"
        res_id = requests.get(url_id, timeout=10).json()
        teks_id = res_id['data']['text']
        surah_name = res_id['data']['surah']['englishName']
        
        return (
            f"✨ {kategori.replace('_', ' ').upper()} ✨\n\n"
            f"{teks_arab}\n\n"
            f" Artinya: \n_{teks_id}_\n\n"
            f"📍 (QS. {surah_name} ayat {ayat})"
        )
    except Exception as e:
        return f" [ ERROR ] Gagal mengambil database: {e}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("✨ Kabar Gembira", callback_data='kabar_gembira'),
         InlineKeyboardButton("🔥 Peringatan Azab", callback_data='azab')],
        [InlineKeyboardButton("🌿 Nasehat Akhlak", callback_data='nasehat'),
         InlineKeyboardButton("🤍 Ketenangan Hati", callback_data='ketenangan')],
        [InlineKeyboardButton("💪 Sabar & Ujian", callback_data='sabar'),
         InlineKeyboardButton("🤲 Doa Pilihan", callback_data='doa')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    pesan_hacker = (
        f" [ SYSTEM ACCESS GRANTED ] \n"
        f"Selamat datang, Agent {user_name}.\n\n"
        f"Database Al-Qur'an terhubung via folder /data.\n"
        f"Pilih kategori amunisi di bawah ini:"
    )
    await update.message.reply_text(pesan_hacker, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    hasil_ayat = ambil_ayat_api(query.data)
    await query.edit_message_text(text=hasil_ayat, reply_markup=query.message.reply_markup, parse_mode='Markdown')

if __name__ == '__main__':
    print("--- V-WARRIOR BOT LIVE ON RENDER ---")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
