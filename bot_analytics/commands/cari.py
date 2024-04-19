from programs.search import search
import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS
from config import TOKEN

from programs.search import search

bot = telepot.Bot(TOKEN)
db = TinyDB('search_results.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    query = message['text']
    
    result = search(query)
    try:
        bot.editMessageText((chat_id, message_id), )