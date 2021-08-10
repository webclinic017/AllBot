from IFR2Backtest import IFR2Backtest
from CrossAverageBacktest import CrossAverageBacktest
from Schemas import IFR2Schema, CrossAverageSchema
import pandas as pd
from backtesting import Backtest
from binance.spot import Spot as Client
import numpy as np



def getRanking():
    symbols = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT']
    timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h']
    robots = [IFR2Backtest, CrossAverageBacktest]
    backtests = []
    for timeframe in timeframes:
        for symbol in symbols:
            df = getCandles(symbol, timeframe)
            for robot in robots:
                bt = Backtest(df, robot, cash=100000, commission=0, exclusive_orders=False)
                result = bt.run()
                result['timeframe'] = timeframe
                result['symbol'] = symbol
                result['robot'] = robot.name
                del result['_strategy']
                del result['_equity_curve']
                del result['_trades']

                dict = result.to_dict()
                for oldKey in list(dict):
                    if isinstance(dict[oldKey], pd._libs.tslibs.timedeltas.Timedelta):
                        dict[oldKey] = str(dict[oldKey])
                    dict[oldKey.replace('.', '').replace(' ', '').replace('#', '')] = dict.pop(oldKey)

                backtests.append(dict)

    sortedByReturn = sorted(backtests, key=lambda k: k['Return[%]'], reverse=True)
    return sortedByReturn


def getCandles(symbol, timeframe):
    df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time'])
    spot_client = Client(base_url="https://api.binance.com")
    candles = spot_client.klines(symbol, timeframe, limit=1000)
    opentime, lopen, lhigh, llow, lclose, lvol, closetime = [], [], [], [], [], [], []

    for candle in candles:
        opentime.append(candle[0])
        lopen.append(candle[1])
        lhigh.append(candle[2])
        llow.append(candle[3])
        lclose.append(candle[4])
        lvol.append(candle[5])
        closetime.append(candle[6])

    df['Date'] = opentime
    df['Open'] = np.array(lopen).astype(float)
    df['High'] = np.array(lhigh).astype(float)
    df['Low'] = np.array(llow).astype(float)
    df['Close'] = np.array(lclose).astype(float)
    df['Volume'] = np.array(lvol).astype(float)
    df['Close_time'] = closetime
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df.set_index('Date', inplace=True)
    return df


def getBacktest(robotSchema):
    if isinstance(robotSchema, IFR2Schema):
        robotType = IFR2Backtest
        robotType.periodIFR = robotSchema.periodIFR
        robotType.periodMean = robotSchema.periodMean
        robotType.lower = robotSchema.lower
        robotType.upper = robotSchema.upper
        robotType.periodMean = robotSchema.periodMean
    elif isinstance(robotSchema, CrossAverageSchema):
        robotType = CrossAverageBacktest
        robotType.periodFast = robotSchema.periodFast
        robotType.periodSlow = robotSchema.periodSlow
    df = getCandles(robotSchema.symbol, robotSchema.timeframe)
    bt = Backtest(df, robotType, cash=100000, commission=0, exclusive_orders=False)
    result = bt.run()
    result['timeframe'] = robotSchema.timeframe
    result['symbol'] = robotSchema.symbol
    result['robot'] = robotType.name
    del result['_strategy']
    del result['_equity_curve']
    del result['_trades']
    dict = result.to_dict()
    for oldKey in list(dict):
        if isinstance(dict[oldKey], pd._libs.tslibs.timedeltas.Timedelta):
            dict[oldKey] = str(dict[oldKey])
        dict[oldKey.replace('.', '').replace(' ', '').replace('#', '')] = dict.pop(oldKey)
    return dict
