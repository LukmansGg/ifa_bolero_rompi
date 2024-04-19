from tinydb import TinyDB
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def answeringMessage(bot_message, chat_id, message, response):
    bot_chat_id = bot_message['chat']['id']
    bot_message_id = bot_message['message_id']
    
    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    try:
        sent_message = bot.editMessageText((bot_chat_id, bot_message_id), response, reply_markup=regenerate)
        message_id = sent_message.get('message_id')
        db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})
    

def regenerate_answer():
    return "Wip"