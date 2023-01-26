import telegram
import logging
chat_id = '846524272' #Teste Daniel
tokenAllBot = "1951818889:AAGqVboLsy1iY8VT_DXhel189Q8o0wl4NeU"
bot = telegram.Bot(token=tokenAllBot)


def sendTelegramMessage(message, robotChatID):
    try:
        if (robotChatID != "") and (robotChatID != "false"):
            bot.sendMessage(chat_id=robotChatID, text=message)
    except:
        logging.info("ChatID inválido")


#message("O seu Robô: HardMarketBTC acabou de ser ativado")
#message("O seu Robô: HardMarketBTC realizou uma compra de U$40 em BTC")