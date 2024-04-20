import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from programs.message import editMessage
from config import TOKEN


bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, user_message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = user_message['text']
    user_message_id = user_message['message_id']

    editMessage(chat_id, message_id, "---- <b>Vidio Tutorial</b> ----\n\nSetelah mengetahui tentang berbagai macam materi tentang bolero/rompi terakhir akan diberikan link untuk melihat tutorial membuat bolero/rompi", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bolero⏸",url='https://youtu.be/YU4Ebfi5m8g')], [InlineKeyboardButton(text="Rompi⏸",url='https://youtu.be/pLHVbeERgFw')]]))