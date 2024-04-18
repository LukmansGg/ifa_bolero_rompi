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

def handle_callback(msg):
  query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

  # Temukan data pertanyaan yang sesuai dalam database
  Question = Query()
  result = db.search((Question.chat_id == from_id) & (Question.answer == query_data))

  if result:
      original_message_id = result[0]['message_id']
      response = gpt3(Question.question)
      bot.editMessageText((from_id, original_message_id), response)


MessageLoop(bot, {'chat': handle_message, 'callback_query': handle_callback}).run_as_thread()
