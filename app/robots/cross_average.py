from app.robots.Robot import Robot
from app.marketData.IndicatorsManager import indicators


class CrossAverage(Robot):
    """Define o robô com a estratégia de cruzamento de médias móveis"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, periodFast, periodSlow):
        super().__init__(id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd)
        self.type = "CROSSAVERAGE"
        self.periodFast = periodFast
        self.periodSlow = periodSlow
        self.smaFast = indicators.getIndicator(self.comb, ['SMA', self.comb, periodFast])
        self.smaSlow = indicators.getIndicator(self.comb, ['SMA', self.comb, periodSlow])

    def newData(self, data, closed):
        """Notificação de novos dados"""

        if closed:
            if self.canSendOrder():
                mFastShift1 = self.smaFast.iloc[-2]
                mSlowShift1 = self.smaSlow.iloc[-2]

                mFastShift2 = self.smaFast.iloc[-3]
                mSlowShift2 = self.smaSlow.iloc[-3]

                if mFastShift1 > mSlowShift1 and (mFastShift2 < mSlowShift2):
                    self.buyMarket()
                    print(self.nickName, "COMPRA")

            elif self.inPosition:
                mFastShift1 = self.smaFast.iloc[-2]
                mSlowShift1 = self.smaSlow.iloc[-2]

                mFastShift2 = self.smaFast.iloc[-3]
                mSlowShift2 = self.smaSlow.iloc[-3]
                if mFastShift1 < mSlowShift1 and (mFastShift2 > mSlowShift2):
                    self.sellMarket()
                    print(self.nickName, "VENDA")

