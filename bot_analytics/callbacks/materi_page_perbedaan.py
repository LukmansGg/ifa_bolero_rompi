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

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='« Back', callback_data = 'homepengertian')]])

    question = 'jelaskan Perbedaan Pakaian Bolero dan Rompi dari segi desain, asal usul, proses pembuatan, dan bahan, sertakan juga sumber website nya'
    response = gpt3(question)
    # Edit pesan asli dengan respon
    bot.editMessageText((from_id, original_message_id), f'-<b>Pengertian Bolero dan Rompi</b>-\n:[ Perbedaan ]:\n\n{response}', parse_mode="HTML", reply_markup=keyboard)
    db.insert({'chat_id': from_id, 'message_id': original_message_id, 'question': question, 'answer': response})
  