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
        links = get_result[0]['links']
        
        # Loop through each link and print title, description, and link
        for link in links:
            title = link['title']
            description = link['description']
            url = link['link']
            print(f"Judul: {title}")
            print(f"Deskripsi: {description}")
            print(f"Tautan: {url}")

        bot.editMessageText((chat_id, message_id), )
    else:
        print("Tidak ditemukan hasil pencarian untuk chat_id dan message_id yang diberikan")