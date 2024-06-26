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
  # Dapatkan ID pesan dari data callback
  original_message_id = msg['message']['message_id']
  callback_id = msg['id']

  # Dapatkan ID obrolan dari data callback
  
  # Cari data pertanyaan yang sesuai dalam database
  Chat = Query()
  result = db.get(Chat.message_id == original_message_id)
  keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-Generate', callback_data = 'regenerate')]])

  if result:
    # Dapatkan pertanyaan dari hasil query
    question = result['question']
    response = gpt3(question)
    # Edit pesan asli dengan respon
    if result['header']:
        bot.editMessageText((from_id, original_message_id), result['header'] + response, parse_mode="HTML", reply_markup=keyboard)
    else:
        bot.editMessageText((from_id, original_message_id), response, parse_mode="HTML", reply_markup=keyboard)
  else:
    bot.answerCallbackQuery(callback_id, "Tidak Dapat Menemukan Pesan")
    pass

