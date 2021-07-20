# from IFR2Backtest import IFRBacktest
# from CrossAverageBacktest import CrossAverageBacktest
# import pandas as pd
# from backtesting import Backtest
# import ta
# import datetime
# from binance.spot import Spot as Client
# import numpy as np
#
#
# def getBacktest(data):
#     dateFrom = datetime.datetime.strptime(data['dateFrom'], '%Y-%m-%d %H:%M')
#     dateTo = datetime.datetime.strptime(data['dateTo'], '%Y-%m-%d %H:%M')
#
#     df = getCandles(data['timeframe'], dateFrom, dateTo)
#     if data['name'] == "IFR2":
#         df['RSI'] = ta.momentum.RSIIndicator(df['Close'], data['params']['period'], True).rsi()
#         df['SMA'] = ta.trend.SMAIndicator(df['Close'], 5, True).sma_indicator()
#         df = df[2:]
#         bt = Backtest(df, IFRBacktest, commission=0, exclusive_orders=False)
#         stats = bt.run().to_json()
#         bt.plot()
#         return stats
#
#     if data['name'] == "Cross Average":
#         df['mFast'] = ta.trend.SMAIndicator(df['Close'], data['params']['periodFast'], True).sma_indicator()
#         df['mSlow'] = ta.trend.SMAIndicator(df['Close'], data['params']['periodSlow'], True).sma_indicator()
#         df = df[2:]
#         bt = Backtest(df, CrossAverageBacktest, commission=0, exclusive_orders=False)
#         stats = bt.run().to_json()
#         return stats
#
#
# def getCandles(symbol, timeframe, startTime, endTime, limit=1000):
#     df = pd.DataFrame(columns=['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time'])
#     spot_client = Client(base_url="https://testnet.binance.vision")
#     candles = spot_client.klines(symbol, timeframe, startTime, endTime, limit)
#
#     opentime, lopen, lhigh, llow, lclose, lvol, closetime = [], [], [], [], [], [], []
#
#     for candle in candles:
#         opentime.append(candle[0])
#         lopen.append(candle[1])
#         lhigh.append(candle[2])
#         llow.append(candle[3])
#         lclose.append(candle[4])
#         lvol.append(candle[5])
#         closetime.append(candle[6])
#
#     df['Open_time'] = opentime
#     df['Open'] = np.array(lopen).astype(np.float)
#     df['High'] = np.array(lhigh).astype(np.float)
#     df['Low'] = np.array(llow).astype(np.float)
#     df['Close'] = np.array(lclose).astype(np.float)
#     df['Volume'] = np.array(lvol).astype(np.float)
#     df['Close_time'] = closetime
#     return df
#
#
# print(getCandles())
