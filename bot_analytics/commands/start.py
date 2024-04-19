import telepot
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.exception import TelegramError


TOKEN = '6569008899:AAF3DCqPjVg2Sgrr6lH8UDGawuZkB8psF1M'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    message_id = sent_message.get('message_id')
    chat_id = sent_message.get('chat_id')
    
    bot.editMessageText((chat_id, message_id), "Selamat Datang di @Ifa_bolero_dan_rompi_bot\nDisini kita dapat belajar bersama berbagai Hal tentang Bolero/Rompi😁👍\n", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Pengertian✍️️")],
            [KeyboardButton(text="Menyiapkan Ukuran📏")],
            [KeyboardButton(text="Pola📐")],
            [KeyboardButton(text="Bahan🧵")],
            [KeyboardButton(text="Vidio Tutorial⏸")]
        ],
        resize_keyboard= True
    ))
    bot.sendMessage(chat_id, "Pilih salah satu materi disini👇.")
    try:
        bot.deleteMessage((update["message"]["chat"]["id"], update["message"]["message_id"]))
    except TelegramError as e:
        pass
