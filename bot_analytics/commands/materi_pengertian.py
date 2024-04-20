
def command_handler(sent_message, user_message):
    bot.sendMessage(chat_id, "Disini kita akan belajar Materi Pengertian tentang bolero/rompi berikut, pilih salah satu👇", reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="> Sejarah Bolero/Rompi <",callback_data='sejarah')],
        [InlineKeyboardButton(text="> Pengertian Bolero/Rompi <",callback_data='pengertian')],
        [InlineKeyboardButton(text="> Perbedaan Bolero/Rompi <",callback_data='perbedaan')],
        [InlineKeyboardButton(text="> Desain Bolero/Rompi <",callback_data='desain')],
        [InlineKeyboardButton(text="> Macam Bolero/Rompi <",callback_data='macam')]
    ]))