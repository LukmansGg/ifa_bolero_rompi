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

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Regenerate', callback_data = 'regenerate')]])

    question = 'jelaskan sejarah bolero/rompi secara singkat menurut beberapa sumber ini https://www.womanindonesia.co.id/sejarah-jaket-bolero-di-industri-fashion/  dan https://fitinline.com/article/read/vest/ dan https://kumparan.com/hijab-lifestyle/mengulik-sejarah-rompi-yang-sudah-populer-sejak-abad-ke-17-1y1JZmTp0ZL'
    response = gpt3(question)
    # Edit pesan asli dengan respon
    bot.editMessageText((from_id, original_message_id), response, reply_markup=keyboard)
    db.insert({'chat_id': from_id, 'message_id': original_message_id, 'question': message, 'answer': response})
  