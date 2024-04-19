import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.exception import TelegramError

TOKEN = '6569008899:AAGkouDkdodOrx9vIBQGQjwvW7H8XIOk5d8'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(bot_message, message):
    content_type, chat_type, chat_id = telepot.glance(msg)
    sent_message = telepot.message_identifier(bot_message)
    user_message = telepot.message_identifier(message)

    bot.sendMessage(chat_id, "Pilih salah satu materi disini👇.")
    
    
    bot.sendMessage(chat_id, f'Pesan dari bot: Chat ID Anda adalah {chat_id}, dan message ID Anda adalah {message_id} dan {user_message_id}')

    bot.editMessageText(sent_message, "Selamat Datang di @Ifa_bolero_dan_rompi_bot\nDisini kita dapat belajar bersama berbagai Hal tentang Bolero/Rompi😁👍\n", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Pengertian✍️️")],
            [KeyboardButton(text="Menyiapkan Ukuran📏")],
            [KeyboardButton(text="Pola📐")],
            [KeyboardButton(text="Bahan🧵")],
            [KeyboardButton(text="Vidio Tutorial⏸")]
        ],
        resize_keyboard= True
    ))

    # Hapus pesan yang dikirim oleh pengguna
    try:
        bot.deleteMessage(user_message)
    except TelegramError as e:
        pass
