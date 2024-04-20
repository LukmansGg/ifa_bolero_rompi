from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from programs.search import searching  # Pastikan untuk mengimpor searching
import random
from config import TOKEN
from programs.gpt import gpt3
import telepot

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')
search_db = TinyDB('search_results.json')  # Definisikan search_db


def callback_handler(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    original_message_id = msg['message']['message_id']

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Re-Generate', callback_data='pengertian')],
        [InlineKeyboardButton(text='« Back', callback_data='homepengertian')]
    ])

    question = 'jelaskan materi pengertian bolero dan rompi, baik dari perbedaan, asal usul, desain, dll'
    response = gpt3(question)
    # Edit pesan asli dengan respon

    result = searching("pengertian busana bolero dan rompi")
    query = Query()
    get_result = search_db.get(query.search_id == result)

    if get_result:
        links = get_result.get('links', [])
        if links:
            random_index = random.randint(0, min(9, len(links) - 1))  # Pastikan indeks tidak melebihi panjang list
            link = links[random_index]
            url = link['link']
            bot.editMessageText((from_id, original_message_id), f'<b>Pengertian Bolero dan Rompi</b>\n\nMenurut beberapa sumber:\n[ <b>{url}</b> ]\n\n{response}', parse_mode="HTML", reply_markup=keyboard)
        else:
            bot.editMessageText((from_id, original_message_id), f'<b>Pengertian Bolero dan Rompi</b>\n\nMenurut beberapa sumber:\n[ <b>https://kumparan.com/hijab-lifestyle/mengulik-sejarah-rompi-yang-sudah-populer-sejak-abad-ke-17-1y1JZmTp0ZL</b> ]\n\n{response}', parse_mode="HTML", reply_markup=keyboard)
    else:
        bot.editMessageText((from_id, original_message_id), f'<b>Pengertian Bolero dan Rompi</b>\n\nMenurut beberapa sumber:\n[ <b>https://www.womanindonesia.co.id/sejarah-jaket-bolero-di-industri-fashion/</b> ]\n\n{response}', parse_mode="HTML", reply_markup=keyboard)

    db.insert({'chat_id': from_id, 'message_id': original_message_id, 'question': question, 'answer': response})
