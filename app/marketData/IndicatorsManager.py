import ta
import pandas as pd
from binance.spot import Spot as Client


class Indicator:
    def __init__(self, params):
        self.params = params
        self.values = pd.Series()

    def sameIndicator(self, other):
        return self.params == other

    def calc(self, prices):
        if self.params[0] == 'RSI':
            self.values = ta.momentum.rsi(prices, self.params[2])
        elif self.params[0] == 'SMA':
            self.values = ta.trend.sma_indicator(prices, self.params[2])


class IndicatorManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.indicators = {}
        self.prices = {}

    def getIndicator(self, comb, params):
        if comb not in self.prices:
            self.prices[comb] = self.getLastPrices(comb, 200)
        if comb not in self.indicators:
            self.indicators[comb] = []
        for ind in self.indicators[comb]:
            if ind.sameIndicator(params):
                return ind
        indicator = Indicator(params)
        indicator.calc(self.prices[comb])
        self.indicators[comb].append(indicator)
        return indicator

    def getPrices(self, comb):
        if comb in self.prices:
            return self.prices[comb]

    def newData(self, comb, data):
        self.prices[comb] = self.getLastPrices(comb, 200)
        if comb in self.indicators:
            for indicator in self.indicators[comb]:
                indicator.calc(self.prices[comb])

    def getStream(self, symbol):
        return symbol.lower() + '@kline_1m'

    def getLastPrices(self, comb, num):
        symbol, interval = comb.split('/')
        spot_client = Client(base_url="https://testnet.binance.vision")
        return pd.DataFrame(spot_client.klines(symbol, interval, limit=num))[4].astype('float64')

if IndicatorManager._instance is None:
    indicators = IndicatorManager()
