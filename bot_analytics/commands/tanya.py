
def command_handler(sent_message, message):
    answer = gpt3(message)
    answeringMessage(chat_id, message, answer)
