import sys
import os
from flask import Flask, request
import telepot
from telepot.loop import MessageLoop
from bot_analytics.operator import handle_message

sys.path.append('programs')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

if __name__ == '__main__':
    TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, {'chat': handle_message}).run_as_thread()
    app.run(debug=True, host='0.0.0.0', port=8000)
