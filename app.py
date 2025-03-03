import sys
import os
import importlib
from flask import Flask, request
import telepot
from telepot.loop import WebhookServer, OrderedWebhook
from bot_analytics.operator import handle_message, handle_callback, handle_voice_message
from config import TOKEN, WEBHOOK_URL, PORT

app = Flask(__name__)
bot = telepot.Bot(TOKEN)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

@app.route('/ifaa', methods=['POST'])
def webhook():
    """
    Handles incoming Telegram webhook updates.
    """
    update = request.get_json()
    if not update:
        return "Invalid request", 400

    # Process different types of updates
    if 'message' in update:
        handle_message(update['message'])
    elif 'callback_query' in update:
        handle_callback(update['callback_query'])
    elif 'voice' in update:
        handle_voice_message(update['voice'])

    return "OK", 200

if __name__ == '__main__':
    # Set the webhook URL (your public server address)
    bot.setWebhook("technical-joann-lukman.koyeb.app/ifaa")

    # Run Flask app
    app.run(host='0.0.0.0', port=PORT)
