import ta
import pandas as pd
import requests

indicators = {}
prices = {}


class Indicator:
    def __init__(self, type, params):
        self.type = type
        self.params = params
        self.values = pd.Series(dtype='float64')


def getIndicator(comb, type, params):
    if comb not in indicators:
        prices[comb] = getLastPrices(comb, 200)  # Otimizar tamanho
        indicators[comb] = []
    for indicator in indicators[comb]:
        if (indicator.type == type) and (indicator.params == params):
            return indicator
    indicator = Indicator(type, params)

    indicators[comb].append(indicator)
    return indicator


def newData(comb, data):
    prices[comb].drop(index=0, inplace=True)
    prices[comb].append(pd.Series(data['x']))
    for indicator in indicators[comb]:
        calcIndicator(indicator, prices[comb])


def getLastPrices(comb, num):
    url = 'https://api.binance.com/api/v3/klines'

    symbol, interval = comb.split('/')
    params = {
        'symbol': symbol,
        'interval': interval
    }
    response = requests.get(url, params=params)
    return pd.Series(response.json()[-num:])


def calcIndicator(indicator, data):
    if indicator.type == 'RSI':
        indicator.values = ta.momentum.RSIIndicator(data['Close'], indicator['params']['period']).rsi()
    elif indicator.type == 'SMA':
        indicator.values = ta.trend.SMAIndicator(data['Close'], indicator['params']['period']).sma_indicator()
