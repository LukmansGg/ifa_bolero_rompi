import os
import sys
import importlib
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage
from bot_analytics.command import TELEGRAM_COMMANDS

sys.path.append('commands')

TOKEN = '6569008899:AAEJMUCCuusUiMy64z9UaCvzJIhgtLpYjPA'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        for command in TELEGRAM_COMMANDS.keys():
            if command in message:
                module_name = TELEGRAM_COMMANDS[command]
                module = importlib.import_module(module_name, ".")
                #display text
                sent_message = bot.sendMessage(chat_id, "tunggu...")
                
                # runing command class
                module.command_handler(sent_message, message)
            else:
                answer = gpt3(message)
                answeringMessage(chat_id, message, answer)
 
