import telepot
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.exception import TelegramError
from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from config import TOKEN

from programs.gpt import gpt3, gpt4
from programs.message import editMessage
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')
user_db = TinyDB('all_user_id.json')

def command_handler(sent_message, msg):
    message = msg['text']
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    user_message_id = msg['message_id']
    if message == "/broadcast":
        try:
            bot.deleteMessage((chat_id, user_message_id))
        except TelegramError as e:
            pass

        editMessage(chat_id,message_id,  "Mohon Anda masukan kata/kalimat yang ingin anda broadcast pada pengguna lain\ncontoh: '/broadcast info menjual busana bolero'")

    else:
        news = message.replace("/tanya","")
         
        try:
            bot.deleteMessage((chat_id, message_id))
        except TelegramError as e:
            pass
        all_users = user_db.all()
    
        for user_data in all_users:
            user_id = user_data['user_id']
            bot.sendMessage(user_id, news)
        