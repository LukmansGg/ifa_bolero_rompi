import telepot
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.exception import TelegramError

from programs.gpt import gpt3

TOKEN = '6569008899:AAF3DCqPjVg2Sgrr6lH8UDGawuZkB8psF1M'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    answer = gpt3(message)

    message_id = sent_message.get('message_id')
    chat_id = sent_message.get('chat_id')
    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    bot.editMessageText((chat_id, message_id), answer, reply_markup=regenerate)
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})