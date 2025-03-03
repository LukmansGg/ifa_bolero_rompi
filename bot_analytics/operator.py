import os
import sys
import time
import uuid
import importlib
import requests
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
    print(f"Processing message from {chat_id}: {msg}")
    
    if content_type == 'text':
        message = msg.get('text', '')  # ✅ Use `.get()` to prevent KeyError
        message_id = msg.get('message_id')

        User = Query()
        if not user_db.search(User.user_id == chat_id):
            user_db.insert({'user_id': chat_id})
        
        command_found = False

        for command in TELEGRAM_BOT_COMMANDS.keys():
            if message.startswith(command):  # ✅ Use `startswith` for accuracy
                command_found = True
                module_name = TELEGRAM_BOT_COMMANDS[command]
                module = importlib.import_module(module_name, ".")
                
                bot_message = bot.sendMessage(chat_id, "⏳ Tunggu sebentar...", reply_to_message_id=message_id)
                
                try:
                    module.command_handler(bot_message, msg)
                except Exception as e:
                    bot.sendMessage(chat_id, f"⚠️ Terjadi kesalahan: {str(e)}")
                break  

        if not command_found:
            try:
                prompt = (
                    f"Kamu adalah bot dan user mengetik: {message}. "
                    f"Pandu user dengan command: /mulai untuk memulai bot, /tanya untuk bertanya seputar bolero/rompi, dan /cari untuk mencari informasi."
                )
                
                bot_message = bot.sendMessage(chat_id, "⏳ Tunggu sebentar...")
                answer = gpt3(prompt)
                answeringMessage(bot_message, chat_id, prompt, answer)
            
            except Exception as e:
                bot.sendMessage(chat_id, f"⚠️ Gagal menghasilkan jawaban: {str(e)}")

def handle_callback(msg):
    try:
        # Ensure we access 'callback_query' correctly
        callback_query = msg.get("callback_query", {})
        query_id = callback_query.get("id", None)
        from_id = callback_query.get("from", {}).get("id", None)
        query_data = callback_query.get("data", None)

        if query_id is None or from_id is None or query_data is None:
            print(f"⚠️ Invalid callback data received: {msg}")
            return

        # Save user ID if not already in the database
        User = Query()
        if not user_db.search(User.user_id == from_id):
            user_db.insert({'user_id': from_id})

        # Process callback command
        if query_data in TELEGRAM_BOT_CALLBACKS:
            module_name = TELEGRAM_BOT_CALLBACKS[query_data]
            module = importlib.import_module(module_name, ".")

            bot.answerCallbackQuery(query_id, "⏳ Tunggu sebentar...")

            try:
                module.callback_handler(callback_query)
            except Exception as e:
                bot.sendMessage(from_id, f"⚠️ Callback gagal: {str(e)}")

        else:
            bot.answerCallbackQuery(query_id, "⚠️ Callback tidak dikenal.")
            print(f"⚠️ Unknown callback received: {query_data}")

    except Exception as e:
        print(f"⚠️ Error handling callback: {str(e)}")


def handle_voice_message(msg):
    try:
        message = msg.get("message", {})
        if "voice" not in message:
            return

        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'voice':
            file_id = message["voice"].get("file_id", None)
            if not file_id:
                bot.sendMessage(chat_id, "⚠️ File ID tidak ditemukan.")
                return

            # Get file from Telegram
            try:
                file_info = bot.getFile(file_id)
                file_path = file_info['file_path']
                file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
                local_filename = f"temp_voice_{uuid.uuid4()}.ogg"

                response = requests.get(file_url, timeout=10)
                if response.status_code == 200:
                    with open(local_filename, 'wb') as f:
                        f.write(response.content)
                else:
                    bot.sendMessage(chat_id, "⚠️ Gagal mengunduh pesan suara.")
                    return
            except requests.RequestException as e:
                bot.sendMessage(chat_id, f"⚠️ Error saat mengunduh suara: {str(e)}")
                return

            # Transcribe using AssemblyAI
            try:
                upload_url = aai.upload(local_filename)
                transcript = transcriber.transcribe(upload_url)

                if transcript.text:
                    bot.sendMessage(chat_id, f"🎙 Transkripsi: {transcript.text}")
                else:
                    bot.sendMessage(chat_id, "⚠️ Gagal mentranskripsi suara.")
            except Exception as e:
                bot.sendMessage(chat_id, f"⚠️ Gagal memproses pesan suara: {str(e)}")

            finally:
                if os.path.exists(local_filename):
                    os.remove(local_filename)

    except Exception as e:
        print(f"⚠️ Error handling voice message: {str(e)}")
