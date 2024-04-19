import sys
import os
import importlib
from flask import Flask, request
import telepot
from telepot.loop import MessageLoop
from bot_analytics.operator import handle_message
from config import TOKEN

sys.path.append('programs')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, {'chat': handle_message, 'callback_query': handle_callback}).run_as_thread()
    app.run(host='0.0.0.0', port=8000)
