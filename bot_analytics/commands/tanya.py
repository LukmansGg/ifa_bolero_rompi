import telepot
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.exception import TelegramError


TOKEN = '6569008899:AAF3DCqPjVg2Sgrr6lH8UDGawuZkB8psF1M'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    answer = gpt3(message)

    message_id = sent_message.get('message_id')
    chat_id = sent_message.get('chat_id')
    
    bot.editMessageText((chat_id, message_id), answer)