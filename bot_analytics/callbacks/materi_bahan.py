import os
import sys
import importlib
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage
from bot_analytics.command import TELEGRAM_BOT_COMMANDS

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')


def callback_handler(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    original_message_id = msg['message']['message_id']

    bot.editMessageText((from_id, original_message_id), text="---- <b>Merancang bahan</b> ----\n:[ Pemilihan bahan 1/2 ]:\n\nSetelah mengetahui pola bolero/rompi selanjutnya ini adalah materi tentang bahanyang digunakan, baik bahan utama maupun pelengkap. Desain tertentu dari bolero/rompi harus menggunakan bahan pelapis, oleh karena itu analisis desain yang tepat akan membuat kita untuk dapat membuat daftar bahan yang sesuai dan harus disiapkan.\n\nBahan utama : bahan utama dipilih berdasarkan desain, kesempatan penggunaan, dan corak yang diinginkan. Jenis dari bahan apapun jika digunakan untuk bolero/rompi bisa saja tapia da beberapa bahan yang memang digunakan untuk bolero/rompi.\n\nBolero dapat menggunakan bahan duches, satin, brokat ataupun katun.\n\n • duches : https://fitinline.com/article/read/seperti-apa-karakteristik-kain-satin-bridal-itu/ \n • katun : https://tshirtbar.id/apa-itu-bahan-katun/ \n\nRompi biasanya hampir sama seperti jaket, antara lain wool, drill, garbadin dan lainnya.\n\n• Wool : https://ozzakonveksi.com/bahan-wool-ciri-ciri-jenis-kelebihan-kekurangan-wool/ \n • Drill : https://b-ori.kreasimultibisnis.co.id/penjelasan-bahan-kain-drill-lengkap/ \n • Garbadin : https://id.wikipedia.org/wiki/Gabardin", parse_mode='HTML', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Next »",callback_data='next_bahan')], [InlineKeyboardButton(text="Bolero⏸", url='https://youtu.be/sManT9-Cvas')], [InlineKeyboardButton(text="Rompi⏸", url='https://youtu.be/tKIfMwN28EM')]]))

