import os
from flask import Flask, request
import telepot

from bot_analytics.operator import handle_message, handle_callback, handle_voice_message
from config import TOKEN, WEBHOOK_URL, PORT

app = Flask(__name__)
bot = telepot.Bot(TOKEN)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

@app.route('/ifaa', methods=['POST'])
def webhook():
    update = request.get_json()
    print("Webhook received:", update)  # Debugging output
    if not update:
        return "Invalid request", 400

    # Process different types of updates
    if 'message' in update:
        handle_message(update)
    elif 'callback_query' in update:
        handle_callback(update)
    elif 'voice' in update:
        handle_voice_message(update)
    
    if "message" in update:
        handle_message(update["message"])
    else:
        print("No 'message' key in update:", update)
    
    return "OK", 200

if __name__ == '__main__':
    # Set webhook on Telegram
    bot.setWebhook(f"{WEBHOOK_URL}/ifaa")

    # Run Flask app
    app.run(host='0.0.0.0', port=PORT)
