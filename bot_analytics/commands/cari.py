from programs.search import searching
import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from programs.message import editMessage
from config import TOKEN

from programs.search import search

bot = telepot.Bot(TOKEN)
search_db = TinyDB('search_results.json')
chat_db = TinyDB('chat_data.json')

def command_handler(sent_message, message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = message['text']
    user_message_id = message['message_id']
    
    if message_text == "/cari":
        try:
            bot.deleteMessage((chat_id, user_message_id))
 
        except TelegramError as e:
            pass

        editMessage(chat_id, message_id, "Mohon Anda masukan kata/kalimat yang ingin di cari\ncontoh: '/cari busana bolero'")
            
    else:
        query = message_text.replace("/cari","")
        result = searching(query + " dalam bolero/rompi")
        test = Query()
        get_result = search_db.get(test.search_id == result)
        
        if get_result:
            link = get_result['links'][0]
            title = link['title']
            description = link['description']
            url = link['link']
            
            try:
                chat_db.insert({'chat_id': chat_id, 'message_id': message_id, 'search_id': result, 'link_page': 0})
            except:
                pass

            editMessage(chat_id, message_id, f"[1/20]\n<b>Hasil Pencarian🔎:\n [{title}]</b>\n\n{description}\n\n[ <b>{url}</b> ]\n\npowered by [googlesearch]", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="next",callback_data='searchnext')]]))
            
        else:
            editMessage(chat_id, message_id, f"Tidak ditemukan hasil pencarian untuk *[ search-id: {query} ]* yang diberikan")
