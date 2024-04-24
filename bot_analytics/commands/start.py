import telepot
from tinydb import TinyDB, Query
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from config import TOKEN
from programs.message import editMessage

bot = telepot.Bot(TOKEN)
db = TinyDB('welcome_chat.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']

    # Mengambil data terakhir dari database
    last_entry = db.all()[-1]

    # Memeriksa apakah data terakhir adalah teks selamat datang
    if last_entry.get('is_welcome', False):
        bot.deleteMessage((chat_id, last_entry['message_id']))

    message_id = sent_message['message_id']
    editMessage(chat_id, message_id, "Selamat Datang di @Ifa_bolero_dan_rompi_bot\nDisini kita dapat belajar bersama berbagai Hal tentang Bolero/Rompi😁👍\n")

    # Menyimpan pesan selamat datang saat ini
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'is_welcome': True})

    bot.sendMessage(chat_id, "Pilih salah satu materi disini👇.", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Pengertian✍️️")],
            [KeyboardButton(text="Menyiapkan Ukuran📏")],
            [KeyboardButton(text="Pola📐")],
            [KeyboardButton(text="Bahan🧵")],
            [KeyboardButton(text="Vidio Tutorial▶️")]
        ],
        resize_keyboard=True
    ))

    try:
        user_message_id = message.get('message_id')
        bot.deleteMessage((chat_id, user_message_id))
    except telepot.exception.TelegramError as e:
        pass
