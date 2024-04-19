from programs.search import search
import telepot
from tinydb import TinyDB
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from bot_analytics.command import TELEGRAM_COMMANDS
from config import TOKEN

from programs.search import search

bot = telepot.Bot(TOKEN)
db = TinyDB('search_results.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    query = message['text']
    
    result = search(query)
    url = Query()
    get_result = db.get(url.search_id == result)
    
    if get_result:
        # Jika entri ditemukan, ambil links dari entri pertama
        links = get_result['links'][0]
        
        # Loop through each link and print title, description, and link
        link = get_result['links'][0]
        title = link['title']
        description = link['description']
        url = link['link']
        

        db.insert({'chat_id': chat_id, 'message_id': message_id, 'search_id': search_id, 'link_page': 0})

        bot.editMessageText((chat_id, message_id), )
    else:
        print("Tidak ditemukan hasil pencarian untuk chat_id dan message_id yang diberikan")