import os
import importlib
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage

TOKEN = '6569008899:AAF3DCqPjVg2Sgrr6lH8UDGawuZkB8psF1M'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        for command in TELEGRAM_COMMANDS.keys():
            if command in message:
                module_name = TELEGRAM_COMMANDS[command]
                module = importlib.import_module(module_name)
                # runing command class
                module.handle_command()
            else:
                answer = gpt3(message)
                answeringMessage(chat_id, message, answer)
 
