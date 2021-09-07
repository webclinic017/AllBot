from src.robots.Robot import Robot
from src.marketData.IndicatorsManager import indicators


class BollingerBands(Robot):
    """Define o robô com a estratégia IFR2"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify, period, stdDeviation):
        super().__init__(id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify)
        self.type = "BOLLINGERBANDS"
        self.period = period
        self.stdDeviation = stdDeviation
        self.BBLower = indicators.getIndicator(self.comb, ['BBLower', self.comb, period, stdDeviation])
        self.BBUpper = indicators.getIndicator(self.comb, ['BBUpper', self.comb, period, stdDeviation])

    def newData(self, data, closed):
        """Notificação de novos dados"""
        if closed:
            if self.canSendOrder():
                price = self.price()[-1]
                bblower = self.BBLower.values.iloc[-1]
                bblowerShift = self.BBLower.values.iloc[-2]

                print("----BUY", price, bblowerShift, bblower)
                if bblowerShift and (not bblower):
                    self.buyMarket()
                    print(self.nickName, "COMPRA")
            elif self.inPosition:
                price = self.price()[-1]
                bbupper = self.BBUpper.values.iloc[-1]
                bbupperShift = self.BBUpper.values.iloc[-2]

                print("----SELL", price, bbupper, bbupperShift)
                if bbupper:
                    self.closePosition()
                    print(self.nickName, "VENDA")

