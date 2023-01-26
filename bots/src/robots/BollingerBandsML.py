from src.robots.Robot import Robot
from src.marketData.IndicatorsManager import indicators
from src.mobileNotify.SendNotify import sendTelegramMessage
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class BollingerBandsML(Robot):
    """Define o robô com a estratégia Bollinger Bands e filtro ML"""

    def __init__(self, id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition,
                 chatID, onlyNotify, period, stdDeviation):
        super().__init__(id, key, secret, nickName, symbol, timeframe, quantity, intervalBegin, intervalEnd, inPosition,
                         chatID, onlyNotify)
        self.type = "BOLLINGERBANDSML"
        self.period = period
        self.stdDeviation = stdDeviation
        self.BBLower = indicators.getIndicator(self.comb, ['BBLower', self.comb, period, stdDeviation])
        self.BBUpper = indicators.getIndicator(self.comb, ['BBUpper', self.comb, period, stdDeviation])
        self.Volatility10 = indicators.getIndicator(self.comb, ['Volatility10', self.comb, period])
        self.CumVolatility10 = indicators.getIndicator(self.comb, ['CumVolatility10', self.comb, period])
        self.DistanceOfMean80 = indicators.getIndicator(self.comb, ['DistanceOfMean80', self.comb, period])
        self.model = pickle.load(open('model.pkl', 'rb'))

    def newData(self, data, closed):
        """Notificação de novos dados"""
        if self.canSendOrder():
            price = self.price()[-1]
            bblower = self.BBLower.values.iloc[-1]
            bblowerShift = self.BBLower.values.iloc[-2]
            volatility10 = self.Volatility10.values.iloc[-1]
            cumVolatility10 = self.CumVolatility10.values.iloc[-1]
            distanceOfMean80 = self.DistanceOfMean80.values.iloc[-1]

            predDF = pd.DataFrame()
            predDF['H'] = volatility10[-2:]
            predDF['I'] = cumVolatility10[-2:]
            predDF['F'] = distanceOfMean80[-2:]
            predict = self.model.predict(predDF)[-1]

            print("----BUY", price, bblowerShift, bblower)
            if bblowerShift and (not bblower) and predict:
                if self.onlyNotify:
                    sendTelegramMessage('Sinal de Compra ' + self.nickName, self.chatID)
                else:
                    self.buyMarket()
                print(self.nickName, "COMPRA")
        elif self.inPosition:
            price = self.price()[-1]
            bbupper = self.BBUpper.values.iloc[-1]
            bbupperShift = self.BBUpper.values.iloc[-2]

            print("----SELL", price, bbupper, bbupperShift)
            if bbupper:
                if self.onlyNotify:
                    sendTelegramMessage('Sinal de Venda ' + self.nickName, self.chatID)
                else:
                    self.closePosition()
                print(self.nickName, "VENDA")
