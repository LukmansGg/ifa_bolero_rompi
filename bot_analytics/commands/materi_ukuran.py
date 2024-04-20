from programs.search import search
import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from programs.message import editMessage
from config import TOKEN
from programs.gpt import gpt3, gpt4


bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, user_message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = user_message['text']
    user_message_id = user_message['message_id']

    answer = gpt3('jelaskan cara mengukur bolero/rompi secara singkat menurut beberapa sumber ini 1. https://fitinline.com/article/read/cara-mengenali-bentuk-tubuh-wanita-agar-tidak-salah-membeli-baju/ 2. https://id.wikihow.com/Menentukan-Bentuk-Tubuh 3. https://stylo.grid.id/read/141277875/cara-mudah-mengetahui-bentuk-tubuh-dari-ukuran-dada-dan-pinggang?page=all 4. https://hellosehat.com/wanita/penyakit-wanita/bentuk-tubuh-wanita/ 5. https://www.liputan6.com/lifestyle/read/3101698/ketahui-dengan-pasti-bentuk-tubuh-anda-di-sini-yang-manakah')


    editMessage(chat_id, message_id, f"--Menyiapkan ukuran--\n[Bentuk tubuh]\n\nMengenali bentuk tubuh untuk mendapatkan pola busana yang pas pada pelanggan. Umumnya dikenali dari bentuk tubuh  terdiri dari artas ideal, tinggi kurus, tinggi gemuk, pendek kurus, pendek gemuk.\n\n{answer}", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Panduan ukuran",callback_data='panduanUkuran')], [InlineKeyboardButton(text="video penjelasan 1⏸", url="https://youtu.be/f0fKHhow6Pc")], [InlineKeyboardButton(text="video penjelasan 2⏸", url="https://youtu.be/n8Mqed5zwH4")]]))