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

    bot.editMessageText((from_id, original_message_id), "nBahan pelengkap : terdiri sebagai memenuhi kebutuhan informasi,penunjng,fungsi, dn estetik (pemanis).Maksud dari hal tersebut  berisi tentang \n a. Informasi : label berisi informasi yang menerangkan segala sesuatu tentang produk. Label biasanya diberikan pada baju dan merk yang tergantung pada busana terbuat dari kertas yang menempel/menggantung.\nb. Penunjng : bahan yang digunkn untuk menunjang untuk membentuk dan jtuhnya bahan tersebut pada badan seseorang.\nc. Benang jahit : dipilih warna yang sama dengan bahan utama atau 1 tingkat lebih tua dari warna bahan. Benang warna lain dapat dipilih sebagai benang hias. Untuk ketebalan bahan juga disesuaikan dengan benang jahit supaya setelah dijahit setrikannya kuat.\nd. Bahan pelapis : biasanya dibuat untuk furing, dikarenakan rompi dibuat berdasarkan konstruksi jas/jaket.bolero/rompi juga menggunakan bahan pelapis  yang terdiri atas : underlining, interfacing, interlining, lining.\ne. Fungsi : seperti kancing dan resleting, berfungsi sebagai opening atau mempermudah saat memakai bolero/rompi\nf. Estetika (pemanis) : seperti renda/payet dulu digunakan sebagai garniture. Sekarang kain perca yang dibentuk akan memberi nilai jual juga. Kancing dengan desain tertentu juga dapat digunakan sebagai hiasan, begitu pula benang dan resleting juga dapat dimanfaatkan", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="« Back", callback_data='materi_bahan')]]))

