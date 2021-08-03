import telegram

chat_id = '846524272'
bot = telegram.Bot(token="1390390997:AAG26GJIhsqkhxkqKCXZ0I3K_GnQ4E69zLY")


def message(message):
    bot.sendMessage(chat_id=chat_id, text=message)
