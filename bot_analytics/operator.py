import os
import sys
import importlib
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage
from bot_analytics.command import TELEGRAM_BOTS_COMMANDS

#sys.path.append('commands')

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        command_found = False
        
        for command in TELEGRAM_BOTS_COMMANDS.keys():
            if command in message:
                command_found = True
                module_name = TELEGRAM_COMMANDS[command]
                module = importlib.import_module(module_name, ".")
                #display text
                bot_message = bot.sendMessage(chat_id, "tunggu...")
                module.command_handler(bot_message, msg)
                break  # keluar dari loop setelah menemukan perintah
                
        if not command_found:
            # hanya menjawab jika tidak ada perintah yang cocok
            bot_message = bot.sendMessage(chat_id, "tunggu...")
            answer = gpt3(message)
            answeringMessage(bot_message, chat_id, message, answer)

 
def handle_callback(msg):
  query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
  # Dapatkan ID pesan dari data callback
  original_message_id = msg['message']['message_id']

  # Dapatkan ID obrolan dari data callback
  
  # Cari data pertanyaan yang sesuai dalam database
  Chat = Query()
  result = db.get(Chat.message_id == original_message_id)
  keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Regenerate', callback_data = 'regenerate')]])

  if result:
    # Dapatkan pertanyaan dari hasil query
    question = result['question']
    response = gpt3(question)
    # Edit pesan asli dengan respon
    bot.editMessageText((from_id, original_message_id), response, reply_markup=keyboard)
  else:
    # Jika tidak ada entri yang cocok dalam database
    error_message = "Error: No matching entry found in the database."
    # Kirim pemberitahuan langsung ke pengguna melalui bot Telegram
    bot.editMessageText((from_id, original_message_id), error_message, reply_markup=keyboard)
    # Tampilkan ID pesan callback
    bot.sendMessage(from_id, f"Callback message ID: {original_message_id}")
    # Tampilkan semua ID pesan yang ada dalam database
    all_messages = db.all()
    message_ids = [entry['message_id'] for entry in all_messages if 'message_id' in entry]
    bot.sendMessage(from_id, f"All message IDs in database: {message_ids}")

