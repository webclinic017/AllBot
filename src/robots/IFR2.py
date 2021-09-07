from src.robots.Robot import Robot
from src.marketData.IndicatorsManager import indicators


class IFR2(Robot):
    """Define o robô com a estratégia IFR2"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify, periodIFR, upper, lower, periodMean):
        super().__init__(id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify)
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
                print("----BUY", rsi, self.lower)
                if rsi < self.lower:
                    self.buyMarket()
                    print(self.nickName, "COMPRA")
            elif self.inPosition:
                price = self.price()[-1]
                mean = self.SMA.valeus.iloc[-1]
                print("----SELL", price, mean)
                if price > mean:
                    self.closePosition()
                    print(self.nickName, "VENDA")


