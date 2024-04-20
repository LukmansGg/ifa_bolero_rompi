from programs.search import searching
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

    editMessage(chat_id, message_id, "---- **Merancang bahan** ----\n:[ Pemilihan bahan ]:\n\nSetelah mengetahui pola bolero/rompi selanjutnya ini adalah materi tentang bahanyang digunakan, baik bahan utama maupun pelengkap. Desain tertentu dari bolero/rompi harus menggunakan bahan pelapis, oleh karena itu analisis desain yang tepat akan membuat kita untuk dapat membuat daftar bahan yang sesuai dan harus disiapkan.\n\nBahan utama : bahan utama dipilih berdasarkan desain, kesempatan penggunaan, dan corak yang diinginkan. Jenis dari bahan apapun jika digunakan untuk bolero/rompi bisa saja tapia da beberapa bahan yang memang digunakan untuk bolero/rompi.\n\nBolero dapat menggunakan bahan duches, satin, brokat ataupun katun.\n\n • duches : https://fitinline.com/article/read/seperti-apa-karakteristik-kain-satin-bridal-itu/ \n • katun : https://tshirtbar.id/apa-itu-bahan-katun/ \n\nRompi biasanya hampir sama seperti jaket, antara lain wool, drill, garbadin dan lainnya.\n\n• Wool : https://ozzakonveksi.com/bahan-wool-ciri-ciri-jenis-kelebihan-kekurangan-wool/ \n • Drill : https://b-ori.kreasimultibisnis.co.id/penjelasan-bahan-kain-drill-lengkap/ \n • Garbadin : https://id.wikipedia.org/wiki/Gabardin", InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="next",callback_data='next_bahan')]]))