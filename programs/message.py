from tinydb import TinyDB
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6569008899:AAGKZ6ZAi1d_JDYCDZJ9vaGZVi3pItlw56w'
bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def answeringMessage(chat_id, message, response):
    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    sent_message = bot.sendMessage(chat_id, response, reply_markup=regenerate)
    message_id = sent_message.get('message_id')
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})

def regenerate_answer():
    return "Wip"