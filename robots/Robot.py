from datetime import datetime
from roteamento.RoteamentoManager import *

class Robot:
    """Define a estrutura básica de um robô"""

    def __init__(self, nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd):
        self.type = "Robot"
        self.nickName = nickName
        self.symbol = symbol
        self.timeframe = timeframe
        self.quantity = quantity
        self.mode = mode
        self.intervalBegin = intervalBegin
        self.intervalEnd = intervalEnd
        self.magicNumber = 2424
        self.comb = self.symbol + '/' + self.timeframe

    lastTime = 0

    def closeAll(self):
        """Encerra a ordem ou posição em aberto do robô"""
        #closePosition(self.symbol, self.magicNumber)

    def checkTimeRestrictions(self):
        """Verifica as restrições de horário"""
        currentTime = datetime.now().time()
        print(currentTime)
        if (currentTime >= self.intervalBegin) and (currentTime < self.intervalEnd):
            return True
        return False

    def isNewBar(self, actualTime):
        global lastTime
        if lastTime != actualTime:
            lastTime = actualTime
            return True
        return False

    def buyMarket(self):
        if market(self.symbol, 'buy', self.quantity)['clientOrderId'] is not None:
            return True
        return False

    def sellMarket(self):
        if market(self.symbol, 'sell', self.quantity)['clientOrderId'] is not None:
            return True
        return False


