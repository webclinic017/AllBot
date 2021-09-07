import telegram

chat_id = '846524272'
tokenLS = "1390390997:AAG26GJIhsqkhxkqKCXZ0I3K_GnQ4E69zLY"
tokenAllBot = "1951818889:AAGqVboLsy1iY8VT_DXhel189Q8o0wl4NeU"
bot = telegram.Bot(token=tokenAllBot)


def sendTelegramMessage(message, robotChatID):
    if robotChatID != "":
        bot.sendMessage(chat_id=robotChatID, text=message)

#message("O seu Robô: HardMarketBTC acabou de ser ativado")


#message("O seu Robô: HardMarketBTC realizou uma compra de U$40 em BTC")