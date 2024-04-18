import telepot
from telepot.loop import MessageLoop
from g4f.client import Client


client = Client()
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}]
        )
        
        bot.sendMessage(chat_id, response.choices[0].message.content)

TOKEN = '6653553439:AAH6C_O5fWysqxZchHDE-sRHsxBtTy2dGTs'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()

print('Bot sedang berjalan...')

while True:
    pass
  
