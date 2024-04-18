import telepot
from telepot.loop import MessageLoop

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, 'Anda mengirim: {}'.format(msg['text']))

TOKEN = '6653553439:AAH6C_O5fWysqxZchHDE-sRHsxBtTy2dGTs'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()

print('Bot sedang berjalan...')

while True:
    pass
  
