import os
import sys
import time
import uuid
import importlib
from tinydb import TinyDB, Query
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import assemblyai as aai

from config import TOKEN, AAI_TOKEN
from programs.gpt import gpt3
import telepot
from programs.message import answeringMessage
from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from bot_analytics.callback import TELEGRAM_BOT_CALLBACKS

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')
user_db = TinyDB('all_user_id.json')
welcome_db = TinyDB('welcome_chat.json')

aai.settings.api_key = AAI_TOKEN
transcriber = aai.Transcriber()

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        message_id = msg['message_id']
        User = Query()
        if user_db.search(User.user_id == chat_id):
            pass
        else:
            user_db.insert({'user_id': chat_id})
    
        command_found = False
        
        for command in TELEGRAM_BOT_COMMANDS.keys():
            if command in message:
                command_found = True
                module_name = TELEGRAM_BOT_COMMANDS[command]
                module = importlib.import_module(module_name, ".")
                #display text
                bot_message = bot.sendMessage(chat_id, "tunggu...", reply_to_message_id=message_id)
                if "/start" in message:
                    pass
                elif "/mulai" in message:
                    pass
                else:
                    unique_id = str(uuid.uuid4())
                    welcome_db.insert({'id': unique_id, 'chat_id': chat_id, 'message_id': message_id, 'sent_message_id': bot_message['message_id'], 'is_welcome': False})

                module.command_handler(bot_message, msg)
                break  # keluar dari loop setelah menemukan perintah
                
        if not command_found:
            # hanya menjawab jika tidak ada perintah yang cocok
            try:
                bot.deleteMessage((chat_id, msg['message_id']))
            except telepot.exception.TelegramError as e:
                pass

            prompt = f"kamu adalah bot dan user mengetik: {message}, pandu user dengan command, /mulai untuk memulai bot, /tanya untuk bertanya seputar bolero/rompi dan /cari untuk mencari informasi seputar bolero/rompi, parse_mode=HTML"
            bot_message = bot.sendMessage(chat_id, "tunggu...")
            answer = gpt3(prompt)
            answeringMessage(bot_message, chat_id, prompt, answer)
 
def handle_callback(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    callback_id = msg['id']
    callback_found = False
    User = Query()
    if user_db.search(User.user_id == from_id):
        pass
    else:
        user_db.insert({'user_id': from_id})

    for callback in TELEGRAM_BOT_CALLBACKS.keys():
        if callback == query_data:
            callback_found = True
            module_name = TELEGRAM_BOT_CALLBACKS[callback]
            module = importlib.import_module(module_name, ".")
            #display text
            bot.answerCallbackQuery(callback_id, "Tunggu Beberapa Saat...")
            module.callback_handler(msg)
            break  # keluar dari loop setelah menemukan perintah

    if not callback_found:
        # hanya menjawab jika tidak ada perintah yang cocok
        bot.answerCallbackQuery(callback_id, "Perintah Tidak Ditemukan")


def handle_voice_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Memeriksa apakah pesan merupakan pesan suara
    if content_type == 'voice':
        # Mendapatkan file_id dari pesan suara
        file_id = msg['voice']['file_id']
        # Mendapatkan informasi tentang file suara menggunakan file_id
        file_info = bot.get_file(file_id)
        # Mendapatkan URL file suara
        file_url = "https://api.telegram.org/file/bot{}/{}".format(TOKEN, file_info['file_path'])

        # Melakukan transkripsi menggunakan AssemblyAI
        transcript = transcriber.transcribe(file_url)
        # Mengirimkan hasil transkripsi kembali ke pengguna
        bot.sendMessage(chat_id, transcript.text)


            