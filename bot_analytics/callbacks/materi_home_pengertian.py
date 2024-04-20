import os
import sys
import importlib
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage
from bot_analytics.command import TELEGRAM_BOT_COMMANDS

#sys.path.append('commands')

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')


def callback_handler(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    original_message_id = msg['message']['message_id']

    bot.editMessageText((from_id, original_message_id), "Disini kita akan belajar Materi Pengertian tentang bolero/rompi berikut, pilih salah satu👇", InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="› Sejarah Bolero/Rompi ‹",callback_data='sejarah')],
        [InlineKeyboardButton(text="› Pengertian Bolero/Rompi ‹",callback_data='pengertian')],
        [InlineKeyboardButton(text="› Perbedaan Bolero/Rompi ‹",callback_data='perbedaan')],
        [InlineKeyboardButton(text="› Desain Bolero/Rompi ‹",callback_data='desain')],
        [InlineKeyboardButton(text="› Macam Bolero/Rompi ‹",callback_data='macam')]
    ]), text="Teks baru di sini")
