import telepot
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.exception import TelegramError

def command_handler(bot,display, message):
    
    
    bot.sendMessage(chat_id, "Selamat Datang di @Ifa_bolero_dan_rompi_bot\nDisini kita dapat belajar bersama berbagai Hal tentang Bolero/Rompi😁👍\n", reply_markup=ReplyKeyboardMarkup(
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
