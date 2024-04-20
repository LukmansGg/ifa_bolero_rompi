from tinydb import TinyDB
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def answeringMessage(bot_message, chat_id, message, response):
    bot_chat_id = bot_message['chat']['id']
    bot_message_id = bot_message['message_id']
    
    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-Generate', callback_data = 'regenerate')]])
    
    if response == "流量异常,请尝试更换网络环境":
       response = "[Error Lalu Lintas] > silakan coba ubah lingkungan jaringan, tunggu dan coba lagi beberapa saat"

    try:
        sent_message = bot.editMessageText((bot_chat_id, bot_message_id), response, reply_markup=regenerate)
        message_id = sent_message.get('message_id')
        db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})
    except telepot.exception.TelegramError as e:
        sent_message = bot.sendMessage(bot_chat_id, response, reply_markup=regenerate)
        message_id = sent_message.get('message_id')
        db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})
        pass


def editMessage(chat_id, message_id, message, keyboard=None):
    if keyboard:
        try:
            bot.editMessageText((chat_id, message_id), message, reply_markup = keyboard)
        except:
            bot.sendMessage(chat_id, message, reply_markup = keyboard)
            
    else:
        try:
            bot.editMessageText((chat_id, message_id), message)
        except:
            bot.sendMessage(chat_id, message)
    
