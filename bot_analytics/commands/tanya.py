import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS
from config import TOKEN

from programs.gpt import gpt3
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, msg):
    message = msg['text']
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    user_message_id = msg['message_id']
    if message == "/tanya":
        try:
            bot.deleteMessage(chat_id, user_message_id)
        except TelegramError as e:
            bot.sendMessage(chat_id, "Mohon Anda masukan kata/kalimat yang ingin anda tanyakan\ncontoh: '/tanya apa itu bolero dan rompi'")
            pass
    else:
        query = message.replace("/tanya","")
        answer = gpt3(query + " pada busana bolero dan busana rompi")
        
        regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
        
        try:
            bot.editMessageText((chat_id, message_id), answer, reply_markup=regenerate)
            db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': query, 'answer': response})
        except telepot.exception.TelegramError as e:
            pass