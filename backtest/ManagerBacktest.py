from roteamento.ConnectionMT5 import connect
from backtest.IFR2Backtest import IFRBacktest
from backtest.CrossAverageBacktest import CrossAverageBacktest
import MetaTrader5 as mt5
import pandas as pd
from backtesting import Backtest
import ta
import datetime


timeframes = {'M1': mt5.TIMEFRAME_M1, 'M2': mt5.TIMEFRAME_M2, 'M5': mt5.TIMEFRAME_M5, 'M15': mt5.TIMEFRAME_M15,
              'M30': mt5.TIMEFRAME_M30, 'H1': mt5.TIMEFRAME_H1, 'H4': mt5.TIMEFRAME_H4, 'D1': mt5.TIMEFRAME_D1}


def getBacktest(data):

    connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9")
    dateFrom = datetime.datetime.strptime(data['dateFrom'], '%Y-%m-%d %H:%M')
    dateTo = datetime.datetime.strptime(data['dateTo'], '%Y-%m-%d %H:%M')

    df = pd.DataFrame(mt5.copy_rates_range(data['symbol'], timeframes[data['timeframe']], dateFrom, dateTo))
    df.rename(columns={'time': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'},
              inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], unit='s')
    df.set_index('Date', inplace=True)

    if data['name'] == "IFR2":
        df['RSI'] = ta.momentum.RSIIndicator(df['Close'], data['params']['period'], True).rsi()
        df['SMA'] = ta.trend.SMAIndicator(df['Close'], 5, True).sma_indicator()
        df = df[2:]
        bt = Backtest(df, IFRBacktest, commission=0, exclusive_orders=False)
        stats = bt.run().to_json()
        bt.plot()
        return stats

    elif data['name'] == "Cross Average":
        df['mFast'] = ta.trend.SMAIndicator(df['Close'], data['params']['periodFast'], True).sma_indicator()
        df['mSlow'] = ta.trend.SMAIndicator(df['Close'], data['params']['periodSlow'], True).sma_indicator()
        df = df[2:]
        bt = Backtest(df, CrossAverageBacktest, commission=0, exclusive_orders=False)
        stats = bt.run().to_json()
        return stats