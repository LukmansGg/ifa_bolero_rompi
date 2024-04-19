import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS
from config import TOKEN

from programs.gpt import gpt3
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, msg):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    

    message = msg['text']
    answer = gpt3(message)

    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    try:
         bot.editMessageText((chat_id, message_id), answer, reply_markup=regenerate)
        db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})