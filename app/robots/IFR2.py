from app.robots.Robot import Robot
from app.robots.IndicatorsManager import *

class IFR2(Robot):
    """Define o robô com a estratégia IFR2"""

    def __init__(self, nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd, period, upper, lower, periodMean):
        super().__init__(nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd)
        self.type = "IFR2"
        self.period = period
        self.upper = upper
        self.lower = lower
        self.periodMean = periodMean
        self.RSI = getIndicator(self.comb, 'RSI', [period])
        self.SMA = getIndicator(self.comb, 'SMA', [periodMean])

    def newData(self, data):
        """Notificação de novos dados"""

        if self.checkTimeRestrictions():
            rsi = self.RSI.values[-1]
            if rsi < self.lower:
                self.buyMarket()
                print(self.nickName, "COMPRA")
            elif rsi > self.upper:
                self.sellMarket()
                print(self.nickName, "VENDA")
        else:
            price = data.close.iloc[-2]
            sma = self.SMA.values[-1]

