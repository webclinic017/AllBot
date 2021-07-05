from backtest.IFR2Backtest import IFRBacktest
from backtest.CrossAverageBacktest import CrossAverageBacktest
import pandas as pd
from backtesting import Backtest
import ta
from datetime import datetime

import time

inicio = time.time()

symbols = ['GBPUSD', 'EURUSD', 'USDJPY']

robots = ['IFR2', 'CROSSAVERAGE']


dateFrom = datetime(2020, 1, 1)
dateTo = datetime(2020, 12, 31)
cont = 0

for timeframe in timeframes:
    for symbol in symbols:
        df = pd.DataFrame(rates)
        df.rename(columns={'time': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'},
                  inplace=True)

        df['Date'] = pd.to_datetime(df['Date'], unit='s')
        df.set_index('Date', inplace=True)

        df['RSI'] = ta.momentum.RSIIndicator(df['Close'], 2, True).rsi()
        df['SMA'] = ta.trend.SMAIndicator(df['Close'], 5, True).sma_indicator()


        df['mFast'] = ta.trend.SMAIndicator(df['Close'], 5, True).sma_indicator()
        df['mSlow'] = ta.trend.SMAIndicator(df['Close'], 12, True).sma_indicator()

        df = df[2:]

        bt = Backtest(df, IFRBacktest, commission=0, exclusive_orders=False)
        stats = bt.run()
        print(stats)
        break

        bt = Backtest(df, CrossAverageBacktest, commission=0, exclusive_orders=False)
        stats = bt.run()
        cont += 2

print(cont)
fim = time.time()
print(fim - inicio)
