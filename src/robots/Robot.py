from src.marketData.IndicatorsManager import indicators
from src.marketData.RoteamentoManager import buyMarket, sellMarket, closePosition
from datetime import datetime


class Robot:
    """Define a estrutura básica de um robô"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify):
        self.robotType = "Robot"
        self.id = id
        self.key = key
        self.secret = secret
        self.nickName = nickName
        self.symbol = symbol
        self.timeframe = timeframe
        self.quantity = quantity
        self.intervalBegin = intervalBegin
        self.intervalEnd = intervalEnd
        self.comb = self.symbol + '/' + self.timeframe
        self.inPosition = inPosition
        self.chatID = chatID
        self.onlyNotify = onlyNotify
        self.side = ''

    def checkTimeRestrictions(self):
        """Verifica as restrições de horário"""
        currentTime = datetime.now().time()
        return (currentTime >= self.intervalBegin) and (currentTime < self.intervalEnd)

    def canSendOrder(self):
        return not self.inPosition

    def buyMarket(self):
        self.entryOrderId = buyMarket(self)
        if self.entryOrderId:
            self.inPosition = True
            self.side = 'BUY'

    def sellMarket(self):
        self.entryOrderId = sellMarket(self)
        if self.entryOrderId:
            self.inPosition = True
            self.side = 'SELL'

    def closePosition(self):
        if closePosition(self):
            self.inPosition = False

    def price(self):
        return indicators.getPrices(self.comb)
