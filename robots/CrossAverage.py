from robots.Robot import Robot
from roteamento.OrderSend import *
import ta


class CrossAverage(Robot):
    """Define o robô com a estratégia de cruzamento de médias móveis"""

    def __init__(self, nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd, periodFast, periodSlow):
        super().__init__(nickName, symbol, timeframe, quantity, mode, intervalBegin, intervalEnd)
        self.type = "Cross Average"
        self.periodFast = periodFast
        self.periodSlow = periodSlow

    def newData(self, data):
        """Notificação de novos dados"""

        smaFast = ta.trend.SMAIndicator(data['Close'], self.periodFast, True).sma_indicator()
        smaSlow = ta.trend.SMAIndicator(data['Close'], self.periodSlow, True).sma_indicator()

        mFastShift1 = smaFast.iloc[-2]
        mSlowShift1 = smaSlow.iloc[-2]

        mFastShift2 = smaFast.iloc[-3]
        mSlowShift2 = smaSlow.iloc[-3]

        if mFastShift1 > mSlowShift1 and (mFastShift2 < mSlowShift2):
            closePosition(self.symbol, self.magicNumber)
            if self.checkTimeRestrictions():
                buyMarket(self.symbol, self.quantity, 200, 200, self.magicNumber, self.nickName)
                print(self.nickName, "COMPRA")
        elif mFastShift1 < mSlowShift1 and (mFastShift2 > mSlowShift2):
            closePosition(self.symbol, self.magicNumber)
            if self.checkTimeRestrictions():
                sellMarket(self.symbol, self.quantity, 200, 200, self.magicNumber, self.nickName)
                print(self.nickName, "VENDA")
