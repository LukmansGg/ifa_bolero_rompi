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
from bot_analytics.callback import TELEGRAM_BOT_CALLBACKS

#sys.path.append('commands')

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        command_found = False
        
        for command in TELEGRAM_BOT_COMMANDS.keys():
            if command in message:
                command_found = True
                module_name = TELEGRAM_BOT_COMMANDS[command]
                module = importlib.import_module(module_name, ".")
                #display text
                bot_message = bot.sendMessage(chat_id, "tunggu...")
                module.command_handler(bot_message, msg)
                break  # keluar dari loop setelah menemukan perintah
                
        if not command_found:
            # hanya menjawab jika tidak ada perintah yang cocok
            try:
                bot.deleteMessage((chat_id, msg['message_id']))
            except telepot.exception.TelegramError as e:
                pass

            bot_message = bot.sendMessage(chat_id, "tunggu...")
            answer = gpt3(message + " bisakah membantu saya, apa fungsi /start, /tanya, dan /cari untuk menjalankan materi busana bolero dan rompi ini")
            answeringMessage(bot_message, chat_id, message, answer)

 
def handle_callback(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    callback_id = msg['id']

    for callback in TELEGRAM_BOT_CALLBACKS.keys():
        if callback == query_data:
            callback_found = True
            module_name = TELEGRAM_BOT_CALLBACKS[callback]
            module = importlib.import_module(module_name, ".")
            #display text
            bot.answerCallbackQuery(callback_id, "Menjalankan Perintah...")
            module.callback_handler(msg)
            break  # keluar dari loop setelah menemukan perintah

    if not command_found:
        # hanya menjawab jika tidak ada perintah yang cocok
        bot.answerCallbackQuery(callback_id, "Perintah Tidak Ditemukan")
            