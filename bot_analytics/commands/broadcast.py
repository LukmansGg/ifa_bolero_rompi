import telepot
from tinydb import TinyDB
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.exception import TelegramError
from bot_analytics.command import TELEGRAM_BOT_COMMANDS
from config import TOKEN

from programs.gpt import gpt3, gpt4
from programs.message import editMessage

bot = telepot.Bot(TOKEN)
db = TinyDB('chat_data.json')
user_db = TinyDB('all_user_id.json')

def command_handler(sent_message, msg):
    message = msg['text']
    chat_id = sent_message['chat']['id']
    message_id = sent_message['message_id']
    user_message_id = msg['message_id']

    if message == "/broadcast":
        try:
            bot.deleteMessage((chat_id, user_message_id))
        except TelegramError:
            pass

        editMessage(chat_id, message_id, "Mohon Anda masukkan kata/kalimat yang ingin Anda broadcast pada pengguna lain.\nContoh: '/broadcast info menjual busana bolero'")

    elif message == "/broadcast id":
        try:
            bot.deleteMessage((chat_id, user_message_id))
        except TelegramError:
            pass

        all_users = user_db.all()
        user_ids = [str(user['user_id']) for user in all_users]  # Extract user IDs

        if user_ids:
            user_list = "\n".join(user_ids)
        else:
            user_list = "Tidak ada pengguna yang terdaftar."

        editMessage(chat_id, message_id, user_list)

    else:
        news = message.replace("/broadcast", "").strip()

        try:
            bot.deleteMessage((chat_id, message_id))
        except TelegramError:
            pass

        all_users = user_db.all()

        for user_data in all_users:
            user_id = user_data.get('user_id')
            if user_id:
                try:
                    bot.sendMessage(user_id, news, parse_mode='HTML')
                except TelegramError as e:
                    print(f"Gagal mengirim ke {user_id}: {e}")
