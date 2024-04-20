import telepot
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.exception import TelegramError
from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from config import TOKEN

from programs.gpt import gpt3
from programs.message import editMessage
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, msg):
    message = msg['text']
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    user_message_id = msg['message_id']
    if message == "/tanya":
        try:
            bot.deleteMessage((chat_id, user_message_id))
        except TelegramError as e:
            pass

        editMessage(chat_id,message_id,  "Mohon Anda masukan kata/kalimat yang ingin anda tanyakan\ncontoh: '/tanya apa itu bolero dan rompi'")

    else:
        query = message.replace("/tanya","")
        answer = gpt3(query + " pada busana bolero dan busana rompi")
        
        regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
        
        editMessage(chat_id, message_id, answer, regenerate)
        db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': query, 'answer': answer})
        