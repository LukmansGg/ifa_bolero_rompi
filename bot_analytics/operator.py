import os
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from programs.gpt import gpt3
import telepot

TOKEN = '6569008899:AAF3DCqPjVg2Sgrr6lH8UDGawuZkB8psF1M'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        response = gpt3(message)
        db.insert({'chat_id': chat_id, 'question': message, 'answer': response})

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Regenerate', callback_data='regenerate')]])
        bot.sendMessage(chat_id, response, reply_markup=keyboard)
 
