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

    editMessage(chat_id, message_id, "--pola bolero--\n[Alat dan bahan]\n\nMenyiapkan alat dan bahan untuk membuat bolero/rompi dengan sebagai berikut :\nAlat :\na. Pensil hitam 2b \nb. Pita ukur (metlin)\nc. Penggaris pola\nd. Busur, penghapus\ne. Pensil merah biru, gunting kertas, dan lem\nf. Piranti menjahit\ng. Mesin jahit\nh. Mesin pres\n\nBahan :\na. Benang jahit\nb. Kancing\nc. Fiselin\nd. Kertas doslah merah biru \ne. Kertas payung\nf. Bahan bolero/rompi, bahan furing\n\n", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="next", callback_data='pola')]]))