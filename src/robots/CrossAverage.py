from src.robots.Robot import Robot
from src.marketData.IndicatorsManager import indicators
from src.mobileNotify.SendNotify import sendTelegramMessage

class CrossAverage(Robot):
    """Define o robô com a estratégia de cruzamento de médias móveis"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify, periodFast, periodSlow):
        super().__init__(id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition, chatID, onlyNotify)
        self.type = "CROSSAVERAGE"
        self.periodFast = periodFast
        self.periodSlow = periodSlow
        self.smaFast = indicators.getIndicator(self.comb, ['SMA', self.comb, periodFast])
        self.smaSlow = indicators.getIndicator(self.comb, ['SMA', self.comb, periodSlow])

    def newData(self, data, closed):
        """Notificação de novos dados"""

        if self.canSendOrder():
            mFastShift1 = self.smaFast.values.iloc[-2]
            mSlowShift1 = self.smaSlow.values.iloc[-2]

            mFastShift2 = self.smaFast.values.iloc[-3]
            mSlowShift2 = self.smaSlow.values.iloc[-3]

            if mFastShift1 > mSlowShift1 and (mFastShift2 < mSlowShift2):
                if self.onlyNotify:
                    sendTelegramMessage('Sinal de Compra ' + self.nickName, self.chatID)
                else:
                    self.buyMarket()
                print(self.nickName, "COMPRA")

        elif self.inPosition:
            mFastShift1 = self.smaFast.values.iloc[-2]
            mSlowShift1 = self.smaSlow.values.iloc[-2]

            mFastShift2 = self.smaFast.values.iloc[-3]
            mSlowShift2 = self.smaSlow.values.iloc[-3]

            if mFastShift1 < mSlowShift1 and (mFastShift2 > mSlowShift2):
                if self.onlyNotify:
                    sendTelegramMessage('Sinal de Venda ' + self.nickName, self.chatID)
                else:
                    self.closePosition()
                print(self.nickName, "VENDA")

