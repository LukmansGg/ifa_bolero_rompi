


def answeringMessage(chat_id, message, response):
    regenerate = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Re-generate', callback_data = 'regenerate')]])
    sent_message = bot.sendMessage(chat_id, response, reply_markup=keyboard)
    message_id = sent_message.get('message_id')
    db.insert({'chat_id': chat_id, 'message_id': message_id, 'question': message, 'answer': response})