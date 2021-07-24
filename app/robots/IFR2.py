from app.robots.Robot import Robot
from app.marketData.IndicatorsManager import indicators
from app.mobileNotify.SendNotify import *


class IFR2(Robot):
    """Define o robô com a estratégia IFR2"""

    def __init__(self, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, periodIFR, upper, lower, periodMean):
        super().__init__(key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd)
        self.type = "IFR2"
        self.periodIFR = periodIFR
        self.upper = upper
        self.lower = lower
        self.periodMean = periodMean
        self.RSI = indicators.getIndicator(self.comb, ['RSI', self.comb, periodIFR])
        self.SMA = indicators.getIndicator(self.comb, ['SMA', self.comb, periodMean])

    def newData(self, data, closed):
        """Notificação de novos dados"""
        if closed:
            if self.canSendOrder():
                rsi = self.RSI.values.iloc[-1]
                if rsi < self.lower:
                    self.buyMarket()
                    print(self.nickName, "COMPRA")
                    message("COMPRA")
            elif self.inPosition:
                rsi = self.RSI.values.iloc[-1]
                if rsi > self.upper:
                    self.sellMarket()
                    print(self.nickName, "VENDA")
                    message("VENDA")


