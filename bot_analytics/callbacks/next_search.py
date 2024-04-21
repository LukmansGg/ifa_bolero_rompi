from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import telepot
from programs.message import editMessage

bot = telepot.Bot(TOKEN)
chat_db = TinyDB('chat_data.json')
search_db = TinyDB('search_results.json')


def callback_handler(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    chat_message_id = msg['message']['message_id']
    callback_id = msg['id']

    query = Query()
    chat_result = chat_db.get(query.message_id == chat_message_id)
    if chat_result:
        message_search_id = chat_result['search_id']
        search_result = search_db.get(query.search_id == message_search_id)
        if search_result:
            next_page_value = chat_result['link_page'] + 1
            link = search_result['links'][next_page_value]
            title = link['title']
            description = link['description']
            url = link['link']
            
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='»Next»', callback_data='searchnext')], [InlineKeyboardButton(text='«Previous«', callback_data='searchback')]])
            editMessage(from_id, chat_message_id, f"<b>[{next_page_value + 1}/10] Hasil Pencarian: [{title}]</b>\n\n{description}\n\nsumber: {url}\n\npowered by [googlesearch]", keyboard)
            chat_db.update({'link_page': next_page_value}, query.message_id == chat_message_id)
            
    else:
        bot.answerCallbackQuery(callback_id, "Tidak Dapat Menemukan Pesan")
