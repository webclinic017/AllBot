import telegram
from datetime import datetime

chat_id = '846524272'  # Daniel

bot = telegram.Bot(token="1390390997:AAG26GJIhsqkhxkqKCXZ0I3K_GnQ4E69zLY")


def startOperation(robot, asset, timeframe, lot, sl, tp):
    """Envia uma notificação de nova operação"""

    bot.sendMessage(chat_id=chat_id,
                    text='NOVA OPERAÇÃO' + '\n\n'
                         + 'Data/Hora: ' + datetime.now().strftime('%d/%m/%Y %H:%M') + '\n'
                         + 'Robô: ' + str(robot) + '\n'
                         + 'Ativo: ' + str(asset) + '\n'
                         + 'Timeframe: ' + str(timeframe) + '\n'
                         + 'Lote: ' + str(lot) + '\n'
                         + 'Stop Loss: ' + str(sl) + '\n'
                         + 'Take Profit: ' + str(tp))
