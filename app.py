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
    print("📩 Webhook received:", update)  # Debugging output
    if not update:
        return "Invalid request", 400

    try:
        if "message" in update:
            if "voice" in update["message"]:
                handle_voice_message(update["message"])
            else:
                handle_message(update["message"])
        elif "callback_query" in update:
            handle_callback(update)
        else:
            print("Unhandled update type:", update)
    except Exception as e:
        print("Error processing update:", str(e))

    return "OK", 200

if __name__ == '__main__':
    # Ensure PORT is an integer
    try:
        PORT = int(PORT)
    except ValueError:
        print("Invalid PORT value in config.py")
        PORT = 8000  # Default to 8000

    # Set webhook on Telegram
    bot.setWebhook(f"{WEBHOOK_URL}/ifaa")

    # Run Flask app
    app.run(host='0.0.0.0', port=PORT)
