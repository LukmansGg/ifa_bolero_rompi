import telepot
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.exception import TelegramError
from bot_analytics.operator import TOKEN

from programs.gpt import gpt3

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(bot_message, user_message):
    content_type, chat_type, chat_id = telepot.glance(user_message)
    sent_message = telepot.message_identifier(bot_message)
    
    message = msg['text']
    answer = gpt3(message)

    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    bot.editMessageText(sent_message, answer, reply_markup=regenerate)
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})