from programs.search import search
import telepot
from telepot.exception import TelegramError
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from programs.message import editMessage
from config import TOKEN


bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')

def command_handler(sent_message, user_message):
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    message_text = user_message['text']
    user_message_id = user_message['message_id']

    editMessage(chat_id, message_id, "--Menyiapkan ukuran--\n[Bentuk tubuh]\n\nMengenali bentuk tubuh untuk mendapatkan pola busana yang pas pada pelanggan. Umumnya dikenali dari bentuk tubuh  terdiri dari artas ideal, tinggi kurus, tinggi gemuk, pendek kurus, pendek gemuk. Dari lima bentuk tersebut berikut merupakan web yang menyertakan artikel untuk mengetahui bentuk tubuh :\n\n - https://fitinline.com/article/read/cara-mengenali-bentuk-tubuh-wanita-agar-tidak-salah-membeli-baju/\n  - https://id.wikihow.com/Menentukan-Bentuk-Tubuh \n - https://stylo.grid.id/read/141277875/cara-mudah-mengetahui-bentuk-tubuh-dari-ukuran-dada-dan-pinggang?page=all \n - https://hellosehat.com/wanita/penyakit-wanita/bentuk-tubuh-wanita/ \n - https://www.liputan6.com/lifestyle/read/3101698/ketahui-dengan-pasti-bentuk-tubuh-anda-di-sini-yang-manakah \n - https://www.stylecraze.com/articles/different-body-shapes-of-women/", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Panduan ukuran",callback_data='panduanUkuran')], [InlineKeyboardButton(text="video penjelasan 1⏸", url="https://youtu.be/f0fKHhow6Pc")], [InlineKeyboardButton(text="video penjelasan 2⏸", url="https://youtu.be/n8Mqed5zwH4")]]))