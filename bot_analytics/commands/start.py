import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS

TOKEN = 'your_bot_token_here'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']

    bot.editMessageText((chat_id, message_id), "Selamat Datang di @Ifa_bolero_dan_rompi_bot\nDisini kita dapat belajar bersama berbagai Hal tentang Bolero/Rompi😁👍\n", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Pengertian✍️️")],
            [KeyboardButton(text="Menyiapkan Ukuran📏")],
            [KeyboardButton(text="Pola📐")],
            [KeyboardButton(text="Bahan🧵")],
            [KeyboardButton(text="Vidio Tutorial⏸")]
        ],
        resize_keyboard=True
    ))

    bot.sendMessage(chat_id, "Pilih salah satu materi disini👇.")
    try:
        user_message_id = message.get('message_id')
        bot.deleteMessage((chat_id, user_message_id))
    except telepot.exception.TelegramError as e:
        pass
