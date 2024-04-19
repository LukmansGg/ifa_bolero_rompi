from programs.search import search
import telepot
from tinydb import TinyDB, Query
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS
from config import TOKEN

from programs.search import search

bot = telepot.Bot(TOKEN)
search_db = TinyDB('search_results.json')
chat_db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    query = message['text']
    
    result = search(query)
    url = Query()
    get_result = search_db.get(url.search_id == result)
    
    if get_result:
        link = get_result['links'][0]
        title = link['title']
        description = link['description']
        url = link['link']
        

        chat_db.insert({'chat_id': chat_id, 'message_id': message_id, 'search_id': search_id, 'link_page': 0})
        try:
            bot.editMessageText((chat_id, message_id), )
        else:
            pass
    else:
        try:
            bot.editMessageText((chat_id, message_id), "Tidak ditemukan hasil pencarian untuk search_id yang diberikan")
        else:
            pass