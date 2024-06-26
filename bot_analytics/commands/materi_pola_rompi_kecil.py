from programs.search import searching
import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from programs.message import editMessage
from config import TOKEN
from programs.search import searching 
from programs.gpt import gpt3, gpt4


bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, user_message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = user_message['text']
    user_message_id = user_message['message_id']

    answer = gpt3('jelaskan cara membuat pola rompi dengan skala kecil, dan jelaskan berapa itu skala kecil biasanya pada kertas')


    editMessage(chat_id, message_id, f"-- <b>Membuat Pola Rompi</b> --\n:[ Pola Rompi Skala Kecil ]:\n\n{answer}\n\n[ <b>https://anyflip.com/xlqjt/wttc/basic</b> ]", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Re-Generate",callback_data='regenerate')]]))
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': 'jelaskan cara membuat pola rompi dengan skala kecil, dan jelaskan berapa itu skala kecil biasanya pada kertas', 'answer': answer, 'header': '-- <b>Membuat Pola Bolero</b> --\n:[ Pola Rompi Skala Kecil ]:\n\n'})
