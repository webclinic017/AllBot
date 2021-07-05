from robots.Robot import Robot
import ta

class IFR2(Robot):
    """Define o robô com a estratégia IFR2"""

    def __init__(self, nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd, period, upper, lower,
                 periodMean):
        super().__init__(nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd)
        self.type = "IFR2"
        self.period = period
        self.upper = upper
        self.lower = lower
        self.periodMean = periodMean

    def newData(self, data):
        """Notificação de novos dados"""

        if not self.isNewBar(data['time']):
            return

        if not hasOpenPosition(self.symbol) and self.checkTimeRestrictions():
            rsi = ta.momentum.RSIIndicator(data['close'], self.period, True).rsi().iloc[-2]
            if rsi < self.lower:
                self.buyMarket()
                print(self.nickName, "COMPRA")
            elif rsi > self.upper:
                self.sellMarket()
                print(self.nickName, "VENDA")
        else:
            price = data.close.iloc[-2]
            sma = ta.trend.SMAIndicator(data['Close'], self.periodMean, True).sma_indicator().iloc[-2]
            if isLongPosition(self.symbol) and (price > sma):
                closePosition(self.symbol, self.magicNumber)
                print(self.nickName, "ENCERRANDO OPERAÇÃO DE COMPRA")
            elif isShortPosition(self.symbol) and (price < sma):
                closePosition(self.symbol, self.magicNumber)
                print(self.nickName, "ENCERRANDO OPERAÇÃO DE VENDA")
