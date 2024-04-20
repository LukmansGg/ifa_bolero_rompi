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

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='penjelasan', url = 'https://prezi.com/p/tqd0rdnwggrf/bolero-dan-rompi/')], [InlineKeyboardButton(text='« Back', callback_data = 'home_pengertian')]])

    question = 'jelaskan Macam Macam Pakaian Bolero dan Rompi dari detail atau desainnya dan sertakan juga sumber website nya'
    response = gpt3(question)
    # Edit pesan asli dengan respon
    bot.editMessageText((from_id, original_message_id), f'-<b>Pengertian Bolero dan Rompi</b>-\n:[ Desain ]:\n\n{response}\n• https://fitinline.com/article/read/jenis-bolero/\n• https://wevagarment.com/blog/jenis-jenis-rompi-konveksi-surabaya/', parse_mode="HTML", reply_markup=keyboard)
    db.insert({'chat_id': from_id, 'message_id': original_message_id, 'question': question, 'answer': response})
  