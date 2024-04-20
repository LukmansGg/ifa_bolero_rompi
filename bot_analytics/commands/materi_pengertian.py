from programs.search import search
import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from config import TOKEN


bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, user_message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = user_message['text']
    user_message_id = message['message_id']

    try:
        bot.editMessageText((chat_id, message_id), "Disini kita akan belajar Materi Pengertian tentang bolero/rompi berikut, pilih salah satu👇", reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="> Sejarah Bolero/Rompi <",callback_data='sejarah')],
        [InlineKeyboardButton(text="> Pengertian Bolero/Rompi <",callback_data='pengertian')],
        [InlineKeyboardButton(text="> Perbedaan Bolero/Rompi <",callback_data='perbedaan')],
        [InlineKeyboardButton(text="> Desain Bolero/Rompi <",callback_data='desain')],
        [InlineKeyboardButton(text="> Macam Bolero/Rompi <",callback_data='macam')]
    ]))
    except:
        bot.sendMessage(chat_id, "Disini kita akan belajar Materi Pengertian tentang bolero/rompi berikut, pilih salah satu👇", reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="> Sejarah Bolero/Rompi <",callback_data='sejarah')],
        [InlineKeyboardButton(text="> Pengertian Bolero/Rompi <",callback_data='pengertian')],
        [InlineKeyboardButton(text="> Perbedaan Bolero/Rompi <",callback_data='perbedaan')],
        [InlineKeyboardButton(text="> Desain Bolero/Rompi <",callback_data='desain')],
        [InlineKeyboardButton(text="> Macam Bolero/Rompi <",callback_data='macam')]
    ]))
        pass