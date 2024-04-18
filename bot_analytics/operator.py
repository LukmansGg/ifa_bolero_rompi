from programs.gpt import gpt3
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
import os
from tinydb import TinyDB, Query


TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')


def handle_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == 'text':
    message = msg['text']
    response = gpt3(message)
    db.insert({'chat_id': chat_id, 'question': message, 'answer': response})

        # 
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Regenerate', callback_data='regenerate')]])
    bot.sendMessage(chat_id, response, reply_markup=keyboard)


MessageLoop(bot, {'chat': handle_message}).run_as_thread()
